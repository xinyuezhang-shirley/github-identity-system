# github-identity-system

Development workspace for a generative visual identity whose first public
artifact is the GitHub profile README for **Xinyue Zhang**
(`xinyuezhang-shirley`).

This repository is **not** the public profile. The finished surface lives in
[`xinyuezhang-shirley/xinyuezhang-shirley`](https://github.com/xinyuezhang-shirley/xinyuezhang-shirley).

## Direction

**Computational Field Guide** — Echo orbit (`placeOrbitRing`) as the visual
spine; MuseLab paper tokens for light mode; Echo night for dark mode.

See `docs/study-evaluation.md` (Studies A/B/C) and `docs/design-dna.md`.

## Generate

```bash
python3 scripts/generate_profile.py all
python3 -m http.server 8765   # open /previews/index.html
```

## Publish into the profile repo

```bash
python3 scripts/publish_profile.py ../xinyuezhang-shirley
```

## Source lineage

| System | Origin |
|--------|--------|
| Orbit / vortex math | `echo/frontend/helperJS/vortex.js` |
| Light tokens | `MuseLab/frontend/src/index.css` |
| Dark tokens | `echo/frontend/styles.css` |
| Live GitHub data | `scripts/fetch_github_data.py` → `assets/generated/` |

## Layout

```
src/data/           curated identity + observations
src/primitives/     Echo orbit/vortex + themes
src/generators/     SVG compositions
scripts/            fetch / generate / publish
generated/          light + dark SVG panels + PROFILE_README.md
previews/           local GitHub-width preview
docs/               design DNA, study evaluation
prototypes/         earlier Direction B–E sketches (superseded)
```
