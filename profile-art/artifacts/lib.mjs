// Shared helpers for authored typographic figures.
// Text is converted to vector outlines (opentype.js) because SVGs shown through
// GitHub's <img> pipeline cannot load external fonts. Outlines keep the real
// faces (Cormorant Garamond, IBM Plex Mono, Caveat) crisp, dependency-free, and
// animatable via inline CSS.

import opentype from "opentype.js";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const fontDir = join(here, "fonts");

function load(name) {
  const buf = readFileSync(join(fontDir, name));
  return opentype.parse(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength));
}

export const fonts = {
  cormorant: load("cormorant.ttf"),
  mono: load("plexmono.ttf"),
  monoMedium: load("plexmono-medium.ttf"),
  // Caveat is variable-only from Google Fonts; opentype.js mis-reads some of its
  // variable glyphs (e.g. lowercase s). Use a static instance (wght=500),
  // produced with: python3 -m fontTools.varLib.instancer caveat.ttf wght=500 -o caveat-static.ttf
  caveat: load("caveat-static.ttf"),
};

const round = (n) => Math.round(n * 100) / 100;

// Lay out a string as individual glyphs so each can be animated on its own.
// Returns { glyphs: [{d, cx}], width } with paths already positioned at (x,y).
export function layoutGlyphs(font, text, fontSize, x, y, trackingEm = 0) {
  const scale = fontSize / font.unitsPerEm;
  const tracking = trackingEm * fontSize;
  let cursor = x;
  const glyphs = [];
  for (const ch of text) {
    const glyph = font.charToGlyph(ch);
    const advance = glyph.advanceWidth * scale;
    if (ch !== " ") {
      const p = glyph.getPath(cursor, y, fontSize);
      const d = p.toPathData(2);
      if (d) glyphs.push({ d, cx: round(cursor + advance / 2) });
    }
    cursor += advance + tracking;
  }
  return { glyphs, width: round(cursor - tracking - x) };
}

// Single combined path (no per-glyph animation), positioned at (x,y).
export function textPath(font, text, fontSize, x, y, trackingEm = 0) {
  if (!trackingEm) {
    return { d: font.getPath(text, x, y, fontSize).toPathData(2), width: round(font.getAdvanceWidth(text, fontSize)) };
  }
  const { glyphs, width } = layoutGlyphs(font, text, fontSize, x, y, trackingEm);
  return { d: glyphs.map((g) => g.d).join(" "), width };
}

// Every animated figure must have a static fallback: elements default to their
// *resting* (visible) state, and animation only plays them in. This guard also
// honors reduced-motion. If motion is ever stripped, the settled artifact shows.
export const REDUCED_MOTION =
  "@media(prefers-reduced-motion:reduce){*{animation:none!important}}";

export function esc(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// Wrap body markup in a valid, GitHub-<img>-safe SVG: CDATA style (so `<`/`&`
// in CSS never break XML) plus the reduced-motion guard.
export function svgDoc({ w, h, label, css = "", body }) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(label)}">
<style><![CDATA[
${css}
${REDUCED_MOTION}
]]></style>
${body}
</svg>
`;
}

export function measure(font, text, fontSize, trackingEm = 0) {
  if (!trackingEm) return round(font.getAdvanceWidth(text, fontSize));
  const scale = fontSize / font.unitsPerEm;
  let w = 0;
  for (const ch of text) w += font.charToGlyph(ch).advanceWidth * scale + trackingEm * fontSize;
  return round(w - trackingEm * fontSize);
}
