"""Compact, transparent signature visuals for the GitHub profile README.

Architecture rule: Markdown carries content. SVG carries only geometry
Markdown cannot express. No opaque canvases, no embedded name/headings.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from src.primitives.themes import DARK, LIGHT, Theme, with_alpha
from src.generators import svg_utils as U

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "src" / "data" / "content.json"
GEN = ROOT / "assets" / "generated"


def _load() -> dict:
    return json.loads(DATA.read_text())


def _langs() -> dict:
    return json.loads((GEN / "languages.json").read_text())


def signature_orbit(theme: Theme) -> str:
    """Echo gravity rings — transparent, tight crop, no identity text.

    Domains as short labels on rings; selected projects as numbered marks.
    Project names live in Markdown, not here.
    """
    # Tight crop around geometry — no poster padding
    w, h = 520, 268
    cx, cy = 260, 128
    min_r, max_r = 34, 108
    core_r = min_r + (max_r - min_r) * 0.22
    mid_r = min_r + (max_r - min_r) * 0.50
    out_r = min_r + (max_r - min_r) * 0.82

    # Theme-aware strokes that sit on GitHub page chrome, not a poster
    if theme.name == "dark":
        ink = "#e6edf3"
        muted = "#8b949e"
        line = "rgba(255,255,255,0.22)"
        accent = "#c9b896"
        mark_fill = "none"
    else:
        ink = "#1f2328"
        muted = "#656d76"
        line = "rgba(27,31,36,0.18)"
        accent = "#8b6914"
        mark_fill = "none"

    core_domains = [
        ("AI", -0.7),
        ("agents", 0.5),
        ("HCI", 1.6),
        ("design", 2.6),
    ]
    related_domains = [
        ("infra", 0.15),
        ("research", 2.1),
        ("writing", 3.7),
    ]
    # Four selected observations — indices match Markdown list
    marks = [
        ("01", mid_r, -2.3, True),
        ("02", mid_r, -0.4, True),
        ("03", mid_r, 1.2, True),
        ("04", (mid_r + out_r) * 0.55, 2.5, False),
    ]

    parts: list[str] = []
    # NO background rect — GitHub page shows through

    for r, op, dash in (
        (core_r, 0.7, None),
        (mid_r, 0.55, None),
        (out_r, 0.4, "2 5"),
    ):
        parts.append(U.circle(cx, cy, r, stroke=line, sw=1, opacity=op, dash=dash))

    parts.append(U.circle(cx, cy, 2.0, fill=accent, opacity=0.9))

    for label, ang in core_domains:
        x = cx + math.cos(ang) * core_r
        y = cy + math.sin(ang) * core_r * 0.92
        parts.append(
            U.text(
                x, y, label, fill=ink, size=13, family=U.SERIF, weight="500",
                anchor="middle", dominant_baseline="middle",
            )
        )
    for label, ang in related_domains:
        x = cx + math.cos(ang) * out_r
        y = cy + math.sin(ang) * out_r * 0.92
        parts.append(
            U.text(
                x, y, label, fill=muted, size=11, family=U.SERIF,
                anchor="middle", dominant_baseline="middle", opacity=0.9,
            )
        )

    for idx, r, ang, is_core in marks:
        r2 = r + math.sin(ang * 2) * 3
        x = cx + math.cos(ang) * r2
        y = cy + math.sin(ang) * r2 * 0.92
        stroke = ink if is_core else muted
        parts.append(U.circle(x, y, 8 if is_core else 7, fill=mark_fill, stroke=stroke, sw=1.2))
        parts.append(
            U.text(x, y + 3.2, idx, fill=ink if is_core else muted, size=9, family=U.MONO, weight="500", anchor="middle")
        )

    # Minimal caption — mono, quiet; not a section heading
    parts.append(
        U.text(cx, h - 10, "practice gravity  ·  echo orbit", fill=muted, size=9, family=U.MONO, tracking=0.14, anchor="middle")
    )

    body = U.join(parts)
    return U.wrap_svg(
        body,
        width=w,
        height=h,
        aria="Echo orbit of practice domains with numbered project observations",
        bg=None,
    )


def language_topology_compact(theme: Theme) -> str:
    """One quiet data artifact — polar language share, transparent, compact."""
    langs = _langs()
    items = langs["languages"][:7]
    w, h = 560, 200
    cx, cy = 140, 100
    rings = [26, 54, 82]

    if theme.name == "dark":
        ink = "#e6edf3"
        muted = "#8b949e"
        line = "rgba(255,255,255,0.20)"
        accent = "#c9b896"
    else:
        ink = "#1f2328"
        muted = "#656d76"
        line = "rgba(27,31,36,0.16)"
        accent = "#8b6914"

    bands: list[list] = [[], [], []]
    for lang in items:
        pct = lang["share_pct"]
        if pct >= 20:
            bands[0].append(lang)
        elif pct >= 4:
            bands[1].append(lang)
        else:
            bands[2].append(lang)

    parts: list[str] = []
    for bi, r in enumerate(rings):
        parts.append(
            U.circle(cx, cy, r, stroke=line, sw=1, opacity=0.55, dash="2 4" if bi == 2 else None)
        )
    parts.append(U.circle(cx, cy, 1.8, fill=accent, opacity=0.85))

    for bi, band in enumerate(bands):
        r = rings[bi]
        n = max(len(band), 1)
        for i, lang in enumerate(band):
            ang = (i / n) * 2 * math.pi + bi * 0.45
            x = cx + r * math.cos(ang)
            y = cy + r * math.sin(ang) * 0.85
            label = lang["language"].replace("Jupyter Notebook", "Jupyter")
            fs = 12 if bi == 0 else (10.5 if bi == 1 else 9.5)
            parts.append(
                U.text(
                    x, y, label,
                    fill=ink if bi == 0 else muted,
                    size=fs, family=U.SERIF,
                    weight="500" if bi == 0 else "400",
                    anchor="middle", dominant_baseline="middle",
                    opacity=0.95 if bi < 2 else 0.75,
                )
            )

    # Quiet mono ledger — not a bar chart
    lx, ly = 290, 42
    parts.append(U.text(lx, ly, "authored bytes", fill=muted, size=9, family=U.MONO, tracking=0.16))
    y = ly + 22
    for lang in items[:6]:
        label = lang["language"].replace("Jupyter Notebook", "Jupyter")
        parts.append(U.text(lx, y, f"{lang['share_pct']:4.1f}%", fill=accent if lang["share_pct"] >= 20 else muted, size=11, family=U.MONO))
        parts.append(U.text(lx + 52, y, label, fill=ink, size=12, family=U.SERIF))
        y += 20

    excl = ", ".join(langs["excluded_repos"])
    parts.append(
        U.text(lx, h - 14, f"excl. {excl}  ·  vendored", fill=muted, size=9, family=U.MONO)
    )

    body = U.join(parts)
    return U.wrap_svg(
        body,
        width=w,
        height=h,
        aria="Compact language topology from public repository byte shares",
        bg=None,
    )


def project_mark(theme: Theme, index: str, *, core: bool = True) -> str:
    """Optional tiny hollow mark for inline use — 28×28, transparent."""
    ink = "#e6edf3" if theme.name == "dark" else "#1f2328"
    muted = "#8b949e" if theme.name == "dark" else "#656d76"
    stroke = ink if core else muted
    parts = [
        U.circle(14, 14, 10, fill="none", stroke=stroke, sw=1.15),
        U.text(14, 17.5, index, fill=stroke, size=9, family=U.MONO, weight="500", anchor="middle"),
    ]
    return U.wrap_svg(
        U.join(parts),
        width=28,
        height=28,
        aria=f"Observation mark {index}",
        bg=None,
    )
