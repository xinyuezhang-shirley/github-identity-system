# Ten computational visualization ideas

What the primitives in [design-dna.md](design-dna.md) do to real GitHub
data. The brief was: repositories treated as observations inside a field,
not cards. These are ten ways to run actual metadata (see
`assets/generated/`) through Strand 04 (Mathematical DNA) and Strand 03
(Diagram DNA). Two are flagged as needing human judgment, not just data —
a field is only honest if the axes mean something worth signing your name
to.

| # | Idea | Data source | Status |
|---|------|-------------|--------|
| 01 | **Language Topology** — aggregate byte-weighted language totals on the Polar Importance Field, dominant language nearest center. | live · `assets/generated/languages.json` | built · `prototypes/topology/` |
| 02 | **Commit Signal Trace** — the real weekly contribution calendar as a single ink line; the honest sparse-then-burst rhythm, not a manufactured streak. | live · `assets/generated/contribution-calendar.json` | built · `prototypes/instrument/` |
| 03 | **Repository Constraint Field** — repos as points in a force/Voronoi field; cell area ∝ repo size, position ∝ recency × language cluster. | live · `assets/generated/repos.json` | not built — needs a real force-layout pass, not hand-placed points |
| 04 | **Manuscript Gutter Timeline** — commits as numbered manuscript lines; silent weeks render as the same `•` used for blank verse lines in `PoemManuscript.tsx`. | live · contribution calendar | built · `prototypes/folio/` (index numbering only, not yet the full timeline) |
| 05 | **Two-Agent System Diagram** — MuseLab's real workshop-agents / builder-agents split as two adjacent Concentric Rings, not a boxes-and-arrows architecture chart. | static · MuseLab README | not built |
| 06 | **Semantic Underline Bio** — the manuscript-ink underline vocabulary (wavy/dotted/italic) applied to a real first-person paragraph, keyed to actual recurring themes/tools/domains, with a legend. | authored · needs real categories, not invented ones | not built |
| 07 | **Growth-Ring Repo Tree** — repos grouped by year, rendered as recursive branch subdivision; branch thickness ∝ LOC. | live · `pushedAt` year, repo size | not built |
| 08 | **Phase Diagram: coursework vs. self-directed** — 2D scatter, axis 1 course-work↔self-directed, axis 2 language family. | **flagged** — needs the repo owner's own labels; metadata alone can't distinguish CS340 from MuseLab | not built |
| 09 | **Distance-Field Skill Map** — contour/distance-field rendering instead of a bar of logos; ridges are skill clusters. | live · language totals, reshaped | **flagged** — highest legibility risk on this list |
| 10 | **Reaction-Diffusion Footer Mark** — one small precomputed reaction-diffusion texture, used only as a footer signature glyph, scoped small on purpose. | generated once, static asset | not built — the one deliberate exception to "everything must encode," kept tiny so it stays an exception |

Four of the five identity directions in
[identity-directions.md](identity-directions.md) have a working prototype
under `prototypes/`; ideas 03, 05, 06, 07, and 10 are documented here as
backlog, not built yet.
