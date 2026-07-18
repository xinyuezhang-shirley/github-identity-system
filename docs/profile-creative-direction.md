# Creative Direction — GitHub Profile for Xinyue Zhang

**Status:** Creative direction. Approval gate before implementation. No code, assets, or README writes.  
**Role:** Creative Director shipping one profile that could only belong to Xinyue Zhang.  
**Inputs (accepted as constraints):** GitHub README research · Computational Identity research · Design Anthropology · Negative Space · Concept Brief.  
**Rule:** Synthesize, don't invent. When impressive competes with authentic, choose authentic.

This document is intended to be concrete enough that implementation involves almost no further design decisions.

---

## 0. Locked decisions (read this first)

| # | Decision | Value |
| --- | --- | --- |
| D1 | Format | A short research document in GitHub's scroll — not a page, poster, or dashboard |
| D2 | Principle sentence | *I design systems that preserve meaning as it moves between people, language, and computation.* |
| D3 | Alias | "also Shirley" — once, quiet |
| D4 | Chapter order | Identity → Specimen → Selected work → Current questions → Reading the work |
| D5 | Specimen | **Semantic gravity field** — one force/polar settlement where radius encodes importance and edges encode real co-occurrence, run on a real corpus (see Part 5) |
| D6 | Specimen count | Exactly one, dual-theme via `<picture>` |
| D7 | Works | Echo · MuseLab · Differ · one systems/AI piece (see Part 6) |
| D8 | Questions | Three, present tense, unanswered |
| D9 | Voice | Calm, interpretive, curious; no clichés |
| D10 | Divider | GitHub's `---` hairline only; no cards, no emoji rules |
| D11 | Omitted | Stats, streaks, badges, typing SVG, snake, trophies, grain, banners |

Everything below defends these.

---

## PART 1 — The experience (top to bottom)

A narrative of scrolling, described as experience, not markup.

### First contact (before scrolling)
The visitor lands and sees **calm**. A name, a quiet second name, one sentence, and a thin line. No banner shouting, no color, no motion. The emotion is *this person is serious and unhurried*. The first thing noticed is the **sentence**, because nothing competes with it. The question it answers: *who is this and what do they actually do?* It exists first because every later element is read through it.

### The specimen (first scroll)
One image resolves into view: a **field of words held together by gravity** — dense and certain near the center, thinning toward the edges, a few honest lines connecting them. It does not look decorated; it looks *settled*, as if a process was paused. The emotion is **recognition of authorship** — "a person made this system, and the image is a readout of it, not a graphic." The question it answers: *what does their thinking look like?* It appears second because a claim (the sentence) should be immediately followed by evidence you can look at. A small caption underneath tells the truth about it — what it is, what the distances mean, that it is paused. That caption is the tell that this person interprets rather than performs.

### Selected work (second scroll)
Four works, each one line. No thumbnails, no logos, no stacks of tech. The emotion is **range with coherence** — different domains, obviously one mind. The question: *what do they build, and is it a program or a pile?* It appears third because once you believe the person and see how they think, you want proof across domains. Reading these four in order should feel like the same question asked of language, of critique, of lived experience, and of systems under constraint.

### Current questions (third scroll)
Three sentences, each ending in a question. The emotion is **invitation and honesty** — the work is unfinished and the person knows it. The question answered: *is there a throughline, a research program?* It appears fourth because a program is best shown by what someone is still chasing, not by what they've filed. This is where the HCI/research reader locks in.

### Reading the work / the door (final scroll)
One line outward to the portfolio, then three plain links. The emotion is **generosity and restraint** — "the real instruments live elsewhere; go touch them." The question: *where do I go next?* It exists last and exists at all because the profile is a faceplate, not a museum. Ending here prevents the profile from becoming a thing about itself.

**Overall arc:** claim → evidence → range → open questions → exit. A reader is never asked to admire; they are walked through a small, honest argument and then shown the door to the living work.

---

