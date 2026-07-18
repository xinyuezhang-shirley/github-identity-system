"""SVG helpers safe for GitHub README rendering."""

from __future__ import annotations

import html
from typing import Iterable


SERIF = "Georgia, 'Times New Roman', Times, serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def text(
    x: float,
    y: float,
    content: str,
    *,
    fill: str,
    size: float,
    family: str = SERIF,
    weight: str = "400",
    anchor: str = "start",
    opacity: float = 1.0,
    tracking: float | None = None,
    italic: bool = False,
    dominant_baseline: str = "alphabetic",
) -> str:
    ls = f' letter-spacing="{tracking}em"' if tracking is not None else ""
    style = f"font-family:{family};font-size:{size}px;font-weight:{weight}"
    if italic:
        style += ";font-style:italic"
    return (
        f'<text x="{x:.2f}" y="{y:.2f}" fill="{fill}" opacity="{opacity:.3f}" '
        f'text-anchor="{anchor}" dominant-baseline="{dominant_baseline}" '
        f'style="{style}"{ls}>{esc(content)}</text>'
    )


def line(x1, y1, x2, y2, stroke, *, width=1.0, opacity=1.0, dash: str | None = None) -> str:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
        f'stroke="{stroke}" stroke-width="{width}" stroke-opacity="{opacity:.3f}"{d}/>'
    )


def circle(cx, cy, r, *, fill="none", stroke=None, sw=1.0, opacity=1.0, dash=None) -> str:
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" '
        f'opacity="{opacity:.3f}"{s}{d}/>'
    )


def rect(x, y, w, h, *, fill, opacity=1.0, rx=0) -> str:
    return (
        f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
        f'rx="{rx}" fill="{fill}" opacity="{opacity:.3f}"/>'
    )


def wrap_svg(
    body: str,
    *,
    width: int,
    height: int,
    aria: str,
    bg: str | None = None,
) -> str:
    bg_el = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"
     viewBox="0 0 {width} {height}" role="img" aria-label="{esc(aria)}">
  <title>{esc(aria)}</title>
  {bg_el}
  {body}
</svg>
'''


def join(parts: Iterable[str]) -> str:
    return "\n  ".join(p for p in parts if p)
