// Artifacts — project marks.
// Four small stroke sigils, one per work, in a shared 40x40 grammar (neutral
// structure + a single ferric accent). Each encodes the idea of its project,
// not its name (the name/description stay in Markdown). Static — they are their
// own fallback. Theme-aware with mid-tone colors legible on both grounds.

import { writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { svgDoc } from "./lib.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, "out");
const profileAssets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
mkdirSync(outDir, { recursive: true });
mkdirSync(profileAssets, { recursive: true });

const S = 40;
const COLORS = `
  svg{--ink:#7d746a;--ferric:#997419;}
  @media (prefers-color-scheme: dark){svg{--ink:#a89e90;--ferric:#c99c3e;}}
  .ink{stroke:var(--ink);stroke-width:1.7;fill:none;stroke-linecap:round;stroke-linejoin:round;}
  .fer{stroke:var(--ferric);stroke-width:1.7;fill:none;stroke-linecap:round;stroke-linejoin:round;}
  .ferf{fill:var(--ferric);}`;

const D = (r) => (r * Math.PI) / 180;
// right-facing arc centered at (cx,cy)
function arc(cx, cy, r, aDeg) {
  const a = D(aDeg);
  const x1 = (cx + r * Math.cos(-a)).toFixed(2), y1 = (cy + r * Math.sin(-a)).toFixed(2);
  const x2 = (cx + r * Math.cos(a)).toFixed(2), y2 = (cy + r * Math.sin(a)).toFixed(2);
  return `M${x1} ${y1} A${r} ${r} 0 0 1 ${x2} ${y2}`;
}

const MARKS = {
  // Echo — reverberation emanating into a field: a source point, ripples opening.
  "mark-echo.svg": {
    label: "Echo",
    body: `
<circle class="ferf" cx="11" cy="20" r="2.4"/>
<path class="ink" d="${arc(11, 20, 9, 58)}" opacity="0.85"/>
<path class="ink" d="${arc(11, 20, 15, 58)}" opacity="0.55"/>
<path class="ink" d="${arc(11, 20, 21, 58)}" opacity="0.32"/>`,
  },
  // MuseLab — reading a draft: lines of text with a ferric margin annotation.
  "mark-muselab.svg": {
    label: "MuseLab",
    body: `
<path class="fer" d="M12 12 L12 28"/>
<path class="fer" d="M12 20 l3 -2.5 M12 20 l3 2.5"/>
<path class="ink" d="M18 13 H32" opacity="0.85"/>
<path class="ink" d="M18 20 H30" opacity="0.7"/>
<path class="ink" d="M18 27 H27" opacity="0.55"/>`,
  },
  // Differ — divergence across contexts: one path forking into two.
  "mark-differ.svg": {
    label: "Differ",
    body: `
<path class="ink" d="M7 20 H20"/>
<path class="ink" d="M20 20 L33 11"/>
<path class="ink" d="M20 20 L33 29"/>
<circle class="ferf" cx="20" cy="20" r="2.4"/>`,
  },
  // rag_project — retrieval held within constraints: an item drawn into a frame.
  "mark-rag.svg": {
    label: "rag_project",
    body: `
<path class="ink" d="M16 11 H13 V29 H16"/>
<path class="ink" d="M28 11 H31 V29 H28"/>
<circle class="ferf" cx="22" cy="20" r="2.4"/>
<path class="fer" d="M4 20 H12"/>
<path class="fer" d="M9 17 l3 3 l-3 3"/>`,
  },
};

for (const [file, { label, body }] of Object.entries(MARKS)) {
  const svg = svgDoc({ w: S, h: S, label, css: COLORS, body });
  writeFileSync(join(outDir, file), svg);
  copyFileSync(join(outDir, file), join(profileAssets, file));
  console.log(`${file} written (${(svg.length / 1024).toFixed(1)}KB)`);
}