## PART 2 — Reader journey (three audiences × three timescales)

### 1. Software engineer
- **10s:** "Not a template. One real generated image, no badge wall. This person builds systems."
- **30s:** Reads four works — Echo (instrument), MuseLab (multi-agent workshop), Differ (platform), a systems/RAG piece. "These are unusual, architecturally real systems, not CRUD apps."
- **60s:** The caption + questions register: grounded procedures, human-in-the-loop, no 'AI magic'. "This person cares whether the system is honest, not just whether it ships."

### 2. Computational designer
- **10s:** "This has a visual language. Silence, one figure, typographic restraint — authored."
- **30s:** Recognizes the specimen is *generative*, not decorative; the layout encodes meaning. "The image is downstream of a system. That's rare."
- **60s:** Notices the whole document obeys one grammar (captions, hairlines, field-note voice). "Same author as Echo/MuseLab, without copying them."

### 3. HCI / AI researcher
- **10s:** "A principle sentence, not a job title. Promising."
- **30s:** Work selection spans language, interpretation, and contextual fairness (Differ/Airbnb lineage). "There's a program here."
- **60s:** The three questions name the actual research stance — meaning under representation, metric breakdown across context, residue of language. "Coherent research identity."

**Failure check:** If the engineer saw only art, we'd lose them → mitigated by concrete work lines + caption. If the researcher saw only Echo/MuseLab, they'd read 'creative coder' → mitigated by mandatory inclusion of Differ and a systems piece + the questions. If the designer saw a stats template, we'd lose authorship → mitigated by zero widgets. Structure holds for all three; no redesign required.

---

## PART 3 — Information architecture

Challenged against the example order (which put Current Questions before the Specimen). **Rejected that order**: showing questions before any evidence makes the profile read as manifesto — exactly the recursion failure. Evidence must precede introspection. Final structure:

```
I. Identity
      ↓
II. Specimen (one plate)
      ↓
III. Selected work
      ↓
IV. Current questions
      ↓
V. Reading the work (door)
```

| Section | Purpose | Approx height (900px col) | Text/Image | Six-month residue |
| --- | --- | --- | --- | --- |
| I. Identity | State stance in native type | ~120–160px | Text | The sentence's *shape* (short, precise) |
| II. Specimen | The memorable artifact; evidence | ~460–560px incl. caption | Image + 1 caption line | **The gravity-field image** |
| III. Selected work | Program across domains | ~180–220px | Text | "language + critique + fairness + systems" |
| IV. Current questions | Research throughline | ~120–150px | Text | One of the three questions, paraphrased |
| V. Door | Exit to living work | ~60–80px | Text | "the real work is elsewhere" |

Total: a **single, calm scroll** (~1000–1150px), no horizontal regions, no sidebars. Mobile: everything is single-column already; the specimen scales; captions wrap; nothing depends on width beyond the image.

**Why this height budget:** the specimen is deliberately the tallest element so memory attaches to it; every text block is short enough to scan in one fixation.

---

## PART 4 — Visual language

Extracted grammar from Echo + MuseLab, translated to GitHub's legal surface. Every rule justified.

### Typography
- **Native GitHub type only** for all copy. Reason: GitHub renders its own type with dignity; baking type into images produces the "screenshots pasted in Markdown" failure the owner already rejected.
- **One display moment:** the name (GitHub `#` H1). Everything else is body or small. Reason: MuseLab's DNA is one extreme jump between a tiny label and a large title — replicated here as name vs. everything.
- **Micro-labels in monospace** (backtick/inline code) for plate labels and domain line. Reason: Echo/MuseLab use mono for indices, gutters, captions; it reads as instrument annotation, not prose.
- No font embedding, no custom faces in copy. The only "designed" typography lives *inside the specimen image*, where it is data.

