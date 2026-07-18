"""Theme tokens — two studios, not one inverted palette.

LIGHT = MuseLab paper tokens from MuseLab/frontend/src/index.css
DARK  = Echo night tokens from echo/frontend/styles.css
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    name: str
    bg: str
    bg_alt: str
    panel: str
    ink: str
    ink_soft: str
    muted: str
    muted2: str
    line: str
    line_strong: str
    accent: str
    accent_soft: str
    # Material character differs; geometry stays shared.
    grain: bool
    running_is_mono: bool


LIGHT = Theme(
    name="light",
    bg="#f4efe6",
    bg_alt="#ebe3d4",
    panel="#fffcf7",
    ink="#1c1917",
    ink_soft="#332e29",
    muted="#57534e",
    muted2="#8b8478",
    line="#dfd4c8",
    line_strong="#c9bca9",
    accent="#8b6914",
    accent_soft="#b08a3e",
    grain=True,
    running_is_mono=False,
)

DARK = Theme(
    name="dark",
    bg="#000000",
    bg_alt="#000000",
    panel="rgba(255,255,255,0.05)",
    ink="#f5f5f5",
    ink_soft="#e7e7e7",
    muted="#888888",
    muted2="#6b6b6b",
    line="rgba(255,255,255,0.20)",
    line_strong="rgba(255,255,255,0.32)",
    accent="#a89a78",
    accent_soft="#726a56",
    grain=False,
    running_is_mono=True,
)


def with_alpha(hex_or_rgb: str, alpha: float) -> str:
    """Match echo/frontend/helperJS/theme.js withAlpha for hex colors."""
    c = hex_or_rgb.strip()
    if c.startswith("rgba") or c.startswith("rgb"):
        return c
    if c.startswith("#"):
        c = c[1:]
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    r = int(c[0:2], 16)
    g = int(c[2:4], 16)
    b = int(c[4:6], 16)
    return f"rgba({r},{g},{b},{alpha:.3f})"
