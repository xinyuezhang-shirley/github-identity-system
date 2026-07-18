# Portfolio Curation Plan

**Status:** Internal curatorial document — the archivist's blueprint, not a build spec
**Role of this document:** Discover the body of work that already exists, understand it, name what is missing, and specify the artifacts to gather *before* any visual redesign begins.
**Companion documents:** [`Design Anthropology of Xinyue Zhang.md`](./Design%20Anthropology%20of%20Xinyue%20Zhang.md) · [`Negative Space.md`](./Negative%20Space.md) · [`design-dna.md`](./design-dna.md)

> The point is not to decorate a website. The point is to assemble an exhibition whose organizing idea — *systems that preserve meaning as it moves between people, language, and computation* — is legible before a single page is designed. When the collection is complete, the portfolio should feel **inevitable rather than assembled.**

---

## 0. Curatorial thesis (the frame around every room)

Everything in this archive answers one obsession in different dialects:

> **How does meaning survive the trip between a person, their language, and a machine — and how do we keep that survival *visible* instead of hiding it inside a score or a pretty surface?**

Three axes run through the collection at once (from the anthropology, corrected 2026-07-17):

1. **Fidelity / contested meaning** — machines that must show their work when they speak for or with humans.
2. **Beauty through structure** — computation that feels inevitable when you pause it, never ornament bolted on.
3. **Emotional resonance** — systems exist to *hold* human experience (memory, voice, longing, ambiguity), not to be clever in isolation.

The recurring imagery is remarkably stable and should become the exhibition's visual grammar:

- **The field** — words as bodies with gravity: constellation, vortex, orbit, drift, settlement (Echo, MuseLab Pulse/Imprint, dream graph, GitHub specimen).
- **The dossier** — the archive box, the folio, the manuscript, the registration stamp, the receipt (MuseLab).
- **The private symbol set** — house, ocean, mother, stairs, water, door, train, teeth, mirror (dreams) — the emotional substrate under all the instruments.
- **Material honesty** — paper, graphite, ferric ink, hairline rule, photocopy grain; never glass, gradient, or card.
- **Afterlife / residue / imprint** — what language becomes after the sentence ends.

Emotional register throughout: **restrained melancholy + procedural seriousness.** Interfaces that feel like archives, workshops, and museums of memory — never dashboards.

**The single most important curatorial move:** the collection currently *tells* people she is a literary creative-coder (Echo, MuseLab, poetry, dreams) and *under-tells* the fidelity-under-uncertainty twin (Differ, Tesla, Airbnb calibration, POMDP, RAG evaluation). Both halves are the same mind asking the same question. The exhibition must make that one argument once, clearly.

---

## 1. Current Archive

Everything successfully discovered on the machine, grouped and located. Paths are absolute so they can be gathered without re-searching.

### 1.1 Projects (interactive / built)

| Project | Location | State | Exhibition value |
| --- | --- | --- | --- |
| **Echo** — computational text art studio | `~/Desktop/echo/` | Live, deployed (`cs146j-finalproject.onrender.com`), ~7,200 LOC; SQLite gallery empty | **Anchor interactive.** 5 generative modes (network/soup/ascii/vortex/orbit). No exports committed — must be captured. |
| **MuseLab** — literary workshop dossier | `~/Desktop/MuseLab/` | Full React+FastAPI app; hybrid AI pipeline; 39 Playwright UI captures on disk | **Anchor interactive.** 7-tab folio; Pulse force graph; Imprint canvases. Richest existing screenshot set. |
| **Differ** — platform for experiential computing | `~/Desktop/Projects/DTR-1/` | Full research codebase; CHI 2026 first-author submission (Delta Lab) | **Anchor research.** `differ.pdf` (3.7MB), **28 result plots**, `chicago.geojson`, TF-IDF/geopandas modules. |
| **Nommi** — social food discovery (CS278) | `~/Desktop/cs278FoodRecommender/` | Deployed (`cs278-food-recommender.vercel.app`); real user metrics | Deployed product; boba-themed graphics; 31 users / 74% recommendation data. Community lesson. |
| **The Illusion of 5 Stars** — Airbnb rating calibration | `~/Desktop/yelpAnalysis/` | Research repo; 29 publication-style figures | Strong data-viz wall; poster PDF already in portfolio. The clearest "context breaks universal metrics" piece. |
| **theGraveOfIdeas** — dream symbol network | `~/Desktop/theGraveOfIdeas/` | Self-contained D3 page; 7 dreams | **Emotional keystone.** Private-symbol field; the precursor to Echo's semantic gravity. |
| **ai-data-platform** — AI-native data platform API | `~/Desktop/ai-data-platform/` | FastAPI backend; JWT, encrypted datasources, schema introspection | Systems/engineering *work sample* (no visuals). Supports the "I build real infrastructure" claim. |
| **NUSolar data platform** | (described in résumé; not located as standalone repo) | Software Team Lead; CAN-bus telemetry → AWS; two viz pipelines | Engineering lineage of the "make signals readable under time pressure" theme. |
| **GitHub identity system** (this repo) | `~/Desktop/github-identity-system/` | Complete; profile shipped to `xinyuezhang-shirley/xinyuezhang-shirley` | The compression exercise; source of the semantic-gravity specimen + editorial SVG assets. |

**Legacy / precursor builds (mine for content, do not exhibit as-is):**
- `~/Desktop/Projects/xinyuezhang-shirley.github.io/` — original HTML5-UP "Stellar" portfolio: **33 poems**, 28 drawings, 41 photos (some `.HEIC`), Unity game pages (`academicWeapon.html` / "Assignment Assassin", `strawberryCollector.html`), `worldHappinessReport.html`. Git repo appears corrupted (`bad object HEAD`).
- `~/Desktop/Projects/shirley-unlocked-world/` — "unlock your phone → Recruiter vs Friend" Lovable prototype; design-evolution artifact.
- `~/Desktop/Projects/DTR/` — early Yelp reference-system deliverable (scaffolding; 56MB CSV).
- `~/Desktop/cs146j-finalProject/` — Echo's original checkout; **working tree empty** (use `~/Desktop/echo/`).

### 1.2 The current portfolio site (the narrative spine that already exists)

`~/Desktop/xinyuezhang-shirley.github.io/` — **the current, primary** portfolio: Vite + React 18 + TS, React Router, Framer Motion, Tailwind + typography.

- **Routes:** Home · Work (6 case studies: Echo, Nommi, MuseLab, PwC, Tesla, NU Solar) · Research (5: Differ, Airbnb calibration, Poem-to-Song, POMDP aid, IMEC drones) · Creative (Art 12 / Photography 28 / Poetry 11) · About (+ "A Note About My Amateurism") · Resume.
- **Typed content already written:** `src/content/{work,research,creative,about,resume,contact}.ts` — long-form, exhibition-grade prose (the Echo case study "reads like wall text").
- **Visual tokens:** paper `#FAF9F6`, ink `#16140F`, accent burgundy `#8A3324`, line `#E3DFD4`; fonts **Fraunces** (display) + **Inter** (UI).
- **Built `dist/` exists; deployable today.**

> Curatorial note: this site is a *different* visual language (Fraunces / Inter / burgundy) than Echo (neutral) and MuseLab (ferric cream). The eventual redesign must reconcile the portfolio's own dialect with the Echo-orbit / MuseLab-material DNA — but that is the *next* project, not this one.

### 1.3 Writing

| Kind | Where | Notes |
| --- | --- | --- |
| **Philosophy / manifesto prose** | Echo `about.html`, MuseLab `README.md` + `docs/PROJECT_SCRIPT.md` (544 lines) + `design-memory/taste_profile.md` | Exhibition-ready as wall text. "Charts and graphs are evidence. The reading is the product." |
| **The amateurism essay** | portfolio `src/content/about.ts` ("A Note About My Amateurism") | Emotional cornerstone; reclaims "amateur" as *lover*. Still structurally true. |
| **Poetry** | portfolio (11 curated) + legacy site (**33 total**, completed + incomplete) | Includes "Romantic Death — Linguistic Tragedy" (embedded in Echo). |
| **Dreams** | `~/Desktop/theGraveOfIdeas/dreams.js` | 7 first-person entries (Apr 2026); recurring symbol field. |
| **Design doctrine** | `github-identity-system/docs/` (Anthropology, Negative Space, design-dna, creative-direction, production-spec) + `MuseLab/design-memory/` (taste_profile, disliked_patterns, decision log) | The self-policing "workshop for the workshop." |
| **Research writing** | Differ `differ.pdf`; Airbnb `docs/ANALYTIC_PIPELINE.md`; posters (Poem-to-Song, POMDP) | First-author CHI 2026 material. |
| **Résumé** | `~/Desktop/Resume.pdf` + portfolio `public/Xinyue_Zhang_Resume.pdf` | Stanford MSCS (Dec 2026, 3.90) · Northwestern BSCS (Summa Cum Laude, Murphy Scholar, 3.99). |

### 1.4 Media (video)

- **Project demos (usable):** `~/Desktop/Projects/xinyuezhang-shirley.github.io/projects/` → `puppetDemonstration.mov` (25MB), `academicWeapon.mov` (35MB), `APCSP Project (1) copy.mp4` (1.2MB).
- **Screen recordings, unlabeled (needs review):** `~/Desktop/Screen Recording 2026-06-05…`, `…2026-06-03…` (374MB / 438MB), `…2026-03-28…` (1.9GB). Likely project demos — **content must be verified**.
- **Nommi demo:** referenced as an external Google Drive video (not local).
- **Personal / not portfolio:** `~/Desktop/birthdayVideo/` (fan edits, concert fancams, K-pop), `~/Desktop/MVI_1990–1994.MP4` (4.5–31GB camera footage), `~/Movies/4K Video Downloader+/` (music + Buddhist chanting library), `~/Movies/annual update.mov`. These reveal *taste and emotional world* (see §1.8) but are not exhibits.

### 1.5 Assets (design output already generated)