### Spacing & silence
- **Whitespace is active.** One blank line between thought units; hairline between chapters. Reason: taste profile — negative space is composition, "breathable and slow."
- **No dense blocks.** Max ~2 lines per idea. Reason: the profile must be scannable in 10s per audience.
- Silence *before* the specimen (a hairline + label) so the image arrives with room. Reason: image rhythm needs a rest beat.

### Margins & alignment
- **Left-aligned everything.** Reason: document, not poster; centered text signals landing page. MuseLab folios read top-left like manuscripts.
- Specimen **full column width** (`width="100%"` intent, ≤900 display). Reason: one figure owns its band; no floats, no text wrap around it.

### Captions
- Every image gets **one caption line** in field-note voice: procedure · what edges/positions mean · pause state. Reason: contested fidelity — the caption is where the work admits what the image is and isn't. No image ships uncaptioned.

### Image rhythm & figure numbering
- **Exactly one figure.** Numbered `PLATE 01`. Reason: numbering asserts a real sequence (MuseLab index doctrine) and reserves room for at most a future `PLATE 02` — but the profile ships with one. More than one image fractures memory (research finding).
- No inline icons, no per-project images. Reason: negative space; thumbnails become a dashboard.

### Section hierarchy
- H1 name → `---` → mono plate label → figure → caption → `---` → H2 "Selected work" → list → `---` → H2 "Current questions" → list → `---` → outward line.
- Only two heading levels total. Reason: a document with four heading tiers reads as documentation; this is a notebook.

### How Echo appears
- As the **dark theme** temperament of the specimen (flat black, neutral, parametric) and as the first work line. Echo is *felt* in the image's generative honesty, not described.

### How MuseLab appears
- As the **light theme** temperament (warm paper, graphite, ferric restraint) and as the caption/field-note *voice* of the whole document. MuseLab is the interpretive tone; Echo is the procedure.

### Intentionally omitted (and why)
- Stats cards (template gravity), streaks/snake (vanity motion), shields/badges (badge wall), typing SVG (novelty decay), banners/hero art (poster failure), grain/stamps/paper stacks (archival cosplay named in Negative Space), emoji section rules (breaks calm), visitor counters, "connect with me" social grid. Each omission protects authorship over spectacle.

---

## PART 5 — The specimen

Question posed honestly: **if Echo had never existed, what single computational artifact best represents this body of work?**

### Candidates evaluated

| Candidate | Authenticity to whole body | Memorability | GitHub readability @900/mobile | Tie to anthropology | Survives card scale | Long-term growth | Procedure honesty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **A. Force-settlement graph (Echo Network)** | High but reads as *Echo-specific* | High | Good | "generated, residual" | Good | Re-runnable | Genuine (d3-force) |
| **B. Manuscript plate (MuseLab draft + underlines)** | Medium (MuseLab-specific) | Medium | Underlines vanish when scaled → mush | "controlled chaos" | **Poor** | Low (fixed text) | Genuine but fragile |
| **C. Interpretation stack (Evidence→Pattern→Interpretation→Claim)** | **Highest conceptually** (appears in every project) | Medium | Good | The stable principle | Good | Static structure | **Risk: diagram, not procedure** |
| **D. Lexical field / vortex (polar importance)** | High | High | Good | Mathematical DNA (radius ∝ 1/importance) | Good | Re-runnable on any text | Genuine (polar math) |
| **E. New procedural artifact** | Unknown | Risky | Unknown | Might drift from identity | Unknown | Unknown | Must invent — violates "synthesize not invent" |

### The tension
- **C** is the most *honest to the whole body of work* — the evidence→claim chain is the one structure shared by MuseLab, Differ, Airbnb, and the anthropology's stable principles. But rendered directly it becomes a **diagram**, and Negative Space forbids "visualizations without a claim" and "diagram cosplay." A stack of four labeled boxes is not a computational procedure.
- **A** and **D** are genuine procedures but risk reading as "the Echo graph," which the brief explicitly warns against assuming.

### The synthesis (chosen)
**Specimen = a Semantic Gravity Field: one settlement where the layout itself performs the interpretation chain.**

