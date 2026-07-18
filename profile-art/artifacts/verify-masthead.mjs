// Composition check: render the specimen masthead region (plate -> specimen ->
// caption -> handwritten note) inside a GitHub-width column, on both themes,
// using the real published assets. Writes the mock HTML into the assets dir so
// relative <img> loads are same-origin, then cleans up.

import { chromium } from "playwright";
import { writeFileSync, rmSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const assets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");
const outDir = join(here, "out");

const block = (specimen) => `
  <img src="./plate-01.svg" width="520" style="display:block;max-width:100%">
  <p style="margin:16px 0"><img src="./${specimen}" style="width:100%;display:block"></p>
  <p style="font-style:italic;color:var(--fg);opacity:.85;font-family:Georgia,serif;font-size:15px;line-height:1.6;max-width:100%">A settled field of the words my projects and writing keep returning to. Distance from the center follows importance, not layout; the faint lines are real connections between the words. Paused after settling — an instrument, not an animation.</p>
  <img src="./note-field.svg" width="300" style="display:block;max-width:100%">`;

const browser = await chromium.launch();
async function shot(scheme, bg, fg, specimen, out) {
  const name = `_verify-${scheme}.html`;
  writeFileSync(
    join(assets, name),
    `<!doctype html><body style="margin:0;background:${bg};color:${fg}">
      <div style="max-width:880px;margin:0 auto;padding:40px 32px;--fg:${fg}">
        ${block(specimen)}
      </div></body>`
  );
  const page = await browser.newPage({ deviceScaleFactor: 2, colorScheme: scheme });
  await page.goto("file://" + join(assets, name), { waitUntil: "networkidle" });
  await page.waitForTimeout(3400);
  await page.screenshot({ path: join(outDir, out), fullPage: true });
  await page.close();
  rmSync(join(assets, name));
}

await shot("light", "#ffffff", "#1f2328", "specimen-light.png", "masthead-light.png");
await shot("dark", "#0d1117", "#e6edf3", "specimen-dark.png", "masthead-dark.png");
await browser.close();
console.log("masthead-light.png + masthead-dark.png written");
