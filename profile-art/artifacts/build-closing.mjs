// Artifact — closing gesture.
// A quiet colophon near the portfolio link: a faint hairline along which a
// single ferric point slowly settles toward the right — the same "settling
// toward a center" thesis as the specimen, turned into a gesture onward. Plays
// once, then a faint pulse. Transparent, theme-aware, static fallback (the
// point at rest at the line's end).

import { writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { svgDoc } from "./lib.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, "out");
const profileAssets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
mkdirSync(outDir, { recursive: true });
mkdirSync(profileAssets, { recursive: true });

const W = 220, H = 20;
const x1 = 6, x2 = 196, y = 10, travel = x2 - x1;

const css = `
  svg{--ink:#8c8276;--ferric:#997419;}
  @media (prefers-color-scheme: dark){svg{--ink:#8a8175;--ferric:#c99c3e;}}
  .rule{stroke:var(--ink);stroke-width:1;opacity:0.4;}
  .dot{fill:var(--ferric);transform-box:fill-box;transform-origin:center;
       animation:travel 4.5s cubic-bezier(.2,.7,.2,1) .3s both, pulse 7s ease-in-out 5.2s infinite;}
  @keyframes travel{from{transform:translateX(-${travel}px);opacity:0}45%{opacity:1}to{transform:translateX(0);opacity:1}}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}`;

const body = `<line class="rule" x1="${x1}" y1="${y}" x2="${x2}" y2="${y}"/>
<circle class="dot" cx="${x2}" cy="${y}" r="3"/>`;

const svg = svgDoc({ w: W, h: H, label: "colophon", css, body });
writeFileSync(join(outDir, "closing.svg"), svg);
copyFileSync(join(outDir, "closing.svg"), join(profileAssets, "closing.svg"));
console.log(`closing.svg written (${(svg.length / 1024).toFixed(1)}KB)`);
