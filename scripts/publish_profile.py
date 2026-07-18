#!/usr/bin/env python3
"""Copy Markdown-first profile artifacts into the public profile repository.

Usage:
    python3 scripts/publish_profile.py /path/to/xinyuezhang-shirley
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Old poster-panel assets to remove from the public repo
OBSOLETE = [
    "hero-light.svg",
    "hero-dark.svg",
    "observations-light.svg",
    "observations-dark.svg",
    "signal-light.svg",
    "signal-dark.svg",
]


def publish(dest: Path) -> None:
    dest = dest.resolve()
    assets = dest / "assets"
    assets.mkdir(parents=True, exist_ok=True)

    mapping = {
        ROOT / "generated" / "light" / "orbit.svg": assets / "orbit-light.svg",
        ROOT / "generated" / "dark" / "orbit.svg": assets / "orbit-dark.svg",
        ROOT / "generated" / "light" / "languages.svg": assets / "languages-light.svg",
        ROOT / "generated" / "dark" / "languages.svg": assets / "languages-dark.svg",
        ROOT / "generated" / "PROFILE_README.md": dest / "README.md",
    }

    for src, out in mapping.items():
        if not src.exists():
            raise SystemExit(f"missing generated file: {src} — run scripts/generate_profile.py final")
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, out)
        print(f"copied {src.relative_to(ROOT)} → {out}")

    for name in OBSOLETE:
        p = assets / name
        if p.exists():
            p.unlink()
            print(f"removed obsolete {p}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python3 scripts/publish_profile.py /path/to/xinyuezhang-shirley")
        raise SystemExit(2)
    publish(Path(sys.argv[1]))
