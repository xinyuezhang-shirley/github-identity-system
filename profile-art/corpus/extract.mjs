// Phase 0 — Corpus freeze.
// Deterministically extract sentence-level units from the vendored body-of-work
// sources (production-spec Part 1.1 / 1.3). This script performs ONLY the
// sentence-unit extraction. Token processing (lowercase, stopword removal,
// lemma folding, node/edge/importance) is Phase 2 and is intentionally absent
// here to respect phase boundaries.
//
// Reproducibility contract (spec 1.10): given the source files + this script,
// corpus.json is byte-stable. No manual editing.

import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));

// Fixed source order. Each id maps to one vendored prose file (spec Part 1.1).
const SOURCES = [
  { id: "echo", file: "sources/echo.txt" },
  { id: "muselab", file: "sources/muselab.txt" },
  { id: "differ", file: "sources/differ.txt" },
  { id: "rag", file: "sources/rag.txt" },
  { id: "practice", file: "sources/practice.txt" },
];

// Split a source's full text into sentence units.
// Rule (spec 1.3.1): collapse whitespace, then split on sentence terminators
// .?! followed by whitespace. Each line in the source is already a prose block;
// newlines collapse to spaces so multi-sentence blocks split cleanly.
function toUnits(raw) {
  const flat = raw.replace(/\s+/g, " ").trim();
  if (!flat) return [];
  return flat
    .split(/(?<=[.?!])\s+/)
    .map((s) => s.trim())
    .filter((s) => s.length > 0);
}

const units = [];
let index = 0;
for (const src of SOURCES) {
  const raw = readFileSync(join(here, src.file), "utf8");
  for (const text of toUnits(raw)) {
    units.push({ id: `${src.id}-${String(index).padStart(3, "0")}`, source: src.id, text });
    index += 1;
  }
}

const perSource = {};
for (const u of units) perSource[u.source] = (perSource[u.source] || 0) + 1;

const corpus = {
  meta: {
    phase: "0 — corpus freeze",
    spec: "profile-production-spec.md Part 1",
    sourceOrder: SOURCES.map((s) => s.id),
    unitCount: units.length,
    unitsPerSource: perSource,
    note: "Sentence units only. Tokens/weights/edges are computed in Phase 2.",
  },
  units,
};

const outPath = join(here, "corpus.json");
writeFileSync(outPath, JSON.stringify(corpus, null, 2) + "\n", "utf8");
console.log(`corpus.json written: ${units.length} units`);
for (const s of SOURCES) console.log(`  ${s.id}: ${perSource[s.id] || 0}`);
