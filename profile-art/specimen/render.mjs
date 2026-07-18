// Phase 3 — Render the specimen from the frozen layout.
// The renderer consumes ONLY layout.json and never modifies positions.
// Dark and light themes differ solely in visual tokens; geometry is identical.
// Output: two PNGs (2x) written into the profile repo assets + a preview copy,
// plus the intermediate SVGs for audit.

import { readFileSync, writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { chromium } from "playwright";
import sharp from "sharp";

const here = dirname(fileURLToPath(import.meta.url));
const layout = JSON.parse(readFileSync(join(here, "out", "layout.json"), "utf8"));
const { width, height } = layout.meta.canvas;

// Single monospace face for both themes so node-label widths are identical and
// the geometry reads the same in dark and light (the word is the data / label).
const FONT = "ui-monospace, 'SF Mono', Menlo, monospace";

const THEMES = {
  dark: {
    // Echo temperament: flat black, neutral, no accent (spec Part 5).
    bg: "#000000",
    bgGradient: null,
    edge: "255,255,255",
    edgeAlphaBase: 0.05,
    edgeAlphaSpan: 0.11,
    node: "255,255,255",
    nodeAlphaBase: 0.34,
    nodeAlphaSpan: 0.5,
    center: "#ffffff",
  },
  light: {
    // MuseLab temperament: warm paper, graphite ink, ferric accent on center.
    bg: "#f0e9dd",
    bgGradient: ["#f4efe6", "#e8dfd2"],
    edge: "107,98,87",
    edgeAlphaBase: 0.08,
    edgeAlphaSpan: 0.16,
    node: "43,38,32",
    nodeAlphaBase: 0.45,
    nodeAlphaSpan: 0.45,
    center: "#8b6914",
  },
};

const nodeByWord = new Map(layout.nodes.map((n) => [n.word, n]));
const maxEdgeWeight = Math.max(...layout.edges.map((e) => e.weight));

function esc(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function buildSvg(theme) {
  const t = THEMES[theme];

  const defs = t.bgGradient
    ? `<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
         <stop offset="0" stop-color="${t.bgGradient[0]}"/>
         <stop offset="1" stop-color="${t.bgGradient[1]}"/>
       </linearGradient></defs>`
    : "";
  const bgFill = t.bgGradient ? "url(#bg)" : t.bg;

  const edges = layout.edges
    .map((e) => {
      const a = nodeByWord.get(e.source);
      const b = nodeByWord.get(e.target);
      if (!a || !b) return "";
      const wN = e.weight / maxEdgeWeight;
      const alpha = (t.edgeAlphaBase + t.edgeAlphaSpan * wN).toFixed(3);
      const sw = (0.6 + wN * 1.4).toFixed(2);
      return `<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="rgba(${t.edge},${alpha})" stroke-width="${sw}"/>`;
    })
    .join("\n");

  const nodes = layout.nodes
    .map((n) => {
      const fill = n.isCenter
        ? t.center
        : `rgba(${t.node},${(t.nodeAlphaBase + t.nodeAlphaSpan * n.importance).toFixed(3)})`;
      const weight = n.isCenter ? 600 : 400;
      return `<text x="${n.x}" y="${n.y}" font-family="${FONT}" font-size="${n.size}" font-weight="${weight}" fill="${fill}" text-anchor="middle" dominant-baseline="central" letter-spacing="0.02em">${esc(n.word)}</text>`;
    })
    .join("\n");

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
${defs}
<rect width="${width}" height="${height}" fill="${bgFill}"/>
<g>${edges}</g>
<g>${nodes}</g>
</svg>`;
}

const outDir = join(here, "out");
mkdirSync(outDir, { recursive: true });

const profileAssets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
mkdirSync(profileAssets, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 2 });

for (const theme of ["dark", "light"]) {
  const svg = buildSvg(theme);
  const svgPath = join(outDir, `specimen-${theme}.svg`);
  writeFileSync(svgPath, svg);

  const html = `<!doctype html><html><head><meta charset="utf-8"><style>
    html,body{margin:0;padding:0}
    #stage{width:${width}px;height:${height}px}
    svg{display:block}
  </style></head><body><div id="stage">${svg}</div></body></html>`;

  await page.setContent(html, { waitUntil: "networkidle" });
  const stage = await page.$("#stage");
  const raw = await stage.screenshot();

  // Palette-quantize + max deflate. The specimen uses very few hues (flat/near-
  // flat background + graphite/off-white text + one accent), so a 256-color
  // palette is lossless to the eye and keeps each PNG well under the size
  // budget (spec Phase 3: ≤ ~400KB). Geometry is untouched — pixels only.
  const pngPath = join(outDir, `specimen-${theme}.png`);
  await sharp(raw)
    .png({ palette: true, quality: 100, effort: 10, compressionLevel: 9 })
    .toFile(pngPath);

  copyFileSync(pngPath, join(profileAssets, `specimen-${theme}.png`));
  const kb = (readFileSync(pngPath).length / 1024).toFixed(0);
  console.log(`rendered ${theme} -> ${pngPath} (${kb}KB)`);
}

await browser.close();
console.log("done");
