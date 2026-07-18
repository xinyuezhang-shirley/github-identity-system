// Phase 5 — mobile legibility check: render the light specimen at 360px wide
// (phone column) and 320px, so the center term can be inspected at card scale.
import { chromium } from "playwright";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const b64 = (p) => "data:image/png;base64," + readFileSync(join(here, "out", p)).toString("base64");
const light = b64("specimen-light.png");
const dark = b64("specimen-dark.png");
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 400, height: 700 }, deviceScaleFactor: 2 });
const html = `<!doctype html><body style="margin:0;background:#fff;font-family:sans-serif">
  <div style="padding:4px 8px;color:#888;font-size:11px">light @ 360px (phone column)</div>
  <img src="${light}" width="360" style="display:block">
  <div style="padding:4px 8px;color:#888;font-size:11px">dark @ 320px</div>
  <img src="${dark}" width="320" style="display:block">
</body>`;
await page.setContent(html, { waitUntil: "load" });
await page.screenshot({ path: join(here, "out", "mobile-check.png") });
await browser.close();
console.log("mobile-check.png written");
