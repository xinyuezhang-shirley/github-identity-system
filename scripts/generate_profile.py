#!/usr/bin/env python3
"""Generate composition studies and final GitHub profile SVG assets.

Usage:
    python3 scripts/generate_profile.py studies
    python3 scripts/generate_profile.py final
    python3 scripts/generate_profile.py all
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.generators import compositions as C
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
        write(d / "hero.svg", C.profile_hero(theme))
        write(d / "observations.svg", C.profile_observations(theme))
        write(d / "languages.svg", C.profile_languages(theme))
        write(d / "signal.svg", C.profile_signal(theme))

    # also stage a ready-to-copy profile README draft in generated/
    readme = build_profile_readme()
    write(ROOT / "generated" / "PROFILE_README.md", readme)


def build_profile_readme() -> str:
    # Absolute asset URLs help GitHub’s profile surface resolve images
    # immediately after a brand-new special repository is created.
    base = "https://raw.githubusercontent.com/xinyuezhang-shirley/xinyuezhang-shirley/main/assets"
    return f'''# Xinyue Zhang

<!-- computational field guide — geometry from Echo orbit, material from MuseLab / Echo -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{base}/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="{base}/hero-light.svg">
  <img alt="Computational field guide for Xinyue Zhang — Echo orbit of practice domains with numbered project observations" src="{base}/hero-light.svg" width="100%">
</picture>

<p align="center">
  <sub>
    <code>AI systems</code>&nbsp;·&nbsp;
    <code>agentic systems</code>&nbsp;·&nbsp;
    <code>HCI</code>&nbsp;·&nbsp;
    <code>computational design</code>&nbsp;·&nbsp;
    <code>software</code>&nbsp;·&nbsp;
    <code>research</code>
  </sub>
</p>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{base}/observations-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="{base}/observations-light.svg">
  <img alt="Indexed observations of selected projects — Echo, MuseLab, rag_project, and related work — with domain and provenance annotations" src="{base}/observations-light.svg" width="100%">
</picture>

### Links

| # | Project | Notes |
|---|---------|-------|
| 01 | [Echo](https://github.com/cs146j-26sp/echo) | Computational text-art instrument |
| 02 | [MuseLab](https://github.com/xinyuezhang-shirley/MuseLab) | Literary workshop dossier |
| 03 | [rag_project](https://github.com/xinyuezhang-shirley/rag_project) | Retrieval-augmented generation |
| 04 | [food-recommender](https://github.com/xinyuezhang-shirley/cs278FoodRecommender) | Human-centered recommender work |
| 05 | [cs229-final](https://github.com/xinyuezhang-shirley/cs229FinalProject) | Machine-learning research project |
| 06 | [weibo-topic-scraper](https://github.com/xinyuezhang-shirley/williamest-topic-scraper-weibo) | Social-text collection infrastructure |

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{base}/languages-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="{base}/languages-light.svg">
  <img alt="Language topology from real GitHub byte shares on polar rings — TypeScript and Jupyter lead; cs340Project4 excluded as vendored" src="{base}/languages-light.svg" width="100%">
</picture>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{base}/signal-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="{base}/signal-light.svg">
  <img alt="Unsmoothed 53-week contribution signal from the GitHub contribution calendar" src="{base}/signal-light.svg" width="100%">
</picture>

---

<sub>
Geometry adapted from <a href="https://github.com/cs146j-26sp/echo">Echo</a> orbit/vortex systems.
Light material language from <a href="https://github.com/xinyuezhang-shirley/MuseLab">MuseLab</a>.
Generated from the <a href="https://github.com/xinyuezhang-shirley/github-identity-system">github-identity-system</a> workspace.
</sub>
'''


def generate_preview_html() -> None:
    """Local preview approximating GitHub content width."""
    html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Profile preview</title>
<style>
  :root { color-scheme: light dark; }
  body { margin: 0; background: #0d1117; color: #e6edf3; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
  .bar { display:flex; gap:8px; padding:12px 16px; border-bottom:1px solid #30363d; position:sticky; top:0; background:#0d1117; z-index:2; flex-wrap:wrap; align-items:center; }
  .bar button { background:#21262d; color:#e6edf3; border:1px solid #30363d; border-radius:6px; padding:6px 10px; cursor:pointer; font-size:12px; }
  .bar button.active { border-color:#58a6ff; color:#58a6ff; }
  .frame { margin: 24px auto; background: #ffffff; color:#1f2328; border:1px solid #d0d7de; border-radius:6px; padding: 32px 24px; box-sizing:border-box; }
  body.dark .frame { background:#0d1117; color:#e6edf3; border-color:#30363d; }
  .frame.w1012 { width: min(1012px, 100%); }
  .frame.w768 { width: min(768px, 100%); }
  .frame.w480 { width: min(480px, 100%); }
  .frame.w360 { width: min(360px, 100%); }
  img { max-width:100%; height:auto; display:block; margin: 0 0 20px; }
  table { width:100%; border-collapse: collapse; font-size:14px; margin: 12px 0 28px; }
  th, td { border-top:1px solid #d0d7de; padding:8px; text-align:left; }
  body.dark th, body.dark td { border-color:#30363d; }
  a { color: #0969da; } body.dark a { color:#58a6ff; }
  sub, .meta { color:#656d76; } body.dark sub, body.dark .meta { color:#8b949e; }
  .studies img { margin-bottom:40px; border:1px solid #d0d7de; }
  body.dark .studies img { border-color:#30363d; }
</style>
</head>
<body class="dark">
<div class="bar">
  <strong style="margin-right:8px">Preview</strong>
  <button data-w="w1012" class="active">1012</button>
  <button data-w="w768">768</button>
  <button data-w="w480">480</button>
  <button data-w="w360">360</button>
  <button id="themeBtn">toggle theme</button>
  <button data-view="final" class="active">final</button>
  <button data-view="studies">studies</button>
</div>
<div class="frame w1012" id="frame"></div>
<script>
const light = matchMedia('(prefers-color-scheme: light)');
const state = { w: 'w1012', view: 'final', dark: true };
const frame = document.getElementById('frame');

function asset(name) {
  const mode = state.dark ? 'dark' : 'light';
  return `../generated/${mode}/${name}.svg`;
}

function renderFinal() {
  const mode = state.dark ? 'dark' : 'light';
  frame.innerHTML = `
    <img src="${asset('hero')}" alt="hero">
    <p style="text-align:center"><sub><code>AI systems</code> · <code>agentic systems</code> · <code>HCI</code> · <code>computational design</code> · <code>software</code> · <code>research</code></sub></p>
    <img src="${asset('observations')}" alt="observations">
    <h3>Links</h3>
    <table>
      <tr><th>#</th><th>Project</th><th>Notes</th></tr>
      <tr><td>01</td><td>Echo</td><td>Computational text-art instrument</td></tr>
      <tr><td>02</td><td>MuseLab</td><td>Literary workshop dossier</td></tr>
      <tr><td>03</td><td>rag_project</td><td>Retrieval-augmented generation</td></tr>
    </table>
    <img src="${asset('languages')}" alt="languages">
    <img src="${asset('signal')}" alt="signal">
    <p class="meta"><sub>Geometry from Echo · material from ${mode === 'dark' ? 'Echo night' : 'MuseLab paper'}</sub></p>
  `;
}

function renderStudies() {
  const mode = state.dark ? 'dark' : 'light';
  frame.innerHTML = `<div class="studies">
    <h2>Study A — Orbit Instrument</h2>
    <img src="../generated/studies/A-orbit-instrument-${mode}.svg">
    <h2>Study B — Spiral Field Notes</h2>
    <img src="../generated/studies/B-spiral-field-${mode}.svg">
    <h2>Study C — Trajectory Folio</h2>
    <img src="../generated/studies/C-trajectory-folio-${mode}.svg">
  </div>`;
}

function render() {
  document.body.classList.toggle('dark', state.dark);
  frame.className = 'frame ' + state.w;
  if (state.view === 'studies') renderStudies(); else renderFinal();
}

document.querySelectorAll('[data-w]').forEach(btn => btn.onclick = () => {
  document.querySelectorAll('[data-w]').forEach(b => b.classList.remove('active'));
  btn.classList.add('active'); state.w = btn.dataset.w; render();
});
document.querySelectorAll('[data-view]').forEach(btn => btn.onclick = () => {
  document.querySelectorAll('[data-view]').forEach(b => b.classList.remove('active'));
  btn.classList.add('active'); state.view = btn.dataset.view; render();
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
    if cmd in ("final", "all"):
        generate_final()
    if cmd in ("preview", "all", "final", "studies"):
        generate_preview_html()


if __name__ == "__main__":
    main(sys.argv)
