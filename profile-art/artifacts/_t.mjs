import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { fonts, layoutGlyphs } from "./lib.mjs";
const here = dirname(fileURLToPath(import.meta.url));
for (const [name, txt] of [["t-shape","shape"],["t-ss","s s s"],["t-word","the shape"]]) {
  const { glyphs, width } = layoutGlyphs(fonts.caveat, txt, 58, 10, 76, 0);
  const W = Math.ceil(width + 20);
  const paths = glyphs.map((g,i)=>`<path fill="#333" d="${g.d}"/>`).join("");
  writeFileSync(join(here,"out",name+".svg"),
   `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="115" viewBox="0 0 ${W} 115">${paths}</svg>`);
}
console.log("ok");
