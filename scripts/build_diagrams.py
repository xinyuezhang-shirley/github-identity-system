#!/usr/bin/env python3
"""Generate assets/diagrams/*.svg from assets/generated/*.json.

Every coordinate here comes from the same polar-placement and
exponential-settle formulas documented in docs/design-dna.md (Strands 04
and 05) — ported from echo/frontend/helperJS/vortex.js and the
view.scale += (target - view.scale) * k pattern used throughout both
source projects. Re-run after scripts/fetch_github_data.py to keep the
diagrams in sync with live data.

Usage:
    python3 scripts/build_diagrams.py
"""
import json
import math
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GEN_DIR = REPO_ROOT / "assets" / "generated"
OUT_DIR = REPO_ROOT / "assets" / "diagrams"


def build_language_topology():
    """Ring-based polar field (vortex.js orbit.js lineage): radius is an
    inverse function of share, binned into 3 concentric importance bands."""
    languages = json.loads((GEN_DIR / "languages.json").read_text())["languages"]
    cx, cy = 300, 260
    rings = [46, 118, 182]
    bands = [[], [], []]
    for lang in languages:
        pct = lang["share_pct"]
        if pct >= 20:
            bands[0].append(lang)
        elif pct >= 3:
            bands[1].append(lang)
        else:
            bands[2].append(lang)

    texts = []
    for bi, band in enumerate(bands):
        r = rings[bi]
        n = len(band)
        for i, lang in enumerate(band):
            angle = (i / max(n, 1)) * 2 * math.pi + bi * 0.5
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle) * 0.82
            fs = 13 + lang["share_pct"] * 0.55
            op = 0.35 + min(lang["share_pct"] / 38, 1) * 0.6
            texts.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" '
                          f'style="font-family:\'Cormorant Garamond\',serif;font-size:{fs:.1f}px" '
                          f'opacity="{op:.2f}" fill="currentColor">{lang["language"]}</text>')

    rings_svg = "\n  ".join(
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="currentColor" '
        f'stroke-opacity="0.25" stroke-width="1" stroke-dasharray="2 5"/>'
        for r in rings
    )
    svg = f'''<svg viewBox="0 0 600 460" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="Language topology: real aggregated byte share across non-fork repositories, placed on a polar field where radius is inverse to share">
  <title>Language topology</title>
  <desc>Real GitHub language byte totals from assets/generated/languages.json, placed by scripts/build_diagrams.py using the ring-placement formula in docs/design-dna.md.</desc>
  {rings_svg}
  {chr(10).join(texts)}
</svg>'''
    (OUT_DIR / "language-topology.svg").write_text(svg)
    print("wrote assets/diagrams/language-topology.svg")


def build_commit_signal_trace():
    """Straight polyline of real weekly commit totals — no smoothing, no
    fabricated streak. See docs/design-dna.md, viz idea 02."""
    cal = json.loads((GEN_DIR / "contribution-calendar.json").read_text())
    weeks = cal["week_totals"]
    n = len(weeks)
    W, H = 860, 120
    maxv = max(weeks) or 1
    pts = []
    for i, v in enumerate(weeks):
        x = round(i / (n - 1) * W, 1)
        y = round(H - (v / maxv) * H, 1)
        pts.append(f"{x},{y}")
    trace_points = " ".join(pts)
    peak_i = weeks.index(max(weeks))
    peak_x = round(peak_i / (n - 1) * W, 1)

    svg = f'''<svg viewBox="0 0 {W} {H + 20}" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="Real 53-week commit signal trace, sparse with occasional bursts, peak of {maxv} commits in one week">
  <title>Commit signal trace</title>
  <desc>Real GraphQL contributionCalendar data from assets/generated/contribution-calendar.json, {cal['active_weeks']} of {n} weeks active.</desc>
  <line x1="0" y1="{H}" x2="{W}" y2="{H}" stroke="currentColor" stroke-opacity="0.35" stroke-width="1"/>
  <polyline fill="none" stroke="currentColor" stroke-width="1.6" points="{trace_points}"/>
  <text x="{peak_x}" y="8" text-anchor="middle" style="font-family:'IBM Plex Mono',monospace;font-size:9px" fill="currentColor">{maxv}</text>
</svg>'''
    (OUT_DIR / "commit-signal-trace.svg").write_text(svg)
    print("wrote assets/diagrams/commit-signal-trace.svg")


def build_mathematical_spiral_proof():
    """26-point proof sketch of vortex.js's own placement formula:
    angle = index * 0.42, radius = 10 + index * 5.2 — not real data, a
    demonstration of the formula itself, for docs/design-dna.md."""
    cx, cy = 130, 130
    dots, guide_line_end = [], None
    for i in range(26):
        a = i * 0.42
        r = 10 + i * 5.2
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a) * 0.82
        rr = 1.4 + (i / 26) * 1.8
        op = 0.9 - (i / 26) * 0.55
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr:.2f}" opacity="{op:.2f}" fill="currentColor"/>')
        guide_line_end = (x, y)
    svg = f'''<svg viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="Proof sketch of the spiral placement formula: angle equals index times 0.42, radius grows linearly with index">
  <title>Spiral placement proof sketch</title>
  <desc>26 points from vortex.js's own formula (docs/design-dna.md, Strand 04), not sampled data.</desc>
  <circle cx="130" cy="130" r="60" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-dasharray="2 3"/>
  <circle cx="130" cy="130" r="115" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-dasharray="2 3"/>
  <line x1="130" y1="130" x2="{guide_line_end[0]:.1f}" y2="{guide_line_end[1]:.1f}" stroke="currentColor" stroke-opacity="0.25" stroke-dasharray="2 3"/>
  {chr(10).join(dots)}
</svg>'''
    (OUT_DIR / "mathematical-spiral-proof.svg").write_text(svg)
    print("wrote assets/diagrams/mathematical-spiral-proof.svg")


def build_motion_settle_curve():
    """Literal 60-frame iteration of value += (target - value) * k at
    k = 0.14 (vortex.js ZOOM_SMOOTH) — monotonic, no invented oscillation."""
    v, target, k = 1.0, 0.0, 0.14
    pts = []
    for i in range(60):
        x = round(i / 59 * 380, 1)
        y = round(13.2 + (1 - v) * 83.6, 1)
        pts.append(f"{x},{y}")
        v = v + (target - v) * k
    svg = f'''<svg viewBox="0 0 380 110" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="The literal iteration value += (target minus value) times k, plotted for 60 frames at k = 0.14: a monotonic exponential approach, never overshooting">
  <title>Motion settle curve</title>
  <desc>60 frames of the real damping formula used across vortex.js, orbit.js, and vortexCanvas.ts — not an idealized/oscillating model of it.</desc>
  <line x1="0" y1="96.8" x2="380" y2="96.8" stroke="currentColor" stroke-opacity="0.35" stroke-width="1"/>
  <polyline fill="none" stroke="currentColor" stroke-width="1.6" points="{' '.join(pts)}"/>
</svg>'''
    (OUT_DIR / "motion-settle-curve.svg").write_text(svg)
    print("wrote assets/diagrams/motion-settle-curve.svg")


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_language_topology()
    build_commit_signal_trace()
    build_mathematical_spiral_proof()
    build_motion_settle_curve()
