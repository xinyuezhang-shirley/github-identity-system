// Artifact — "Plate 01" masthead.
// An exhibition-catalogue plate header for the specimen: an oversized Cormorant
// plate number, a ferric hairline that draws in, and the label emerging
// letter-by-letter in IBM Plex Mono small caps. Transparent; the number
// breathes on a slow seamless loop after the intro settles.

import { writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { fonts, layoutGlyphs, textPath, measure } from "./lib.mjs";

const here = dirname(fileURLToPath(import.meta.url));

const W = 900;
const H = 150;

// --- number ---------------------------------------------------------------
const numSize = 132;
const num = textPath(fonts.cormorant, "01", numSize, 4, 118);
const numRight = 4 + num.width;

// --- right column ---------------------------------------------------------
const colX = numRight + 46;
const plate = layoutGlyphs(fonts.mono, "PLATE", 15, colX, 46, 0.34);
const ruleY = 66;
const ruleX2 = W - 6;
const label = layoutGlyphs(fonts.monoMedium, "SEMANTIC GRAVITY FIELD", 20, colX, 108, 0.3);
const ruleLen = ruleX2 - colX;

const plateGlyphs = plate.glyphs
  .map((g, i) => `<path class="g" style="animation-delay:${(0.15 + i * 0.05).toFixed(2)}s" d="${g.d}"/>`)
  .join("");
const labelGlyphs = label.glyphs
  .map((g, i) => `<path class="g" style="animation-delay:${(1.0 + i * 0.045).toFixed(2)}s" d="${g.d}"/>`)
  .join("");

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="Plate 01 — semantic gravity field">
<style><![CDATA[
  /* Mid-tone defaults stay legible on BOTH GitHub themes even where an
     img-context SVG ignores prefers-color-scheme; the media query only
     refines, it is never a dependency for legibility. */
  svg{--label:#8c8276;--plate:#a39a8c;--ferric:#997419;}
  @media (prefers-color-scheme: dark){svg{--label:#b3a999;--plate:#8a8175;--ferric:#c99c3e;}}
  .num{fill:var(--ferric);opacity:0;transform-box:fill-box;transform-origin:center;
       animation:rise 1.3s cubic-bezier(.2,.7,.2,1) .1s forwards, breathe 7.5s ease-in-out 1.6s infinite;}
  .plate{fill:var(--plate);}
  .label{fill:var(--label);}
  .g{opacity:0;animation:fade .9s ease-out forwards;}
  .rule{stroke:var(--ferric);stroke-width:1.1;fill:none;
        stroke-dasharray:${ruleLen.toFixed(1)};stroke-dashoffset:${ruleLen.toFixed(1)};
        animation:draw 1.4s cubic-bezier(.4,0,.2,1) .35s forwards;}
  @keyframes rise{from{opacity:0;transform:translateY(9px)}to{opacity:1;transform:translateY(0)}}
  @keyframes breathe{0%,100%{opacity:1}50%{opacity:.8}}
  @keyframes fade{to{opacity:1}}
  @keyframes draw{to{stroke-dashoffset:0}}
]]></style>
<path class="num" d="${num.d}"/>
<g class="plate">${plateGlyphs}</g>
<line class="rule" x1="${colX}" y1="${ruleY}" x2="${ruleX2}" y2="${ruleY}"/>
<g class="label">${labelGlyphs}</g>
</svg>
`;

const outDir = join(here, "out");
mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "plate-01.svg");
writeFileSync(outPath, svg);

const profileAssets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
mkdirSync(profileAssets, { recursive: true });
copyFileSync(outPath, join(profileAssets, "plate-01.svg"));

console.log(`plate-01.svg written (${(svg.length / 1024).toFixed(1)}KB)  num.width=${num.width}  label.width=${label.width}`);
