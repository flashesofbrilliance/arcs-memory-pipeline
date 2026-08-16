# Track 2 — Creative File Index

## Purpose
Index all ARCS Space files by character count as a creativity proxy.

## Usage
```bash
# 1. Drop your exported Space .md / .json files into /origins
# 2. Run:
python indexer/index_creative_files.py
# 3. Output: output/creative_index.csv
```

## Threshold
Default: **500,000 characters**. Adjust `CREATIVITY_THRESHOLD` in the script.

## Output CSV Columns
| Column | Description |
|--------|-------------|
| filename | File name |
| char_count | Approximate character count |
| creative | True if above threshold |
| created | File creation timestamp |
