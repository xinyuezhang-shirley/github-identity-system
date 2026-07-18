// Phase 2 — Deterministic semantic-gravity specimen generator.
// Consumes the frozen corpus (Phase 0) and produces a frozen layout.
// Every visual position is traceable to this pipeline; no hand placement,
// no nudging, no aesthetic adjustment. Rules: production-spec Part 1.3–1.9.
//
// Pipeline:
//   corpus units -> tokens -> node weights (top 30) -> edges (co-occurrence)
//   -> importance -> radius (inverse of importance) -> seeded force settle
//   -> normalized positions centered on the highest-importance node.
//
// Output:
//   layout.json  — nodes (word, weight, importance, size, x, y), edges, meta
//   audit.json   — extracted terms, weights, edge list (for auditing)

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import {
  forceSimulation,
  forceManyBody,
  forceCollide,
  forceLink,
  forceRadial,
} from "d3-force";

const here = dirname(fileURLToPath(import.meta.url));
const corpusDir = join(here, "..", "corpus");

// ---- frozen constants -------------------------------------------------------
const SEED = 20260718; // fixed PRNG seed — determinism (spec 1.8)
const TICKS = 600; // fixed settle length (spec 1.8)
const TOP_N = 30; // node cap (spec 1.6)
const EDGE_MIN_WEIGHT = 2; // edge threshold (spec 1.7)
const EDGE_FALLBACK_CAP = 40; // fallback cap if <20 edges (spec 1.7)
const MIN_TOKEN_LEN = 3; // spec 1.3.3

// Canvas (card scale, spec Part 5 / 6). Layout is computed here in display px;
// the renderer exports at 2x.
const WIDTH = 900;
const HEIGHT = 520;
const MARGIN = 70;

// Radius band as a fraction of the available half-extent (spec 1.8: radius is
// an inverse function of importance; highest importance -> smallest radius).
const R_MIN_FRAC = 0.05;
const R_MAX_FRAC = 0.9;

// Label sizing by importance (spec 1.8: node size proportional to importance).
const SIZE_MIN = 12;
const SIZE_MAX = 34;

