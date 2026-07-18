// Artifact — identity wordmark.
// The name set in Cormorant Garamond (Echo/MuseLab's shared display serif) as
// the document masthead. Glyphs write in left-to-right, then rest. Paired
// light/dark exports (no media dependency), transparent, with a static
// resting fallback. Used inside an <h1> so it stays a real heading whose alt
// text carries the name — the plain name is not duplicated elsewhere.

import { writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { fonts, layoutGlyphs, svgDoc } from "./lib.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, "out");
const profileAssets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
mkdirSync(outDir, { recursive: true });
mkdirSync(profileAssets, { recursive: true });

const NAME = "Xinyue Zhang";
const size = 66;
const padX = 6;
const baseline = Math.round(size * 0.9);
const H = Math.round(size * 1.3);

const { glyphs, width } = layoutGlyphs(fonts.cormorant, NAME, size, padX, baseline, 0.005);
const W = Math.ceil(width + padX * 2);

// Slow, dignified write-in across the whole name; then rest (no loop).
const span = 1.8;
const per = glyphs.length > 1 ? span / glyphs.length : 0;

function build(file, ink, label) {
  const paths = glyphs
    .map((g, i) => `<path class="g" style="animation-delay:${(0.1 + i * per).toFixed(2)}s" d="${g.d}"/>`)
    .join("");
  const css = `
  .g{fill:${ink};opacity:1;transform-box:fill-box;transform-origin:50% 100%;
     animation:ink 1s cubic-bezier(.2,.7,.2,1) both;}
  @keyframes ink{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}`;
  const svg = svgDoc({ w: W, h: H, label, css, body: `<g>${paths}</g>` });
  writeFileSync(join(outDir, file), svg);
  copyFileSync(join(outDir, file), join(profileAssets, file));
  console.log(`${file} written ${W}x${H} (${(svg.length / 1024).toFixed(1)}KB)`);
}

build("wordmark-light.svg", "#1f2328", "Xinyue Zhang");
build("wordmark-dark.svg", "#ece6da", "Xinyue Zhang");