- **Procedure (genuine):** Take a real corpus, extract weighted terms and real co-occurrence, then settle them with the practice's actual **Mathematical DNA** — *radius is an inverse function of importance* (the rule shared by Echo's vortex/orbit and MuseLab's Pulse gravity), stabilized by force. Distance from center is not decoration: **center = the claim, periphery = the evidence.** The image is the interpretation stack (C) rendered *as a real settled field* (A/D) rather than as boxes.
- **Why this and not plain force graph:** in a plain force graph, position is arbitrary/aesthetic. Here position **encodes meaning** (importance → gravity), so the caption can tell the truth and the image satisfies "every diagram encodes a real relationship." It is Echo-*grammar* without being Echo-*the-orbit*.
- **Corpus decision (authenticity):** run it on the **union of the four work descriptions + the practice sentence** — i.e., the body of work *as language*. The specimen is therefore literally a computed reading of this profile's own contents. Caption can state this plainly. This also gives **long-term growth**: when the work changes, re-running the same procedure yields a new honest freeze — the profile ages truthfully.
- **Dual theme:** same graph, two material temperaments — Echo night (dark) / MuseLab paper (light) — proving one procedure, two studios.
- **Label:** words are the nodes (label *is* the node — Diagram DNA); no icons, no legend translating shapes back to English.

### Defense
It is authentic (own math, own corpus), memorable (a field with a gravitational center is one image, not ten widgets), readable (large central terms survive scaling; periphery can blur without losing the point), tied to the anthropology (importance-gravity + evidence→claim in one object), card-scale safe (center-weighted crop), and growth-friendly (re-runnable). The procedure — importance-weighted settlement of real co-occurrence — matters more than the final look, exactly as required.

**Non-negotiables:** no hand-placed nodes; positions come from the settle; caption must survive a peer audit of the generator; no added grain or fake depth.

---

## PART 6 — Project curation

Goal: four works that *collectively explain the body of work*, not four favorites. Each must carry a distinct facet; overlaps get cut.

### Selected

1. **Echo** — *text becomes living visual fields.*  
   - Belongs: it is the origin of the visual grammar and the purest "beauty through structure."  
   - Demonstrates: computation as an expressive, generative instrument; language as material.  
   - Facet: **making language visible.**

2. **MuseLab** — *a workshop that interprets writing instead of rewriting it.*  
   - Belongs: the fullest expression of interpretation-over-automation and human-in-the-loop.  
   - Demonstrates: multi-agent systems, hybrid grounding, the evidence→claim chain, taste-as-infrastructure.  
   - Facet: **judgment kept with the human.**

3. **Differ** — *where a designed experience breaks down across who and where.*  
   - Belongs: proves the fidelity/measurement twin the anthropology says the public identity under-credits; CHI-level research.  
   - Demonstrates: contextual fairness, accountable perspectives, research rigor.  
   - Facet: **meaning breaks across context.**

4. **One systems/AI piece** — *retrieval and agents under real constraints.*  
   - Candidate: `rag_project` (public) with a one-line nod to professional agentic-contracting work at the portfolio level.  
   - Belongs: gives the software engineer a load-bearing "real systems under constraint" signal that isn't creative-coding.  
   - Demonstrates: production judgment, evaluation, "what makes AI reliable has little to do with the model."  
   - Facet: **systems that must be trustworthy.**

