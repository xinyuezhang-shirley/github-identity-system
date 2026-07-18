"""Three composition studies + final profile SVG panels.

Geometry from Echo orbit/vortex. Material from MuseLab (light) / Echo (dark).
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

from src.primitives import orbit as orbit_mod
from src.primitives import vortex as vortex_mod
from src.primitives.themes import DARK, LIGHT, Theme, with_alpha
from src.generators import svg_utils as U

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "src" / "data" / "content.json"
GEN = ROOT / "assets" / "generated"


def load_content() -> dict:
    return json.loads(DATA.read_text())


def load_languages() -> dict:
    return json.loads((GEN / "languages.json").read_text())


def load_calendar() -> dict:
    return json.loads((GEN / "contribution-calendar.json").read_text())


# ---------------------------------------------------------------------------
# Study A — Orbit Instrument (Echo Gravity)
# Asymmetric: name left, concentric practice/project rings right as spine.
# ---------------------------------------------------------------------------

def study_a_orbit_instrument(theme: Theme, *, width=1012, height=540) -> str:
    content = load_content()
    identity = content["identity"]
    obs = content["observations"]

    cx, cy = width * 0.62, height * 0.52
    field_w, field_h = width * 0.72, height * 0.9

    # Domain cores + project observations as orbit pool
    pool = []
    for d in identity["domains"]:
        pool.append(
            {
                "text": d["label"],
                "type": "core" if d["band"] == "core" else "related",
                "size": 1.1 if d["band"] == "core" else 0.7,
                "opacity": 0.92 if d["band"] == "core" else 0.55,
                "semanticScore": 0.95 if d["band"] == "core" else 0.4,
                "meta": {"kind": "domain", "id": d["id"]},
            }
        )
    for o in obs:
        pool.append(
            {
                "text": o["name"],
                "type": "core" if o["ring"] == "core" else "related",
                "size": 0.95 if o["ring"] == "core" else 0.65,
                "opacity": 0.9 if o["ring"] == "core" else 0.5,
                "semanticScore": 0.85 if o["ring"] == "core" else 0.45,
                "meta": {"kind": "project", "id": o["id"], **o},
            }
        )

    items = orbit_mod.build_orbit_items(
        pool, field_w, field_h, motion=0.32, intensity=0.38, padding=28
    )
    min_r, max_r, guides = orbit_mod.ring_radii(field_w, field_h, padding=28)

    parts = []
    # background atmosphere
    if theme.grain:
        parts.append(
            f'<rect width="{width}" height="{height}" fill="url(#paperGrad)"/>'
        )
    else:
        parts.append(U.rect(0, 0, width, height, fill=theme.bg))

    # defs
    defs = f'''<defs>
    <linearGradient id="paperGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{theme.bg}"/>
      <stop offset="55%" stop-color="{theme.bg_alt}"/>
      <stop offset="100%" stop-color="{with_alpha(theme.accent, 0.08) if theme.name=='light' else theme.bg}"/>
    </linearGradient>
  </defs>'''

    # left typographic column — anchored relative to field, not centered hero
    parts.append(
        U.text(48, 56, "FIELD GUIDE  ·  OBS. SYSTEM", fill=theme.muted, size=10, family=U.MONO, tracking=0.28, weight="500")
    )
    parts.append(
        U.text(48, 118, identity["name"], fill=theme.ink, size=54, family=U.SERIF, weight="500")
    )
    parts.append(
        U.line(48, 132, 220, 132, theme.line_strong, width=1)
    )
    parts.append(
        U.text(48, 156, f"also {identity['preferred']}", fill=theme.muted, size=13, family=U.MONO, tracking=0.12, italic=False)
    )
    # statement — short measure, literary
    y = 210
    for i, line in enumerate(_wrap(identity["statement"], 28)):
        parts.append(
            U.text(48, y + i * 22, line, fill=theme.ink_soft, size=16, family=U.SERIF, italic=True)
        )

    parts.append(
        U.text(48, 310, "PRACTICE BANDS", fill=theme.muted2, size=9, family=U.MONO, tracking=0.22)
    )
    parts.append(
        U.text(48, 330, "inner  ·  AI · agents · HCI · design", fill=theme.muted, size=11, family=U.MONO)
    )
    parts.append(
        U.text(48, 348, "outer  ·  infra · research · writing", fill=theme.muted, size=11, family=U.MONO)
    )
    parts.append(
        U.text(48, 380, "Projects are observations on the rings,", fill=theme.muted, size=12, family=U.SERIF, italic=True)
    )
    parts.append(
        U.text(48, 398, "not cards in a grid.", fill=theme.muted, size=12, family=U.SERIF, italic=True)
    )

    # field guides
    for i, r in enumerate(guides):
        parts.append(
            U.circle(
                cx, cy, r,
                stroke=theme.line,
                sw=1,
                opacity=0.55 if i < 2 else 0.35,
                dash="2 6" if i == 2 else None,
            )
        )
    # center mark
    parts.append(U.circle(cx, cy, 2.2, fill=theme.accent, opacity=0.85))
    parts.append(
        U.text(cx, cy - max_r - 18, "GRAVITY  ·  ECHO ORBIT", fill=theme.muted2, size=9, family=U.MONO, tracking=0.2, anchor="middle")
    )

    # place items — domains as text, projects as hollow marks + labels
    for item in items:
        x, y = orbit_mod.project(item, cx, cy, squash=0.92)
        meta = item.meta or {}
        if meta.get("kind") == "project":
            # hollow observation mark
            r_mark = 4.5 if item.kind == "core" else 3.2
            parts.append(
                U.circle(x, y, r_mark, fill="none", stroke=theme.ink if item.kind == "core" else theme.muted, sw=1.2, opacity=item.opacity)
            )
            parts.append(
                U.text(
                    x, y - 12,
                    f"{meta.get('id','')}  {item.text}",
                    fill=theme.ink if item.kind == "core" else theme.muted,
                    size=12 if item.kind == "core" else 10.5,
                    family=U.SERIF,
                    weight="500" if item.kind == "core" else "400",
                    anchor="middle",
                    opacity=min(1, item.opacity + 0.1),
                )
            )
        else:
            parts.append(
                U.text(
                    x, y,
                    item.text,
                    fill=theme.ink if item.kind == "core" else theme.muted,
                    size=13 + item.size * 4 if item.kind == "core" else 10.5 + item.size * 3,
                    family=U.SERIF,
                    weight="500" if item.kind == "core" else "400",
                    anchor="middle",
                    opacity=item.opacity * (1 if item.kind == "core" else 0.75),
                    dominant_baseline="middle",
                )
            )

    # footer meta
    parts.append(U.line(48, height - 36, width - 48, height - 36, theme.line, width=1, opacity=0.8))
    parts.append(
        U.text(48, height - 16, "study A  ·  orbit instrument  ·  echo/frontend/helperJS/vortex.js placeOrbitRing", fill=theme.muted2, size=9, family=U.MONO, tracking=0.06)
    )
    parts.append(
        U.text(width - 48, height - 16, theme.name.upper(), fill=theme.muted2, size=9, family=U.MONO, tracking=0.16, anchor="end")
    )

    body = defs + "\n  " + U.join(parts)
    return U.wrap_svg(
        body,
        width=width,
        height=height,
        aria="Study A: Orbit instrument — practice domains and selected projects placed with Echo gravity rings",
        bg=None,
    )


# ---------------------------------------------------------------------------
# Study B — Spiral Field Notes (Echo Vortex)
# Spiral of languages + projects; notebook annotation gutters.
# ---------------------------------------------------------------------------

def study_b_spiral_field(theme: Theme, *, width=1012, height=560) -> str:
    content = load_content()
    langs = load_languages()["languages"][:8]
    identity = content["identity"]
    obs = content["observations"]

    cx, cy = width * 0.55, height * 0.48
    pool = []
    for i, lang in enumerate(langs):
        pool.append(
            {
                "text": lang["language"].replace("Jupyter Notebook", "Jupyter"),
                "type": "core" if i < 2 else "related",
                "frequency": lang["share_pct"] / 8,
                "size": 0.7 + lang["share_pct"] / 40,
                "semanticScore": min(1, lang["share_pct"] / 40),
                "meta": {"kind": "lang", "pct": lang["share_pct"]},
            }
        )
    for o in obs[:4]:
        pool.append(
            {
                "text": o["name"],
                "type": "core",
                "frequency": 3,
                "size": 1.2,
                "semanticScore": 0.9,
                "meta": {"kind": "project", "id": o["id"]},
            }
        )

    particles = vortex_mod.build_vortex_particles(pool, len(pool), motion=0.22, intensity=0.45)
    fit = min(width, height) / 520

    parts = []
    if theme.name == "light":
        parts.append(f'<rect width="{width}" height="{height}" fill="url(#paperGrad)"/>')
    else:
        parts.append(U.rect(0, 0, width, height, fill=theme.bg))

    defs = f'''<defs>
    <linearGradient id="paperGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#faf6ef"/>
      <stop offset="100%" stop-color="{theme.bg_alt}"/>
    </linearGradient>
  </defs>'''

    # manuscript gutter
    parts.append(U.rect(0, 0, 36, height, fill=with_alpha(theme.accent, 0.06 if theme.name == "light" else 0.0)))
    parts.append(
        U.text(18, height / 2, "SPIRAL  ·  FIELD NOTES", fill=theme.muted2, size=9, family=U.MONO, tracking=0.28, anchor="middle")
    )
    # rotate gutter label via transform
    parts[-1] = (
        f'<g transform="translate(18,{height/2}) rotate(-90)">'
        + U.text(0, 0, "SPIRAL  ·  FIELD NOTES", fill=theme.muted2, size=9, family=U.MONO, tracking=0.28, anchor="middle")
        + "</g>"
    )

    parts.append(
        U.text(56, 48, "STUDY B", fill=theme.accent, size=10, family=U.MONO, tracking=0.24)
    )
    parts.append(
        U.text(56, 88, identity["name"], fill=theme.ink, size=42, family=U.SERIF, weight="500")
    )
    parts.append(
        U.text(56, 116, identity["statement"], fill=theme.muted, size=14, family=U.SERIF, italic=True)
    )

    # spiral arm guide (sampled)
    arm = []
    for i in range(48):
        fake = vortex_mod.VortexParticle("·", "related", i * 0.42, 18 + i * 5.2, 0, 8, 0.3, 0.5)
        x, y = vortex_mod.project(fake, cx, cy, time=0, fit_scale=fit * 0.95, intensity=0.45, rotation=-0.4)
        arm.append(f"{x:.1f},{y:.1f}")
    parts.append(
        f'<polyline fill="none" stroke="{theme.line}" stroke-width="1" stroke-opacity="0.45" points="{" ".join(arm)}"/>'
    )
    parts.append(U.circle(cx, cy, 2, fill=theme.accent, opacity=0.7))

    for i, p in enumerate(particles):
        x, y = vortex_mod.project(p, cx, cy, time=12 + i, fit_scale=fit * 0.95, intensity=0.45, rotation=-0.4)
        meta = p.meta or {}
        if meta.get("kind") == "project":
            parts.append(U.circle(x, y, 3.5, fill="none", stroke=theme.ink, sw=1.15, opacity=0.9))
            parts.append(
                U.text(x + 8, y + 4, f"{meta['id']} {p.text}", fill=theme.ink, size=13, family=U.SERIF, weight="500")
            )
        else:
            parts.append(
                U.text(
                    x, y,
                    p.text,
                    fill=theme.ink if p.kind == "core" else theme.muted,
                    size=p.size * 0.85,
                    family=U.SERIF,
                    weight="500" if p.kind == "core" else "400",
                    anchor="middle",
                    opacity=p.opacity,
                    dominant_baseline="middle",
                )
            )

    # side annotation column
    ax = width - 210
    parts.append(U.line(ax - 20, 80, ax - 20, height - 60, theme.line, width=1, opacity=0.7))
    parts.append(U.text(ax, 96, "MAPPING", fill=theme.muted2, size=9, family=U.MONO, tracking=0.22))
    parts.append(U.text(ax, 120, "radius ↓  importance ↑", fill=theme.muted, size=11, family=U.MONO))
    parts.append(U.text(ax, 140, "angle = index × 0.42", fill=theme.muted, size=11, family=U.MONO))
    parts.append(U.text(ax, 180, "DATA", fill=theme.muted2, size=9, family=U.MONO, tracking=0.22))
    parts.append(U.text(ax, 204, "languages.json", fill=theme.ink_soft, size=12, family=U.SERIF, italic=True))
    parts.append(U.text(ax, 224, "byte share → score", fill=theme.muted, size=11, family=U.MONO))
    parts.append(U.text(ax, 260, "excl. cs340Project4", fill=theme.muted2, size=10, family=U.MONO))
    parts.append(U.text(ax, 278, "(vendored blob)", fill=theme.muted2, size=10, family=U.MONO))

    parts.append(U.line(56, height - 36, width - 40, height - 36, theme.line, opacity=0.8))
    parts.append(
        U.text(56, height - 16, "study B  ·  spiral field notes  ·  echo vortex createVortexParticle", fill=theme.muted2, size=9, family=U.MONO)
    )

    body = defs + "\n  " + U.join(parts)
    return U.wrap_svg(body, width=width, height=height, aria="Study B: Spiral field notes with language topology and project marks")


# ---------------------------------------------------------------------------
# Study C — Trajectory Folio
# Horizontal indexed trajectory; projects as disturbances; language rings inset.
# ---------------------------------------------------------------------------

def study_c_trajectory_folio(theme: Theme, *, width=1012, height=520) -> str:
    content = load_content()
    identity = content["identity"]
    obs = content["observations"]
    langs = load_languages()["languages"][:6]
    cal = load_calendar()

    parts = []
    if theme.name == "light":
        parts.append(f'<rect width="{width}" height="{height}" fill="{theme.bg}"/>')
        parts.append(
            f'<rect x="0" y="0" width="{width}" height="{height}" fill="url(#wash)" opacity="0.9"/>'
        )
    else:
        parts.append(U.rect(0, 0, width, height, fill=theme.bg))

    defs = f'''<defs>
    <radialGradient id="wash" cx="18%" cy="0%" r="70%">
      <stop offset="0%" stop-color="{with_alpha(theme.accent, 0.12)}"/>
      <stop offset="100%" stop-color="{theme.bg}" stop-opacity="0"/>
    </radialGradient>
  </defs>'''

    parts.append(U.text(40, 40, "FOLIO  ·  INDEXED TRAJECTORY", fill=theme.muted, size=10, family=U.MONO, tracking=0.26))
    parts.append(U.text(40, 86, identity["name"], fill=theme.ink, size=48, family=U.SERIF, weight="500"))
    parts.append(U.text(40, 112, identity["statement"], fill=theme.muted, size=14, family=U.SERIF, italic=True))

    # main trajectory
    y0 = 210
    parts.append(U.line(40, y0, width - 40, y0, theme.line_strong, width=1.2))
    # tick marks for domains
    domains = [d["label"] for d in identity["domains"] if d["band"] == "core"]
    for i, d in enumerate(domains):
        x = 80 + i * ((width - 160) / max(len(domains) - 1, 1))
        parts.append(U.line(x, y0 - 6, x, y0 + 6, theme.muted, width=1))
        parts.append(U.text(x, y0 + 22, d, fill=theme.muted2, size=9, family=U.MONO, tracking=0.08, anchor="middle"))

    # project disturbances along trajectory — angle encodes domain, height encodes emphasis
    domain_x = {d: 80 + i * ((width - 160) / 3) for i, d in enumerate(["ai", "hci", "design", "research"])}
    domain_x["agents"] = domain_x["ai"] + 40
    domain_x["infra"] = domain_x["design"] + 60
    domain_x["writing"] = domain_x["research"]

    for o in obs:
        x = domain_x.get(o["domain"], width / 2) + (hash(o["name"]) % 40 - 20)
        amp = 70 if o["emphasis"] == "computational" else 42
        direction = -1 if o["ring"] == "core" else 1
        y = y0 + direction * (amp * (0.55 + 0.45 * o["recency"]))
        parts.append(U.line(x, y0, x, y, theme.line, width=1, opacity=0.7, dash="2 3"))
        parts.append(U.circle(x, y, 4 if o["ring"] == "core" else 3, fill=theme.bg, stroke=theme.ink if o["ring"] == "core" else theme.muted, sw=1.25))
        parts.append(
            U.text(x + 8, y + 4, f"{o['id']}  {o['name']}", fill=theme.ink, size=13, family=U.SERIF, weight="500")
        )
        parts.append(
            U.text(x + 8, y + 20, o["provenance"], fill=theme.muted2, size=9, family=U.MONO, tracking=0.1)
        )

    # language topology inset (bottom-left rings)
    lcx, lcy = 150, 420
    for bi, r in enumerate([28, 52, 76]):
        parts.append(U.circle(lcx, lcy, r, stroke=theme.line, sw=1, opacity=0.4, dash="2 4" if bi == 2 else None))
    for i, lang in enumerate(langs):
        band = 0 if lang["share_pct"] >= 20 else (1 if lang["share_pct"] >= 5 else 2)
        r = [28, 52, 76][band]
        ang = (i / len(langs)) * math.pi * 2 + band * 0.5
        x = lcx + r * math.cos(ang)
        y = lcy + r * math.sin(ang) * 0.85
        parts.append(
            U.text(x, y, lang["language"].replace("Jupyter Notebook", "Jupyter")[:10], fill=theme.muted if band else theme.ink, size=10 if band else 12, family=U.SERIF, anchor="middle", dominant_baseline="middle")
        )
    parts.append(U.text(lcx, lcy + 100, "language topology  ·  byte share", fill=theme.muted2, size=9, family=U.MONO, tracking=0.08, anchor="middle"))

    # signal pulse (bottom-right)
    weeks = cal["week_totals"]
    sx0, sy0 = 420, 455
    sw, sh = 540, 50
    maxv = max(weeks) or 1
    pts = []
    for i, v in enumerate(weeks):
        x = sx0 + i / (len(weeks) - 1) * sw
        y = sy0 - (v / maxv) * sh
        pts.append(f"{x:.1f},{y:.1f}")
    parts.append(U.line(sx0, sy0, sx0 + sw, sy0, theme.line, opacity=0.5))
    parts.append(f'<polyline fill="none" stroke="{theme.ink}" stroke-width="1.4" stroke-opacity="0.75" points="{" ".join(pts)}"/>')
    parts.append(
        U.text(sx0, sy0 + 18, f"signal  ·  {cal['total_contributions']} contributions  ·  {cal.get('active_weeks', sum(1 for w in weeks if w))} active weeks  ·  unsmothed", fill=theme.muted2, size=9, family=U.MONO)
    )

    parts.append(U.line(40, height - 28, width - 40, height - 28, theme.line, opacity=0.7))
    parts.append(
        U.text(40, height - 12, "study C  ·  trajectory folio  ·  projects as disturbances along practice axis", fill=theme.muted2, size=9, family=U.MONO)
    )

    body = defs + "\n  " + U.join(parts)
    return U.wrap_svg(body, width=width, height=height, aria="Study C: Trajectory folio with project disturbances and language inset")


# ---------------------------------------------------------------------------
# FINAL — Computational Field Guide (chosen: Study A refined + supporting panels)
# ---------------------------------------------------------------------------

def profile_hero(theme: Theme, *, width=1012, height=430) -> str:
    """Opening composition: asymmetric name + Echo orbit spine.

    Domains use short labels on rings (Echo: label IS the node).
    Projects are numbered marks only; names live on the right rail
    so the field stays legible at GitHub width.
    """
    content = load_content()
    identity = content["identity"]
    obs = content["observations"]

    # Orbit center sits in the right half — name claims the left.
    cx, cy = 620, 248
    min_r, max_r = 48, 155
    # Echo band logic: core 0–0.4, related 0.55–0.95 of [min,max]
    core_r = min_r + (max_r - min_r) * 0.22
    mid_r = min_r + (max_r - min_r) * 0.48
    out_r = min_r + (max_r - min_r) * 0.82

    # Short labels — full phrases move to markdown / rail
    core_domains = [
        ("AI", -0.55),
        ("agents", 0.35),
        ("HCI", 1.35),
        ("design", 2.35),
    ]
    related_domains = [
        ("infra", 0.2),
        ("research", 2.0),
        ("writing", 3.6),
    ]

    # Project angles: evenly spaced on mid/out rings by band
    core_obs = [o for o in obs if o["ring"] == "core"]
    rel_obs = [o for o in obs if o["ring"] != "core"]

    parts: list[str] = []
    if theme.name == "light":
        parts.append(f'<rect width="{width}" height="{height}" fill="url(#pg)"/>')
    else:
        parts.append(U.rect(0, 0, width, height, fill=theme.bg))

    defs = f'''<defs>
    <linearGradient id="pg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#faf6ef"/>
      <stop offset="52%" stop-color="{theme.bg}"/>
      <stop offset="100%" stop-color="{theme.bg_alt}"/>
    </linearGradient>
  </defs>'''

    parts.append(
        U.text(36, 34, "COMPUTATIONAL FIELD GUIDE", fill=theme.muted, size=10, family=U.MONO, tracking=0.3, weight="500")
    )
    parts.append(
        U.text(width - 36, 34, "XZ · SYS", fill=theme.muted2, size=10, family=U.MONO, tracking=0.18, anchor="end")
    )

    parts.append(
        U.text(36, 104, identity["name"], fill=theme.ink, size=56, family=U.SERIF, weight="500")
    )
    parts.append(U.line(36, 118, 236, 118, theme.line_strong, width=1))
    parts.append(
        U.text(36, 142, "Shirley", fill=theme.muted, size=12, family=U.MONO, tracking=0.14)
    )

    for i, line in enumerate(_wrap(identity["statement"], 30)):
        parts.append(
            U.text(36, 180 + i * 22, line, fill=theme.ink_soft, size=15, family=U.SERIF, italic=True)
        )

    parts.append(U.text(36, 255, "MAPPING", fill=theme.muted2, size=9, family=U.MONO, tracking=0.22))
    parts.append(U.text(36, 276, "inner ring  ·  practice cores", fill=theme.muted, size=11, family=U.MONO))
    parts.append(U.text(36, 294, "mid marks  ·  selected work", fill=theme.muted, size=11, family=U.MONO))
    parts.append(U.text(36, 312, "outer ring ·  related concerns", fill=theme.muted, size=11, family=U.MONO))
    parts.append(
        U.text(36, 348, "Projects are numbered observations", fill=theme.muted, size=12, family=U.SERIF, italic=True)
    )
    parts.append(
        U.text(36, 366, "in the field — not portfolio cards.", fill=theme.muted, size=12, family=U.SERIF, italic=True)
    )

    # Orbit guides — Echo gravity
    for r, op, dash in (
        (core_r, 0.55, None),
        (mid_r, 0.45, None),
        (out_r, 0.32, "2 5"),
    ):
        parts.append(U.circle(cx, cy, r, stroke=theme.line, sw=1, opacity=op, dash=dash))
    parts.append(U.circle(cx, cy, 2.2, fill=theme.accent, opacity=0.9))
    parts.append(
        U.text(cx, cy - out_r - 16, "ECHO ORBIT  ·  practice gravity", fill=theme.muted2, size=9, family=U.MONO, tracking=0.16, anchor="middle")
    )

    # Domain labels on rings
    for label, ang in core_domains:
        x = cx + math.cos(ang) * core_r
        y = cy + math.sin(ang) * core_r * 0.9
        parts.append(
            U.text(x, y, label, fill=theme.ink, size=14, family=U.SERIF, weight="500", anchor="middle", dominant_baseline="middle")
        )
    for label, ang in related_domains:
        x = cx + math.cos(ang) * out_r
        y = cy + math.sin(ang) * out_r * 0.9
        parts.append(
            U.text(x, y, label, fill=theme.muted, size=11, family=U.SERIF, anchor="middle", dominant_baseline="middle", opacity=0.85)
        )

    # Project marks — Echo hollow nodes; indices only.
    # Angles chosen for legibility while staying on Echo band radii.
    core_angles = [-2.4, -0.55, 1.15]
    rel_angles = [-1.5, 0.35, 2.0]
    mark_positions = []
    for i, o in enumerate(core_obs):
        ang = core_angles[i % len(core_angles)]
        r = mid_r + math.sin(ang * 2) * 3.5
        x = cx + math.cos(ang) * r
        y = cy + math.sin(ang) * r * 0.9
        mark_positions.append((o, x, y, True))
    for i, o in enumerate(rel_obs):
        ang = rel_angles[i % len(rel_angles)]
        r = out_r * 0.72 + math.sin(ang * 2) * 4
        x = cx + math.cos(ang) * r
        y = cy + math.sin(ang) * r * 0.9
        mark_positions.append((o, x, y, False))

    for o, x, y, is_core in mark_positions:
        parts.append(
            U.circle(x, y, 9 if is_core else 7.5, fill=theme.bg, stroke=theme.ink if is_core else theme.muted, sw=1.25, opacity=0.98)
        )
        parts.append(
            U.text(x, y + 3.5, o["id"], fill=theme.ink if is_core else theme.muted, size=9, family=U.MONO, weight="500", anchor="middle")
        )

    # Right annotation rail — project names keyed to marks
    rail_x = 860
    parts.append(U.line(rail_x - 24, 90, rail_x - 24, 390, theme.line, width=1, opacity=0.65))
    parts.append(U.text(rail_x, 100, "OBS", fill=theme.muted2, size=9, family=U.MONO, tracking=0.24))
    ry = 128
    for o in obs:
        parts.append(U.text(rail_x, ry, o["id"], fill=theme.accent, size=10, family=U.MONO, weight="500"))
        parts.append(U.text(rail_x + 28, ry, o["name"], fill=theme.ink, size=13, family=U.SERIF, weight="500"))
        parts.append(
            U.text(rail_x + 28, ry + 16, f"{o['domain']} · {o['provenance']}", fill=theme.muted2, size=9, family=U.MONO)
        )
        ry += 42

    parts.append(U.line(36, height - 28, width - 36, height - 28, theme.line, opacity=0.75))
    parts.append(
        U.text(
            36,
            height - 12,
            "geometry: echo placeOrbitRing  ·  material: "
            + ("muselab paper" if theme.name == "light" else "echo night"),
            fill=theme.muted2,
            size=9,
            family=U.MONO,
        )
    )

    body = defs + "\n  " + U.join(parts)
    return U.wrap_svg(
        body,
        width=width,
        height=height,
        aria="Xinyue Zhang computational field guide — Echo orbit of practice domains with numbered project observations",
    )


def profile_observations(theme: Theme, *, width=1012, height=400) -> str:
    """Projects as an indexed observation plate — not cards.

    Two columns keyed to orbit indices. Hairlines + mono stamps only.
    """
    content = load_content()
    obs = content["observations"]
    professional = content["professional"]

    parts = []
    parts.append(U.rect(0, 0, width, height, fill=theme.bg))

    parts.append(U.text(36, 34, "01  ·  OBSERVATIONS", fill=theme.muted, size=10, family=U.MONO, tracking=0.28))
    parts.append(U.text(36, 64, "Selected work in the field", fill=theme.ink, size=26, family=U.SERIF, weight="500"))
    parts.append(
        U.text(
            36,
            88,
            "Index matches the orbit above. Core band = denser practice; related band = supporting probes.",
            fill=theme.muted,
            size=12,
            family=U.SERIF,
            italic=True,
        )
    )

    # two-column instrument plate
    col_w = (width - 72 - 40) / 2
    for i, o in enumerate(obs):
        col = i % 2
        row = i // 2
        x0 = 36 + col * (col_w + 40)
        y0 = 118 + row * 72
        parts.append(
            U.circle(x0 + 12, y0 + 14, 11, fill="none", stroke=theme.ink if o["ring"] == "core" else theme.muted, sw=1.2)
        )
        parts.append(
            U.text(x0 + 12, y0 + 18, o["id"], fill=theme.ink, size=10, family=U.MONO, anchor="middle", weight="500")
        )
        parts.append(U.text(x0 + 34, y0 + 10, o["name"], fill=theme.ink, size=17, family=U.SERIF, weight="500"))
        parts.append(
            U.text(
                x0 + 34,
                y0 + 30,
                f"{o['domain']}  ·  {o['provenance']}  ·  {o['availability']}",
                fill=theme.muted2,
                size=9,
                family=U.MONO,
                tracking=0.04,
            )
        )
        # one-line blurb
        blurb = o["blurb"]
        if len(blurb) > 68:
            blurb = blurb[:67] + "…"
        parts.append(U.text(x0 + 34, y0 + 48, blurb, fill=theme.muted, size=11.5, family=U.SERIF))

    y = 340
    parts.append(U.line(36, y, width - 36, y, theme.line, opacity=0.7))
    parts.append(U.text(36, y + 22, "ALSO", fill=theme.muted2, size=9, family=U.MONO, tracking=0.22))
    parts.append(U.text(90, y + 22, professional["label"], fill=theme.ink, size=14, family=U.SERIF, weight="500"))
    parts.append(
        U.text(36, y + 44, professional["note"], fill=theme.muted, size=11.5, family=U.SERIF, italic=True)
    )

    body = U.join(parts)
    return U.wrap_svg(
        body,
        width=width,
        height=height,
        aria="Indexed observations of selected projects with domain and provenance annotations",
    )


def profile_languages(theme: Theme, *, width=1012, height=340) -> str:
    langs_data = load_languages()
    langs = langs_data["languages"]
    cx, cy = 280, 175
    rings = [40, 90, 140]
    bands: list[list] = [[], [], []]
    for lang in langs:
        pct = lang["share_pct"]
        if pct >= 20:
            bands[0].append(lang)
        elif pct >= 3:
            bands[1].append(lang)
        else:
            bands[2].append(lang)

    parts = []
    parts.append(U.rect(0, 0, width, height, fill=theme.bg))
    parts.append(U.text(36, 36, "02  ·  LANGUAGE TOPOLOGY", fill=theme.muted, size=10, family=U.MONO, tracking=0.28))
    parts.append(U.text(36, 68, "Authored bytes across public repositories", fill=theme.ink, size=24, family=U.SERIF, weight="500"))
    parts.append(
        U.text(36, 92, f"Excluded: {', '.join(langs_data['excluded_repos'])} — {langs_data['exclusion_reason']}", fill=theme.muted2, size=10, family=U.MONO)
    )

    for bi, r in enumerate(rings):
        parts.append(U.circle(cx, cy, r, stroke=theme.line, sw=1, opacity=0.45, dash="2 5" if bi == 2 else None))
    parts.append(U.circle(cx, cy, 2.2, fill=theme.accent, opacity=0.85))

    for bi, band in enumerate(bands):
        r = rings[bi]
        n = max(len(band), 1)
        for i, lang in enumerate(band):
            ang = (i / n) * 2 * math.pi + bi * 0.5
            x = cx + r * math.cos(ang)
            y = cy + r * math.sin(ang) * 0.82
            label = lang["language"].replace("Jupyter Notebook", "Jupyter")
            fs = 12 + min(lang["share_pct"], 40) * 0.35
            op = 0.4 + min(lang["share_pct"] / 38, 1) * 0.55
            parts.append(
                U.text(x, y, label, fill=theme.ink if bi == 0 else theme.muted, size=fs, family=U.SERIF, weight="500" if bi == 0 else "400", anchor="middle", opacity=op, dominant_baseline="middle")
            )

    # legend / shares as mono ledger — not a bar chart
    lx = 520
    parts.append(U.text(lx, 120, "SHARE", fill=theme.muted2, size=9, family=U.MONO, tracking=0.22))
    y = 148
    for lang in langs[:8]:
        label = lang["language"].replace("Jupyter Notebook", "Jupyter Notebook")
        parts.append(U.text(lx, y, f"{lang['share_pct']:5.1f}%", fill=theme.accent if lang["share_pct"] >= 20 else theme.muted, size=12, family=U.MONO))
        parts.append(U.text(lx + 70, y, label, fill=theme.ink, size=13, family=U.SERIF))
        # proportional hairline — not a filled bar card
        lw = max(4, lang["share_pct"] * 4.2)
        parts.append(U.line(lx + 70, y + 8, lx + 70 + lw, y + 8, theme.line_strong, width=1.2, opacity=0.85))
        y += 22

    body = U.join(parts)
    return U.wrap_svg(body, width=width, height=height, aria="Language topology from real GitHub byte shares on Echo-style polar rings")


def profile_signal(theme: Theme, *, width=1012, height=180) -> str:
    cal = load_calendar()
    weeks = cal["week_totals"]
    maxv = max(weeks) or 1
    parts = []
    parts.append(U.rect(0, 0, width, height, fill=theme.bg))
    parts.append(U.text(36, 32, "03  ·  CONTRIBUTION SIGNAL", fill=theme.muted, size=10, family=U.MONO, tracking=0.28))
    parts.append(
        U.text(36, 56, f"{cal['total_contributions']} contributions across {cal['weeks']} weeks  ·  sparse, unsmoothed", fill=theme.ink_soft, size=13, family=U.SERIF, italic=True)
    )

    sx0, sy0 = 36, 130
    sw, sh = width - 72, 54
    pts = []
    for i, v in enumerate(weeks):
        x = sx0 + i / (len(weeks) - 1) * sw
        y = sy0 - (v / maxv) * sh
        pts.append(f"{x:.1f},{y:.1f}")
        if v > 0:
            parts.append(U.circle(x, y, 1.6 if v < 5 else 2.4, fill=theme.ink, opacity=0.55 + 0.4 * (v / maxv)))
    parts.append(U.line(sx0, sy0, sx0 + sw, sy0, theme.line, opacity=0.5))
    parts.append(f'<polyline fill="none" stroke="{theme.ink}" stroke-width="1.35" stroke-opacity="0.7" points="{" ".join(pts)}"/>')
    peak = max(weeks)
    peak_i = weeks.index(peak)
    peak_x = sx0 + peak_i / (len(weeks) - 1) * sw
    parts.append(U.text(peak_x, sy0 - sh - 8, f"peak {peak}", fill=theme.muted2, size=9, family=U.MONO, anchor="middle"))

    body = U.join(parts)
    return U.wrap_svg(body, width=width, height=height, aria="Unsmoothed 53-week contribution signal from GitHub contribution calendar")


def _wrap(text: str, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur: list[str] = []
    for w in words:
        trial = (" ".join(cur + [w]))
        if len(trial) > width and cur:
            lines.append(" ".join(cur))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(" ".join(cur))
    return lines
