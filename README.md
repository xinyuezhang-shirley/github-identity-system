# github-identity-system

Development workspace for Xinyue Zhang’s generative identity.
Public surface: [`xinyuezhang-shirley/xinyuezhang-shirley`](https://github.com/xinyuezhang-shirley/xinyuezhang-shirley).

## Architecture

**Markdown carries content. SVG carries only geometry Markdown cannot express.**

The public README is a continuous editorial document:

1. Native name + introduction  
2. One transparent signature orbit (Echo gravity)  
3. Native selected-work list (numbered, linked)  
4. Native practice note  
5. One compact language topology  

No full-width poster panels. No duplicated project lists. No opaque canvases.

## Generate / publish

```bash
python3 scripts/generate_profile.py final
python3 -m http.server 8765   # /previews/index.html
python3 scripts/publish_profile.py ../xinyuezhang-shirley
```

## Source lineage

| Piece | Origin |
|-------|--------|
| Orbit geometry | `echo/frontend/helperJS/vortex.js` (`placeOrbitRing`) |
| Light strokes / accent | MuseLab paper tokens |
| Dark strokes | Echo night neutrals on transparent |
| Live language data | `assets/generated/languages.json` |
