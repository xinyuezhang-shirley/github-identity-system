# GitHub Profile Concept — Approval Brief

**Status:** Concept only. No implementation until approved.  
**Synthesizes:** Design Anthropology · Negative Space · Computational Identity Research · Profile README Strategy  
**Subject:** `xinyuezhang-shirley` profile README as compressed public face of the body of work  

---

## 1. Concept (the entire README in one idea)

### Title

**Field notes from an instrument lab**

### Thesis

The profile is not a landing page, not a poster, and not a résumé skin.  
It is a **short research document** someone opens the way they open a notebook left on a bench: identity at the top, one frozen run of a real procedure in the middle, a small shelf of instruments below, the questions still open, then a door out.

Someone should leave knowing — without a manifesto — that you build **systems that preserve meaning as it moves between people, language, and computation**, and that those systems are **beautiful because their structure is honest**, not because they are decorated.

### Metaphor (held lightly, never cosplayed)

**Specimen plate + lab index.**  
One computational freeze is the specimen. Everything else is native Markdown — captions, inventory, questions — the way a lab labels a slide and then lists the shelves.

Not: museum wallpaper, SaaS dashboard, creative-coding carnival, AI-engineer badge wall.

### What “Echo and MuseLab compressed” means here

| Inherited grammar | How it appears on GitHub |
| --- | --- |
| Echo’s *frozen process* | One card-scale field image from a real settle / force / imprint run — not a composed collage |
| Echo’s night / paper dual | `<picture>` light + dark specimens from the same procedure |
| MuseLab’s *dossier voice* | Chapter headings, micro-labels, short interpretive lines — native type |
| MuseLab’s *interpretation over automation* | Work described as instruments and questions, never as “powered by AI” |
| Contested fidelity | Captions that name the model and the freeze; no fake live UI |
| Beauty through structure | The specimen’s beauty is the geometry of real relations |
| Emotional resonance | Restraint, silence, one memorable image — not cold benchmark chrome |
| Negative space | Explicitly absent: stats cards, streak widgets, shader toys, archival scrapbook |

### Principle sentence (native Markdown — the stance)

Draft for approval (one of these, or a merge):

**A (preferred):**  
> I design systems that preserve meaning as it moves between people, language, and computation.

**B (companion compression):**  
> Systems of contested fidelity — computation that shows its work.

Recommend **A** as the only sentence under the name. B is too manifesto-like for the profile surface; it can stay in anthropology.

### Success impressions (the three visitors)

| Visitor | Intended aftertaste | How the profile causes it |
| --- | --- | --- |
| Software engineer | “This person builds unusual systems.” | Specimen from a real procedure + inventory of instruments (not CRUD apps) |
| Computational designer | “This visual language has authorship.” | One authored field image + typographic silence; no template widgets |
| HCI / research | “This person has a coherent research program.” | Current questions + work that spans language instruments, workshops, calibration/context |

---

## 2. Wireframe

Designed for GitHub’s **~900px reading column**, phone-narrowing, and document scroll.  
Widths are conceptual; heights are proportions, not pixels.

```
┌─────────────────────────────────────────────────────────────┐
│  PROFILE README  ·  document scroll  ·  ~900px column       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Xinyue Zhang                                               │
│  also Shirley                                               │
│                                                             │
│  I design systems that preserve meaning as it moves         │
│  between people, language, and computation.                 │
│                                                             │
│  language · agents · HCI · computational design             │
│                                                             │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│                                                             │
│  PLATE 01 · force settlement · lexical field                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │         [ ONE COMPUTATIONAL SPECIMEN ]              │   │
│  │         card-scale · ~900 × 420–520                 │   │
│  │         dual theme via <picture>                    │   │
│  │         real Echo/MuseLab procedure freeze          │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│  Settled from manuscript graph · N nodes · M edges ·       │
│  paused after T ticks · not a live instrument              │
│                                                             │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│                                                             │
│  Selected work                                              │
│                                                             │
│  Echo          text → living fields · instrument           │
│  MuseLab       manuscript → workshop dossier               │
│  Differ        experience → accountable perspectives       │
│  [systems]     retrieval / agents under real constraints   │
│                                                             │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│                                                             │
│  Current questions                                          │
│                                                             │
│  · How does meaning survive when a model must speak?        │
│  · Where do universal metrics break across contexts?        │
│  · What remains of language after the sentence ends?        │
│                                                             │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│                                                             │
│  Reading the work                                           │
│  Live instruments and notes → portfolio                     │
│  Echo · MuseLab · writing                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Chapter map (scroll order)

```
I. Identity
      ↓
