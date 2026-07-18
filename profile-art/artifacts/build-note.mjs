// Artifact — handwritten field-note.
// A quiet marginal gloss in the designer's hand (Caveat), set beside the
// specimen: it reframes the field as a self-portrait rather than restating the
// caption. The words write in left-to-right (per-glyph emergence), then rest
// and breathe faintly. Transparent; vector outlines; theme-aware.

import { writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { fonts, layoutGlyphs, svgDoc } from "./lib.mjs";

const here = dirname(fileURLToPath(import.meta.url));

const text = "the shape my thinking makes";
const size = 58;
const padX = 10;
const padY = 18;
const baseline = size; // within the padded box

const { glyphs, width } = layoutGlyphs(fonts.caveat, text, size, padX, padY + baseline, 0.0);
const W = Math.ceil(width + padX * 2);
const H = Math.ceil(size + padY * 2 + size * 0.35); // room for descenders + rise

// Glyphs emerge left-to-right, as if being written.
const spanTotal = 1.6; // seconds across the whole line
const perGlyph = glyphs.length > 1 ? spanTotal / glyphs.length : 0;
const inked = glyphs
  .map((g, i) => `<path class="ink" style="animation-delay:${(0.15 + i * perGlyph).toFixed(2)}s" d="${g.d}"/>`)
  .join("");

// Base state is the resting (visible) hand; the words only play in.
const css = `
  svg{--ink:#8b8175;}
  @media (prefers-color-scheme: dark){svg{--ink:#b7ad9f;}}
  .ink{fill:var(--ink);opacity:1;transform-box:fill-box;transform-origin:center;
       animation:write .7s ease-out both, breathe 8s ease-in-out 2.2s infinite;}
  @keyframes write{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:translateY(0)}}
  @keyframes breathe{0%,100%{opacity:1}50%{opacity:.86}}`;

const svg = svgDoc({ w: W, h: H, label: `Handwritten note: ${text}`, css, body: `<g>${inked}</g>` });

const outDir = join(here, "out");
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "note-field.svg"), svg);

const profileAssets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
mkdirSync(profileAssets, { recursive: true });
copyFileSync(join(outDir, "note-field.svg"), join(profileAssets, "note-field.svg"));

console.log(`note-field.svg written ${W}x${H} (${(svg.length / 1024).toFixed(1)}KB)`);
