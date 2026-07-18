// Artifacts — plate mastheads.
// Exhibition-catalogue plate headers in a shared grammar: an oversized Cormorant
// numeral, a ferric hairline, and a Plex Mono kicker. Plate 01 heads the
// specimen and plays in (draw · emerge · breathe); Plate 02 is a quiet static
// folio that opens the Selected-work section. Transparent, vector outlines,
// theme-aware, with a static resting fallback.

import { writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { fonts, layoutGlyphs, textPath, svgDoc } from "./lib.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, "out");
const profileAssets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
mkdirSync(outDir, { recursive: true });
mkdirSync(profileAssets, { recursive: true });

const W = 900;
const H = 150;

const COLORS = `
  svg{--label:#8c8276;--plate:#a39a8c;--ferric:#997419;}
  @media (prefers-color-scheme: dark){svg{--label:#b3a999;--plate:#8a8175;--ferric:#c99c3e;}}`;

function build({ file, numText, kicker, label, animated }) {
  const numSize = 132;
  const num = textPath(fonts.cormorant, numText, numSize, 4, 118);
  const colX = 4 + num.width + 46;
  const plate = layoutGlyphs(fonts.mono, "PLATE", 15, colX, 46, 0.34);
  const ruleY = 66;
  const ruleX2 = W - 6;
  const ruleLen = ruleX2 - colX;
  const kick = layoutGlyphs(fonts.monoMedium, kicker, 20, colX, 108, 0.3);

  // Base states are the *resting* (visible) state so the artifact is complete
  // without motion; animation only plays elements in.
  const css = animated
    ? `${COLORS}
  .num{fill:var(--ferric);transform-box:fill-box;transform-origin:center;
       animation:rise 1.3s cubic-bezier(.2,.7,.2,1) .1s both, breathe 7.5s ease-in-out 1.6s infinite;}
  .plate{fill:var(--plate);}
  .label{fill:var(--label);}
  .g{opacity:1;animation:fade .9s ease-out both;}
  .rule{stroke:var(--ferric);stroke-width:1.1;fill:none;stroke-dasharray:${ruleLen.toFixed(1)};stroke-dashoffset:0;
        animation:draw 1.4s cubic-bezier(.4,0,.2,1) .35s both;}
  @keyframes rise{from{opacity:0;transform:translateY(9px)}to{opacity:1;transform:translateY(0)}}
  @keyframes breathe{0%,100%{opacity:1}50%{opacity:.8}}
  @keyframes fade{from{opacity:0}to{opacity:1}}
  @keyframes draw{from{stroke-dashoffset:${ruleLen.toFixed(1)}}to{stroke-dashoffset:0}}`
    : `${COLORS}
  .num{fill:var(--ferric);}
  .plate{fill:var(--plate);}
  .label{fill:var(--label);}
  .rule{stroke:var(--ferric);stroke-width:1.1;fill:none;}`;

  const plateGlyphs = plate.glyphs
    .map((g, i) => animated
      ? `<path class="g" style="animation-delay:${(0.15 + i * 0.05).toFixed(2)}s" d="${g.d}"/>`
      : `<path d="${g.d}"/>`)
    .join("");
  const kickGlyphs = kick.glyphs
    .map((g, i) => animated
      ? `<path class="g" style="animation-delay:${(1.0 + i * 0.045).toFixed(2)}s" d="${g.d}"/>`
      : `<path d="${g.d}"/>`)
    .join("");

  const body = `<path class="num" d="${num.d}"/>
<g class="plate">${plateGlyphs}</g>
<line class="rule" x1="${colX}" y1="${ruleY}" x2="${ruleX2}" y2="${ruleY}"/>
<g class="label">${kickGlyphs}</g>`;

  const svg = svgDoc({ w: W, h: H, label, css, body });
  writeFileSync(join(outDir, file), svg);
  copyFileSync(join(outDir, file), join(profileAssets, file));
  console.log(`${file} written (${(svg.length / 1024).toFixed(1)}KB) ${animated ? "animated" : "static"}`);
}

build({
  file: "plate-01.svg",
  numText: "01",
  kicker: "SEMANTIC GRAVITY FIELD",
  label: "Plate 01 — semantic gravity field",
  animated: true,
});

build({
  file: "plate-02.svg",
  numText: "02",
  kicker: "FOUR SYSTEMS",
  label: "Plate 02 — four systems",
  animated: false,
});
