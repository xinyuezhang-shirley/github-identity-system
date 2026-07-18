"""Echo vortex spiral placement — ported from echo/frontend/helperJS/vortex.js

Exact formulas:
  angle  = index * 0.42
  radius = 18 + index * spiralStep + (1 - semanticScore) * outerSpread
  z      = sin(index * 0.7) * intensity * 120
  project: x = cos(a)*r, y = (sin(a)*r*0.62 + z*depthScale)
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Sequence


@dataclass
class VortexParticle:
    text: str
    kind: str
    angle: float
    radius: float
    z: float
    size: float
    opacity: float
    semantic_score: float
    meta: dict | None = None


def vortex_params(motion: float = 0.28, intensity: float = 0.4) -> dict:
    # echo getVortexParams — using Echo values (not MuseLab's retuned set)
    return {
        "motion_scale": 2 + motion * 22,
        "wobble_amount": 3 + intensity * 28,
        "wobble_rate": 0.006 + intensity * 0.022,
        "depth_scale": 0.08 + intensity * 0.28,
        "spiral_spacing": 3.5 + intensity * 8,
        "vortex_speed": 4 + motion * 26,
        "outer_spread": 40 + intensity * 60,
        "intensity": intensity,
    }


def create_vortex_particle(
    template: dict, index: int, params: dict, *, particle_count: int = 40
) -> VortexParticle:
    is_core = template.get("type") == "core"
    importance = float(template.get("frequency") or template.get("size") or 1)
    if is_core:
        semantic = min(1.0, float(template.get("semanticScore", importance / 5)))
    else:
        semantic = min(1.0, float(template.get("semanticScore", 0.35)))

    density_tighten = min(1.0, 100 / max(particle_count, 1))
    spiral_step = (params["spiral_spacing"] + params["intensity"] * 3) * density_tighten

    # Deterministic seed (no Math.random) — index-based
    wobble_seed = (index * 2.3999632) % (math.pi * 2)

    return VortexParticle(
        text=template["text"],
        kind="core" if is_core else "related",
        angle=index * 0.42,
        radius=18 + index * spiral_step + (1 - semantic) * params["outer_spread"] * density_tighten,
        z=math.sin(index * 0.7) * params["intensity"] * 120,
        size=(
            min(34, 16 + importance * 8)
            if is_core
            else min(22, 12 + semantic * 10)
        ),
        opacity=0.94 if is_core else 0.28 + semantic * 0.42,
        semantic_score=semantic,
        meta=template.get("meta"),
    )


def build_vortex_particles(
    source_pool: Sequence[dict],
    count: int,
    *,
    motion: float = 0.28,
    intensity: float = 0.4,
) -> List[VortexParticle]:
    params = vortex_params(motion, intensity)
    params["particle_count"] = count
    out: List[VortexParticle] = []
    for i in range(count):
        tmpl = source_pool[i % len(source_pool)]
        out.append(create_vortex_particle(tmpl, i, params, particle_count=count))
    return out


def project(
    p: VortexParticle,
    cx: float,
    cy: float,
    *,
    time: float = 0.0,
    fit_scale: float = 1.0,
    motion: float = 0.28,
    intensity: float = 0.4,
    rotation: float = -0.35,
) -> tuple[float, float]:
    params = vortex_params(motion, intensity)
    # freeze time for static SVG; allow small deterministic phase
    speed = 0.0015 + (1 - p.semantic_score) * 0.002
    a = p.angle + time * speed * params["motion_scale"] * params["vortex_speed"] * 0.00135 + rotation
    spiral = p.radius + math.sin(time * params["wobble_rate"] + (p.angle) + 0.4) * (
        params["wobble_amount"] * 0.25
    )
    x = math.cos(a) * spiral * fit_scale
    y = (math.sin(a) * spiral * 0.62 + p.z * params["depth_scale"]) * fit_scale
    return cx + x, cy + y
