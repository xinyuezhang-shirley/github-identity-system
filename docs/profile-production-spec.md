# Production Specification — GitHub Profile for Xinyue Zhang

**Status:** FROZEN design spec. Final review before production. No code, assets, or README in this document.  
**Role:** Lead Creative Director — final authority; freeze the spec, remove ambiguity.  
**Supersedes:** the corpus definition in `profile-creative-direction.md` Part 5 (see Part 0, challenge C6). All other accepted docs stand.  
**Bar:** a competent engineer implements this with zero further design decisions.

---

## PART 0 — Challenge the assumptions

Nothing survives because it was written. Each major assumption is attacked, then accepted or changed.

### C1 — Is a "quiet research document" the right format at all?
**Attack:** GitHub profiles that get remembered are often bold single images (Andrew6rant) or living dashboards (simonw). A calm document could read as *under-designed* and forgettable.  
**Alternatives:** (a) one full-bleed hero specimen only; (b) auto-updating index.  
**Verdict: ACCEPT the document.** (a) collapses to the poster failure the owner already rejected three times; (b) is simonw's identity, not hers, and violates "beauty through structure / interpretation over automation." The document format is the only one that lets *typography carry stance* and *one figure carry memory* — the two things the anthropology says are load-bearing. Kept.

### C2 — Is the chapter order optimal?
**Attack:** Maybe questions should come first (hook curiosity) or the specimen should open (maximum impact).  
**Alternatives:** Questions→Identity→Specimen; Specimen→Identity.  
**Verdict: ACCEPT Identity → Specimen → Work → Questions → Door.** Questions-first reads as manifesto (recursion failure). Specimen-first strands the image without a claim to interpret it. A stance, then evidence, then range, then open threads, then exit is the honest argument shape. Kept.

### C3 — Is the semantic gravity field actually the strongest specimen?
Fully re-opened in Part 2 (not assumed). Outcome there: **kept, but redefined** so its procedure represents the *practice* (importance-as-gravity + evidence→claim), not Echo the project.

### C4 — Are these the four right projects?
Fully re-opened in Part 3. Outcome: Echo, MuseLab, Differ retained; the fourth slot interrogated (rag_project vs Airbnb vs POMDP vs contracting). Resolved in Part 3.

### C5 — Anything inherited from Echo just because Echo exists?
**Found:** the dark theme "flat black" and the temptation to make the specimen *look like* Echo's orbit. **Action:** dark theme is justified independently (see C7), but the specimen must be **importance-encoded**, not an orbit render; any orbit-like appearance must be a *consequence* of the math, never the goal. The word "orbit" is banned from labels/captions. Inheritance audited, constrained.

