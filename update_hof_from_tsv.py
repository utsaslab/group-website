#!/usr/bin/env python3
"""Process hall of fame data from a TSV file."""

import csv
import datetime
import json
import re
import time
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

INPUT_FILE = Path("_data/hof-raw.tsv")
OUTPUT_FILE = Path("_data/hof.csv")

# Configuration for counting recent publications
VENUES = ["osdi", "sosp"]
DBLP_API = "https://dblp.org/search/publ/api"
MAX_RESULTS = 1000
SLEEP_TIME = 1.0  # seconds between API calls


def parse_rows(path: Path):
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for raw in reader:
            # Normalize column names by stripping leading question marks
            record = {k.lstrip("?"): v for k, v in raw.items()}
            raw_name = record.get("name", "").strip("\"")
            affiliation = record.get("affiliation", "").strip("\"")
            freq = int(record.get("freq", 0))
            dblp = record.get("dblp", "").strip("<>")
            orcid = record.get("orcid", "").strip("<>")
            rows.append(
                {
                    # Preserve the author's name as provided so middle
                    # initials remain in the generated CSV, but also
                    # keep a sanitized version for internal
                    # comparisons against DBLP records.
                    "name": raw_name,
                    "sanitized": sanitize_name(raw_name),
                    "affiliation": affiliation,
                    "freq": freq,
                    "dblp": dblp,
                    "orcid": orcid,
                }
            )
    return rows


def sanitize_name(name: str) -> str:
    """Normalize author names for comparison.

    In addition to stripping trailing DBLP disambiguation markers and
    numbers, some author entries include middle initials (e.g., "Remzi
    H. Arpaci-Dusseau").  DBLP is inconsistent about whether those
    initials are present, which can lead to mismatched publication
    counts.  To avoid this, drop any middle-name tokens that are a
    single letter (with or without a trailing period).
    """

    # Remove trailing "(disambiguation)" and numeric suffixes such as
    # "John Smith 0001" which DBLP uses for disambiguation.
    name = re.sub(r"\s+\(disambiguation\)$", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\s+\d+$", "", name)

    # Remove middle initials like "H." or "C" that can appear or
    # disappear across different records.
    parts = [p for p in name.split() if len(p.rstrip(".")) > 1]
    return " ".join(parts)


def count_recent_publications(rows):
    """Count SOSP/OSDI publications in the last five years for each author."""
    current_year = datetime.date.today().year
    years = range(current_year - 4, current_year + 1)
    # Use sanitized author names for matching so that names like
    # "Jane Doe 0001" from DBLP match the sanitized entries produced
    # when parsing ``hof-raw.tsv``.
    author_name_set = {r["sanitized"] for r in rows}
    counts = defaultdict(int)

    for venue in VENUES:
        for year in years:
            query = f"venue:{venue} year:{year}"
            params = urlencode({"q": query, "h": MAX_RESULTS, "format": "json"})
            url = f"{DBLP_API}?{params}"
            try:
                with urlopen(url) as resp:
                    data = json.load(resp)
            except Exception as e:
                print(f"Failed to fetch {venue} {year}: {e}")
                continue

            hits = data.get("result", {}).get("hits", {}).get("hit", [])
            for hit in hits:
                authors = hit.get("info", {}).get("authors", {}).get("author", [])
                if isinstance(authors, dict):
                    authors = [authors]
                for author in authors:
                    # DBLP often appends numerical disambiguators to
                    # author names (e.g., "Jane Doe 0001").  We strip
                    # those here so the comparison with our sanitized
                    # names succeeds.
                    name = sanitize_name(author.get("text", "").strip())
                    if name in author_name_set:
                        counts[name] += 1

            time.sleep(SLEEP_TIME)

    return counts


def main() -> None:
    if not INPUT_FILE.exists():
        raise SystemExit(f"Input file {INPUT_FILE} does not exist")

    rows = parse_rows(INPUT_FILE)
    recent_counts = count_recent_publications(rows)
    for row in rows:
        sanitized = row["sanitized"]
        row["last"] = sanitized.split()[-1] if sanitized else ""
        row["lastfive"] = recent_counts.get(sanitized, 0)
        # ``sanitized`` is only needed for internal processing; drop it
        # so the CSV output retains the original author name with any
        # middle initials intact.
        del row["sanitized"]

    rows.sort(key=lambda r: r["freq"], reverse=True)

    if rows:
        cutoff = rows[99]["freq"] if len(rows) >= 100 else rows[-1]["freq"]
    else:
        cutoff = 0

    filtered = [r for r in rows if r["freq"] >= cutoff]

    fieldnames = ["name", "last", "affiliation", "freq", "lastfive", "dblp", "orcid"]
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in filtered:
            writer.writerow(row)

    print(f"Wrote {len(filtered)} authors to {OUTPUT_FILE} (cutoff {cutoff})")


if __name__ == "__main__":
    main()