- **GitHub profile editorial SVGs** — `github-identity-system/profile-art/artifacts/` + shipped in `xinyuezhang-shirley/assets/`: `wordmark-{light,dark}.svg`, `plate-01.svg`, `plate-02.svg`, `mark-{echo,muselab,differ,rag}.svg`, `note-field.svg`, `closing.svg`.
- **Semantic gravity specimen** — `profile-art/specimen/` (deterministic generator + `layout.json`, transparent PNG/SVG renders).
- **MuseLab UI captures** — `MuseLab/builder-agents/previews/runs/20260524-054042UTC/` (**39 PNGs, 6.4MB**): landing, poem-filled, loading, and all 7 dossier tabs, desktop + mobile.
- **MuseLab design reference board** — `MuseLab/design-memory/references/` (8 annotated inspiration PNGs).
- **MuseLab brand marks** — `frontend/public/favicon.svg`, `icons.svg`.
- **Echo hero image** — `~/Desktop/echo/frontend/assets/aboutBackground.JPEG` (3.2MB grainy celestial/butterfly print — genuinely exhibition-quality).
- **Differ result plots** — `Projects/DTR-1/result_plots/` (28 PNGs) + `conceptual_result/` CSVs.
- **Airbnb figures** — `yelpAnalysis/outputs/figures/` (29 PNGs) + tables.
- **Nommi graphics** — `cs278FoodRecommender/public/graphics/` (logo, bg pattern, empty/loading states) + favicon/icons SVG.
- **The specimen toolchain / design-DNA diagrams** — `mathematical-spiral-proof.svg`, `motion-settle-curve.svg`, `tokens.css`.

### 1.6 Research

- **Differ** (`Projects/DTR-1/`): `differ.pdf` (3.7MB), 28 plots, `chicago.geojson`, `interface.py` / `perspectiveModels.py` / `issueModels.py`. CHI 2026, first author, Delta Lab.
- **Airbnb "Illusion of 5 Stars"** (`yelpAnalysis/`): notebooks 01–09, VADER + statsmodels, 29 figures, `airbnb-rating-calibration-poster.pdf`.
- **Poem-to-Song** — `public/research/poem-to-song-poster.pdf` (cross-modal affect embedding — the "poem↔song" prototype the anthropology cites).
- **POMDP aid allocation** — `public/research/pomdp-aid-allocation-paper.pdf` (planning under environmental constraints).
- **IMEC drones** — referenced in `research.ts` (assets not yet located).

### 1.7 Photography

- **Graduation portrait set** — `~/Desktop/Memories/graduationPhotos/` (**299 Canon `0W5A*.JPG`**) — a full professional shoot; source for a portrait/hero.
- **Portfolio photography** — `xinyuezhang-shirley.github.io/public/photography/` (~28: dance series, portraits, still life, `Zhang_hero-portrait.jpg`, `Zhang_WeThePeople.jpg`).
- **Legacy photos** — `Projects/xinyuezhang-shirley.github.io/photos/` (41, incl. `.HEIC`).
- **Digital art** — portfolio `public/art/` (12: `goddess.PNG`, `zion.PNG`, `xueMiGong.jpg`, fan/idol portraits, commissions) + legacy `drawings/` (28: `Commission1–4`, album covers).
- **Zine** — `~/Desktop/Memories/Jae Final Zine Spreads.pdf` (1MB print/editorial artifact).
- **Echo draft image** — `~/Pictures/echoDraft.jpg`.

### 1.8 Audio

- **Echo ambient soundtrack** — `~/Desktop/echo/frontend/assets/backgroundMusic.mp3` (3.4MB; the only *authored-into-a-system* audio).
- **Video-editing project audio** — `~/Movies/JianyingPro/…` (CapCut caches from fan-edit / montage projects; not original composition).
- **Music library** — `~/Music/Music/…` (a few large `.m4a`).
- **Taste signal (not exhibits):** the downloaded-video library reveals the emotional palette that funds the melancholy — SEVENTEEN / P1Harmony / K-pop, Nijisanji EN VTubers, Chinese indie (告五人, 爛泥), *恋与深空*, and a substantial Buddhist chanting collection (楞嚴咒, 地藏菩薩, 淨空法師). Worth knowing when choosing sound and tone; not for display.

### 1.9 Personal writing / private symbolic material

- **Dreams** (`theGraveOfIdeas`) — *"a private sky of recurring symbols."* Symbols: house, ocean, mother, hallway, stairs, water, door, train, teeth, mirror, birds, upstairs.
- **Poetry** — identity/self-shattering, insufficiency + persistence, amateur devotion.
- **"Current Favorites"** (legacy site footer) — SEVENTEEN, *On Earth We're Briefly Gorgeous* (Ocean Vuong), *Nimona* — the literary/emotional lineage.

### 1.10 Explicitly confidential / non-exhibitable (named so they are not chased)

- **Tesla** (`~/Desktop/InternEra/tesla/`): only HR/legal onboarding PDFs (privacy notice, code of ethics, confidentiality return form) + one screenshot. **No work product on disk, and it is confidential by contract.** Exhibit only the non-confidential résumé-level summary (brake-degradation ML pipeline + human-in-the-loop monitoring), no artifacts.
- **PwC** (RAG / multi-agent Langflow work): confidential; no local artifacts. Exhibit as a described systems narrative only (multi-agent routing + RAG evaluation logic).

---

## 2. Missing Archive

What the collection *needs* and does not yet have. Ordered roughly by how much each gap weakens the exhibition. Be ruthless: most of these are captures and recordings, not new inventions.

### 2.1 Critical gaps (the exhibition is weaker without these)

1. **Echo — the five modes have no exports at all.** The single most important missing asset in the whole archive. Need: high-resolution screen recordings *and* frozen stills of network / soup / ascii / vortex / orbit, in both Moonlight and Paper, driven by a chosen canonical passage. Without this, the anchor interactive is invisible in any static context (GitHub, PDF, print).
2. **A canonical "specimen text."** One passage (likely "Romantic Death — Linguistic Tragedy" or a chosen poem) used consistently across Echo captures, the MuseLab dossier, and the semantic specimen, so the same words recur across rooms and the collection feels composed rather than sampled.
3. **MuseLab Imprint / Pulse as motion.** The Playwright PNGs exist, but the *interactive* residue (vortex spin, soup drift, ASCII breathe) and the Pulse force-settlement have no recorded motion. These are the most "alive" moments in the whole body of work.
4. **Verification of the three large unlabeled screen recordings** (`2026-03-28` 1.9GB, `2026-06-03` 438MB, `2026-06-05` 374MB). One or more may already *be* an Echo/MuseLab/Differ demo. Must be watched before commissioning new recordings.
5. **Differ demo / walkthrough.** A first-author CHI platform has a 3.7MB paper and 28 plots but no narrated demo showing the *interface* doing accountable-perspective reasoning. Needs a 60–90s screen recording or a composed "reading" of 3–4 key plots.
6. **A single portrait that matches the tone.** 299 graduation photos exist, but none has been selected/graded to the restrained, ferric-paper register. Need one chosen, color-graded hero portrait (and a small "colophon" variant).

### 2.2 Important gaps

7. **Nommi demo video, local + high quality.** Currently only an external Google Drive link. Need a local, captioned capture plus a couple of clean UI stills beyond the graphics.
8. **Airbnb calibration — a "claim" figure, not just 29 description figures.** The set is publication-style but the exhibition needs the *one* plate that states the argument ("4.9 ≠ 4.9 across cities") with a caption, not a folder of heatmaps.
9. **Poem-to-Song artifact beyond the poster.** The cross-modal prototype is one of the most on-brand ideas (affect embedding + human judgment) but exists only as a poster PDF. Need an audio/visual pairing artifact (poem text ↔ matched song excerpt ↔ embedding view).
10. **POMDP aid + IMEC drones assets.** POMDP has a paper PDF; IMEC has no located assets at all. Both need at least one legible figure + a two-sentence stakes statement, or a decision to cut them.
11. **`.HEIC` → web-native conversion** for the 41 legacy photos, if any are to be used.
12. **A consistent research-poster template.** The three posters (Airbnb, Poem-to-Song, POMDP) were made for different venues and don't share a visual dialect; they read as separate authors.

### 2.3 Nice-to-have gaps

13. **Handwritten / notebook scans.** The design DNA leans on marginalia and the Caveat "handwritten tether," but there are **no actual notebook or manuscript scans** in the archive. A handful of real process pages (sketches, force-graph doodles, poem drafts with edits) would make the "human process traces" theme true instead of typographic.
14. **A soundscape that isn't Echo's.** Only one authored ambient track exists. A single low, settling drone for gallery/transition use would let sound become a connective layer.
15. **Zine documentation.** "Jae Final Zine Spreads.pdf" is a real editorial artifact but undocumented — needs 2–3 photographed spreads and a one-line context.
16. **A unifying colophon / identity mark for the *portfolio itself*** (distinct from the GitHub wordmark) that bridges Fraunces/burgundy with the Echo/MuseLab DNA.
17. **Alt text / captions corpus.** Accessibility-critical text for every figure, written in the calm interpretive voice (this is also good wall text).

### 2.4 Deliberately *not* pursued

- Tesla and PwC artifacts (confidential — §1.10).
- Any new force-graph "because it's the muscle memory" — the anthropology flags force-directed repetition as a fatigue risk.
- More doctrine documents about the doctrine (recursion).

---

## 3. Asset Library

Reusable **assets**, not pages. Each is defined once and reappears across rooms so the exhibition reads as one hand. For each: *purpose · where it appears · how it moves · static fallback · dependencies.* Motion budget for the whole portfolio stays small (see Execution Plan): slow, quiet, asynchronous, procedural.

### A. Structural / identity assets

