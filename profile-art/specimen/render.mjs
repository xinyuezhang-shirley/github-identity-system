// Phase 3 — Render the specimen from the frozen layout.
// The renderer consumes ONLY layout.json and never modifies node positions.
// Art direction lives here (type, hierarchy, crop, tokens); geometry is the
// algorithm's and is left untouched. Dark and light differ only in tokens.
//
// The field is set in Cormorant Garamond — the same face MuseLab's Imprint uses
// for its word-particle fields (vortexCanvas / soupCanvas), and Echo's display
// serif — with the focal term heavier and the periphery lightening toward the
// edges. A tight, slightly top-weighted crop frames the field as a composed
// plate rather than a cluster floating in an empty rectangle.

import { readFileSync, writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { chromium } from "playwright";
import sharp from "sharp";

const here = dirname(fileURLToPath(import.meta.url));
const layout = JSON.parse(readFileSync(join(here, "out", "layout.json"), "utf8"));

// Field face (Echo / MuseLab shared display serif). Cormorant is narrower than
// the monospace the layout was settled against, so switching to it only opens
// gaps — it never introduces overlap.
const SERIF = "'Cormorant Garamond', Georgia, serif";
const SIZE_BOOST = 1.32; // serif reads finer than mono at equal px; give presence
const SERIF_ADVANCE = 0.46; // ~lowercase advance, for the crop bounding box
const LETTER_SPACING = 0.01; // em

// Hierarchy: weight steps and an eased opacity ramp so one term dominates and
// the periphery quiets to evidence.
const ease = (t) => Math.pow(t, 1.35);
function nodeWeight(n) {
  if (n.isCenter) return 600;
  return n.importance >= 0.5 ? 500 : 400;
}

const THEMES = {
  dark: {
    // Echo temperament: warm near-black, neutral ink, no accent — the focal
    // term is simply the brightest, per the frozen theme decision.
    bg: "#0b0a09",
    edge: "245,242,236",
    edgeAlphaBase: 0.04,
    edgeAlphaSpan: 0.09,
    node: "245,242,236",
    nodeAlphaBase: 0.26,
    nodeAlphaSpan: 0.62,
    center: "#f6f2ea",
  },
  light: {
    // MuseLab temperament: warm paper, ferric ink reserved for the one center
    // term where importance peaks.
    bg: "#f4efe6",
    edge: "92,83,72",
    edgeAlphaBase: 0.05,
    edgeAlphaSpan: 0.12,
    node: "28,25,23",
    nodeAlphaBase: 0.32,
    nodeAlphaSpan: 0.6,
    center: "#8b6914",
  },
};

const nodeByWord = new Map(layout.nodes.map((n) => [n.word, n]));
const maxEdgeWeight = Math.max(...layout.edges.map((e) => e.weight));

// ---- intentional crop: frame the field by its content, not the work canvas ---
let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
for (const n of layout.nodes) {
  const px = n.size * SIZE_BOOST;
  const hw = (SERIF_ADVANCE * px * n.word.length) / 2;
  const hh = 0.44 * px; // cap-height + descender allowance
  minX = Math.min(minX, n.x - hw);
  maxX = Math.max(maxX, n.x + hw);
  minY = Math.min(minY, n.y - hh);
  maxY = Math.max(maxY, n.y + hh);
}
const maxPx = Math.max(...layout.nodes.map((n) => n.size * SIZE_BOOST));
// Generous, slightly top-weighted margins for editorial air.
const padX = maxPx * 1.15;
const padTop = maxPx * 1.25;
const padBottom = maxPx * 1.0;
const viewX = minX - padX;
const viewY = minY - padTop;
const viewW = maxX - minX + padX * 2;
const viewH = maxY - minY + padTop + padBottom;

function esc(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function buildSvg(theme) {
  const t = THEMES[theme];

  const edges = layout.edges
    .map((e) => {
      const a = nodeByWord.get(e.source);
      const b = nodeByWord.get(e.target);
      if (!a || !b) return "";
      const wN = e.weight / maxEdgeWeight;
      const alpha = (t.edgeAlphaBase + t.edgeAlphaSpan * wN).toFixed(3);
      const sw = (0.5 + wN * 0.9).toFixed(2);
      return `<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="rgba(${t.edge},${alpha})" stroke-width="${sw}"/>`;
    })
    .join("\n");

  const nodes = layout.nodes
    .map((n) => {
      const fill = n.isCenter
        ? t.center
        : `rgba(${t.node},${(t.nodeAlphaBase + t.nodeAlphaSpan * ease(n.importance)).toFixed(3)})`;
      const px = (n.size * SIZE_BOOST).toFixed(2);
      return `<text x="${n.x}" y="${n.y}" font-family="${SERIF}" font-size="${px}" font-weight="${nodeWeight(n)}" fill="${fill}" text-anchor="middle" dominant-baseline="central" letter-spacing="${LETTER_SPACING}em">${esc(n.word)}</text>`;
    })
    .join("\n");

  // Transparent ground: the field sits directly on GitHub's page (paper or ink)
  // like the other editorial assets. Ink tokens stay theme-specific and are
  // paired via <picture>, so contrast is correct on both themes.
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${viewW}" height="${viewH}" viewBox="${viewX} ${viewY} ${viewW} ${viewH}">
<g>${edges}</g>
<g>${nodes}</g>
</svg>`;
}

const outDir = join(here, "out");
mkdirSync(outDir, { recursive: true });
const profileAssets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
mkdirSync(profileAssets, { recursive: true });

const fontLink = `<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">`;

const browser = await chromium.launch();
const scale = 2;
const page = await browser.newPage({
  viewport: { width: Math.ceil(viewW), height: Math.ceil(viewH) },
  deviceScaleFactor: scale,
});

for (const theme of ["dark", "light"]) {
  const svg = buildSvg(theme);
  writeFileSync(join(outDir, `specimen-${theme}.svg`), svg);

  const html = `<!doctype html><html><head><meta charset="utf-8">${fontLink}<style>
    html,body{margin:0;padding:0;background:transparent}
    #stage{width:${viewW}px;height:${viewH}px}
    svg{display:block}
  </style></head><body><div id="stage">${svg}</div></body></html>`;

  await page.setContent(html, { waitUntil: "networkidle" });
  await page.evaluate(async () => {
    await document.fonts.load("600 40px 'Cormorant Garamond'");
    await document.fonts.load("400 20px 'Cormorant Garamond'");
    await document.fonts.ready;
  });
  const stage = await page.$("#stage");
  const raw = await stage.screenshot({ omitBackground: true });

  // Full RGBA (not palette): the field is anti-aliased type and faint edges over
  // transparency, which need a true alpha channel to composite cleanly on any
  // GitHub background.
  const pngPath = join(outDir, `specimen-${theme}.png`);
  await sharp(raw)
    .png({ quality: 100, effort: 10, compressionLevel: 9 })
    .toFile(pngPath);

  copyFileSync(pngPath, join(profileAssets, `specimen-${theme}.png`));
  const kb = (readFileSync(pngPath).length / 1024).toFixed(0);
  console.log(`rendered ${theme} -> ${Math.round(viewW * scale)}x${Math.round(viewH * scale)} (${kb}KB)`);
}

await browser.close();
console.log("done");