// ---- seeded PRNG (mulberry32) ----------------------------------------------
// d3-force uses Math.random internally for jiggle; override it so the settle
// is fully deterministic and reproducible.
function mulberry32(a) {
  return function () {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ---- load frozen inputs -----------------------------------------------------
const corpus = JSON.parse(readFileSync(join(corpusDir, "corpus.json"), "utf8"));
const stop = JSON.parse(readFileSync(join(corpusDir, "stopwords.json"), "utf8"));
const lemma = JSON.parse(readFileSync(join(corpusDir, "lemma-map.json"), "utf8"));

const STOPWORDS = new Set([...stop.standard, ...stop.filler]);
const LEMMA = lemma.map;

// ---- tokenization (spec 1.3–1.5) -------------------------------------------
function tokenizeUnit(text) {
  const cleaned = text
    .normalize("NFKD")
    .toLowerCase()
    .replace(/[^a-z\s-]/g, "") // strip to [a-z\s-]; disallowed chars removed
    .replace(/\s+/g, " ")
    .trim();
  const out = [];
  for (const raw of cleaned.split(" ")) {
    if (!raw) continue;
    const folded = LEMMA[raw] || raw; // minimal singular folding (1.5)
    if (folded.length < MIN_TOKEN_LEN) continue; // drop short (1.3.3)
    if (STOPWORDS.has(folded)) continue; // stopword removal (1.4)
    out.push(folded);
  }
  return out;
}

// Per-unit token lists (used for both weighting and co-occurrence).
const unitTokens = corpus.units.map((u) => tokenizeUnit(u.text));

// ---- node weights + top N (spec 1.6) ---------------------------------------
const freq = new Map();
for (const toks of unitTokens) {
  for (const t of toks) freq.set(t, (freq.get(t) || 0) + 1);
}

// Sort by weight desc, ties alphabetical (deterministic, spec 1.6).
const ranked = [...freq.entries()].sort((a, b) =>
  b[1] !== a[1] ? b[1] - a[1] : a[0] < b[0] ? -1 : 1
);
const topEntries = ranked.slice(0, TOP_N);
const nodeWords = topEntries.map(([w]) => w);
const nodeSet = new Set(nodeWords);
const maxWeight = topEntries[0][1];

// ---- edges: co-occurrence within a unit among top-N (spec 1.7) -------------
const pairWeight = new Map(); // "a\tb" (a<b) -> count of units co-occurring
for (const toks of unitTokens) {
  const present = [...new Set(toks)].filter((t) => nodeSet.has(t)).sort();
  for (let i = 0; i < present.length; i++) {
    for (let j = i + 1; j < present.length; j++) {
      const key = `${present[i]}\t${present[j]}`;
      pairWeight.set(key, (pairWeight.get(key) || 0) + 1);
    }
  }
}

const nodeIndex = new Map(nodeWords.map((w, i) => [w, i]));
let allEdges = [...pairWeight.entries()].map(([key, weight]) => {
  const [a, b] = key.split("\t");
  return { source: a, target: b, weight };
});

// Keep weight >= 2; if fewer than 20, drop to >=1 and cap at 40 highest
// (tie-break by node-index sum, then alphabetical) — spec 1.7.
let edges = allEdges.filter((e) => e.weight >= EDGE_MIN_WEIGHT);
if (edges.length < 20) {
  edges = [...allEdges].sort((a, b) => {
    if (b.weight !== a.weight) return b.weight - a.weight;
    const sa = nodeIndex.get(a.source) + nodeIndex.get(a.target);
    const sb = nodeIndex.get(b.source) + nodeIndex.get(b.target);
    if (sa !== sb) return sa - sb;
    const ka = `${a.source}\t${a.target}`;
    const kb = `${b.source}\t${b.target}`;
    return ka < kb ? -1 : 1;
  }).slice(0, EDGE_FALLBACK_CAP);
}

// ---- importance, radius, size (spec 1.8) -----------------------------------
const cx = WIDTH / 2;
const cy = HEIGHT / 2;
const halfExtent = Math.min(WIDTH, HEIGHT) / 2 - MARGIN;
const R_MIN = R_MIN_FRAC * halfExtent;
const R_MAX = R_MAX_FRAC * halfExtent;
const GOLDEN = Math.PI * (3 - Math.sqrt(5)); // 2.399963...

// Monospace glyph advance as a fraction of font-size (used for label boxes).
const CHAR_ADVANCE = 0.62;
const LABEL_PAD = 7; // px gap enforced between label boxes

const nodes = topEntries.map(([word, weight], rank) => {
  const importance = weight / maxWeight; // (0,1]
  const targetRadius = R_MAX - (R_MAX - R_MIN) * importance; // inverse (1.8)
  const angle = rank * GOLDEN; // golden-angle by importance rank (1.8)
  const size = SIZE_MIN + (SIZE_MAX - SIZE_MIN) * importance;
  return {
    word,
    weight,
    rank,
    importance,
    targetRadius,
    size,
    hw: (CHAR_ADVANCE * size * word.length) / 2, // label half-width
    hh: size / 2, // label half-height
    // deterministic initial position on the target ring (avoids coincidence)
    x: cx + targetRadius * Math.cos(angle),
    y: cy + targetRadius * Math.sin(angle),
  };
});

// Highest-importance node is pinned at canvas center (spec 1.9: the center node
// is centered in the crop). Pinning it also keeps the field radially balanced.
const center = nodes.reduce((a, b) => (b.importance > a.importance ? b : a));
center.fx = cx;
center.fy = cy;

// Rectangular (AABB) overlap separation. d3's forceCollide treats nodes as
// circles, which cannot prevent text labels from overlapping; node marks here
// are words, so overlap is resolved on label bounding boxes instead. A pinned
// node (center) never moves; its partner takes the full correction.
function separate(list, strength) {
  for (let i = 0; i < list.length; i++) {
    for (let j = i + 1; j < list.length; j++) {
      const a = list[i];
      const b = list[j];
      const dx = b.x - a.x;
      const dy = b.y - a.y;
      const ox = a.hw + b.hw + LABEL_PAD - Math.abs(dx);
      const oy = a.hh + b.hh + LABEL_PAD - Math.abs(dy);
      if (ox <= 0 || oy <= 0) continue; // no overlap on one axis -> clear
      const aFixed = a.fx !== undefined;
      const bFixed = b.fx !== undefined;
      if (ox < oy) {
        const push = (dx < 0 ? -1 : 1) * ox * strength;
        if (aFixed && !bFixed) b.x += push * 2;
        else if (bFixed && !aFixed) a.x -= push * 2;
        else { a.x -= push; b.x += push; }
      } else {
        const push = (dy < 0 ? -1 : 1) * oy * strength;
        if (aFixed && !bFixed) b.y += push * 2;
        else if (bFixed && !aFixed) a.y -= push * 2;
        else { a.y -= push; b.y += push; }
      }
    }
  }
}

// ---- seeded force settle (spec 1.8) ----------------------------------------
const realRandom = Math.random;
Math.random = mulberry32(SEED);

const linkForce = forceLink(
  edges.map((e) => ({ source: e.source, target: e.target, weight: e.weight }))
)
  .id((d) => d.word)
  .strength(0.015) // very weak: edges bend the field slightly, never dominate
  .distance(90);

const sim = forceSimulation(nodes)
  .force("charge", forceManyBody().strength(-90)) // spread nodes angularly
  .force(
    "radial",
    forceRadial((d) => d.targetRadius, cx, cy).strength(0.9) // dominant (1.8)
  )
  .force("link", linkForce)
  .stop();

for (let i = 0; i < TICKS; i++) {
  sim.tick();
  separate(nodes, 0.5); // co-settle labels without overlap
}

Math.random = realRandom; // restore

// ---- normalize: fill card width, then guarantee non-overlap + fit (1.9) -----
// The settled field is roughly circular; the card is wide, so stretch
// horizontally about the pinned center to use the width. This is an affine
// transform about the center — the center node stays centered.
const STRETCH_X = 1.5;
for (const n of nodes) n.x = cx + (n.x - cx) * STRETCH_X;

// Resolve any residual overlaps introduced by the stretch (radial no longer
// applied, so this cannot reintroduce overlap).
for (let i = 0; i < 120; i++) separate(nodes, 0.5);

// Uniformly scale about the center so every label box fits within the margins.
let maxAbsX = 0;
let maxAbsY = 0;
for (const n of nodes) {
  maxAbsX = Math.max(maxAbsX, Math.abs(n.x - cx) + n.hw);
  maxAbsY = Math.max(maxAbsY, Math.abs(n.y - cy) + n.hh);
}
const fit = Math.min(
  (WIDTH / 2 - MARGIN) / (maxAbsX || 1),
  (HEIGHT / 2 - MARGIN) / (maxAbsY || 1),
  1
);
if (fit < 1) {
  for (const n of nodes) {
    n.x = cx + (n.x - cx) * fit;
    n.y = cy + (n.y - cy) * fit;
  }
  for (let i = 0; i < 60; i++) separate(nodes, 0.5);
}

for (const n of nodes) {
  n.x = Math.round(n.x * 100) / 100;
  n.y = Math.round(n.y * 100) / 100;
  n.importance = Math.round(n.importance * 1000) / 1000;
  n.size = Math.round(n.size * 100) / 100;
}

// ---- write outputs ----------------------------------------------------------
const outDir = join(here, "out");
mkdirSync(outDir, { recursive: true });

const layout = {
  meta: {
    phase: "2 — specimen generator",
    spec: "profile-production-spec.md Part 1.3–1.9",
    seed: SEED,
    ticks: TICKS,
    canvas: { width: WIDTH, height: HEIGHT, margin: MARGIN },
    centerWord: center.word,
    nodeCount: nodes.length,
    edgeCount: edges.length,
  },
  center: center.word,
  nodes: nodes.map((n) => ({
    word: n.word,
    weight: n.weight,
    importance: n.importance,
    size: n.size,
    x: n.x,
    y: n.y,
    isCenter: n.word === center.word,
  })),
  edges: edges.map((e) => ({ source: e.source, target: e.target, weight: e.weight })),
};

writeFileSync(join(outDir, "layout.json"), JSON.stringify(layout, null, 2) + "\n");

const audit = {
  totalUnits: corpus.units.length,
  distinctTerms: freq.size,
  top30: topEntries.map(([word, weight], rank) => ({ rank, word, weight })),
  centerWord: center.word,
  edgeCount: edges.length,
  edges: layout.edges,
};
writeFileSync(join(outDir, "audit.json"), JSON.stringify(audit, null, 2) + "\n");

console.log(`center: ${center.word} (weight ${center.weight})`);
console.log(`nodes: ${nodes.length}  edges: ${edges.length}`);
console.log("top 10:", topEntries.slice(0, 10).map(([w, c]) => `${w}:${c}`).join("  "));