II. Specimen (one plate)
      ↓
III. Selected work (≤4)
      ↓
IV. Current questions (≤3)
      ↓
V. Reading the work / door
```

No hero banner. No sidebar. No floating badges. No second decorative image.

---

## 3. Reasoning behind every section

### I — Identity

**Job:** State who you are in native GitHub type — the one surface GitHub renders with dignity.

**Contains:**
- Name: Xinyue Zhang  
- Quiet alias: also Shirley  
- One principle sentence (A above)  
- One mono-style domain line (plain text, not shields): `language · agents · HCI · computational design`

**Why this section exists:**  
Engineer + researcher both need a sentence before an image. Designers need to see authorship starts in prose, not only in pixels. This is contested fidelity in language form — a claim you stand behind without a diagram.

**What it must not do:**  
Bio buzzwords (“Full-stack AI enthusiast”), emoji skill rows, typing SVGs, location flair.

---

### II — One computational specimen

**Job:** The six-month memory. The only visual. Echo/MuseLab compressed into a freeze.

**Contains:**
- Micro-label above the image (field-note voice): e.g. `PLATE 01 · force settlement · lexical field`  
- One `<picture>` (light = MuseLab paper temperament / dark = Echo night temperament — **same underlying graph and settle**, different material tokens)  
- One caption under the image naming: procedure, what the edges mean, that it is paused — not live

**Why this section exists:**  
Without it, the profile is a clever essay and fails the computational designer. With more than one image, memorability fractures and we re-enter poster/dashboard failure modes.

**Procedure constraint (non-negotiable):**  
Export must come from a **genuine** run (Echo Network settle or MuseLab Pulse-class graph with real co-presence / lexical edges). No hand-placed “aesthetic” nodes. No scrapbook grain layers. Caption must be able to tell the truth.

**Scale:** ~900×420–520 display intent (card figure, Distill-scale — not 1700px tall poster).

**Why beauty still happens:**  
Beauty through structure — if the settle is honest, the freeze is already authored. We do not add atmosphere to compensate.

---

### III — Selected work

**Job:** Prove the research program and the “unusual systems” claim with four doors, not a repo dump.

**Contains (proposed set — adjustable):**

| Work | Seven-word-ish phrase | Visitor it serves |
| --- | --- | --- |
| **Echo** | Language continues as living fields | Engineer + designer |
| **MuseLab** | Workshop dossier; interpretation over rewrite | All three |
| **Differ** | Where designed experience breaks by context | HCI / research |
| **One systems piece** | RAG / agents under real constraints (rag_project or high-level contracting note) | Engineer |

Each line: **title** · short phrase · link.  
Optional one-word role tag in mono (`instrument` / `dossier` / `research` / `systems`) — only if it stays quiet.

**Why this section exists:**  
Anthropology warned that public identity overweighting Echo/MuseLab alone misreads the fidelity/measurement twin. Differ (or equivalent) must appear so the HCI visitor sees a program, not a hobbyist creative-coder. Four is the ceiling (negative space: no inventory bloat).

**What it must not do:**  
Tech stacks, star counts, “Built with React/PyTorch,” GIF previews per project.

---

### IV — Current questions

**Job:** Show how you think without a manifesto. Research-program signal.

**Contains:** Exactly three questions, present tense, unfinished:

1. How does meaning survive when a model must speak for someone?  
2. Where do universal metrics break across contexts?  
3. What remains of language after the sentence ends?

**Why this section exists:**  
Questions are the anthropology’s obsessive core, compressed. They unify MuseLab, Differ/Airbnb, and Echo without naming the papers. They also enact “refuse to decide” — the profile does not pretend the work is finished.

**What it must not do:**  
Paragraph answers, buzzword research agendas, citation dumps.

---

### V — Reading the work (door)

**Job:** Honesty that GitHub is a faceplate. The living instruments are elsewhere.

**Contains:**
- One line: `Live instruments and notes →` + portfolio URL  
- Optional second line of three plain links: Echo · MuseLab · writing (or site sections)

**Why this section exists:**  
Computational-identity research: Victor/Dynamicland honesty — the real medium is offsite. Prevents the README from becoming recursion (another identity about identity).

---

## 4. Why every visual element exists

| Element | Exists because | Forbidden substitute |
| --- | --- | --- |
| **Principle sentence (native text)** | Stance must be selectable, accessible, readable at any theme | Sentence baked into the PNG |
| **Domain mono line** | Quiet classification without badge walls | Shields.io skill row |
| **Hairline / `---` chapter breaks** | Document chapters; MuseLab hairline grammar in GitHub’s only legal divider | Card sections, emoji rules |
| **PLATE micro-label** | Field-note / dossier caption voice; tells the specimen what it is | Decorative eyebrow with no content |
| **One specimen image** | Six-month memory; beauty through structure; Echo freeze | Multiple images, banner, orbit logo sticker |
| **Dual theme `<picture>`** | Echo night + MuseLab paper as sibling temperaments of one procedure | Two unrelated artworks |
| **Plate caption** | Contested fidelity — names model, edges, pause | “My generative art ✨” |
| **Four work links** | Program breadth without dashboard | Stats, snakes, trophy GIFs |
| **Three questions** | Thought pattern made public | Long About Me essay |
| **Outbound door** | Profile is faceplate, not museum | Recreating the portfolio inside README |

**Visual elements that do not exist (on purpose):**  
Grain overlays, stamps, faux paper stacks, word clouds, contribution snakes, visitor counters, typing animations, logo walls, second “accent” diagram, project thumbnail grid.

---

## 5. Specimen specification (for later build — not building now)

**Model:** One dominant procedure — **force settlement on a semantic identity / manuscript graph** (Echo Network DNA), with nodes = real lexical or practice entities and edges = real relations (co-presence, typed links from content — not decorative spaghetti).

**Composition:** Identity-centered crop at **card scale**; sparse essential edges; typography inside the image limited to **optional micro coordinates / node words that are the data** — not a second headline competing with the Markdown name.

**Themes:**  
- Dark = Echo neutrals (flat black field)  
- Light = MuseLab warm paper + graphite (no purple SaaS, no cream-template pastiche)

**Caption contract:** Must remain true if a peer audits the generator.

**Archive:** Tall poster attempts stay off the profile surface.

---

## 6. Tone and copy rules

- Interpretive, calm, short.  
- No “I love building with AI.”  
- No “passionate about.”  
- Prefer instruments, dossiers, questions, plates.  
- Prefer showing over naming “contested fidelity” on the public surface.  
- Shirley appears once, quietly — not as a brand flourish.

---

## 7. Explicit non-goals (from Negative Space)

Will not ship:

- Generic AI wrapper positioning  
- Decorative generative art  
- Productivity / dashboard aesthetics  
- Growth-SaaS energy  
- Visualizations without a claim  
- Archive cosplay  
- Identity recursion (profile about the profile system)

---

## 8. Approval checklist

Please approve or revise:

1. **Metaphor:** Field notes + one specimen plate — yes / change  
2. **Principle sentence:** A / B / your rewrite  
3. **Chapter order:** Identity → Specimen → Work → Questions → Door — yes / change  
4. **Work four:** Echo, MuseLab, Differ, systems piece — swap any?  
5. **Questions:** the three drafts — edit freely  
6. **Specimen:** force-settlement lexical/identity field at card scale, dual theme — yes / different single procedure  

**No code, assets, or README writes until you say proceed.**

---

*End of concept brief.*
