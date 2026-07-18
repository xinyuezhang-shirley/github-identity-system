// Gallery preview: all new assets on both themes, marks shown inline with
// sample text to check baseline alignment and mobile legibility.
import { chromium } from "playwright";
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, "out");

const row = (label, html) =>
  `<div style="margin:14px 0"><div style="font:10px -apple-system,sans-serif;color:#888;margin-bottom:6px">${label}</div>${html}</div>`;
const mark = (f, word) =>
  `<p style="font:16px Georgia,serif;color:var(--fg);margin:4px 0"><img src="./${f}" height="20" align="middle"> ${word}</p>`;

const content = `
  ${row("header wordmark (h1)", `<img src="./wordmark-THEME.svg" width="300">`)}
  ${row("plate 02 (static folio)", `<img src="./plate-02.svg" width="480">`)}
  ${row("project marks inline", `
    ${mark("mark-echo.svg", "Echo — text becomes living visual fields.")}
    ${mark("mark-muselab.svg", "MuseLab — a workshop that reads a draft.")}
    ${mark("mark-differ.svg", "Differ — where an experience breaks down.")}
    ${mark("mark-rag.svg", "rag_project — retrieval held to real constraints.")}`)}
  ${row("closing gesture", `<img src="./closing.svg" width="200">`)}`;

const browser = await chromium.launch();
async function shot(scheme, bg, fg, out) {
  const name = `_gallery-${scheme}.html`;
  writeFileSync(
    join(outDir, name),
    `<!doctype html><body style="margin:0;background:${bg};color:${fg}">
      <div style="max-width:640px;padding:32px;--fg:${fg}">${content.replaceAll("THEME", scheme)}</div>
    </body>`
  );
  const page = await browser.newPage({ deviceScaleFactor: 2, colorScheme: scheme });
  await page.goto("file://" + join(outDir, name), { waitUntil: "networkidle" });
  await page.waitForTimeout(3200);
  await page.screenshot({ path: join(outDir, out), fullPage: true });
  await page.close();
}
await shot("light", "#ffffff", "#1f2328", "gallery-light.png");
await shot("dark", "#0d1117", "#e6edf3", "gallery-dark.png");
await browser.close();
console.log("gallery-light.png + gallery-dark.png written");
