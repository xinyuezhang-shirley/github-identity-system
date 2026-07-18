# GitHub Profile README — Design Research & Strategy

**Status:** Research only. No implementation. No README / asset / commit changes.  
**Authoring context:** Creative-technology strategy before next build.  
**Date:** 2026-07-18  
**Subject:** Xinyue Zhang (`xinyuezhang-shirley`) — computational identity surface on GitHub  

---

## Executive summary

The strongest GitHub profile READMEs do **not** behave like full-screen posters. They behave like **documents inside a fixed, sanitized reading column**: short enough to scan, dense enough to signal identity, with visual craft achieved through **images/SVGs that GitHub will display as media**, not through page CSS.

Our recent force-settlement artwork correctly discovered a visual language (Echo-native, generated, residual). It **incorrectly assumed** that GitHub’s profile surface can host a tall, typographically fine computational plate as the primary UX. On the live profile, that plate becomes a **scaled-down card image**: hierarchy collapses, silence becomes empty chrome, and the artifact reads as “a PNG in a README,” not as an instrument.

**Strategic pivot (to approve before building):** treat the profile README as a **field notebook / instrument index** that *points* to Echo, MuseLab, and the portfolio site — not as a substitute for them.

---

## Method

Evidence sources:

1. **Live profile repositories** — raw `README.md`, repo trees, `.github/workflows` via GitHub API / raw content (2026-07-18).
2. **Curated index** — [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme).
3. **Platform docs** — GitHub Docs (profile README prerequisites; Markdown/`picture`); [github/markup](https://github.com/github/markup) pipeline notes; GitHub Changelog (theme-aware images, 2022-05-19).
4. **Craft writeups** — trueberryless “technically impressive” SVG/foreignObject approach; DenverCoder1 typing-SVG FAQ; community SVG dark-mode investigations.
5. **Local product study** — Echo + MuseLab codebases (read-only), summarized as design primitives.

Screenshots were **not** archived as binary assets (per research brief). First impressions below are from rendered README structure and asset strategy as observed in repository sources.

---

# Part 1 — Exemplary profiles (~30)

Each entry: profile URL · repo URL · first impression · succeeds · fails · techniques.

### Editorial / minimal / identity-forward

| # | Profile | Repo | First impression | Succeeds | Fails | Techniques |
|---|---|---|---|---|---|---|
| 1 | [cassidoo](https://github.com/cassidoo) | [cassidoo/cassidoo](https://github.com/cassidoo/cassidoo) | Pure voice; newsletter + projects as links | Personality readable in native type; longevity | Little visual craft; easy to miss in a visual feed | Pure Markdown; no workflows; no stats widgets |
| 2 | [AmruthPillai](https://github.com/AmruthPillai) | [AmruthPillai/AmruthPillai](https://github.com/AmruthPillai/AmruthPillai) | Tiny logo + one sentence + site link | Extreme restraint; website is the product | Almost no GitHub-native information | Single PNG logo; Markdown link-out |
| 3 | [caneco](https://github.com/caneco) | [caneco/caneco](https://github.com/caneco/caneco) | Short bio bullets; design-aware without decoration | Clear identity; scannable | Generic emoji-list pattern | Pure Markdown |
| 4 | [f](https://github.com/f) (Fatih Kadir Akın) | [f/f](https://github.com/f/f) | Compact personal note | Memorable shortness | Minimal signal for technical depth | Pure Markdown |
| 5 | [jh3y](https://github.com/jh3y) | [jh3y/jh3y](https://github.com/jh3y/jh3y) | One spinning gem SVG → personal site | Single iconic motion object; strong CTA | Almost no textual bio on GitHub | Animated SVG via `<img>`; link wraps image |
| 6 | [bdougie](https://github.com/bdougie) | [bdougie/bdougie](https://github.com/bdougie/bdougie) | Literally `hi` | Anti-portfolio joke; memorable | No professional signal | Minimal Markdown; Actions exist for other experiments |
| 7 | [lauragift21](https://github.com/lauragift21) | [lauragift21/lauragift21](https://github.com/lauragift21/lauragift21) | Clean intro, light visual accents | Balanced minimal + friendly | Not highly distinctive visually | Markdown + light imagery |
| 8 | [rednafi](https://github.com/rednafi) | [rednafi/rednafi](https://github.com/rednafi/rednafi) | Code-mode / developer essay tone | Feels authored, not templated | Less “designed” | Mostly Markdown |

### Technical documentation / living index

| # | Profile | Repo | First impression | Succeeds | Fails | Techniques |
|---|---|---|---|---|---|---|
| 9 | [simonw](https://github.com/simonw) | [simonw/simonw](https://github.com/simonw/simonw) | Release feed + blog index in a table | Profile as **operating system for attention**; always fresh | Dense; not “beautiful” | Python `build_readme.py` + Actions; HTML `<table>`; section markers |
| 10 | [tw93](https://github.com/tw93) | [tw93/tw93](https://github.com/tw93/tw93) | Product engineer index; releases + stats | Clear craft + product narrative; bilingual energy | Table layout is utilitarian | Actions + `build_readme.py`; `<table>`; GIF accent |
| 11 | [ouuan](https://github.com/ouuan) | [ouuan/ouuan](https://github.com/ouuan/ouuan) | Research student dossier with blog + followers | Serious, auto-updated, anti-copy disclaimer | Stats card still template-ish | Actions (blog, waka, followers); `<picture>` for stats; HTML tables |
| 12 | [muesli](https://github.com/muesli) | [muesli/muesli](https://github.com/muesli/muesli) | Right-floated project art + generated activity | Illustration as product identity; readable prose | Generator pattern can feel dated | `readme-scribe` Actions; PNG float `align="right"` |
| 13 | [filiptronicek](https://github.com/filiptronicek) | [filiptronicek/filiptronicek](https://github.com/filiptronicek/filiptronicek) | Dynamic personal dashboard | High information freshness | Visual clutter risk | Actions + dynamic images |
| 14 | [JessicaLim8](https://github.com/JessicaLim8) | [JessicaLim8/JessicaLim8](https://github.com/JessicaLim8/JessicaLim8) | Word-cloud of languages/topics via Actions | Unique generative touch tied to activity | Clouds age poorly; badges dominate | Actions (`wordcloud.yml`); shields.io flood |
| 15 | [MartinHeinz](https://github.com/MartinHeinz) | [MartinHeinz/MartinHeinz](https://github.com/MartinHeinz/MartinHeinz) | “Everything” profile with metrics | Comprehensive | Template gravity | Stats APIs + Markdown sections |

### Visual / SVG / motion / experimental

| # | Profile | Repo | First impression | Succeeds | Fails | Techniques |
|---|---|---|---|---|---|---|
| 16 | [trueberryless](https://github.com/trueberryless) | [trueberryless/trueberryless](https://github.com/trueberryless/trueberryless) | Entire profile is **one SVG** (`![](./html-wrapper.svg)`) | Maximum craft inside GitHub constraints; bento layout via SVG/`foreignObject` pipeline; Actions refresh modules | Fragile; hard to maintain; accessibility/text selection weak; depends on SVG embedding tricks | Generated SVG; `src/` + scripts; workflows for bento/snake/spotify |
| 17 | [anuraghazra](https://github.com/anuraghazra) | [anuraghazra/anuraghazra](https://github.com/anuraghazra/anuraghazra) | Illustrated header PNG + stats ecosystem | Header is **linkable identity**; invented the stats genre | Stats widgets are now cliché when copied | Local PNG header (~80% width); github-readme-stats; badges |
| 18 | [DenverCoder1](https://github.com/DenverCoder1) | [DenverCoder1/DenverCoder1](https://github.com/DenverCoder1/DenverCoder1) | Banner + typing SVG + dense badge grid | Motion without JS; theme-aware patterns documented | High noise; “badge wall” | typing-svg service; shields; stats; `<picture>` patterns |
| 19 | [WaylonWalker](https://github.com/WaylonWalker) | [WaylonWalker/WaylonWalker](https://github.com/WaylonWalker/WaylonWalker) | Banner image as site doorway; story thumbnail | Strong personal brand; blog funnel | Icon row can feel social-media | PNG banner; float thumbnail; Actions for follower SVG |
| 20 | [blackcater](https://github.com/blackcater) | [blackcater/blackcater](https://github.com/blackcater/blackcater) | Animated hi + SVG social chips + generated body | Config-driven generation (`config.json` + `main.js`) | Looks like a productized template | Actions `update-readme.yml`; SVG icons; GIF |
| 21 | [novatorem](https://github.com/novatorem) | [novatorem/novatorem](https://github.com/novatorem/novatorem) | Spotify / realtime music card | Clever dynamic SVG | Depends on external auth/services | Serverless/API + SVG cards |
| 22 | [DoubleGremlin181](https://github.com/DoubleGremlin181) | [DoubleGremlin181/DoubleGremlin181](https://github.com/DoubleGremlin181/DoubleGremlin181) | Interactive/game-like profile experiments | Memorable novelty | Novelty decays; maintenance | Game-mode README patterns |
| 23 | [Raymo111](https://github.com/Raymo111) | [Raymo111/Raymo111](https://github.com/Raymo111/Raymo111) | Illustrated / multi-section visual | High production | Busy | Mix of images + Markdown |
| 24 | [adamalston](https://github.com/adamalston) | [adamalston/adamalston](https://github.com/adamalston/adamalston) | Polished “little of everything” | Friendly completeness | Template convergence | Images + stats + lists |
| 25 | [halfrost](https://github.com/halfrost) | [halfrost/halfrost](https://github.com/halfrost/halfrost) | Long-form technical presence | Depth | Heavy scroll | Markdown + images |

### Diagram / illustration / hybrid

| # | Profile | Repo | First impression | Succeeds | Fails | Techniques |
|---|---|---|---|---|---|---|
| 26 | [arturssmirnovs](https://github.com/arturssmirnovs) | [arturssmirnovs/arturssmirnovs](https://github.com/arturssmirnovs/arturssmirnovs) | Wide banner PNG + short bio | Classic “just images” category done simply | Banner can be generic stock-illustration energy | Static PNG banner |
| 27 | [ashleymavericks](https://github.com/ashleymavericks) | [ashleymavericks/ashleymavericks](https://github.com/ashleymavericks/ashleymavericks) | Gif-heavy social proof | Energetic | Dated GIF culture | GIFs + shields |
| 28 | [fnky](https://github.com/fnky) | [fnky/fnky](https://github.com/fnky/fnky) | Centered GIF stack welcome | Playful motion | Low information | Multiple GIFs; centered `<div>` |
| 29 | [Thaiane](https://github.com/Thaiane) | [Thaiane/Thaiane](https://github.com/Thaiane/Thaiane) | Code-mode aesthetic | Distinctive among templates | Niche | Code-block identity patterns |
| 30 | [natemoo-re](https://github.com/natemoo-re) | [natemoo-re/natemoo-re](https://github.com/natemoo-re/natemoo-re) | Values statement + work narrative | Ethical clarity; points to real work | Spotty visual system | Markdown + light HTML/table; Spotify tooling in repo |

### Additional reference (tools / meta, not all “best profiles”)

- [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) — defines the stats-card genre.
- [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) — SMIL/CSS-in-SVG motion via `<img>`.
- [awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) — taxonomy of genres.

---

# Part 2 — Reverse engineering (implementation patterns)

### Pattern A — Pure Markdown voice
**Examples:** cassidoo, caneco, AmruthPillai (near-pure), f  
**Build:** `README.md` only. No Actions required.  
**Why it works:** GitHub’s native typography *is* the design system; personality carries.

### Pattern B — Banner / hero image + Markdown body
**Examples:** anuraghazra, WaylonWalker, arturssmirnovs  
**Build:** Designed PNG/SVG in `/assets` or `/images`; `width="80%"` or full-width `<img>`; prose + links below.  
**Why it works:** Visual identity is **authored at image resolution**, then scaled by GitHub; body remains readable HTML/Markdown.

### Pattern C — Generated document (Actions)
**Examples:** simonw, tw93, ouuan, muesli, blackcater, JessicaLim8  
**Build:** Scripts (`build_readme.py`, `main.js`, templates) + workflows on schedule/push; markers like `<!--START_SECTION:...-->`.  
**Why it works:** Profile stays current without manual editing; content is structured data.

### Pattern D — Dynamic SVG services
**Examples:** DenverCoder1, stats users, typing-svg, capsule-render, Spotify cards  
**Build:** `<img src="https://…vercel.app/…">` or self-hosted generators.  
**Why it works:** Motion/data without client JS.  
**Risk:** Camo caching, service downtime, theme mismatch, sameness.

### Pattern E — Whole-README-as-SVG (extreme)
**Example:** trueberryless  
**Build:** README is a single image reference to a large SVG; CI regenerates modules (bento, snake, spotify). Internals use SVG (often with `foreignObject`/HTML-in-SVG pipelines in the generator).  
**Why it works:** Escapes Markdown layout limits.  
**Cost:** Accessibility, maintainability, text search, and “document” semantics suffer.

### Pattern F — Float / table layout hacks
**Examples:** muesli (`align="right"`), simonw/tw93/ouuan (`<table>`)  
**Build:** Allowed HTML subset for multi-column illusions.  
**Why it works:** Approximates editorial layouts without CSS Grid/Flex in Markdown.

### What almost nobody does successfully
- Relying on **custom page CSS** (stripped).
- Expecting **inline SVG** in Markdown HTML to behave like a web app (sanitized / unreliable; community consensus: ship SVG via `<img>`).
- Using a **single ultra-tall poster** as the only content (scales into unreadability on the profile card).

---

# Part 3 — GitHub limitations (documented)

### Profile README prerequisites
Per [Managing your profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme):

- Repo name **matches username**
- Repo is **public**
- Root `README.md` with content
- Repos created before July 2020 may need **Share to profile**

### Rendering pipeline
Per [github/markup](https://github.com/github/markup):

1. Convert Markdown → HTML  
2. **Sanitize aggressively** (scripts, many attributes, dangerous tags)  
3. Syntax highlight  
4. Extra filters (emoji, autolinks, image CDN/camo, etc.)  
5. Render on GitHub.com  

### Custom CSS
**No.** User CSS/`style`/`class`/`id` on README HTML are not a supported design surface. Visual systems must live **inside images/SVGs** or accept GitHub’s default Markdown chrome.

### HTML
GitHub allows a **whitelist** of tags in Markdown HTML (exact list evolves; community inventories commonly include structural tags such as `div`, `table`, `details`/`summary`, `picture`/`source`, `img`, headings, lists, etc., while stripping scripts and most styling hooks). Treat anything beyond Docs examples as **empirical**, not guaranteed.

### Scripts
**No.** Client JavaScript in READMEs does not run.

### Images & Camo
External images are typically proxied (Camo). Relative repo images are rewritten to raw URLs. Prefer assets in-repo for longevity.

### Dark / light images
Officially supported via `<picture>` + `prefers-color-scheme` ([Changelog 2022-05-19](https://github.blog/changelog/2022-05-19-specify-theme-context-for-images-in-markdown-beta/); also documented under image/`picture` in [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)).

Caveat (community-tested): **SVG referenced as `<img>` does not inherit GitHub’s `html[data-color-mode]`**. Dual assets via `<picture>` remain the reliable approach (see DenverCoder1 FAQ; Dries Vints investigation).

### SVG features
- **Via `<img src="*.svg">`:** broadly the practical path. SMIL/`<animate>` often works; complex CSS/JS inside SVG is inconsistent; `foreignObject` can work in some pipelines but is fragile across clients.
- **Inline SVG in Markdown HTML:** generally a bad bet (sanitization).

### Width / mobile
- Profile README renders in a **content card**, not viewport-fullscreen. Desktop readable width is roughly **~850–950px** class (varies with layout chrome); mobile is narrower with padding.
- Images with `width="900"` or `width="100%"` scale down. **Fine type baked into a tall 1200×1720 plate becomes sub-pixel mush.**
- Mobile: tall images force long scroll; motion GIFs cost bandwidth; tables often stack poorly.

### What scales
Native Markdown headings/lists/links; coarse imagery; short SVG banners; dual theme images; Actions-updated text sections.

### What breaks
Page CSS; hover interactions; scroll-linked motion; tiny type in rasters; assuming the profile is a canvas app; depending on third-party generators without fallbacks.

---

# Part 4 — Pattern analysis

### Recurring successful strategies
1. **Identity in the first screenful** — name/role/link visible without decoding an image.
2. **One strong visual accent** (banner, gem, float illustration) — not five competing heroes.
3. **Body as scannable text** — projects as links, not paragraphs inside pixels.
4. **Outbound gravity** — best profiles push to a site, blog, or product.
5. **Automation for freshness** — releases, posts, metrics — not for decoration.
6. **Theme pairs** when visuals matter (`<picture>`).

### Approximate genre frequencies (among curated “awesome” + sampled set)
| Strategy | Prevalence | Notes |
|---|---|---|
| Stats / shields wall | Very high | Saturated; low originality now |
| Single hero banner + text | High | Still effective if banner is distinctive |
| Actions-generated sections | High among “serious” builders | Best for indexes |
| Pure Markdown minimal | Medium | Highest longevity / lowest spectacle |
| GIF motion | Medium | Fun; ages into noise |
| Whole-SVG page | Rare | High craft ceiling; high cost |
| Giant single poster only | Rare among strong profiles | Matches our failed assumption |

### Information density that survives
- 1 short bio sentence  
- 3–6 project links with one-line descriptors  
- Optional 1 visual module  
- Optional 1 dynamic module (blog/releases)  
- Clear path to website  

### Typography that remains readable
- GitHub-native H1/H2/body  
- Image type: **display sizes designed for ~900px display width** (think 48–96px name at export, not 152px intended for a poster viewed at 100%)  
- Mono captions ≥ ~11–12px at display size  

### Layouts that fail
- Dashboard widget grids that fight mobile  
- Tiny labels in dense diagrams  
- “Silence” that only works at full-bleed museum scale  
- Forcing Echo’s live canvas interaction into a static card without translation  

---

# Part 5 — Critique of our current approach

### What worked
- **Correct medium insight (late):** craft must be rendered *outside* GitHub, then embedded.
- **Force-settlement as metaphor:** “paused simulation / residue” is a real Echo emotion — worth preserving as a *module*, not as the whole profile.
- **Dual theme pipeline:** `<picture>` light/dark is platform-correct.
- **Semantic graph discipline:** edges-as-relations is the right ethic even if the crop failed socially.

### What fundamentally cannot work inside GitHub
- Echo/MuseLab **application CSS**, webfonts, hover stretch, sliders, dossier tab motion.
- Expecting a **1200×1720 fine-type plate** to remain a typographic experience at profile-card scale.
- Using **negative space like a poster** when the surrounding GitHub chrome already supplies noise (pins, contributions, sidebar).
- “Interactive instrument” without leaving GitHub.

### What to preserve
- Night / paper dual atmospheres  
- Serif + mono duality (as *image* type or native Markdown hierarchy)  
- Field-summary caption voice (`mode · intensity · …`)  
- Manuscript/annotation grammar (MuseLab) as a *section*, not a wallpaper  
- Imprint residue as bridge between Echo and MuseLab  
- Outbound links to portfolio / projects  

### What to discard (for the profile surface)
- Single giant poster as the entire README  
- Tiny embedded hierarchy that only works at export resolution  
- Explaining the simulation in the artwork  
- Treating the profile as a replacement for the website  
- Stats-card sameness (unless used ironically/minimally)  

---

# Part 6 — Echo & MuseLab primitives (reusable)

*Extracted read-only from local codebases. Not a redesign.*

### Echo primitives
| Primitive | Why it succeeds | Emotion | In GitHub profile? |
|---|---|---|---|
| Night / paper tokens | Structural invert, not cosmetic | Contemplative / editorial desk | **Yes** as dual image atmospheres |
| Giant serif wordmark + thin mono meta | Brand *is* the composition | Monumental, slow | **Partial** — as short SVG/PNG banner, not full app hero |
| Lexical particle systems (vortex/soup/network/ascii) | Semantics drive geometry | Language as weather | **Yes** as stills / short GIF modules |
| Intensity·density·motion triad | One instrument model | Agency without chrome | **Partial** — caption + 2–3 stills |
| Field-summary strip | Gallery label tone | Curatorial | **Yes** as Markdown captions |
| About split (photo + poem tabs) | Controlled asymmetry | Intimate, literary | **Yes** as one still; no live reveal |

### MuseLab primitives
| Primitive | Why it succeeds | Emotion | In GitHub profile? |
|---|---|---|---|
| Folio type dialect (Cormorant/Literata/Plex/Caveat) | Role-clear hierarchy | Intelligent melancholy | **Partial** — rasterize or SVG-embed fonts |
| PaperSheet materials | Tactile without scrapbook chaos | Archival desk | **Yes** as stills |
| Dossier tab rail | Physical filing metaphor | Workshop intimacy | **Yes** as identity still |
| Manuscript ink grammar | Marks mean something | Scholarly care | **Yes** — annotated SVG poem + legend |
| Interpretation stack | Argument as UI | Trust | **Yes** — native Markdown sections |
| Pulse semantic force | Honest co-presence | Quiet constellation | **Yes** — exported graph still |
| Imprint residue suite | Echo math × MuseLab tone | Afterglow | **Yes** — bridge module |
| Archival easing | Shared motion language | Soft settle | **No** live; bake into GIF if needed |

### Iconic moments to quote (not clone)
1. Echo hero void + `ECHO` wordmark  
2. Echo studio vortex/soup after transform  
3. MuseLab landing intake stamp form  
4. MuseLab draft + ink marks  
5. MuseLab Imprint close  

---

# Part 7 — Ten directions (concepts only)

Each: GitHub fit · scroll · imagery · typography · static vs generated · Echo · MuseLab · website funnel.

### 1. Scientific notebook
- **Fit:** High — native Markdown + a few figures.  
- **Scroll:** Short–medium.  
- **Imagery:** Sparse figures with captions.  
- **Type:** GitHub-native + figure captions in mono.  
- **Static/generated:** Mostly static; optional Actions for “latest experiment.”  
- **Echo:** One vortex still as “Fig. 1.”  
- **MuseLab:** Interpretation-stack section.  
- **Site:** “Full lab notes →”.

### 2. Computational atlas
- **Fit:** Medium–high — multi-plate images.  
- **Scroll:** Medium.  
- **Imagery:** 3 coordinated plates (not one poster).  
- **Type:** Large in-image titles designed for 900px.  
- **Static/generated:** Offline render pipeline.  
- **Echo:** Map plates from modes.  
- **MuseLab:** Folio keys/legends.  
- **Site:** Atlas index links out.

### 3. Research paper
- **Fit:** High.  
- **Scroll:** Medium.  
- **Imagery:** Abstract + one method figure.  
- **Type:** Native headings as “sections.”  
- **Static/generated:** Static abstract; generated bibliography of repos via Actions optional.  
- **Echo/MuseLab:** Cited as works.  
- **Site:** “PDF / site”.

### 4. Observatory
- **Fit:** Medium — needs careful image scale.  
- **Scroll:** Short.  
- **Imagery:** Sky/field still + observation log.  
- **Type:** Sparse mono log lines.  
- **Static/generated:** Generated “tonight’s objects” (pinned projects) via Actions.  
- **Echo:** Constellation/network still.  
- **MuseLab:** Pulse graph as sky object.  
- **Site:** Deeper sky.

### 5. Laboratory
- **Fit:** High.  
- **Scroll:** Short.  
- **Imagery:** Instrument panel SVG (controls as labels, not interactive).  
- **Type:** Mono instrument labels + serif title.  
- **Static/generated:** Static panel; link “Run Echo”.  
- **Echo:** Primary.  
- **MuseLab:** Secondary bench.  
- **Site:** Live instruments.

### 6. Archive / dossier
- **Fit:** High for MuseLab DNA.  
- **Scroll:** Medium.  
- **Imagery:** One dossier tab still + stamped entries.  
- **Type:** Native list as catalog cards.  
- **Static/generated:** Catalog can be Actions-updated.  
- **Echo:** Imprint folder.  
- **MuseLab:** Primary metaphor.  
- **Site:** Open full archive.

### 7. Field notebook
- **Fit:** Very high.  
- **Scroll:** Short.  
- **Imagery:** 1–2 sketches max.  
- **Type:** Mostly native; handwriting only as rare SVG marginalia.  
- **Static/generated:** Mostly static.  
- **Echo/MuseLab:** Specimens taped in.  
- **Site:** Extended notes.

### 8. Operating manual
- **Fit:** High for systems builders.  
- **Scroll:** Medium.  
- **Imagery:** Diagrams of “how I work.”  
- **Type:** Numbered procedures in Markdown.  
- **Static/generated:** Manual static; changelog via Actions.  
- **Echo:** Modes as “operations.”  
- **MuseLab:** Critique protocol.  
- **Site:** Full manual.

### 9. Computational specimen
- **Fit:** Medium — one exquisite module.  
- **Scroll:** Very short.  
- **Imagery:** Single high-craft SVG/PNG specimen with plate caption.  
- **Type:** Caption carries meaning; native title above.  
- **Static/generated:** Offline freeze of real Echo/MuseLab run.  
- **Echo:** Specimen source.  
- **MuseLab:** Labeling/taxonomic voice.  
- **Site:** Interactive specimen viewer.

### 10. Interactive instrument (index)
- **Fit:** High **if** interaction is offsite.  
- **Scroll:** Short.  
- **Imagery:** Static “power-on” frame.  
- **Type:** Native CTA buttons-as-links.  
- **Static/generated:** Static frame; live on site.  
- **Echo/MuseLab:** The instruments themselves.  
- **Site:** Mandatory — profile is only the faceplate.

---

# Part 8 — Decision matrix

Scores: 1 (weak) – 5 (strong). Subjective but comparative.

| Direction | Orig. | Long. | Read. | GH fit | Mobile | Effort | Visual | Echo | MuseLab | Iconic | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 Scientific notebook | 4 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 4 | 4 | **41** |
| 2 Computational atlas | 4 | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 3 | 4 | **37** |
| 3 Research paper | 3 | 5 | 5 | 5 | 5 | 2 | 3 | 3 | 4 | 3 | **38** |
| 4 Observatory | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | **38** |
| 5 Laboratory | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | **39** |
| 6 Archive / dossier | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 5 | 4 | **39** |
| 7 Field notebook | 5 | 5 | 5 | 5 | 5 | 2 | 4 | 4 | 4 | 5 | **44** |
| 8 Operating manual | 3 | 5 | 5 | 5 | 5 | 2 | 2 | 3 | 4 | 3 | **37** |
| 9 Computational specimen | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 4 | 5 | **43** |
| 10 Instrument faceplate | 4 | 4 | 5 | 5 | 5 | 2 | 3 | 5 | 4 | 4 | **41** |
| *Current giant poster (control)* | 3 | 2 | 2 | 2 | 2 | 4 | 4 | 4 | 2 | 2 | **27** |

### Reading the scores
- **Leaders:** Field notebook (7), Computational specimen (9), Scientific notebook (1), Instrument faceplate (10).  
- **Strong MuseLab path:** Archive/dossier (6).  
- **Strong Echo path:** Laboratory (5), Specimen (9), Observatory (4).  
- **Control (poster-only)** loses on readability, GH fit, mobile, longevity, iconic potential.

### Recommended shortlist for approval (not yet building)
1. **Field notebook** — default strategy: native text hierarchy + 1–2 specimens.  
2. **Computational specimen** — if we want one unforgettable Echo freeze that still captions in Markdown.  
3. **Archive/dossier** — if MuseLab should lead the public face.  
4. **Instrument faceplate** — if the website/portfolio must be the primary experience.

Hybrid likely ideal: **Faceplate title (native) + one specimen image + dossier-style project list + site CTA**.

---

## Constraints for any future build (pre-approved principles)

1. Design for **~900px card width**, then check mobile.  
2. **Never** put primary identity type only inside a tall raster.  
3. Prefer **modules** over monoliths (≤3 visual plates).  
4. Use `<picture>` for theme-sensitive art.  
5. Put relationships/projects in **Markdown links**.  
6. Generate offline; embed results; automate only what must stay fresh.  
7. Funnel curiosity to **Echo, MuseLab, and the portfolio site**.  
8. If a pixel cannot answer “why are you here?” with data or identity, remove it.

---

## Appendix — Key citations

- GitHub Docs — *Managing your profile README*  
- GitHub Docs — *Basic writing and formatting syntax* (`picture`)  
- GitHub Changelog — *Specify theme context for images in Markdown (Beta)* (2022-05-19)  
- github/markup — sanitization pipeline description  
- abhisheknaiidu/awesome-github-profile-readme — genre taxonomy  
- Empirical reverse-engineering of public profile repos listed in Part 1 (2026-07-18)  
- Local Echo + MuseLab sources (read-only primitives brief)

---

## Decision requested

Approve one primary direction (or a named hybrid) before any further README, asset, or pipeline work.

**Suggested default pending your call:**  
**Field notebook + one computational specimen** (native hierarchy, Echo/MuseLab still as figure, dossier-like project list, strong site link).