### C6 — Anything inherited from MuseLab just because MuseLab exists? (and the corpus problem)
**Found two things:**  
1. The field-note caption voice — **justified**: it is the interpretive tone that unifies the whole practice, not MuseLab-specific chrome. Kept.  
2. **The creative-direction corpus (the README's own words) is wrong.** The new instruction is explicit: *the specimen should be generated from the body of work, not from the README itself.* The self-referential corpus was clever but circular.  
**Action: CHANGE.** Corpus is redefined in Part 1 as the **authored descriptions of the body of work**. This is the one substantive reversal in this review.

### C7 — Is dual-theme (Echo dark / MuseLab light) a gimmick?
**Attack:** Two themes could read as "two brands," contradicting one identity.  
**Verdict: ACCEPT, constrained.** The two themes must be the **same graph, same positions**, only material tokens differ — proving *one procedure, two temperaments* (the sibling-studios truth from the anthropology). If positions differed between themes it would be two artworks; that is forbidden. Kept as a single procedure rendered twice.

### C8 — Is "also Shirley" earned?
**Verdict: ACCEPT.** Real preferred name; signals the person behind the system (emotional-resonance axis). One occurrence, small. Kept.

### C9 — Four works — too many? too few?
**Attack:** Three would be more memorable; five would show range.  
**Verdict: ACCEPT four.** Three drops the systems/trust facet and re-reads as creative-coder; five re-enters coverage-pile. Four is the minimum that carries four distinct facets. Kept.

**Summary of Part 0 changes:** exactly one reversal — the specimen corpus (C6). Everything else survives attack with tightened justification.

---

## PART 1 — Freeze the corpus

The specimen is generated from the **body of work**. Deterministic and regenerable by anyone from these rules.

### 1.1 Included sources (canonical, authored text only)

| Source | Path | Extract |
| --- | --- | --- |
| Echo — project description | `echo/README.md` (intro) + `echo/frontend/about.html` (`.about-copy` + mode-card text) | Prose only; strip nav/code |
| MuseLab — project description | `MuseLab/README.md` (intro through "What makes it different" + the decisions list intro lines) | Prose only; strip code fences, tables, run instructions |
| Differ — research description | `xinyuezhang-shirley.github.io/src/content/research.ts` → `differ` `abstract` + `keyFindings[]` + `story[]` | String literals only |
| Systems piece — description | `xinyuezhang-shirley.github.io/src/content/work.ts` → `pwc` (RAG) `teaser` + `story[]` | String literals only |
| Practice statement | `github-identity-system/src/data/content.json` → `identity.statement` | The one sentence |

### 1.2 Excluded (explicitly)
- The README copy itself (Part 0 C6).
- All code, config, Markdown tables, code fences, run instructions, license text, nav labels.
- `node_modules`, generated files, prototypes, prior profile-art exports.
- Non-selected projects (Nommi, poem-to-song, POMDP, Airbnb, Tesla, NU Solar, scrapers) — they are not in the four-work narrative, so they are not in the specimen corpus. The specimen and the work list describe the **same** body of work.
- Poems, dreams, photography (private/aesthetic layer; not the public systems corpus).

### 1.3 Tokenization
1. Concatenate all included text into one document, preserving **sentence boundaries** (split on `.?!` and list-item boundaries → each becomes one "unit").
2. Lowercase; NFKD-normalize; strip to `[a-z\s-]`; collapse whitespace.
3. Split on whitespace; drop tokens shorter than 3 chars.

### 1.4 Stop words
- Standard English stop list (articles, pronouns, prepositions, auxiliaries, conjunctions, common adverbs).
- **Domain-generic build filler removed** so the center is meaningful, not procedural: `project, projects, built, build, building, using, use, used, made, make, thing, things, work, works, lot, kind, way, ways`.
- **Deliberately NOT removed** (these are the practice and must be allowed to reach the center if the data puts them there): `system, systems, meaning, language, human, interpretation, model, judgment, context, computation, computational, text, workshop, evidence, experience`.
- No other curation. The gravitational center is whatever the corpus actually elects.

### 1.5 Lemma folding (minimal, deterministic)
Merge only these pairs to their singular root; no stemmer: `systems→system`, `models→model`, `agents→agent`, `words→word`, `humans→human`, `interpretations→interpretation`, `contexts→context`, `poems→poem`, `metaphors→metaphor`, `questions→question`. Everything else stays as written.

### 1.6 Node definition
- Node = a surviving lemma.
- Node weight = raw frequency across the whole corpus.
- Keep the **top 30 nodes** by weight (ties broken alphabetically for determinism). 30 is fixed.

### 1.7 Edge definition
- Edge = two nodes co-occurring in the **same unit** (sentence/list item from 1.3.1).
- Edge weight = number of units in which the pair co-occurs.
- Keep edges with weight ≥ 2. If that yields fewer than 20 edges, lower threshold to ≥1 but cap total edges at the 40 highest-weight (deterministic tie-break by node-index sum, then alphabetical).

### 1.8 Importance & placement (the practice's math, not Echo's picture)
- `importance(node) = weight / maxWeight` ∈ (0,1].
- **Radius is an inverse function of importance** (the shared Mathematical DNA): `r = R_max - (R_max - R_min) * importance`. Highest-importance node → smallest radius → center.
- Initial angle: golden-angle spacing by importance rank `θ = rank * 2.399963` (radians) for even distribution; deterministic.
- **Force settle** (d3-force) with: charge (repulsion) for legibility, a **radial force pinning each node to its importance radius** (dominant), light collision to prevent label overlap. Link force at low strength so edges bend the field slightly without overriding radius.
- **Deterministic:** seed the PRNG (fixed seed constant); run a fixed tick count (e.g. 600) then freeze. Same input → same output, every run.
- Node visual size ∝ importance (label font size scales with weight). **Label is the node** — the word is drawn at its coordinate; no circles-as-icons, no legend.

### 1.9 Normalization for canvas
- After settle, compute bounding box of node positions; scale+translate to fit the export canvas with a fixed margin; **center the highest-importance node** in the crop. No per-node hand nudging.

### 1.10 Regeneration contract
Given §1.1 sources unchanged + these rules + the fixed seed, the graph is bit-stable. Any visible node position that cannot be traced to this pipeline is a **defect**. No hand placement, no manual editing, no decorative marks.

---

## PART 2 — Choose the specimen

Re-opened from zero (force graph not assumed).

| Candidate | Authenticity | Computational honesty | Tie to anthropology | GitHub readability | Memorability | Scalability | Evolves over time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **A. Semantic gravity field** (importance→radius, real co-occurrence) | High — her own math | High — deterministic settle | High — polar-importance DNA **+** evidence→claim (center=claim) | Good — big center survives scaling | High — "words fall to a heavy center" | Good — center-crop | High — re-run on new corpus |
| **B. Manuscript plate** (draft + semantic underlines) | Med — MuseLab-specific | Med — real features but fragile | Med — controlled chaos | **Poor** — underlines mush at 900px | Med | Poor | Low — fixed text |
| **C. Interpretation stack** (Evidence→Pattern→Interpretation→Claim) | High conceptually | **Low** — it's a labeled diagram, not a procedure | Highest concept | Good | Med | Good | Low — static |
| **D. Lexical topology / contour** (density field) | Med | High | Med — Diagram DNA | **Poor** — highest legibility risk (flagged in viz-ideas #09) | Low–Med | Med | Med |
| **E. Provenance graph** (projects→influences→time) | Med | Med — needs curated labels/edges (subjective) | Med | Med | Med | Med | Med — but edges are hand-judged → honesty risk |
| **F. New procedural artifact** | Unknown | Unknown | May drift | Unknown | Risky | Unknown | Unknown — violates "synthesize, don't invent" |

**Chosen: A — Semantic gravity field.**

**Why the others lose:**
- **B** dies on GitHub readability — fine underlines become sub-pixel mush at card scale (the exact failure documented in README research).
- **C** fails computational honesty — a four-box stack is a diagram, and Negative Space bans "visualizations without a claim" and diagram cosplay. (We *keep its idea* by making center=claim inside A.)
- **D** carries the highest legibility risk by our own prior assessment; contour fields read as decoration without a legend, and legends are banned.
- **E** requires hand-judged influence edges → subjective, not regenerable, fails the corpus contract.
- **F** requires inventing a procedure; the mandate is synthesis.

**Why A represents the practice, not just Echo:** the defining move is *importance becomes gravity* — the same math in Echo's vortex/orbit **and** MuseLab's Pulse — combined with *center = the claim, periphery = the evidence*, which is the evidence→claim chain that recurs in MuseLab, Differ, and Airbnb. Rendered on the **body-of-work corpus**, the image is a computed reading of what she builds. The procedure (deterministic importance-weighted settlement of real co-occurrence) is the point; appearance is a consequence. "Orbit" is banned as a description to prevent Echo-mimicry.

---

## PART 3 — Project curation

Optimize for narrative. Four facets, no overlap.

### Selected (order = the argument)

1. **Echo** — *text becomes living visual fields.*  
   - Belongs: origin of the visual grammar; purest "beauty through structure."  
   - Unique facet: **making language visible / computation as expression.**  
   - Prevents misconception: that her work is only backend/ML with no aesthetic authorship.

2. **MuseLab** — *a workshop that reads a draft instead of rewriting it.*  
   - Belongs: fullest expression of interpretation-over-automation, multi-agent + hybrid grounding, taste-as-infrastructure.  
   - Unique facet: **judgment stays with the human.**  
   - Prevents misconception: that "AI project" means a generation/chat wrapper.

3. **Differ** — *where a designed experience breaks down across who and where.*  
   - Belongs: the fidelity/measurement twin the anthropology says is under-credited; CHI-level research.  
   - Unique facet: **meaning breaks across context.**  
   - Prevents misconception: that she's a creative coder without a research program.

4. **rag_project** — *retrieval and agents held to real constraints.*  
   - Belongs: load-bearing "real systems under constraint" signal for the engineer that isn't creative-coding.  
   - Unique facet: **systems that must be trustworthy.**  
   - Prevents misconception: that the work is only expressive/academic and not production-grade.

### Fourth-slot interrogation (resolved)
- **vs Airbnb calibration:** duplicates Differ's context-breakage facet → excluded.  
- **vs POMDP aid:** strong, but "planning under uncertainty" adds a fifth theme that dilutes the four-facet story → excluded.  
- **vs professional agentic-contracting:** private, not linkable at repo level; keep it as a one-clause portfolio-level mention only, not a work line.  
- **Decision:** `rag_project` holds the systems/trust slot because it is public, links cleanly, and names the trust facet.  
- **Fallback (mechanical, not a design choice):** if `rag_project` is not public/linkable at build time, the line links to the portfolio's PwC case study instead, same copy — no other change.

### Excluded (with reasons)
- **Nommi / food-recommender:** consumer-social territory; its lesson overlaps nothing in the throughline and risks "app builder" read.  
- **poem-to-song:** beautiful, but cross-modal affect ≈ Echo/MuseLab facet already carried.  
- **Airbnb, POMDP:** see fourth-slot; theme duplication / dilution.  
- **Tesla, NU Solar, Weibo scrapers:** real engineering, but telemetry/infra doesn't state the meaning-fidelity thesis at a glance; they live on the résumé/portfolio.  
- **The portfolio site:** it is the door, not a work line.

---

## PART 4 — Reader journey

### Scroll, section by section

**I. Identity.** Notices the sentence first (nothing competes). Answers *who is this and what do they do?* Exists to set the lens for everything after. Remembers: a short, precise stance — not a job title.

**II. Specimen.** Notices a field of words with a heavy center thinning outward. Answers *what does their thinking look like?* Exists as evidence immediately after the claim. Remembers: **the gravity-field image + "importance, not layout."**

**III. Selected work.** Notices four one-line works, no logos. Answers *is this a program or a pile?* Exists to prove range with coherence. Remembers: "language + critique + fairness + systems, one mind."

**IV. Current questions.** Notices three unanswered questions. Answers *is there a throughline?* Exists to show thinking without a manifesto. Remembers: one question, probably *what's left of language after the sentence ends?*

**V. Door.** Notices one outward line + three links. Answers *where do I go?* Exists so the profile stays a faceplate. Remembers: "the real instruments are elsewhere."

### Timed simulation

**Software engineer** — 10s: "Not a template; a real generated image; unusual systems." 30s: reads four works → "architecturally real, not CRUD." 60s: caption + questions → "cares about honesty/reliability, human-in-the-loop."

**Computational designer** — 10s: "Authored visual language; silence; one figure." 30s: "the image is generative, position encodes meaning." 60s: "same grammar as Echo/MuseLab without copying them."

**HCI / AI researcher** — 10s: "A principle, not a title." 30s: "work spans language, interpretation, contextual fairness — a program." 60s: "the three questions name a coherent research stance."

**Failure guard:** each audience is served by a different element (works for the engineer, figure for the designer, questions for the researcher); losing one element doesn't lose one audience entirely. Structure holds.

---

## PART 5 — Visual system (frozen)

Every rule justified; nothing for "looks nice."

### Typography
- **Native GitHub Markdown type only** for all copy. *Why:* GitHub renders its type with dignity; baked-in type caused the "screenshots in Markdown" failure.
- **One display element:** the name as H1. *Why:* one extreme label↔display jump is the practice's typographic DNA.
- **Monospace (inline code ticks)** for: the domain line, the `PLATE 01 · semantic gravity field` label. *Why:* mono = index/gutter/annotation voice in both Echo and MuseLab.
- **H2** only for "Selected work" and "Current questions" and "Reading the work." *Why:* two heading levels total keeps it a notebook, not documentation.
- No other type styling; no bold runs inside body except a work **name** may be a link (link styling is enough emphasis).

### Spacing, margins, white space
- One blank line between thought units; never dense paragraphs (max ~2 lines/idea). *Why:* scannable in 10s; negative space is active composition.
- Everything **left-aligned**. *Why:* document, not poster; centered = landing page.
- A hairline (`---`) before and after the specimen. *Why:* the figure needs a rest beat on both sides.

### Captions
- Exactly one caption line under the figure, field-note voice: *what it is · what position means · that it is paused.* *Why:* contested fidelity — the caption is where the image admits what it is and isn't. No uncaptioned image ships.

### Hairlines
- GitHub `---` is the **only** divider. *Why:* it is MuseLab's 1px-rule grammar and the only legal divider; no cards, no emoji rules, no shadows.

### Section rhythm
`# Name` → mono alias → sentence → mono domain line → `---` → mono plate label → figure → caption → `---` → `## Selected work` → 4 lines → `---` → `## Current questions` → 3 lines → `---` → `## Reading the work` → door → links.

### Image rhythm & figure treatment
- **Exactly one figure**, numbered `PLATE 01`. *Why:* numbering asserts a real sequence and reserves (not fills) room for a future plate; one image = one memory.
- Figure spans the column (`width="100%"`, natural height); no float, no text wrap. *Why:* the figure owns its band.
- Label-as-node inside the figure; no legend, no icons. *Why:* Diagram DNA — the word is the data.

### Dark theme (Echo temperament)
- Background: flat black (`#000`), no gradient, no grain. Nodes: neutral off-white; edges: dim gray; center term brightest. Accent: none (a whisper at most). *Why:* Echo's real tokens (`styles.css` is pure neutral); flat black is honest to Echo, not a mood choice.

### Light theme (MuseLab temperament)
- Background: warm paper (`#f4efe6`→`#e8dfd2` subtle), graphite nodes, ferric accent `#8b6914` reserved for the **single center term only**. Edges: warm gray. *Why:* MuseLab's real tokens; accent used once, where importance peaks, so color encodes meaning rather than decorates.

### Removed rules (were tempting, cut)
- No drop shadows, no rounded frames, no border on the image, no second accent, no animation/GIF, no per-section icons, no background texture in either theme. Each removed because it adds appearance without encoding anything.

---

## PART 6 — GitHub constraints & behavior

Designed to feel native to GitHub, not a website in Markdown.

- **Rendering model:** README of the special repo `xinyuezhang-shirley/xinyuezhang-shirley`. Only sanitized Markdown + a small allow-listed HTML subset (`<picture>`, `<source>`, `<img>`, `<a>`). No CSS, no JS, no `<style>`. Spec uses only these.
- **Dual theme:** one `<picture>` with `<source media="(prefers-color-scheme: dark)">` + light `<img>` fallback. *Behavior:* GitHub swaps by the viewer's theme; the `<img>` alt text describes the specimen for screen readers and slow loads.
- **Asset URLs:** absolute raw URLs to committed PNGs in the profile repo (not relative), so images resolve on the profile overview. *Why:* relative paths have broken on profile renders before.
- **Format:** **PNG** for the specimen (fidelity; SVG fine-type mushes at scale). Two files (dark, light). Target display width 900; export at 2× (1800px) for retina, file kept lean.
- **Desktop/laptop:** ~900px reading column; figure fills it; type at native sizes. 
- **Tablet:** column narrows; single-column already; figure scales down — center term still legible (it's the largest).
- **Phone:** everything is single column; figure scales to ~320–390px wide — center-weighted crop guarantees the claim word stays readable while periphery gracefully shrinks. No element depends on hover or width beyond the image.
- **Dark/light mode:** handled by `<picture>`; both PNGs pre-rendered; no runtime theming.
- **Slow connections / image loading:** copy is native text and renders instantly without the image; alt text conveys the specimen's meaning; only one image to load; lazy by default. The profile is fully legible with images disabled.
- **Markdown limitations respected:** no tables-as-layout, no HTML `<div>`/CSS grid, no foreignObject tricks; links are standard `[text](url)`; the domain/label "mono" is inline code — a documented, stable render.
- **Accessibility:** alt text on the specimen; all links have descriptive text; contrast meets AA in both themes (off-white on black; graphite on warm paper).

---

## PART 7 — Acceptance test (reviewers → convergence)

### Round 1
**Reviewer A (interaction designer):** Structure clean; one figure good. *Concern:* caption must not be jargon; "co-occurrence" too technical. *Concern:* ensure the center term is genuinely legible on phone.  
**Reviewer B (GitHub engineer):** `<picture>` + PNG + absolute URLs + alt text required; confirm repo is public and named exactly; confirm profile render (Share-to-Profile if needed). *Concern:* keep PNG file size reasonable at 2×.  
**Reviewer C (design professor):** Importance-as-position is a defensible thesis, not decoration — good. *Concern:* is dropping stop-word filler curating the result too much? *Concern:* honesty — can a stranger regenerate the graph?

### Revision 1
- Caption reworded to lead with meaning; replace "co-occurrence" with "real connections between the words," keep exactly one honest technical clause ("distance follows importance, not layout"). 
- Phone legibility promoted to a Phase-3 success criterion (center term must be readable at 320px).
- Stop-word list frozen and published (Part 1.4) with an explicit "not removed" list, so curation is a *documented rule*, not taste; professor's concern answered by the regeneration contract (1.10).
- File-size budget added to Phase 3 (≤ ~400KB per PNG target).

### Round 2
**A:** "Caption humane; phone criterion added. Converged."  
**B:** "Picture/alt/URLs/format/size all specified; render checkpoint present. Converged."  
**C:** "Frozen stop-list + regeneration contract make it honest and reproducible. Converged."

**Converged.** No design items remain open; all residual items are production tasks.

---

## PART 8 — Freeze implementation

### Phase 0 — Corpus freeze
- **Deliverables:** a committed `corpus.json` (or equivalent) capturing the exact extracted text units from Part 1.1, plus the frozen stop-list and lemma map as data.
- **Dependencies:** access to the five sources (all local/public).
- **Success criteria:** re-extraction from sources reproduces `corpus.json` byte-for-byte; excluded content (1.2) absent.
- **Checkpoint:** owner confirms the corpus is the body of work, not the README.

### Phase 1 — Wireframe
- **Deliverables:** text-only README mock using Part 7 copy from `profile-creative-direction.md` (identity, labels, four works, three questions, door), no image yet.
- **Dependencies:** Phase 0 not required; copy already frozen.
- **Success criteria:** chapter order, headings, hairlines, link targets match this spec; reads calmly top-to-bottom.
- **Checkpoint:** owner approves voice/order on the text-only version.

### Phase 2 — Specimen generator
- **Deliverables:** deterministic generator implementing Part 1.3–1.9 (tokenize → nodes(top 30) → edges → importance → radius → seeded force settle → freeze positions → normalized layout). Reuse honest parts of `profile-art/` (graph/settle) only where they match these rules.
- **Dependencies:** Phase 0 corpus.
- **Success criteria:** same input+seed → identical positions across runs; highest-importance node is centered; every position traceable to the pipeline (no hand placement).
- **Checkpoint:** audit run — dump node weights + positions; confirm center term is meaningful (expected candidates: `system`/`meaning`/`language`) and the field is truthful.

### Phase 3 — Rendering
- **Deliverables:** two PNGs (dark = Echo tokens, light = MuseLab tokens), same positions, label-as-node, center term emphasized (light: ferric accent; dark: brightest), 1800px export for ~900px display, ≤ ~400KB each; committed to the profile repo assets.
- **Dependencies:** Phase 2 positions; Part 5 tokens.
- **Success criteria:** center term legible at 320px; periphery degrades gracefully; no grain/shadow/legend; passes AA contrast; looks authored not templated at 900px and on a phone.
- **Checkpoint:** scale + theme test in both modes; Negative-Space pass (no forbidden element).

### Phase 4 — README construction
- **Deliverables:** final `README.md` in `xinyuezhang-shirley/xinyuezhang-shirley`: native copy, `<picture>` dual-theme specimen with absolute raw URLs + alt text, four work links (rag_project fallback per Part 3), three questions, door link.
- **Dependencies:** Phases 1–3; assets committed and served at their raw URLs.
- **Success criteria:** renders on the live profile overview; light/dark swap works; mobile holds; no broken links; text legible with images disabled.
- **Checkpoint:** confirm profile visibility (Share-to-Profile if the overview doesn't show it); owner sign-off.

### Phase 5 — Verification
- **Deliverables:** three-audience 10/30/60s read-through notes; a fresh-viewer 30s memory test; Negative-Space final audit; archive old tall poster off the profile surface.
- **Dependencies:** Phase 4 live.
- **Success criteria:** all Success Criteria + the memory test yields "words falling to a heavy center" + a paraphrased idea/feeling (not "cool graph").
- **Checkpoint:** owner final acceptance.

---

## Design Decisions Frozen

**Finalized:**
1. **Format:** short research document in GitHub's scroll (not page/poster/dashboard).
2. **Chapter order:** Identity → Specimen → Selected work → Current questions → Reading the work (door).
3. **Principle sentence:** *I design systems that preserve meaning as it moves between people, language, and computation.*
4. **Alias:** "also Shirley," once, mono, small.
5. **Specimen:** Semantic gravity field — deterministic importance-weighted force settlement of real co-occurrence; center = highest importance (the claim), periphery = evidence; label-as-node; no legend; "orbit" banned as description.
6. **Corpus (REVERSED from creative direction):** the body of work — Echo, MuseLab, Differ, rag/PwC descriptions + practice statement — **not** the README's own words. Exact sources, tokenization, stop-list, lemma map, node (top 30), edge (≥2 co-occurrence), importance/radius math, seed, and normalization frozen in Part 1; regenerable and hand-placement-free.
7. **Specimen count/format:** exactly one figure; two PNGs (dark/light), same positions; `<picture>` swap; 1800px export, ≤ ~400KB, absolute raw URLs, alt text.
8. **Themes:** dark = Echo flat-black neutral (no accent); light = MuseLab warm paper with ferric accent reserved for the single center term.
9. **Works (order = argument):** Echo (make language visible) · MuseLab (judgment stays human) · Differ (meaning breaks across context) · rag_project (systems that must be trusted). rag_project fallback = PwC portfolio link if repo not linkable.
10. **Questions (three, unanswered):** meaning when a model must speak for someone · where universal measures stop meaning the same thing · what's left of language after the sentence ends.
11. **Visual grammar:** native type only; one H1 display; mono for labels/domain; two H2s max; `---` sole divider; left-aligned; one caption per figure; no shadows/rounded/grain/second accent/animation/badges/stats/streaks.
12. **Copy:** as drafted in `profile-creative-direction.md` Part 7, with caption reworded per Part 7 revision here (lead with meaning; "real connections," keep "importance, not layout").
13. **Repo target:** `xinyuezhang-shirley/xinyuezhang-shirley`, public, exact-name.

**Intentionally left open (with justification):**
- **A1 — Final center term** (`system` vs `meaning` vs `language`): not a design choice; it is an *output* of the frozen procedure and must not be pre-decided or nudged. Verified, not chosen, in Phase 2. Leaving it open is required for honesty.
- **A2 — Exact node/edge counts within the frozen caps** (≤30 nodes, edge thresholds): determined by the data under the frozen rules; not tunable for aesthetics.
- **A3 — rag_project link target** (repo vs PwC portfolio): resolved mechanically at build time by public availability (Part 3 fallback); no design judgment involved.

No subjective design decisions remain. Implementation may proceed through Phases 0–5 mechanically upon approval.

*End of production specification. Do not begin implementation.*
