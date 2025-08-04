#!/usr/bin/env python3
"""Print coauthors who have published with me in the last two years.

This script reads ``_data/co-authors.yml`` and outputs the names of all
coauthors whose most recent collaboration year is within the past two
years relative to the current calendar year.

The script tries to use PyYAML if available but falls back to a minimal
parser so it has no external dependencies.
"""

from __future__ import annotations

import datetime as _dt
from pathlib import Path
from typing import List, Dict, Any

try:  # pragma: no cover - optional dependency
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    yaml = None  # type: ignore


def _load_entries(path: Path) -> List[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        return yaml.safe_load(text) or []

    # Fallback minimal parser tailored for the file's simple structure
    entries: List[Dict[str, Any]] = []
    current: Dict[str, Any] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("- "):
            if current:
                entries.append(current)
            current = {}
            line = line[2:].strip()
        if ":" in line:
            key, value = line.split(":", 1)
            current[key.strip()] = value.strip()
    if current:
        entries.append(current)
    return entries


def main() -> None:
    data_path = Path("_data") / "co-authors.yml"
    entries = _load_entries(data_path)

    current_year = _dt.date.today().year
    cutoff = current_year - 2

    recent = [
        item.get("name")
        for item in entries
        if int(item.get("last_coauthored", 0)) >= cutoff
    ]

    for name in recent:
        print(name)


if __name__ == "__main__":
    main()
