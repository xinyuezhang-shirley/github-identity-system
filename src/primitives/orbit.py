"""Echo orbit / gravity placement — ported from echo/frontend/helperJS/vortex.js

Exact formulas preserved:
  placeOrbitRing / buildOrbitItems / orbitDynamics
Static freeze: time=0, no wobble animation (deterministic README frame).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, List, Sequence


@dataclass
class OrbitItem:
    text: str
    kind: str  # core | related
    angle: float
    base_radius: float
    radius: float
    semantic_score: float
    size: float
    opacity: float
    meta: dict | None = None


def orbit_dynamics(motion: float = 0.35, intensity: float = 0.4) -> dict:
    # echo vortex.js orbitDynamics
    return {
        "wobble_amp": 0.06 + intensity * 0.9,
        "base_speed": 0.002 + motion * 0.028,
        "wobble_radius": 8 + intensity * 22,
    }


def place_orbit_ring(
    group: Sequence[dict],
    inner_band: float,
    outer_band: float,
    max_radius: float,
    min_radius: float,
    *,
    freeze_wobble: bool = True,
    motion: float = 0.35,
    intensity: float = 0.4,
) -> List[OrbitItem]:
    """Port of placeOrbitRing from echo vortex.js."""
    placed: List[OrbitItem] = []
    if not group:
        return placed

    dynamics = orbit_dynamics(motion, intensity)
    wobble_amp = dynamics["wobble_amp"]
    wobble_radius = dynamics["wobble_radius"]

    rings = min(3, max(1, math.ceil(len(group) / 4)))
    per_ring = math.ceil(len(group) / rings)

    for i, p in enumerate(group):
        ring_idx = min(rings - 1, i // per_ring)
        slot_on_ring = i - ring_idx * per_ring
        slots_this_ring = min(per_ring, len(group) - ring_idx * per_ring)
        ring_t = 0.5 if rings <= 1 else ring_idx / (rings - 1)
        radius = min_radius + (max_radius - min_radius) * (
            inner_band + ring_t * (outer_band - inner_band)
        )
        angle = (slot_on_ring / max(slots_this_ring, 1)) * math.pi * 2 + ring_idx * 0.45

        # Static frame: optional freeze of sin wobble at angle-derived phase
        if freeze_wobble:
            r = radius + math.sin(angle * 2) * wobble_amp * (wobble_radius * 0.35)
        else:
            r = radius

        kind = p.get("type", "related")
        placed.append(
            OrbitItem(
                text=p["text"],
                kind=kind,
                angle=angle,
                base_radius=radius,
                radius=r,
                semantic_score=float(p.get("semanticScore", 0.5)),
                size=float(p.get("size", 0.8)),
                opacity=float(p.get("opacity", 0.8)),
                meta=p.get("meta"),
            )
        )
    return placed


def build_orbit_items(
    source_pool: Sequence[dict],
    width: float,
    height: float,
    *,
    motion: float = 0.35,
    intensity: float = 0.4,
    padding: float = 36,
) -> List[OrbitItem]:
    """Port of buildOrbitItems from echo vortex.js."""
    max_radius = max(70.0, min(width, height) * 0.42 - padding)
    min_radius = max_radius * 0.2

    core = [p for p in source_pool if p.get("type") == "core"]
    related = [p for p in source_pool if p.get("type") != "core"]

    items: List[OrbitItem] = []
    items.extend(
        place_orbit_ring(
            core, 0, 0.4, max_radius, min_radius, motion=motion, intensity=intensity
        )
    )
    items.extend(
        place_orbit_ring(
            related, 0.55, 0.95, max_radius, min_radius, motion=motion, intensity=intensity
        )
    )
    return items


def project(item: OrbitItem, cx: float, cy: float, *, squash: float = 1.0) -> tuple[float, float]:
    x = cx + math.cos(item.angle) * item.radius
    y = cy + math.sin(item.angle) * item.radius * squash
    return x, y


def ring_radii(width: float, height: float, padding: float = 36) -> tuple[float, float, list[float]]:
    """Guide rings for drawing — derived from Echo max/min radius."""
    max_r = max(70.0, min(width, height) * 0.42 - padding)
    min_r = max_r * 0.2
    # three guide rings spanning core and related bands
    guides = [
        min_r + (max_r - min_r) * 0.2,
        min_r + (max_r - min_r) * 0.48,
        min_r + (max_r - min_r) * 0.82,
    ]
    return min_r, max_r, guides
