"""Track 2: Index Space files by creativity proxy (character count)."""
import os
import json
import csv
from datetime import datetime

CREATIVITY_THRESHOLD = 500_000  # chars
SPACE_FILES_DIR = "../origins"  # drop raw .md/.json exports here
OUTPUT_CSV = "../output/creative_index.csv"

def index_files(directory: str, threshold: int) -> list[dict]:
    results = []
    for fname in os.listdir(directory):
        fpath = os.path.join(directory, fname)
        if not os.path.isfile(fpath):
            continue
        size = os.path.getsize(fpath)
        char_count = size  # bytes ≈ chars for UTF-8 ASCII-heavy content
        results.append({
            "filename": fname,
            "char_count": char_count,
            "creative": char_count >= threshold,
            "created": datetime.fromtimestamp(os.path.getctime(fpath)).isoformat(),
        })
    return sorted(results, key=lambda x: x["char_count"], reverse=True)

def write_csv(records: list[dict], output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["filename", "char_count", "creative", "created"])
        writer.writeheader()
        writer.writerows(records)
    print(f"Written: {output_path}")

if __name__ == "__main__":
    records = index_files(SPACE_FILES_DIR, CREATIVITY_THRESHOLD)
    write_csv(records, OUTPUT_CSV)
    creative = [r for r in records if r["creative"]]
    print(f"Total files: {len(records)} | Creative (>={CREATIVITY_THRESHOLD:,} chars): {len(creative)}")