### Deliberately excluded (with reasons)
- **Nommi / food-recommender:** strong, but its lesson (community before features) overlaps social-platform territory that doesn't advance the throughline; and it risks reading as consumer-app. Cut to protect coherence.  
- **Poem-to-song, POMDP aid, Airbnb calibration:** excellent, but each duplicates a facet already carried (cross-modal meaning ≈ Echo/MuseLab affect; calibration ≈ Differ's context-breakage). Keep one representative (Differ) to avoid a coverage pile.  
- **Tesla / NU Solar / scrapers:** real engineering, but telemetry/infra doesn't communicate the meaning-fidelity thesis at a glance; belongs on the résumé/portfolio, not the compressed face.  
- **Portfolio site itself:** it's the door (Part V), not a work line.

### Ordering logic
Echo → MuseLab → Differ → systems piece = *make language visible → interpret it with judgment → show meaning breaking across people → build systems that must be trusted.* Reading top to bottom is the argument.

---

## PART 7 — Public copy (draft, final-intent)

All copy below is the actual proposed text. Calm, interpretive, no clichés.

### Identity
```
# Xinyue Zhang
`also Shirley`

I design systems that preserve meaning as it moves
between people, language, and computation.

`language · agents · human-computer interaction · computational design`
```

### Specimen label + caption
```
`PLATE 01 · semantic gravity field`

[ image ]

A settled field of this profile's own words. Distance from the
center follows importance, not layout; the lines are real
co-occurrence. Paused after settling — an instrument, not an animation.
```

### Selected work
```
## Selected work

Echo — text becomes living visual fields.
MuseLab — a workshop that reads a draft instead of rewriting it.
Differ — where a designed experience breaks down across who and where.
rag_project — retrieval and agents held to real constraints.
```
(Each name links to its repo; the phrase stays unlinked.)

### Current questions
```
## Current questions

How does meaning survive when a model has to speak for someone?
Where do universal measures quietly stop meaning the same thing?
What is left of language after the sentence ends?
```

### Door
```
## Reading the work

Live instruments and notes → [portfolio]
Echo · MuseLab · writing
```

**Copy rules applied:** no "passionate," no "AI engineer," no "I love building," no inspirational tail. Every line either states a stance, names a facet, or opens a question.

---

## PART 8 — Memory test (30 seconds → six months)

- **Remembered image:** a cluster of words with a heavy, certain center dissolving toward the edges — "the thing where the important words fall to the middle." (One image, not "a cool graph," because the *gravity* is the idea.)
- **Remembered idea:** "she builds systems that keep meaning honest between people and machines — interprets instead of automating." Possibly one question survives verbatim: *what's left of language after the sentence ends?*
- **Remembered feeling:** calm, serious, a little melancholic; "an unusually thoughtful person; the work is elsewhere and I want to see it."

**Failure guard:** if the residue were "cool graph," we failed. The gravity semantics + the caption ("importance, not layout") convert the graph from spectacle into an idea. That is the deliberate difference.

---

## PART 9 — Critique & convergence

### Round 1

**Reviewer A — Senior interaction designer**
- Praise: strong restraint; one figure; clear arc.  
- Concern: caption risks being too technical; "co-occurrence" may alienate non-technical viewers.  
- Concern: three questions could feel precious if phrased too poetically.

**Reviewer B — GitHub engineer**
- Concern: dual-theme must use `<picture>` with `prefers-color-scheme`; ensure alt text and that the image link works when clicked; PNG fallback since fine SVG type mush at scale.  
- Concern: links must be absolute (raw asset URLs) or they break on the profile; four repo links must be public or clearly external.  
- Praise: no external services = nothing to rot (unlike stats/spotify cards).

**Reviewer C — Design professor**
- Praise: the specimen's "position encodes importance" is a defensible thesis; avoids diagram cosplay.  
- Concern: is the self-referential corpus (profile's own words) too clever/circular? Could read as gimmick.  
- Concern: "also Shirley" needs a reason to exist or cut it.

### Revision 1
- Caption reworded to lead with meaning, not jargon: "Distance from the center follows importance, not layout" (kept), and "co-occurrence" softened to "the lines are real connections between words." Keep one honest technical noun, not a lecture.
- Questions kept to plain declaratives ending in "?"; removed any ornate phrasing. "What is left of language after the sentence ends?" retained as the one lyrical allowance (it's the Echo thesis).
- `<picture>` + PNG fallback + descriptive alt + absolute URLs written into the implementation plan as hard requirements.
- Corpus: **keep self-referential but make it honest, not circular** — the field is built from the four work descriptions + practice sentence (the body of work as language), and the caption says "this profile's own words." Professor's gimmick risk is mitigated because the caption is transparent about it; transparency converts cleverness into method.
- "also Shirley": justified — it's the real preferred name and signals the human behind the system (emotional resonance). Kept, once, small.

### Round 2

**A:** "Caption now humane. Convergent."  
**B:** "With `<picture>`, alt, absolute URLs, public repos — technically sound. Convergent."  
**C:** "Transparent self-reference is a legitimate method, not a gimmick. Convergent."

**Converged.** No structural changes remain; open items are implementation requirements, not design decisions.

---

## PART 10 — Implementation plan

Only mechanics remain. Each phase has deliverables, dependencies, and a checkpoint.

### Phase 1 — Wireframe lock
- **Deliverables:** static text mock of the README (copy from Part 7) in a scratch file; confirm chapter order, headings, hairlines, link targets.
- **Dependencies:** approved principle sentence, work list, questions.
- **Checkpoint:** owner reads the text-only version and confirms voice/order before any pixels.

### Phase 2 — Specimen generator (procedure first)
- **Deliverables:** a real generator that (1) loads the corpus (four work lines + practice sentence), (2) extracts weighted terms + real connections, (3) settles with radius-∝-inverse-importance + force, (4) exports positions. Reuse existing `profile-art/` settle/graph modules where honest; no hand-placement.
- **Dependencies:** Phase 1 copy (corpus text is finalized copy).
- **Checkpoint:** audit — do node positions come only from the procedure? Does the center hold the most important term? Caption must be true.

### Phase 3 — Visual assets (render + theme)
- **Deliverables:** two exports (Echo-night dark, MuseLab-paper light), card-scale (~900×460–520), center-weighted crop, label-as-node, no grain. PNG (fidelity) with the exact same graph in both themes.
- **Dependencies:** Phase 2 positions.
- **Checkpoint:** scale test at 900px and on a phone; does the center survive; does periphery blur gracefully; does it look authored, not templated.

### Phase 4 — README construction
- **Deliverables:** final `README.md` in `xinyuezhang-shirley/xinyuezhang-shirley` with native copy, `<picture>` dual-theme specimen (absolute raw URLs), descriptive alt text, four repo links, three questions, door link.
- **Dependencies:** Phases 1–3; assets committed and served.
- **Checkpoint:** render on the live profile overview (confirm Share-to-Profile if needed); verify light/dark swap; verify mobile; verify no broken links.

### Phase 5 — Polish & verification
- **Deliverables:** three-audience 10/30/60s read-through; memory test with a fresh viewer; Negative-Space pass (no forbidden element crept in); archive the old tall poster off the profile surface.
- **Dependencies:** Phase 4 live.
- **Checkpoint:** all Success Criteria satisfied; owner sign-off.

---

## Success criteria (restated as acceptance tests)

- [ ] Feels unmistakably authored (no template artifact anywhere)
- [ ] Could only belong to Xinyue Zhang (specimen procedure = her math; voice = her doctrine)
- [ ] Immediately readable on GitHub (calm scroll, native type)
- [ ] Survives mobile (single column, scalable specimen)
- [ ] Every visual comes from a real procedure (audited generator)
- [ ] Every project reinforces one body of work (four facets, no overlap)
- [ ] Invites people into Echo and MuseLab without replacing them (door, not museum)

---

## Approval gate

Confirm or amend:
1. Specimen = **semantic gravity field on the profile's own words** (Part 5) — approve / choose another candidate.
2. Four works incl. **Differ** + **rag_project** — approve / swap.
3. Copy in **Part 7** — approve / edit lines.
4. Chapter order (Identity → Specimen → Work → Questions → Door) — approve / change.

On approval, implementation proceeds through Phases 1–5 with no further design decisions.

*End of creative direction.*
