# ARCS Memory Export Pipeline

Three-track system for exporting memories, indexing creative Space files, and filtering by time threshold.

## Track 1 — Memory Export
Manually export Perplexity account memories (Settings > Personalize > Manage Memories).
Store snapshots in `/memories/`.

## Track 2 — Creative File Index
Index all Space files by character count as a creativity proxy (threshold: >500k chars).
Scripts in `/indexer/`.

## Track 3 — Time Threshold Filter
Parse `time-quality-attribution-rom.json` to filter files by time mode and quality score.
Scripts in `/time-filter/`.

## Folder Structure
```
/memories       → Memory snapshots (JSON/MD)
/indexer        → Creative file index scripts
/time-filter    → Time-threshold filter scripts
/origins        → Raw Space file exports
/output         → Final indexed artifacts
```

## Usage
1. Run `indexer/index_creative_files.py` to generate `output/creative_index.csv`
2. Run `time-filter/filter_by_time.py` to apply time threshold
3. Copy qualifying files to `origins/`
