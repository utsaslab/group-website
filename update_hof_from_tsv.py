#!/usr/bin/env python3
"""Process hall of fame data from a TSV file."""

import csv
from pathlib import Path

INPUT_FILE = Path("_data/hof-raw.tsv")
OUTPUT_FILE = Path("_data/hof.csv")


def parse_rows(path: Path):
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for raw in reader:
            # Normalize column names by stripping leading question marks
            record = {k.lstrip("?"): v for k, v in raw.items()}
            name = record.get("name", "").strip("\"")
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


def main() -> None:
    if not INPUT_FILE.exists():
        raise SystemExit(f"Input file {INPUT_FILE} does not exist")

    rows = parse_rows(INPUT_FILE)
    for row in rows:
        row["last"] = row["name"].split()[-1] if row["name"] else ""

    rows.sort(key=lambda r: r["freq"], reverse=True)

    if rows:
        cutoff = rows[99]["freq"] if len(rows) >= 100 else rows[-1]["freq"]
    else:
        cutoff = 0

    filtered = [r for r in rows if r["freq"] >= cutoff]

    fieldnames = ["name", "last", "affiliation", "freq", "dblp", "orcid"]
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in filtered:
            writer.writerow(row)

    print(f"Wrote {len(filtered)} authors to {OUTPUT_FILE} (cutoff {cutoff})")


if __name__ == "__main__":
    main()
