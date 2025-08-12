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
            name = sanitize_name(record.get("name", "").strip("\""))
            affiliation = record.get("affiliation", "").strip("\"")
            freq = int(record.get("freq", 0))
            dblp = record.get("dblp", "").strip("<>")
            orcid = record.get("orcid", "").strip("<>")
            rows.append(
                {
                    "name": name,
                    "affiliation": affiliation,
                    "freq": freq,
                    "dblp": dblp,
                    "orcid": orcid,
                }
            )
    return rows


def sanitize_name(name: str) -> str:
    """Remove trailing numbers and '(disambiguation)' from a name."""
    name = re.sub(r"\s+\(disambiguation\)$", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\s+\d+$", "", name)
    return name


def count_recent_publications(rows):
    """Count SOSP/OSDI publications in the last five years for each author."""
    current_year = datetime.date.today().year
    years = range(current_year - 4, current_year + 1)
    author_name_set = {r["name"].strip() for r in rows}
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
        row["last"] = row["name"].split()[-1] if row["name"] else ""
        row["lastfive"] = recent_counts.get(row["name"], 0)

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
