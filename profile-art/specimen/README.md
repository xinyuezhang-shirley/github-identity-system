# Specimen — semantic gravity field

Deterministic generator + renderer for the `PLATE 01` figure on the GitHub
profile (`xinyuezhang-shirley/xinyuezhang-shirley`). Implements Part 1.3–1.9 of
the frozen production specification. Every node position is an output of the
procedure; there is no hand placement.

## Regenerate

```bash
# from profile-art/
node corpus/extract.mjs     # Phase 0: sources/*.txt -> corpus/corpus.json
node specimen/generate.mjs  # Phase 2: corpus -> out/layout.json + out/audit.json
node specimen/render.mjs     # Phase 3: layout -> dark/light PNGs (+ copies to profile assets)
```

`render.mjs` writes the two PNGs into `../../xinyuezhang-shirley/assets/`.
Requires a Chromium for Playwright (`npx playwright install chromium`) and
`sharp` for palette compression.

## Contract

- **Deterministic.** Same sources + `SEED` (in `generate.mjs`) → byte-identical
  `layout.json` and PNGs on every run.
- **Auditable.** `out/audit.json` dumps the top-30 terms, their weights, the
  center term, and the full edge list. `out/layout.json` holds the frozen
  positions the renderer consumes.
- **Corpus, not README.** The field is built from the *body of work*
  (`corpus/sources/*.txt` — Echo, MuseLab, Differ, rag, practice statement), not
  from the profile's own copy.
- **Center term is an output**, never chosen. It is currently `system`.

## Files

| Path | Role |
| --- | --- |
| `../corpus/sources/*.txt` | Frozen authored prose (the corpus inputs) |
| `../corpus/stopwords.json` | Standard English stop list + build filler |
| `../corpus/lemma-map.json` | Minimal singular folding |
| `generate.mjs` | Tokenize → nodes → edges → importance → seeded settle |
| `render.mjs` | Layout → two themed PNGs (geometry identical) |
| `verify-mobile.mjs` | Renders the specimen at 320/360px to check phone legibility |
| `out/layout.json`, `out/audit.json` | Frozen layout + audit trail |