**A1 — Semantic field engine (`fieldEngine`)**
- *Purpose:* the one visual idea that unifies the collection — words as bodies with importance-driven gravity. Reused, not re-invented, per room.
- *Where:* Echo captures, MuseLab Imprint/Pulse, dream graph, GitHub specimen, and any new "portrait of a text."
- *Motion:* exponential settle only — `value += (target − value) × k, k ≈ 0.14`; discrete easing `easeArchival = cubic-bezier(0.22,1,0.36,1)`; **no spring, no bounce** (per design-dna Strand 05).
- *Static fallback:* the frozen settled frame is itself the artifact (a "paused simulation").
- *Dependencies:* D3 v7 / canvas; `vortex-field.js` + `theme-colors.js` already implement `place()`, `emphasis()`, `ease()`.

**A2 — Portfolio wordmark + colophon**
- *Purpose:* identity signature distinct from the GitHub profile wordmark; bridges Fraunces/burgundy with ferric DNA.
- *Where:* site header, footer colophon, PDF résumé header, exhibition placards.
- *Motion:* glyphs "write in" from `opacity:0 / translateY(6px)`; fill-mode both so it rests visible.
- *Static fallback:* fully rendered wordmark (vector outlines, no live font dependency).
- *Dependencies:* reuse `build-header.mjs` pattern (opentype.js vector outlines).

**A3 — Plate / folio number system**
- *Purpose:* asserts the collection is an *ordered sequence* (Plate 01, 02 …; `I · vortex`), not a pile of cards.
- *Where:* every room header; section transitions.
- *Motion:* static (numbers do not animate — false precision otherwise).
- *Static fallback:* n/a (already static).
- *Dependencies:* Cormorant/IBM Plex Mono outline SVGs (extend `build-plate.mjs`).

**A4 — Hairline divider + registration marks**
- *Purpose:* the only structural divider that exists (1px full-measure rule); corner registration/stamp marks as archive-box labeling.
- *Where:* between every section; margins of figures.
- *Motion:* the hairline may "draw in" once on first reveal; marks static.
- *Static fallback:* drawn rule.
- *Dependencies:* inline SVG.

### B. Typographic assets

**B1 — Micro-label eyebrow (`label()`)**
- *Purpose:* every content block gets a tracked 9–11px mono uppercase eyebrow before its headline (the 1:6 label:display jump from design-dna Strand 01).
- *Where:* every room, figure, and caption.
- *Motion:* none.
- *Fallback:* n/a.
- *Dependencies:* IBM Plex Mono; tracking 0.16–0.38em.

**B2 — Display masthead**
- *Purpose:* the oversized Cormorant/Fraunces headline that carries a room's title.
- *Where:* room openers.
- *Motion:* optional single fade/settle; never looping.
- *Fallback:* static headline.
- *Dependencies:* display font.

**B3 — Manuscript markup marks (`mark(token, category)`)**
- *Purpose:* underline/italic/weight keyed to a *real* category (repeat / emotion / abstract / sensory), always with a legend — graphite, never alarm red.
- *Where:* poem rooms, MuseLab Draft, any annotated text.
- *Motion:* none (or a one-time reveal).
- *Fallback:* static marks + legend.
- *Dependencies:* MuseLab's existing category keying.

**B4 — Margin annotation (Caveat tether)**
- *Purpose:* the rare handwritten intrusion — human interruption on a strong grid, <5% of any surface.
- *Where:* one per room at most; against a figure or poem.
- *Motion:* "writes in" once, then rests.
- *Fallback:* static handwriting (vector outline).
- *Dependencies:* Caveat static instance (already solved via fontTools).

### C. Figure / diagram assets

**C1 — Frozen specimen plate**
- *Purpose:* a settled semantic field exported as a still "evidence plate" with caption — the recurring signature figure.
- *Where:* home, Echo room, GitHub-style specimen, section transitions.
- *Motion:* static (it is the freeze); optionally an animated sibling (A1).
- *Fallback:* is the fallback.
- *Dependencies:* A1 + specimen renderer (transparent PNG/SVG).

**C2 — Interpretation-stack diagram**
- *Purpose:* the argument spine made visible — Evidence → Pattern → Interpretation → Claim → Revision question.
- *Where:* MuseLab room, Differ room, research rooms; also the About/thesis page.
- *Motion:* none, or sequential reveal top-to-bottom.
- *Fallback:* static stacked blocks.
- *Dependencies:* reuse MuseLab `literaryInterpretation.ts` structure.

**C3 — Research figure frame**
- *Purpose:* a single consistent frame (hairline, mono caption, plate number) that makes Differ plots, Airbnb figures, and posters read as one author.
- *Where:* all research/data rooms.
- *Motion:* none.
- *Fallback:* is static.
- *Dependencies:* the shared poster/figure template (see Missing §2.2.12).

**C4 — Architecture / pipeline diagram**
- *Purpose:* honest system diagrams (hybrid grounding: deterministic → ML sensors → agents → synthesis; RAG routing) drawn in the same hairline dialect — **no diagram cosplay** (edges must encode real relations).
- *Where:* MuseLab, PwC (described), Tesla (described), ai-data-platform, NUSolar.
- *Motion:* none, or a single directional trace.
- *Fallback:* static diagram.
- *Dependencies:* inline SVG; must pass the five-question diagram test (design-dna Strand 03).

### D. Media assets

**D1 — Demo capture (looping, muted, captioned)**
- *Purpose:* the honest moving record of each interactive (Echo modes, MuseLab motion, Nommi, Differ).
- *Where:* each project room, as a bounded figure — never autoplaying full-bleed.
- *Motion:* seamless slow loop; poster-frame until in view; respects reduced-motion.
- *Fallback:* poster still (C1/screenshot) + text description (room must read with images off).
- *Dependencies:* screen-recording + light editing; transparent-background GIF/`webm` where motion materially helps.

**D2 — Portrait (graded)**
- *Purpose:* one human presence at the tone of the work.
- *Where:* Home hero, About, colophon.
- *Motion:* none (or the FloatingCircles photo-fragment treatment already in the site).
- *Fallback:* is static.
- *Dependencies:* selection + color grade from graduationPhotos.

**D3 — Notebook / process scan**
- *Purpose:* real human process trace (sketch, doodle, poem draft with edits).
- *Where:* one per room where process matters; About.
- *Motion:* none.
- *Fallback:* is static.
- *Dependencies:* **needs to be created/scanned** (Missing §2.3.13).

### E. Ambient / connective assets

**E1 — Room soundscape (optional, off by default)**
- *Purpose:* low settling drone as a connective emotional layer; honesty over spectacle.
- *Where:* gallery/immersive mode only, user-initiated.
- *Motion:* n/a (audio); tied to a visible toggle.
- *Fallback:* silence; nothing depends on it.
- *Dependencies:* Echo's `backgroundMusic.mp3` + one new neutral drone (Missing §2.3.14).

**E2 — Page/section transition**
- *Purpose:* the "archival" settle between rooms — a hairline sweep or specimen re-settle, not a slide.
- *Where:* route changes.
- *Motion:* `easeArchival`, ≤ ~500ms, asynchronous.
- *Fallback:* instant cut.
- *Dependencies:* Framer Motion (already in the site).

**E3 — Token sheet (`tokens.css`)**
- *Purpose:* one source of truth for color/type/motion so no room drifts into its own palette (anti-pattern: dialect drift).
- *Where:* every surface.
- *Motion:* n/a.
- *Fallback:* n/a.
- *Dependencies:* extend existing `assets/tokens.css` to reconcile portfolio + Echo + MuseLab calibrations.

> **Motion discipline (applies to all D/E assets):** ≤ 3–5 animated elements visible at once; slow, quiet, asynchronous, procedural; every animated asset has a visible resting state and honors `prefers-reduced-motion`. Beauty through structure, not decoration.

---

## 4. Portfolio Rooms

Each project is a room. For every room: *story · artifacts · motion · media · supporting writing · diagrams · process · emotional tone.* Rooms are sequenced so the two halves of the practice (fidelity / afterlife-of-language) are braided, not siloed.

### Room 0 — Threshold (Identity + Thesis)
- **Story:** one sentence — *systems that preserve meaning as it moves between people, language, and computation* — and a graded portrait. The whole collection's frame.
- **Artifacts:** A2 wordmark, D2 portrait, C1 a single frozen specimen as the "signature."
- **Motion:** wordmark writes in once; specimen optionally settles once. Nothing loops.
- **Media:** portrait.
- **Writing:** the thesis sentence + 2–3 lines from the amateurism essay.
- **Diagrams:** none (restraint).
- **Process:** n/a.
- **Tone:** quiet arrival; restrained melancholy; confident, not loud.

