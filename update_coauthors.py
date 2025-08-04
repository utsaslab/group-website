#!/usr/bin/env python3
"""Generate co-author data from the bibliography."""

from __future__ import annotations

import re
from pathlib import Path

BIB_PATH = Path("assets/ref.bib")
OUTPUT_PATH = Path("_data/co-authors.yml")
SELF_NAME = "Vijay Chidambaram"


def normalize(name: str) -> str:
    name = re.sub(r"\s+", " ", name.strip())
    if "," in name:
        last, first = [p.strip() for p in name.split(",", 1)]
        name = f"{first} {last}"
    return name


def parse_entries(text: str):
    pattern = re.compile(r"@.*?{[^@]*}", re.DOTALL)
    for match in pattern.finditer(text):
        yield match.group(0)


def extract_authors_year(entry: str):
    m_auth = re.search(r"author\s*=\s*{([^}]*)}", entry, re.IGNORECASE | re.DOTALL)
    m_year = re.search(r"year\s*=\s*{([^}]*)}", entry, re.IGNORECASE)
    if not (m_auth and m_year):
        return None, None
    year_text = m_year.group(1)
    year_match = re.search(r"\d{4}", year_text)
    year = int(year_match.group(0)) if year_match else None
    authors_field = m_auth.group(1).replace("\n", " ")
    authors = [normalize(a) for a in authors_field.split(" and ") if a.strip()]
    return authors, year


def main() -> None:
    if not BIB_PATH.exists():
        raise SystemExit(f"Input file {BIB_PATH} does not exist")
    text = BIB_PATH.read_text(encoding="utf-8")
    coauthors: dict[str, int] = {}
    for entry in parse_entries(text):
        authors, year = extract_authors_year(entry)
        if not authors or year is None:
            continue
        normalized_self = normalize(SELF_NAME).lower()
        normalized_authors = [normalize(a).lower() for a in authors]
        if normalized_self not in normalized_authors:
            continue
        for author in authors:
            if normalize(author).lower() == normalized_self:
                continue
            key = normalize(author)
            coauthors[key] = max(year, coauthors.get(key, 0))
    lines = []
    for name in sorted(coauthors):
        lines.append(f"- name: {name}")
        lines.append(f"  last_coauthored: {coauthors[name]}")
        lines.append("  website: ")
        lines.append("")
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(coauthors)} co-authors to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
