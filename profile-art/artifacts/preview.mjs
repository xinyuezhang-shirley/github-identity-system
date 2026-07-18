// Preview any artifact SVG on light + dark grounds (to check transparency,
// theme colors, and composition). Renders the FINAL animation state.
// Usage: node preview.mjs plate-01.svg [width]
import { chromium } from "playwright";
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const file = process.argv[2] || "plate-01.svg";
const dispW = Number(process.argv[3] || 520);
const outDir = join(here, "out");

// Embed exactly as GitHub does: an <img> pointing at the SVG (same-origin file,
// so the <img> loads; external fonts blocked, CSS animation running).
const browser = await chromium.launch();

async function shot(bg, scheme, label, out) {
  const htmlName = `_preview-${scheme}.html`;
  writeFileSync(
    join(outDir, htmlName),
    `<!doctype html><body style="margin:0;width:${dispW + 52}px;background:${bg}">
       <div style="padding:24px 26px">
         <div style="font:11px -apple-system,sans-serif;color:#888;margin-bottom:10px">${label}</div>
         <img src="./${file}" style="width:${dispW}px;height:auto">
       </div></body>`
  );
  const page = await browser.newPage({ deviceScaleFactor: 2, colorScheme: scheme });
  await page.goto("file://" + join(outDir, htmlName), { waitUntil: "networkidle" });
  await page.waitForTimeout(3200); // let intro settle
  await page.screenshot({ path: join(outDir, out), fullPage: true });
  await page.close();
}

await shot("#f4efe6", "light", "on warm paper · light OS", "preview-light.png");
await shot("#0d1117", "dark", "on GitHub dark · dark OS", "preview-dark.png");
await browser.close();
console.log("preview-light.png + preview-dark.png written");
