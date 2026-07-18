// Full-README verification: reconstruct the profile in a GitHub-ish column and
// screenshot desktop + mobile widths on both themes, using the real published
// assets. Checks composition, density (native Markdown vs authored assets), and
// mobile legibility of the inline marks.

import { chromium } from "playwright";
import { writeFileSync, rmSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const assets = join(here, "..", "..", "..", "xinyuezhang-shirley", "assets");

const wm = (s) => `wordmark-${s}.svg`;
const sp = (s) => `specimen-${s}.png`;

const doc = (scheme) => `
  <h1 style="margin:.2em 0"><img src="./${wm(scheme)}" width="320"></h1>
  <p><code>also Shirley</code></p>
  <p style="font-size:16px">I design systems that preserve meaning as it moves between people, language, and computation.</p>
  <p><code>language · agents · human-computer interaction · computational design</code></p>
  <hr>
  <img src="./plate-01.svg" width="520" style="max-width:100%">
  <p><img src="./${sp(scheme)}" style="width:100%"></p>
  <p style="font-style:italic;opacity:.85;font-family:Georgia,serif">A settled field of the words my projects and writing keep returning to. Distance from the center follows importance, not layout; the faint lines are real connections between the words. Paused after settling — an instrument, not an animation.</p>
  <img src="./note-field.svg" width="300" style="max-width:100%">
  <hr>
  <img src="./plate-02.svg" width="480" style="max-width:100%">
  <h2>Selected work</h2>
  <p><img src="./mark-echo.svg" height="22" align="middle"> Echo — text becomes living visual fields.</p>
  <p><img src="./mark-muselab.svg" height="22" align="middle"> <a href="#">MuseLab</a> — a workshop that reads a draft instead of rewriting it.</p>
  <p><img src="./mark-differ.svg" height="22" align="middle"> Differ — where a designed experience breaks down across who and where.</p>
  <p><img src="./mark-rag.svg" height="22" align="middle"> <a href="#">rag_project</a> — retrieval and agents held to real constraints.</p>
  <hr>
  <h2>Current questions</h2>
  <p>How does meaning survive when a model has to speak for someone?</p>
  <p>Where do universal measures quietly stop meaning the same thing?</p>
  <p>What is left of language after the sentence ends?</p>
  <hr>
  <h2>Reading the work</h2>
  <p>Live instruments and notes → <a href="#">portfolio</a></p>
  <p>Echo · MuseLab · writing</p>
  <img src="./closing.svg" width="200">`;

const browser = await chromium.launch();
async function shot(scheme, width, bg, fg, out) {
  const name = `_readme-${out}.html`;
  writeFileSync(
    join(assets, name),
    `<!doctype html><body style="margin:0;background:${bg};color:${fg};font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;line-height:1.6">
       <div style="max-width:${width}px;margin:0 auto;padding:32px 16px">${doc(scheme)}</div>
       <style>hr{border:0;border-top:1px solid ${scheme === "dark" ? "#30363d" : "#d8d4cc"};margin:24px 0}
              a{color:${scheme === "dark" ? "#4493f8" : "#0969da"}}
              code{background:${scheme === "dark" ? "#161b22" : "#eff1f3"};padding:2px 6px;border-radius:5px;font-size:13px}
              h2{border-bottom:1px solid ${scheme === "dark" ? "#21262d" : "#d8d4cc"};padding-bottom:.3em}</style>
     </body>`
  );
  const page = await browser.newPage({ deviceScaleFactor: 2, colorScheme: scheme });
  await page.goto("file://" + join(assets, name), { waitUntil: "networkidle" });
  await page.waitForTimeout(3400);
  await page.screenshot({ path: join(here, "out", out), fullPage: true });
  await page.close();
  rmSync(join(assets, name));
}

await shot("light", 860, "#ffffff", "#1f2328", "readme-desktop-light.png");
await shot("dark", 860, "#0d1117", "#e6edf3", "readme-desktop-dark.png");
await shot("dark", 380, "#0d1117", "#e6edf3", "readme-mobile-dark.png");
await browser.close();
console.log("readme desktop light/dark + mobile dark written");
