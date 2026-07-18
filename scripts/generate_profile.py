#!/usr/bin/env python3
"""Generate profile assets with Markdown-first architecture.

Native Markdown carries content. SVG carries only geometry Markdown cannot
express: one signature orbit + one compact language topology.

Usage:
    python3 scripts/generate_profile.py final
    python3 scripts/generate_profile.py all
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.generators.signature import language_topology_compact, project_mark, signature_orbit
from src.generators import compositions as C  # studies only
from src.primitives.themes import DARK, LIGHT


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    print(f"wrote {path.relative_to(ROOT)}")


def generate_studies() -> None:
    out = ROOT / "generated" / "studies"
    write(out / "A-orbit-instrument-light.svg", C.study_a_orbit_instrument(LIGHT))
    write(out / "A-orbit-instrument-dark.svg", C.study_a_orbit_instrument(DARK))
    write(out / "B-spiral-field-light.svg", C.study_b_spiral_field(LIGHT))
    write(out / "B-spiral-field-dark.svg", C.study_b_spiral_field(DARK))
    write(out / "C-trajectory-folio-light.svg", C.study_c_trajectory_folio(LIGHT))
    write(out / "C-trajectory-folio-dark.svg", C.study_c_trajectory_folio(DARK))


def generate_final() -> None:
    for theme in (LIGHT, DARK):
        d = ROOT / "generated" / theme.name
        write(d / "orbit.svg", signature_orbit(theme))
        write(d / "languages.svg", language_topology_compact(theme))
        for i, core in (("01", True), ("02", True), ("03", True), ("04", False)):
            write(d / f"mark-{i}.svg", project_mark(theme, i, core=core))

    write(ROOT / "generated" / "PROFILE_README.md", build_profile_readme())
    generate_preview_html()


def build_profile_readme() -> str:
    """Markdown-first profile. Content once. SVG only for geometry."""
    base = "https://raw.githubusercontent.com/xinyuezhang-shirley/xinyuezhang-shirley/main/assets"

    return f'''# Xinyue Zhang

I design systems that move between computation, language, and human judgment.

<sub>also Shirley · AI systems · agentic systems · HCI · computational design · research</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{base}/orbit-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="{base}/orbit-light.svg">
  <img alt="Echo practice orbit — domains on concentric rings with numbered project observations" src="{base}/orbit-light.svg" width="520">
</picture>

## Selected work

**01 — [Echo](https://github.com/cs146j-26sp/echo)**  
Computational text-art instrument: vortex, orbit, constellation, and imprint modes over analyzed language.  
<sub>`computational design` · course</sub>

**02 — [MuseLab](https://github.com/xinyuezhang-shirley/MuseLab)**  
Literary workshop dossier for manuscript critique, semantic pulse graphs, and generative interpretation.  
<sub>`AI systems` · independent</sub>

**03 — [rag_project](https://github.com/xinyuezhang-shirley/rag_project)**  
Retrieval-augmented generation under real constraints — indexing, retrieval, and answer assembly.  
<sub>`AI systems` · independent</sub>

**04 — [food-recommender](https://github.com/xinyuezhang-shirley/cs278FoodRecommender)**  
Human-centered recommender work: preference, context, and the interface between taste and model output.  
<sub>`HCI` · course</sub>

Also: agentic contracting systems in professional work — described only at portfolio summary level.

## Practice

Work moves across AI and agentic systems, human-computer interaction, computational design, software infrastructure, and research writing. Geometry above places those concerns as bands; projects appear as numbered observations rather than a catalog of cards.

## Language topology

Authored bytes across public repositories (excluding vendored blobs).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{base}/languages-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="{base}/languages-light.svg">
  <img alt="Compact language topology from public repository byte shares" src="{base}/languages-light.svg" width="560">
</picture>

---

<sub>
Orbit geometry from [Echo](https://github.com/cs146j-26sp/echo) · light material from [MuseLab](https://github.com/xinyuezhang-shirley/MuseLab) · source [github-identity-system](https://github.com/xinyuezhang-shirley/github-identity-system)
</sub>
'''


def generate_preview_html() -> None:
    html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Profile preview — Markdown first</title>
<style>
  :root { color-scheme: light dark; }
  body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    background: #0d1117; color: #e6edf3; }
  body.light { background: #ffffff; color: #1f2328; }
  .bar { display:flex; gap:8px; padding:12px 16px; border-bottom:1px solid #30363d; position:sticky; top:0;
    background: inherit; z-index:2; flex-wrap:wrap; align-items:center; font-size:12px; }
  body.light .bar { border-color: #d0d7de; }
  .bar button { background: transparent; color: inherit; border:1px solid #30363d; border-radius:6px;
    padding:6px 10px; cursor:pointer; font-size:12px; }
  body.light .bar button { border-color: #d0d7de; }
  .bar button.active { border-color:#58a6ff; color:#58a6ff; }
  .frame { margin: 24px auto; padding: 0 16px 48px; box-sizing:border-box; line-height:1.6; }
  .frame.w1012 { width: min(1012px, 100%); }
  .frame.w768 { width: min(768px, 100%); }
  .frame.w480 { width: min(480px, 100%); }
  .frame.w360 { width: min(360px, 100%); }
  h1 { font-size: 2em; font-weight: 600; margin: 0 0 0.5em; border-bottom: 1px solid #21262d; padding-bottom: 0.3em; }
  body.light h1 { border-color: #d8dee4; }
  h2 { font-size: 1.35em; font-weight: 600; margin: 1.6em 0 0.6em; border-bottom: 1px solid #21262d; padding-bottom: 0.25em; }
  body.light h2 { border-color: #d8dee4; }
  p { margin: 0 0 1em; }
  sub, .meta { color: #8b949e; } body.light sub, body.light .meta { color: #656d76; }
  code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.9em;
    background: rgba(110,118,129,0.2); padding: 0.15em 0.35em; border-radius: 4px; }
  a { color: #58a6ff; text-decoration: none; } body.light a { color: #0969da; }
  a:hover { text-decoration: underline; }
  img { max-width: 100%; height: auto; display: block; margin: 1em 0 1.4em; }
  hr { border: 0; border-top: 1px solid #21262d; margin: 2em 0; }
  body.light hr { border-color: #d8dee4; }
  .proj { margin: 0 0 1.25em; }
  .proj strong { font-weight: 600; }
</style>
</head>
<body>
<div class="bar">
  <strong>Markdown-first preview</strong>
  <button data-w="w1012" class="active">1012</button>
  <button data-w="w768">768</button>
  <button data-w="w480">480</button>
  <button data-w="w360">360</button>
  <button id="themeBtn">toggle theme</button>
</div>
<div class="frame w1012" id="frame"></div>
<script>
const state = { w: 'w1012', dark: true };
const frame = document.getElementById('frame');
function asset(name) {
  return `../generated/${state.dark ? 'dark' : 'light'}/${name}.svg`;
}
function render() {
  document.body.classList.toggle('light', !state.dark);
  frame.className = 'frame ' + state.w;
  frame.innerHTML = `
    <h1>Xinyue Zhang</h1>
    <p>I design systems that move between computation, language, and human judgment.</p>
    <p><sub>also Shirley · AI systems · agentic systems · HCI · computational design · research</sub></p>
    <img src="${asset('orbit')}" alt="orbit" width="640">
    <h2>Selected work</h2>
    <div class="proj"><p><strong>01 — <a href="#">Echo</a></strong><br>
      Computational text-art instrument: vortex, orbit, constellation, and imprint modes over analyzed language.<br>
      <sub><code>computational design</code> · course</sub></p></div>
    <div class="proj"><p><strong>02 — <a href="#">MuseLab</a></strong><br>
      Literary workshop dossier for manuscript critique, semantic pulse graphs, and generative interpretation.<br>
      <sub><code>AI systems</code> · independent</sub></p></div>
    <div class="proj"><p><strong>03 — <a href="#">rag_project</a></strong><br>
      Retrieval-augmented generation under real constraints — indexing, retrieval, and answer assembly.<br>
      <sub><code>AI systems</code> · independent</sub></p></div>
    <div class="proj"><p><strong>04 — <a href="#">food-recommender</a></strong><br>
      Human-centered recommender work: preference, context, and the interface between taste and model output.<br>
      <sub><code>HCI</code> · course</sub></p></div>
    <p class="meta">Also: agentic contracting systems in professional work — described only at portfolio summary level.</p>
    <h2>Practice</h2>
    <p>Work moves across AI and agentic systems, human-computer interaction, computational design, software infrastructure, and research writing. Geometry above places those concerns as bands; projects appear as numbered observations rather than a catalog of cards.</p>
    <h2>Language topology</h2>
    <p class="meta">Authored bytes across public repositories (excluding vendored blobs).</p>
    <img src="${asset('languages')}" alt="languages" width="640">
    <hr>
    <p><sub>Orbit geometry from Echo · light material from MuseLab · source github-identity-system</sub></p>
  `;
}
document.querySelectorAll('[data-w]').forEach(btn => btn.onclick = () => {
  document.querySelectorAll('[data-w]').forEach(b => b.classList.remove('active'));
  btn.classList.add('active'); state.w = btn.dataset.w; render();
});
document.getElementById('themeBtn').onclick = () => { state.dark = !state.dark; render(); };
render();
</script>
</body>
</html>
'''
    write(ROOT / "previews" / "index.html", html)


def main(argv: list[str]) -> None:
    cmd = argv[1] if len(argv) > 1 else "all"
    if cmd in ("studies", "all"):
        generate_studies()
    if cmd in ("final", "all", "preview"):
        generate_final()


if __name__ == "__main__":
    main(sys.argv)