### Room 1 — Echo (*afterlife of language*)
- **Story:** speed strips emotional weight from language; Echo gives text an afterlife by turning it into a field that keeps moving after the sentence ends.
- **Artifacts:** C1 frozen plates for each mode; `aboutBackground.JPEG` as the room's celestial backdrop; the embedded poem as wall text.
- **Motion:** D1 loop of one or two modes (soup drift + vortex spin are strongest); Moonlight primary, Paper as a diptych.
- **Media:** 5-mode capture suite (Missing §2.1.1); optional E1 (Echo's own soundtrack).
- **Writing:** "words that continue breathing"; "each form gives language a different kind of afterlife"; Borges epigraph.
- **Diagrams:** small honest note on the pipeline (text → co-occurrence + Datamuse → field) — evidence, not decoration.
- **Process:** `echoDraft.jpg`; a force-graph sketch (D3 scan) if created.
- **Tone:** elegiac, celestial, monochrome, reverent.

### Room 2 — Differ (*contested fidelity, made accountable*)
- **Story:** the same designed experience fails differently across populations; Differ makes those differences legible so designers can be *accountable* for whom meaning breaks. (This is the fidelity twin's flagship — deliberately placed second so the collection isn't read as "only literary.")
- **Artifacts:** C3-framed selection of ~4 result plots; `differ.pdf`; `chicago.geojson` map still.
- **Motion:** minimal — perhaps one plot that reveals its layers; otherwise still.
- **Media:** Differ interface walkthrough (Missing §2.1.5).
- **Writing:** the CHI abstract, compressed; "accountable perspectives — who/where meaning breaks."
- **Diagrams:** C2 interpretation stack applied to a real case; C4 platform architecture.
- **Process:** notebook/plot iteration scans if available.
- **Tone:** rigorous, humane, quietly political.

### Room 3 — MuseLab (*interpretation as dossier*)
- **Story:** AI writing tools treat a poem like a support ticket; MuseLab answers *what is this text actually about* with an archival dossier, not a chat — and keeps its own taste honest with a workshop-for-the-workshop.
- **Artifacts:** the 39 Playwright PNGs curated into a folio sequence (Landing → Loading → Draft → Pulse → Margins → Imprint); the 8-pin reference board as didactic context.
- **Motion:** D1 loops of Imprint (vortex/soup/ascii) and the Pulse force-settlement (Missing §2.1.3); ArchiveLoading scan band.
- **Media:** custom-poem Imprint captures using the canonical specimen text.
- **Writing:** "Charts and graphs are evidence. The reading is the product."; taste_profile + disliked_patterns excerpts as wall text.
- **Diagrams:** C2 Evidence→Claim; C4 hybrid pipeline; the two-agent-systems meta-note (poetry agents vs builder agents).
- **Process:** design decision log excerpt; before/after builder-preview strip.
- **Tone:** warm ferric vellum, workshop calm, slightly melancholic.

### Room 4 — The Illusion of 5 Stars (*a metric that lies across contexts*)
- **Story:** 4.9 does not mean the same thing in Hong Kong and Chicago; a single calibration argument the general public can feel.
- **Artifacts:** the *one* claim figure (Missing §2.2.8) foregrounded; supporting figures in C3 frames; the poster PDF.
- **Motion:** none (data honesty).
- **Media:** none required.
- **Writing:** the argument in two sentences; short method note.
- **Diagrams:** C3 figure frames; a small city-comparison plate.
- **Process:** pipeline doc excerpt.
- **Tone:** clear, analytic, a little wry.

### Room 5 — The Grave of Ideas (*the private field under the instruments*)
- **Story:** before Echo's semantic gravity and MuseLab's Pulse, there was a private sky of recurring dream symbols. This room reveals the emotional substrate — and shows the field metaphor is autobiographical, not borrowed.
- **Artifacts:** the live dream graph; selected dream lines as wall text.
- **Motion:** the graph's gentle settle + hover (already built).
- **Media:** none beyond the graph.
- **Writing:** "a private sky of recurring symbols"; "every room opened into another staircase and every staircase led to the ocean."
- **Diagrams:** the graph *is* the diagram.
- **Process:** this is the process — private material becoming instrument.
- **Tone:** intimate, blue, dream-logic; the collection's emotional low light.

### Room 6 — Systems & Signals (*fidelity under time pressure*) — a grouped room
- **Story:** the engineering twin — making signals readable for humans when being wrong is consequential. Groups the confidential/described and infrastructure work under one honest banner instead of six thin cards.
- **Artifacts / sub-stories:**
  - **Tesla** — brake-degradation ML + human-in-the-loop monitoring (described only; C4 abstracted diagram; **no confidential artifacts**).
  - **PwC** — multi-agent Langflow routing + RAG evaluation (described only; C4 routing diagram).
  - **NUSolar** — CAN telemetry → AWS → dual viz pipelines (the origin of "make signals readable").
  - **ai-data-platform** — API/systems design as a work sample.
- **Motion:** none; C4 diagrams may trace direction once.
- **Media:** none (or a sanitized pipeline animation).
- **Writing:** the HITL principle — "classifiers are sensor readings, not verdicts."
- **Diagrams:** C4 for each sub-story, in one dialect.
- **Tone:** competent, sober, trustworthy.

### Room 7 — Creative Archive (*poetry, art, photography, zine*)
- **Story:** the polymath seriousness that funds everything — poems, drawings, photographs, a zine — without carnival branding.
- **Artifacts:** curated poems (with B3 markup where earned), selected art/photography in C3-style frames, zine spreads.
- **Motion:** at most one B4 handwritten tether; otherwise still.
- **Media:** graded photographs; zine spread photos.
- **Writing:** the amateurism essay in full; a small set of the strongest poems (quality over the 33-poem archive).
- **Diagrams:** none.
- **Process:** poem drafts with edits (D3 scans).
- **Tone:** tender, devoted, unhurried.

### Room 8 — Nommi (*community is the hard part*) — optional / honest
- **Story:** a shipped social product that taught the real lesson — features without critical mass are empty. Included precisely because it complicates the "everything works" narrative.
- **Artifacts:** UI stills, graphics, the real metrics.
- **Motion:** D1 demo loop.
- **Media:** local high-quality demo (Missing §2.2.7).
- **Writing:** the analytics/ethics note; an honest reflection.
- **Diagrams:** optional architecture.
- **Tone:** candid, warm, self-aware.

### Room 9 — Colophon / Door
- **Story:** the exit — a single restrained gesture and the invitation into Echo/MuseLab/GitHub, not a summary.
- **Artifacts:** A1 specimen re-settle or `closing.svg`; contact.
- **Motion:** one quiet settle.
- **Writing:** one line.
- **Tone:** open door, not a period.

> **Sequencing logic:** Threshold → Echo → **Differ** → MuseLab → Illusion of 5 Stars → Grave of Ideas → Systems & Signals → Creative → (Nommi) → Door. The literary and the fidelity work alternate so a 60-second visitor from *any* audience (engineer, designer, researcher) meets their entry point early and leaves understanding both halves are one mind.

---

## 5. Creative Wishlist

No time constraints. Everything that would make this portfolio *unforgettable*, then sorted by who/what must produce it. Bias: procedural over illustrated; capture over invent; one perfect artifact over ten adequate ones.

### The dream list (unsorted, ambition-first)

- A **canonical specimen text** whose words recur across Echo, MuseLab, the dream graph, and the home specimen — so the whole exhibition is visibly one composition.
- **Echo, all five modes**, captured as slow seamless loops *and* frozen plates, Moonlight + Paper.
- **MuseLab Imprint + Pulse in motion** — the most alive footage in the archive.
- A **"portrait of a text"** generator: drop any passage, get a frozen semantic-gravity plate in the house style — the reusable signature figure, and a small interactive toy.
- **Differ, narrated** — a 60–90s reading of accountable-perspective analysis on one real case.
- The **one Airbnb claim plate** — "4.9 ≠ 4.9" — that a stranger understands in ten seconds.
- **Poem-to-Song** as an actual audio-visual pairing (poem ↔ matched song excerpt ↔ affect embedding), not just a poster.
- **Real notebook/process scans** — force-graph doodles, poem drafts with edits, dream sketches — so "human process traces" is literally true.
- One **graded hero portrait** in the ferric-paper register; a colophon variant.
- A **single low settling drone** for gallery mode + the Echo track — sound as connective tissue.
- A **unified research-poster / figure template** so Differ, Airbnb, Poem-to-Song, POMDP read as one author.
- The **dream graph** promoted from experiment to a first-class room.
- **Zine spreads** photographed and contextualized.
- An **immersive "gallery mode"** — optional, keyboard-navigable, museum-paced, sound-on-by-choice — as an alternate to the résumé-fast view.
- A **reconciled token sheet** binding Fraunces/burgundy to Echo/MuseLab DNA so the portfolio stops being a third dialect.

### Sorted by production path

**Already exists (curate / crop / caption):**
- Echo `aboutBackground.JPEG`; Echo soundtrack.
- MuseLab 39 Playwright PNGs + 8 reference pins + brand SVGs.
- Differ `differ.pdf` + 28 plots + `chicago.geojson`.
- Airbnb 29 figures + poster; Poem-to-Song + POMDP posters.
- Dream graph (live); GitHub editorial SVGs + semantic specimen.
- Nommi graphics + metrics; ai-data-platform code.
- 299 graduation photos; portfolio art/photography; zine PDF; the written case studies + amateurism essay + 33 poems.

**Can be generated (from existing code/data, low new input):**
- Echo 5-mode captures + frozen plates (run the app).
- MuseLab Imprint/Pulse motion; custom-poem Imprint stills; before/after builder strip; ArchiveLoading loop.
- "Portrait of a text" frozen plates via the existing `fieldEngine`.
- The one Airbnb claim plate (recompose from existing figures).
- C3/C4 diagram set; reconciled `tokens.css`; A2/A3/A4/B-series SVGs (extend `profile-art/artifacts` toolchain).

**Needs me (Shirley) to create / decide:**
- Choose the canonical specimen text.
- Curate the poem short-list and finalize the amateurism essay for exhibition.
- Watch + label the three large unlabeled screen recordings; decide POMDP/IMEC keep-or-cut.
- Approve the Tesla/PwC described-only framing.

**Needs new photography:**
- Select + color-grade one hero portrait (+ colophon variant) from graduationPhotos.
- Photograph the zine spreads; re-shoot or convert `.HEIC` legacy photos worth keeping.

**Needs new recordings:**
- Echo demo; MuseLab motion; Differ walkthrough; local Nommi demo. (Some may already exist in the unlabeled recordings — verify first.)

**Needs new writing:**
- The single thesis sentence (final wording); captions/alt-text corpus in the calm voice; two-sentence stakes lines for each research room; the one honest Nommi reflection.

**Needs music / sound:**
- One neutral settling drone (gallery/transition). Echo's track already covers Room 1.

**Needs illustration / hand:**
- Notebook/process scans (D3) — the one genuinely absent material category.
- Optional Caveat margin tethers (already tooled).

**Needs interaction (net-new build — the *next* project, flagged here so it isn't lost):**
- "Portrait of a text" interactive toy; immersive gallery mode; reconciled cross-room token system.

---

## 6. Execution Plan

Collect and create **assets before redesigning pages.** Prioritized highest-impact / lowest-effort first. Each phase produces reviewable artifacts; nothing here redesigns the portfolio yet.

### Phase 0 — Triage & decisions (½ day, blocks everything, near-zero effort)
- Watch the three large unlabeled screen recordings; label or discard. *(Removes duplicate work if a demo already exists.)*
- Choose the **canonical specimen text**.
- Decide Tesla/PwC framing (described-only) and POMDP/IMEC keep-or-cut.
- **Deliverable:** a one-page "decisions frozen" note. **Highest leverage in the whole plan.**

### Phase 1 — Harvest what already exists (1–2 days, high impact, low effort)
- Copy into a single `portfolio-archive/` tree, grouped by room: MuseLab PNGs, Differ plots + PDF, Airbnb figures + posters, Nommi graphics, Echo hero image + soundtrack, GitHub SVGs + specimen, dream graph, the 3 usable project videos.
- Convert `.HEIC` → web; export the zine spreads.
- **Deliverable:** a complete, de-duplicated source archive. Everything downstream reads from here.

### Phase 2 — Capture the interactives (2–4 days, highest impact, medium effort)
- Run Echo → record 5 modes (Moonlight + Paper) + frozen plates, using the canonical text.
- Run MuseLab → record Imprint (vortex/soup/ascii) + Pulse settle + ArchiveLoading; capture custom-poem Imprint stills.
- Record Differ walkthrough; record/collect local Nommi demo.
- Edit to slow muted loops + poster frames; respect reduced-motion.
- **Deliverable:** the D1 media set — the assets whose absence most weakens the collection.

### Phase 3 — Author the recurring figures (2–3 days, high impact, medium effort)
- Build the reconciled `tokens.css`; extend the SVG toolchain for A2/A3/A4 + B-series.
- Produce the "portrait of a text" frozen plates (C1) from `fieldEngine`.
- Compose the one Airbnb claim plate; build the shared research-figure/poster frame (C3) and re-frame Differ/Airbnb/posters through it.
- Draw the C2 interpretation stack + C4 architecture diagrams (pass the diagram five-question test).
- **Deliverable:** one coherent figure/diagram system across all rooms.

### Phase 4 — Human materials (2–3 days, medium impact, needs Shirley)
- Select + grade the hero portrait (+ colophon); photograph zine spreads.
- Create/scan notebook & process pages (D3).
- Curate the poem short-list; finalize the amateurism essay; write the thesis sentence + captions/alt-text + research stakes lines + Nommi reflection.
- Record/commission one settling drone.
- **Deliverable:** the emotional + accessibility layer — portrait, process scans, wall text, sound.

### Phase 5 — Assemble the collection (1 day, synthesis, low effort)
- Lay every asset into the Room structure (§4) as a **flat catalogue** (a slide/board deck or a plain index) — *not* a redesigned site.
- Check the collection reads with images off; check the 10s/30s/60s test for engineer / designer / researcher; check motion budget (≤3–5 animated, all with resting states).
- **Deliverable:** the complete, sequenced exhibition inventory — the point at which "assemble vs redesign" hands off. **The redesign is a separate project that starts here.**

### Priority summary (impact ↓, effort →)

| Priority | Action | Impact | Effort |
| --- | --- | --- | --- |
| 1 | Phase 0 triage & decisions | ★★★ | ▁ |
| 2 | Phase 2 Echo + MuseLab capture | ★★★ | ▃▃ |
| 3 | Phase 1 harvest existing | ★★★ | ▂ |
| 4 | Phase 3 recurring figures + tokens | ★★☆ | ▃ |
| 5 | Phase 4 portrait, scans, wall text, sound | ★★☆ | ▃ |
| 6 | Phase 5 assemble catalogue | ★★☆ | ▂ |

---

## 7. What this plan deliberately refuses (negative space, applied)

To keep the collection from drifting into "looks like her, isn't her":
- No new force-graph purely from muscle memory; the field engine is *reused with a reason*, not multiplied.
- No archival paper/grain/stamps as costume over content with no semantic payload.
- No autoplaying full-bleed video, particle candy, or motion-as-decoration.
- No KPI/streak/dashboard chrome; no card-stack default for projects.
- No confidential Tesla/PwC artifacts.
- No further doctrine-about-the-doctrine — this document is the last meta-artifact before gathering real material.

---

# Part II — Production Inventory

Operational conversion of the archive into things to acquire, build, or capture. **No redesign here.** The goal is to fill the current visual stump (`~/Desktop/xinyuezhang-shirley.github.io`, already liked) with authored material — not to replace it.

**Legend (used in every table below):**

- **Prov** (who provides): **A** = assistant can produce/capture/convert · **S** = Shirley must provide/decide/record · **A→S** = assistant produces, owner approves before publish.
- **State/Class:** `AS-IS` usable now · `CLEANUP` exists but needs work · `CREATE` derivable from existing material · `MISSING` must be captured/made · `DECIDE` blocked on owner decision.
- **Vis** (visibility class): **PUB** public artifact may appear directly · **PRIV** private, taste-only, never published · **DERIV** derived-only, reveals nothing private.
- **Eff:** S (<1h) · M (a few hours) · L (a day+).
- **Prio:** P1 anchor-critical · P2 important · P3 nice-to-have.

---

## II.0 The three buckets (explicit privacy classification)

Nothing below moves from a stricter bucket to a looser one without an owner tick in §D.

### Bucket 1 — Private source material (taste-only, NEVER published)
- Apple Notes content (not accessed; assumed private).
- `~/Desktop/birthdayVideo/` (fan edits, fancams), `~/Movies/4K Video Downloader+/` (music + Buddhist chanting library), `MVI_1990–1994.MP4` — **taste/emotional-palette signal only.**
- `~/Desktop/InternEra/tesla/` HR/legal PDFs — confidential by contract.
- PwC internal RAG/Langflow specifics — confidential.
- Raw personal photos in `~/Pictures/Photos Library` / `Photo Booth`.
- Lease/tenant/personal PDFs in `~/Documents`.
- **Dream texts** (`theGraveOfIdeas/dreams.js`) — **default PRIVATE** until owner rules otherwise (they may be promoted to DERIV or PUB in §D).

### Bucket 2 — Public artifacts (may appear directly, pending normal approval)
- Echo, MuseLab, Differ, Airbnb, Nommi, ai-data-platform code + their generated figures/UI.
- Written case studies, amateurism essay, research posters, résumé.
- Digital art, selected photography, zine spreads (owner selects which).
- GitHub identity SVGs + semantic specimen.

### Bucket 3 — Derived-only (inspired by private material, reveals nothing)
- A **dream-shaped field** that reuses the graph *form* with neutral/abstract tokens and **no dream text** (if dreams stay private).
- The **semantic-gravity signature** trained on a *public* canonical text, echoing the private symbol structure without exposing it.
- Emotional color/motion grading informed by the private music/taste library.

> **Rule:** poems, dreams, Notes content, private work docs, and personal symbols are treated as **not publishable by default.** Each is flagged for explicit approval in §D.

---

## II.1 Asset Acquisition Matrix

Grouped by source. Columns: **Asset · Role · Path · State · Action · Prov · Vis · Format · Eff · Prio · Section · Fallback**.

### Echo — `~/Desktop/echo/`
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5-mode capture suite | Show the studio alive | (runtime only) | MISSING | Run app; record network/soup/ascii/vortex/orbit, Moonlight+Paper, canonical text | A→S | PUB | mp4/webm loop + poster | L | P1 | Anchor: Echo | frozen plates (below) |
| Frozen mode plates | Static evidence stills | (runtime only) | CREATE | Screenshot each settled mode | A | PUB | PNG/SVG transparent | M | P1 | Anchor: Echo | About hero image |
| Celestial hero image | Room backdrop | `echo/frontend/assets/aboutBackground.JPEG` (3.2MB) | AS-IS | Crop/grade variants | A | PUB | JPEG/WEBP | S | P1 | Anchor: Echo | solid ink field |
| Ambient soundtrack | Optional room sound | `echo/frontend/assets/backgroundMusic.mp3` (3.4MB) | DECIDE | Confirm usage rights/source | S | PUB | mp3 | S | P2 | Anchor: Echo (audio) | silence |
| Embedded poem | Wall text | `echo/frontend/about.html` ("Romantic Death…") | DECIDE | Confirm OK to publish in full | S | PUB | text | S | P1 | Anchor: Echo | excerpt only |
| Pipeline note | Honest "how" | `echo/backend/lib/analyzeText.js` | CREATE | Draw C4 mini-diagram | A | DERIV | SVG | S | P3 | Anchor: Echo | one sentence |

### MuseLab — `~/Desktop/MuseLab/`
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dossier folio sequence | Narrate the product | `MuseLab/builder-agents/previews/runs/20260524-054042UTC/` (39 PNG) | AS-IS | Curate 6–8, caption | A | PUB | PNG | S | P1 | Anchor: MuseLab | single landing shot |
| Imprint motion | The most "alive" moment | (runtime only) | MISSING | Record vortex/soup/ascii | A→S | PUB | webm loop | M | P1 | Anchor: MuseLab | `dossier-imprint.png` |
| Pulse settle | Force graph as evidence | (runtime only) | MISSING | Record settle + capture still | A→S | PUB | webm + PNG | M | P1 | Anchor: MuseLab | `dossier-pulse.png` |
| Reference board | Didactic taste context | `MuseLab/design-memory/references/` (8 PNG + md) | AS-IS | Optional selection | A | PUB | PNG | S | P3 | Study: process | omit |
| Brand marks | Room mark | `frontend/public/favicon.svg`, `icons.svg` | AS-IS | Recolor to tokens | A | PUB | SVG | S | P2 | Anchor: MuseLab | plate number |
| Taste/doctrine excerpts | Wall text | `design-memory/taste_profile.md`, `disliked_patterns.md` | CLEANUP | Excerpt 3–5 lines | A→S | PUB | text | S | P2 | Anchor: MuseLab | omit |
| Custom-poem Imprint | Tie to canonical text | (runtime only) | CREATE | Submit canonical text, capture | A | PUB | PNG | M | P2 | Anchor: MuseLab | mock-poem run |

### Differ — `~/Desktop/Projects/DTR-1/`
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paper | Research spine | `DTR-1/differ.pdf` (3.7MB) | DECIDE | Confirm CHI submission is citable publicly | S | PUB | PDF | S | P1 | Anchor: Differ | title + abstract only |
| Result plots (curated) | Evidence figures | `DTR-1/result_plots/` (28 PNG) | CLEANUP | Select ~4, reframe (C3) | A→S | PUB | PNG | M | P1 | Anchor: Differ | one plot |
| Chicago map still | Geographic accountability | `DTR-1/chicago.geojson` | CREATE | Render one map plate | A | PUB | SVG/PNG | M | P2 | Anchor: Differ | text |
| Interface walkthrough | Show the platform reasoning | (runtime) | MISSING | Record 60–90s (or narrate) | S | PUB | mp4 | L | P1 | Anchor: Differ | annotated stills |
| Abstract excerpt | Wall text | `DTR-1/differ.pdf` | CLEANUP | Compress to 3 sentences | A→S | PUB | text | S | P1 | Anchor: Differ | — |

### Airbnb — "The Illusion of 5 Stars" — `~/Desktop/yelpAnalysis/`
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The claim plate | "4.9 ≠ 4.9 across cities" | `yelpAnalysis/outputs/figures/` (29 PNG) | CREATE | Recompose ONE argument figure | A→S | PUB | SVG/PNG | M | P1 | Anchor: Airbnb | `city_threshold_summary.png` |
| Supporting figures | Method evidence | same folder | CLEANUP | Frame 2–3 in C3 | A | PUB | PNG | S | P2 | Anchor: Airbnb | claim plate only |
| Poster | Formal artifact | `.github.io/public/research/airbnb-rating-calibration-poster.pdf` | AS-IS | Link/thumbnail | A | PUB | PDF | S | P2 | Anchor: Airbnb | — |
| Method note | Honest "how" | `yelpAnalysis/docs/ANALYTIC_PIPELINE.md` | CLEANUP | 2-sentence stakes line | A→S | PUB | text | S | P2 | Anchor: Airbnb | — |

### Nommi — `~/Desktop/cs278FoodRecommender/`
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demo video (local, HQ) | Show shipped product | external Google Drive link | MISSING | Record local 20–30s @1440p | S | PUB | mp4 | M | P2 | Study: Nommi | UI stills |
| UI stills | Product evidence | `cs278FoodRecommender/public/graphics/` | AS-IS | Screenshot a few screens | A | PUB | PNG | S | P2 | Study: Nommi | graphics only |
| Graphics/brand | Room mark | same `graphics/` + favicon/icons | AS-IS | Use directly | A | PUB | PNG/SVG | S | P3 | Study: Nommi | — |
| Metrics + ethics note | Honest reflection | `scripts/seed/ANALYTICS_AND_ETHICS.md` | CLEANUP | Excerpt + write 1 candid line | S | PUB | text | S | P2 | Study: Nommi | — |

### Systems & Signals — Tesla / PwC / NUSolar / ai-data-platform
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tesla summary | Fidelity-under-stakes narrative | résumé only | DECIDE | Confirm safe non-confidential wording | S | PUB(text) | text | S | P2 | Study: Systems | omit project |
| Tesla HITL diagram | Abstracted concept | — | CREATE | Draw generic HITL (no internals) | A→S | DERIV | SVG | M | P3 | Study: Systems | text |
| PwC summary | Multi-agent/RAG narrative | résumé only | DECIDE | Confirm safe wording | S | PUB(text) | text | S | P2 | Study: Systems | omit project |
| NUSolar viz | "make signals readable" origin | not located | MISSING | Owner locate repo/screens or describe | S | PUB | PNG/text | M | P3 | Study: Systems | text-only |
| ai-data-platform | Systems work sample | `~/Desktop/ai-data-platform/` | AS-IS | Architecture diagram (C4) | A | PUB | SVG | M | P3 | Study: Systems | repo link |

### Other research — Poem-to-Song / POMDP / IMEC
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Poem-to-Song poster | Cross-modal affect | `.github.io/public/research/poem-to-song-poster.pdf` | AS-IS | Thumbnail + link | A | PUB | PDF | S | P3 | Study: research plate | — |
| Poem↔Song pairing | On-brand artifact | — | MISSING | Owner supplies poem+song+embedding | S | DERIV | audio+img | L | P3 | Study: research plate | poster only |
| POMDP paper | Planning under limits | `.github.io/public/research/pomdp-aid-allocation-paper.pdf` | AS-IS | One figure + stakes line | A→S | PUB | PDF | S | P3 | Study: research plate | title only |
| IMEC drones | Research entry | not located | MISSING | Owner: keep-or-cut + assets | S | PUB | ? | S | P3 | Study or CUT | cut |

### The Grave of Ideas / dreams — `~/Desktop/theGraveOfIdeas/`
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dream graph (live) | Emotional keystone | `theGraveOfIdeas/dreams.{html,js,css}` | DECIDE | Owner rules PRIV/DERIV/PUB | S | PRIV(default) | web | S | P1(gate) | Study: Grave | derived field |
| 7 dream texts | Wall text (if allowed) | `dreams.js` | DECIDE | Explicit per-text approval | S | PRIV(default) | text | S | P2 | Study: Grave | none |
| Derived symbol field | Reveals nothing private | (from graph form) | CREATE | Rebuild form w/ neutral tokens, no text | A | DERIV | SVG/web | M | P2 | Study: Grave | omit |

### Creative archive — poems / art / photography / zine
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Poems (curated) | Literary voice | `.github.io/src/content/*` (11) + legacy `poetry.html` (33) | DECIDE | Owner selects 3–6 publishable | S | PUB(selected) | text | M | P2 | Room: Creative | omit poems |
| Digital art | Polymath breadth | `.github.io/public/art/` (12) + legacy `drawings/` (28) | CLEANUP | Owner selects 8–12; frame | S→A | PUB(selected) | PNG/JPG | M | P2 | Room: Creative | 4-image strip |
| Photography | Human eye | `.github.io/public/photography/` (28) + legacy `photos/` (41 incl HEIC) | CLEANUP | Owner selects; A converts HEIC | S→A | PUB(selected) | WEBP | M | P2 | Room: Creative | portrait only |
| Zine spreads | Editorial print artifact | `~/Desktop/Memories/Jae Final Zine Spreads.pdf` | DECIDE | Confirm authorship/OK; photograph 2–3 | S | PUB | JPG | M | P3 | Room: Creative | omit |
| Hero portrait | Human presence at tone | `~/Desktop/Memories/graduationPhotos/` (299) | CREATE | Owner picks 1–2; A grades | S→A | PUB | WEBP | M | P1 | Threshold/About | existing `Zhang_hero-portrait.jpg` |

### Portfolio shell & identity — `~/Desktop/xinyuezhang-shirley.github.io/`
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| React shell | The stump to fill | whole repo | AS-IS | Keep; ingest assets into content `.ts` | A | PUB | code | — | P1 | All | — |
| Written case studies | Narrative spine | `src/content/{work,research,creative,about}.ts` | AS-IS | Light edit toward thesis | A→S | PUB | text | M | P1 | All rooms | — |
| Token sheet | One dialect | `tailwind.config.ts` + new `tokens.css` | CLEANUP | Reconcile Fraunces/burgundy ↔ Echo/MuseLab | A | PUB | css | M | P1 | Global | current tokens |
| GitHub identity SVGs | Reusable marks | `github-identity-system/profile-art/artifacts/` | AS-IS | Reuse/extend | A | PUB | SVG | S | P2 | Global | — |
| Semantic specimen | Signature figure | `profile-art/specimen/` | AS-IS | Re-render on canonical text | A | PUB/DERIV | SVG/PNG | S | P1 | Threshold | static plate |

### Unlabeled media (triage before anything)
| Asset | Role | Path | State | Action | Prov | Vis | Format | Eff | Prio | Section | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 large screen recordings | May already be demos | `~/Desktop/Screen Recording 2026-{03-28,06-03,06-05}.*` | DECIDE | Owner watches; label/keep/cut | S | ? | mp4 | S | P1 | TBD | ignore |
| Project demo videos | Older demos | `Projects/.github.io/projects/{puppetDemonstration,academicWeapon}.mov` | AS-IS | Review relevance | S | PUB | mov | S | P3 | Study/archive | omit |

---

## A. Anchor rooms

Four projects earn full narrative case studies — deliberately **two literary + two fidelity** so the collection's single argument is unmistakable. Everything else is a study or archive entry (§B).

### Anchor 1 — Echo *(afterlife of language)*
- **Core story:** modern speed strips emotional weight from language; Echo gives a text an afterlife by turning it into a field that keeps moving after the sentence ends.
- **Exact visual assets:** frozen plates of all 5 modes (Moonlight + Paper); `aboutBackground.JPEG` as backdrop; re-rendered semantic specimen on the canonical text.
- **Exact videos:** one 15–25s seamless loop pairing **soup drift + vortex spin** (strongest motion); optional second loop of network settle.
- **Diagrams:** one small honest pipeline note (text → co-occurrence + Datamuse → field).
- **Text excerpts:** "words that continue breathing"; "each form gives language a different kind of afterlife"; Borges epigraph; the embedded poem (pending approval).
- **Interaction:** link out to the live app; optional inline "portrait of a text" toy (net-new, later).
- **Sound (justified?):** yes — Echo's own ambient track, off by default, one visible toggle (rights pending).
- **Newly created:** 5-mode capture suite + loops (biggest single gap).
- **Already exists:** hero image, soundtrack, poem, live deploy, specimen toolchain.
- **Remember:** *a field of words that keeps breathing after you stop reading.*

### Anchor 2 — MuseLab *(interpretation as dossier)*
- **Core story:** AI tools treat a poem like a support ticket; MuseLab answers *what is this text about* with an archival dossier, not a chat — and keeps its own taste honest.
- **Exact visual assets:** curated 6–8 of the 39 Playwright PNGs (Landing → Loading → Draft → Pulse → Margins → Imprint); recolored brand mark.
- **Exact videos:** Imprint residue loop (vortex/soup/ascii); Pulse force-settle clip.
- **Diagrams:** Evidence→Pattern→Interpretation→Claim→Revision stack (C2); hybrid pipeline (C4); the two-agent-systems meta-note.
- **Text excerpts:** "Charts and graphs are evidence. The reading is the product."; taste_profile / disliked_patterns lines.
- **Interaction:** link to live app; custom-poem Imprint still using the canonical text.
- **Sound:** none (workshop calm).
- **Newly created:** Imprint + Pulse motion captures; custom-poem run.
- **Already exists:** 39 UI PNGs, reference board, brand SVGs, doctrine prose.
- **Remember:** *a workshop that reads your poem back to you as evidence, not advice.*

### Anchor 3 — Differ *(contested fidelity, made accountable)*
- **Core story:** the same designed experience fails differently across populations; Differ makes *who and where meaning breaks* legible so designers can be accountable. (Placed high to prove the practice isn't "only literary.")
- **Exact visual assets:** ~4 reframed result plots (C3); one rendered Chicago map plate.
- **Exact videos:** 60–90s interface walkthrough of one accountable-perspective case (owner-recorded or narrated).
- **Diagrams:** platform architecture (C4); interpretation stack applied to a real case (C2).
- **Text excerpts:** compressed CHI abstract (3 sentences); "accountable perspectives — who/where meaning breaks."
- **Interaction:** none required; optional plot hover if time.
- **Sound:** none.
- **Newly created:** the walkthrough video; the map plate; C3 reframing.
- **Already exists:** paper, 28 plots, geojson, code.
- **Remember:** *a metric can be "fair" on average and still betray a specific group — this shows you which.*

### Anchor 4 — The Illusion of 5 Stars *(a metric that lies across contexts)*
- **Core story:** 4.9 does not mean the same thing in Hong Kong and Chicago — a calibration argument any visitor can feel. The public-legible face of the fidelity twin.
- **Exact visual assets:** the single recomposed **claim plate**; 2–3 supporting figures (C3); poster thumbnail.
- **Exact videos:** none (data honesty).
- **Diagrams:** small city-comparison plate.
- **Text excerpts:** the argument in two sentences; short method note.
- **Interaction:** none.
- **Sound:** none.
- **Newly created:** the one claim plate (recomposed from 29 existing figures).
- **Already exists:** 29 figures, poster PDF, pipeline doc.
- **Remember:** *the same number means different things to different people — and that's measurable.*

> **Why these four:** each has a shippable asset base, each carries one memorable idea, and together they braid afterlife-of-language (Echo, MuseLab) with fidelity-under-uncertainty (Differ, Airbnb). No fifth anchor — additional full rooms would flatten the argument into "everything is equally important."

---

## B. Studies and archive

Smaller entries — short studies, plates, or archive items, **not** full rooms.

| Entry | Form | Why NOT an anchor |
| --- | --- | --- |
| **The Grave of Ideas (dreams)** | Study / plate (gated) | Emotionally central but **privacy-gated**; can't anchor a public exhibition on unpublished dream text. Becomes a quiet study (derived field by default; live graph only if approved). |
| **Nommi** | Short study | Shipped and honest, but its lesson (community/critical mass) is a *complication*, not a thesis pillar; one candid study serves better than a full room. |
| **Systems & Signals** (Tesla, PwC, NUSolar, ai-data-platform) | Grouped study | Tesla/PwC are confidential (described-only); NUSolar/ai-data-platform lack exhibition visuals. Grouping avoids four thin cards and still lands the engineering credibility. |
| **Poem-to-Song / POMDP / IMEC** | Research plates | Strong ideas but thin local assets (posters/paper only; IMEC unlocated). Belong as framed plates in a research shelf, not rooms. IMEC is a keep-or-cut. |
| **Creative archive** (poems, art, photography, zine) | Room-as-archive (curated) | It's a *collection*, not a single narrative; curate the strongest few rather than build a case study around any one piece. |
| **Legacy Unity games / world-happiness viz / older demos** | Deep archive (optional) | Undergraduate scope, off-thesis; keep as an "earlier work" index at most. |

---

## C. Global asset system

Reusable, portfolio-wide. Acquisition tag per asset: **[EXTRACT]** from existing project · **[PROCEDURAL]** regenerate from code/data · **[RECORD]** new capture · **[PHOTO/SCAN]** · **[WRITE]** owner-authored · **[SELECT]** from archive.

| Asset | Purpose | Acquisition | Notes |
| --- | --- | --- | --- |
| **Floating Echo graphs** | Signature field motif across rooms | **[PROCEDURAL]** via `fieldEngine` (`vortex-field.js`) + **[EXTRACT]** Echo/MuseLab | Reuse with reason; canonical-text-driven; frozen-plate fallback. |
| **Typographic plates** | Plate/folio numbering, room mastheads | **[PROCEDURAL]** extend `profile-art/artifacts` (opentype outlines) | Static numbers (no false-precision animation). |
| **Manuscript fragments** | Annotated-text texture (Draft-style) | **[EXTRACT]** MuseLab markup + **[SCAN]** real drafts | Category-keyed marks + legend; needs 1–2 real scans to be honest. |
| **Project marks** | Per-project sigils | **[EXTRACT]** existing `mark-{echo,muselab,differ,rag}.svg`; **[PROCEDURAL]** add Airbnb/Nommi | Recolor to unified tokens. |
| **Motion language** | One physics everywhere | **[EXTRACT]** design-dna: `ease k=0.14`, `easeArchival` | No spring/bounce; ≤3–5 animated at once. |
| **Audio controls** | Honest, opt-in sound | **[WRITE]/[PROCEDURAL]** minimal toggle component | Off by default; visible control; nothing depends on audio. |
| **Captions / alt-text** | Wall text + accessibility | **[WRITE]** owner voice (assistant drafts, owner approves) | Calm interpretive voice; every figure gets one. |
| **Dividers** | Only structural separator | **[PROCEDURAL]** 1px hairline + registration marks | Optional one-time "draw-in." |
| **Loading states** | Archival settle, not spinner | **[EXTRACT]** MuseLab `ArchiveLoading` + **[PROCEDURAL]** | Scan-band / specimen re-settle. |
| **Mobile fallbacks** | GitHub-mobile + phone legibility | **[PROCEDURAL]** responsive rules | Frozen plate replaces heavy loops; single-column rooms. |
| **Reduced-motion fallbacks** | Respect `prefers-reduced-motion` | **[PROCEDURAL]** every animated asset | Rest at visible state; loops → poster stills. |

---

## D. Owner request list

Concrete, itemized. Check each; nothing publishes from Bucket 1/3 without a tick here.

**Privacy & confidentiality decisions**
1. Rule on the **7 dream texts** (`theGraveOfIdeas/dreams.js`): mark each as **public**, **derived-only** (form reused, no text), or **private**.
2. Confirm whether the **live dream graph** may be embedded publicly, shown as a derived neutral field, or kept private.
3. Confirm the **Tesla** one-paragraph summary wording is non-confidential and safe to publish (or say "omit Tesla").
4. Confirm the **PwC** multi-agent/RAG summary wording is safe to publish (or say "omit PwC").
5. Confirm the **Differ paper** (CHI 2026 submission) may be cited/linked publicly now, or only title+abstract until acceptance.
6. Confirm the **Echo soundtrack** (`backgroundMusic.mp3`) source and that you have rights to publish it.
7. Confirm you authored / may publish the **zine** ("Jae Final Zine Spreads").

**Selections from your archive**
8. **Select 3–6 poems** you are comfortable publishing (from the 11 curated + 33 legacy).
9. **Choose 8–12 artworks** from `public/art/` + legacy `drawings/`.
10. **Choose 8–15 photographs** (I'll convert any `.HEIC`).
11. **Pick 1–2 graduation portraits** from the 299 for me to color-grade into a hero + colophon.
12. Pick **1 canonical specimen text** (a poem/passage) to recur across Echo, MuseLab, and the specimen.

**Recordings (you record, or approve me to auto-capture)**
13. **Record a 20–30s MuseLab dossier walkthrough @1440p** (or approve automated Playwright capture).
14. **Record the Echo 5-mode demo** (or approve me to capture locally): ~15–25s per mode, Moonlight + Paper, using the canonical text.
15. **Record a 60–90s Differ interface walkthrough** of one accountable-perspective case.
16. **Record a 20–30s Nommi demo @1440p** locally (replacing the Drive link).
17. **Watch and label the 3 large unlabeled screen recordings** (`2026-03-28` 1.9GB, `06-03` 438MB, `06-05` 374MB): keep-as-demo / personal / delete.

**Locate / decide**
18. **Locate NUSolar** visualization assets or a repo, or approve a text-only entry.
19. **IMEC drones:** provide assets or **cut** the entry.
20. **Poem-to-Song:** optionally provide poem + matched song excerpt + embedding view for a real pairing artifact (else poster-only).

**Writing (short, in your voice — I can draft, you approve)**
21. Approve/edit the **one-sentence thesis** for the Threshold.
22. Write/approve **one candid Nommi reflection** line.
23. Approve the **two-sentence stakes line** for Differ, Airbnb, POMDP each.

---

## E. First build sequence

Finite and shippable. Fills the liked shell incrementally; the site stays deployable at every step. Do **not** turn all work into equal case studies.

**Step 1 — Keep the shell; wire ingestion (½–1 day).**
Adopt `~/Desktop/xinyuezhang-shirley.github.io` as-is. Create `portfolio-archive/` and the content pipeline into `src/content/*.ts`. Reconcile `tokens.css`. *Ship: same site, cleaner tokens.*

**Step 2 — Ingest what already exists (1–2 days).**
Harvest AS-IS assets (MuseLab PNGs, Differ plots, Airbnb figures, Echo hero, Nommi graphics, GitHub SVGs, specimen). Convert HEIC. Draft captions/alt-text. *Ship: existing rooms get real figures.*

**Step 3 — Build ONE complete anchor room end-to-end: MuseLab (2–3 days).**
Chosen first because it has the richest existing assets (39 PNGs) and needs the least owner input. Curate folio sequence, capture Imprint/Pulse motion, add C2/C4 diagrams + excerpts. *Ship: one fully authored room — the template for the rest.*

**Step 4 — Extract the reusable visual system (1–2 days).**
Promote what worked in Step 3 into the Global Asset System (§C): field motif, plates, marks, motion, dividers, loading, mobile + reduced-motion fallbacks. *Ship: consistent dialect site-wide.*

**Step 5 — Remaining anchor rooms: Echo → Differ → Airbnb (3–5 days).**
Apply the system + newly recorded media (owner items 12–15). *Ship: all four anchors live.*

**Step 6 — Studies & archive (1–2 days).**
Grave of Ideas (per §D ruling), Nommi, Systems & Signals, research plates, curated creative archive. Short forms only. *Ship: full breadth, correctly weighted.*

**Step 7 — Polish (1 day).**
Threshold portrait + thesis, colophon, transitions, sound toggle, accessibility pass, 10/30/60s test for engineer/designer/researcher, motion-budget audit. *Ship: the composed exhibition.*

> **Critical path / owner blockers:** Steps 3–5 depend on owner items 8–17 (selections + recordings + the unlabeled-recording triage). Step 1–2 and the MuseLab room (Step 3) can proceed **immediately** with zero owner input — start there.

---

# Part III — Owner Authorizations & Acquisition Status

**Supersedes** prior owner-blocker assumptions in Part II §D where they conflict.
Standing permission granted 2026-07-18 to discover, duplicate, extract, and curate under read-only archive rules.

## III.0 Operating rules (binding)

**May:** recursively inspect Desktop/projects/Notes/resume/portfolio/repos/media; **duplicate** into `portfolio-archive/`; copy, resize, transcode, crop, thumbnail, extract frames, optimize, generate GIF/SVG/derivatives.

**Must not:** move, rename, delete, or overwrite originals. Treat the archive as read-only.

**Stop only when:** publication rights unclear · confidential material · private writing proposed for public · assets genuinely missing · legal/ethical concern.

**Do not** repeatedly ask permission for discovery/duplication.

### Project constraints (owner)

| Project | Constraint |
| --- | --- |
| **NUSolar, IMEC Drones** | Historical → **concise archive entries only**. No videos, galleries, or elaborate interaction. Extra visual weight goes in an "Earlier Projects / Archive" section — do not inflate these into rooms. |
| **Differ** | Active research. **Do not publish** paper PDF / manuscript / unpublished writing. **May use** screenshots, interface recordings, figures, diagrams, plots, posters, public-safe visuals. |
| **Airbnb** | Full repo + written report + academic poster authorized. Curate figures — do not dump notebook outputs. |
| **Academic posters** | Exhibition artifacts: extract figures, crop details, quote key results; keep full poster as downloadable artifact. |
| **Poems / dreams (Notes)** | Readable. Categorize poems: candidate / inspirational-only / private / Needs Owner Approval. Dreams = source material; propose only those that materially strengthen the portfolio; else private. |
| **Videos** | Duplicate existing; automate capture when professional quality is possible; request manual recording only when automation fails. |
| **Priority** | MuseLab → Echo → Differ → Airbnb → supporting studies → earlier archive. Maximize exhibition quality, not project count. |

Working directory: `~/Desktop/github-identity-system/portfolio-archive/` (gitignored). Log: `portfolio-archive/ACQUISITION_LOG.md`.

---

## III.1 Acquisition completed this session

### Owner-provided files ingested → `_incoming/` / anchors

| Provided path | Disposition |
| --- | --- |
| `Downloads/Differ__…2025_R_R_.pdf` | Copied to `_incoming/` — **PRIVATE; never publish**. Used for curator understanding only. |
| `Downloads/CS281 (7).pdf` | = Airbnb report *The Illusion of 5 Stars* → `anchors/airbnb/report_Illusion_of_5_Stars.pdf` **PUB** |
| `Downloads/CS229_Final_Project_Poster (1).pdf` | Poem-to-Song poster → `_incoming/CS229_poster.pdf` **PUB (extract figures)** |
| `Downloads/Budget_Constrained_Aid_Allocation_as_a_POMDP (1).pdf` | → `_incoming/POMDP_…` + earlier archive **PUB as downloadable / plate** |
| `Downloads/CS146J Final Submission.pdf` | Echo course writeup; reveals **public YouTube demo**: https://youtu.be/DXuX2TFZ5ro |
| `Downloads/278 Final Paper (1).pdf` | Nommi final → study material |
| `Downloads/Buddhist Literature Research Proposal.pdf` | → Needs Owner Approval (not an anchor) |

### Screen recording triage

| Recording | Duration / size | Identified content | Disposition |
| --- | --- | --- | --- |
| `Screen Recording 2026-06-03…` | 4:20 · 438MB · 1206×1912 | **Nommi** mobile Food feed (populated posts + skeleton) | **Usable.** → `studies/nommi/demo_2026-06-03.mov` + stills |
| `Screen Recording 2026-06-05…` | 3:13 · 374MB · 3420×1918 | CapCut editor over **Echo** Studio (Orbit · Romantic Death) | Not a clean demo reel; **Orbit stills extracted** → `anchors/echo/stills/orbit_romantic_death.jpg`. Prefer YouTube demo for motion. |
| `Screen Recording 2026-03-28…` | 1.9GB | Not yet frame-triaged | Pending automated frame pass |

### Harvested from repos (duplicates)

- MuseLab: 8 curated Playwright UI PNGs → `anchors/muselab/ui/`
- Differ: 28 result plots → `anchors/differ/plots/` (**no UI screenshots found**)
- Airbnb: 29 figures → `anchors/airbnb/figures/` + public poster PDF
- Echo: `aboutBackground.JPEG`, `backgroundMusic.mp3`, Orbit stills
- Portfolio research PDFs: Airbnb poster, Poem-to-Song poster, POMDP paper

---

## III.2 Updated visibility / roles (delta from Part II)

| Item | Old assumption | New status |
| --- | --- | --- |
| Differ paper PDF | DECIDE / maybe cite | **PRIVATE — do not publish** (active research) |
| Differ plots | PUB | **PUB** (already harvested) |
| Differ UI / walkthrough | MISSING — request owner record | Still **MISSING** locally; see §III.3 needs list |
| Airbnb report | "I will provide" | **RECEIVED** (`CS281.pdf`) |
| Airbnb poster | In portfolio public/ | **RECEIVED / on hand** |
| Echo demo video | MISSING capture | **FOUND** YouTube https://youtu.be/DXuX2TFZ5ro + Orbit stills from June 5 recording |
| Nommi demo | MISSING local | **FOUND** June 3 screen recording |
| NUSolar / IMEC | Study / keep-or-cut | **Archive entries only** — no video/gallery |
| Poems / dreams via Notes | Blocked on permission | **Authorized to read**; macOS Automation for Notes from Cursor currently hangs — one-time OS permission needed (see §III.4) |

---

## III.3 Differ — resolved (no video; figures from paper)

Owner confirmed: **no Differ video is fine.**

**Action taken:** Extracted figures from the private CHI manuscript into `portfolio-archive/anchors/differ/from_paper/` and promoted exhibition crops to `anchors/differ/selected/` (Fig. 1, 3, 7–11 + DTR-1 analysis plots). **Paper PDF remains private and will not be published or linked.** Captions rewritten as public-safe wall text; no manuscript body text ships.

See `anchors/differ/selected/INDEX.md`.

---

## III.4 Notes access — resolved

Full Disk Access works. AppleScript Automation still times out (unnecessary).

**Exported (read-only duplicates):** `Writing and Poems` (97), `Dreams` (5), 26 dream-mentions elsewhere. Passwords never touched.

**Owner approved 2026-07-18:** Section A poem shortlist (9) · Section B proposed dreams (include if needed) · Grave of Ideas as inspiration + live graph (with its dream texts).

Cleared copies: `portfolio-archive/creative/approved/{poems,dreams,grave_of_ideas}/`  
Record: `portfolio-archive/creative/POEMS_DREAMS_CATEGORIZATION.md`

---

## III.5 Narrowed owner checklist (only remaining gates)

1. **Buddhist Literature Research Proposal** — keep as academic archive plate, or exclude?
2. **Portrait pick** — choose 1–2 from `Memories/graduationPhotos/` (or approve a shortlist of 5).

**Cleared by owner (2026-07-18):** Echo soundtrack · Differ no-video · Differ figures-from-paper (PDF private) · Poem shortlist A · Dream set B · Grave of Ideas graph + inspiration.

**No longer blocking:** Airbnb · Nommi · Echo YouTube · MuseLab UI · Differ figures · poems/dreams/Grave · NUSolar/IMEC archive-only.

---

## III.6 Immediate next autonomous steps (no redesign)

1. Continue MuseLab asset curation (web-optimized crops of the 8 UI PNGs; caption drafts).
2. Pull/transcode Echo YouTube demo into `anchors/echo/` (or hotlink + extract poster frames).
3. Curate Airbnb claim plate from the 29 figures + report (not a dump).
4. Select ~4 Differ plots for C3 framing; draft public-safe captions (no manuscript quotes).
5. Frame Nommi as a short study using the June 3 recording.
6. Retry Notes export once OS permission appears.
7. Frame-triage the 1.9GB March recording when spare time.

---

*End of curation plan. Parts I–III. No redesign proposed — acquisition under standing authorization is underway.*
