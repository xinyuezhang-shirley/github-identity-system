# Artifacts — living editorial figures

Small authored figures that carry Echo/MuseLab's visual voice into the GitHub
profile. Each is a transparent SVG with vector-outlined type and calm,
seamless, procedural motion (draw · emerge · breathe).

## Why outlines

SVGs shown through GitHub's `<img>` pipeline cannot load external fonts. Text is
therefore converted to vector paths with `opentype.js`, so the real faces
(Cormorant Garamond, IBM Plex Mono, Caveat) render everywhere with no
dependency. CSS animation and `prefers-color-scheme` both work in that context;
`<style>` is wrapped in `<![CDATA[…]]>` so the SVG stays valid XML.

## Fonts (not committed)

Fetch the source faces into `fonts/` (from the Google Fonts repo):

```bash
mkdir -p fonts && cd fonts
base=https://raw.githubusercontent.com/google/fonts/main/ofl
curl -sL -o cormorant.ttf       "$base/cormorantgaramond/CormorantGaramond%5Bwght%5D.ttf"
curl -sL -o caveat.ttf          "$base/caveat/Caveat%5Bwght%5D.ttf"
curl -sL -o plexmono.ttf        "$base/ibmplexmono/IBMPlexMono-Regular.ttf"
curl -sL -o plexmono-medium.ttf "$base/ibmplexmono/IBMPlexMono-Medium.ttf"
```

Caveat ships variable-only and `opentype.js` mis-reads some of its variable
glyphs (e.g. lowercase `s`), so instance it to a static weight:

```bash
python3 -m fontTools.varLib.instancer fonts/caveat.ttf wght=500 -o fonts/caveat-static.ttf
```

## Build & preview

```bash
node build-plate.mjs          # -> out/plate-01.svg (+ copy to profile assets)
node preview.mjs plate-01.svg 560   # -> out/preview-light.png / preview-dark.png
```

`preview.mjs` embeds the SVG as an `<img>` on warm-paper and GitHub-dark grounds
and screenshots the settled state, so composition and both themes can be
audited the way GitHub renders them.

## Figures

| File | Role | Motion |
| --- | --- | --- |
| `build-header.mjs` → `wordmark-{light,dark}.svg` | Identity wordmark inside the `<h1>` (paired) | writes in |
| `build-plate.mjs` → `plate-01.svg` | Plate 01 masthead for the specimen | draw · emerge · breathe |
| `build-plate.mjs` → `plate-02.svg` | Plate 02 folio opening Selected work | static |
| `build-note.mjs` → `note-field.svg` | Handwritten field-note under the caption | writes in · breathe |
| `build-marks.mjs` → `mark-{echo,muselab,differ,rag}.svg` | Inline project sigils | static |
| `build-closing.mjs` → `closing.svg` | Colophon near the portfolio link | settle · pulse |

Helpers & checks:

| File | Role |
| --- | --- |
| `lib.mjs` | Font loading, text→outline layout, `svgDoc` (CDATA + reduced-motion guard) |
| `preview.mjs` | Two-theme `<img>`-context preview of one asset |
| `gallery.mjs` | Two-theme preview of the whole asset family |
| `verify-readme.mjs` | Full-README reconstruction at desktop + mobile widths |

Animation budget: four animated elements across the profile (wordmark, Plate 01,
field-note, closing). Every animated asset defaults to its resting/visible state
and only plays in, so it survives when motion is stripped (reduced-motion or a
renderer that ignores SVG animation). The specimen and marks are static.
