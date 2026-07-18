# Five identity system directions

Each is a thesis for how the whole system — README through installation
piece — coheres, not just a skin for one artifact. Scored against
MuseLab's own `disliked_patterns.md`, not against generic taste. Four of
the five have a working prototype under `prototypes/`.

---

## A — Field Notes

The identity is a naturalist's notebook for software — every artifact
reads as an observation logged in the same notebook, dated, numbered,
unglamorous on purpose.

**Extends to:** README = notebook page · Poster = one full-spread
observation · Slides = sequential notebook pages, one claim per page.

**Against the doctrine:** closest to how MuseLab's own dossier already
talks about itself. Lowest risk of drifting into decoration — the
notebook conceit forces every element to justify itself as a recorded
fact.

**Prototype:** none yet — the closest existing structural analogue is
`prototypes/folio/`, but Field Notes wants a flatter, less numbered
register than Folio's index.

---

## B — Instrument

Every surface reads as an unfinished scientific instrument's readout —
dials, traces, calibration marks. Motion DNA's "settle" register becomes
literal: things look mid-measurement.

**Extends to:** README = instrument face · Installation = a literal
running instrument with live data · Keynote slides = calibration-panel
layout, one dial per claim.

**Against the doctrine:** best match for the brief's "motion should
communicate computation" instruction.

**Risk:** without live/near-real-time data behind it, the instrument
conceit is partly aspirational — a static README is a photo of a dial, not
a dial. `prototypes/instrument/` uses real (if not live-updating) commit
data to close some of that gap.

**Prototype:** `prototypes/instrument/`

---

## C — Folio System

The dossier/index metaphor, generalized system-wide: everything is a
numbered folio entry. Closest extension of what MuseLab already calls
itself.

**Extends to:** Portfolio = a folio catalog · Papers = literally use
folio numbering as the section system · Posters = a folio cover, one
large numeral.

**Against the doctrine:** most directly reuses existing, working
components (`DossierTabRail`, index numbering). Most buildable within a
static README's constraints — no runtime needed.

**Prototype:** `prototypes/folio/`

---

## D — Topology

The whole practice as one connected, evolving map — skills, projects, and
time as a single field. The Diagram/Mathematical DNA becomes the central
artifact; typography moves to captioning the map rather than anchoring
the page.

**Extends to:** Research papers = the topology map as a recurring figure,
re-rendered per paper · Installation = a walkable/zoomable version of the
same map · Website = the map as primary navigation, not a menu.

**Against the doctrine:** most "computational beauty," most distinct from
every other GitHub profile. **Inverts the brief's own instruction that
"typography should anchor, math should breathe"** — flagged, not
disqualifying, but worth naming every time this direction is picked up
again.

**Risk:** highest legibility cost. A map you can't read in ten seconds
fails the brief's own "curiosity in ten seconds" test.

**Prototype:** `prototypes/topology/`

---

## E — Ledger

Everything is an accounting of real work — tabular, dated, countable. The
Tabular Ledger Row primitive is the connective tissue across every
surface. Closest in spirit to Giorgia Lupi's data-humanism.

**Extends to:** Papers = a ledger appendix that's also the paper's
structure · Portfolio = itemized, dated, no hierarchy games · Posters =
one large ledger, printed at scale.

**Against the doctrine:** least "generative art," most "systems map" —
the safest, most legible of the five. Lowest ceiling for the "I want to
click every repository" reaction the original brief asked for.

**Prototype:** `prototypes/ledger/`
