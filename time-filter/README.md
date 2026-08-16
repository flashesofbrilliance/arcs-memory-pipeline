# Track 3 — Time Threshold Filter

## Purpose
Filter creative files using ARCS `time-quality-attribution-rom.json`. A file qualifies via **either** of two independent paths.

## Dual-Path Qualification

| Path | Logic | ROM Anchor |
|------|-------|------------|
| **A — Time** | `minutes >= 30` AND `mode` in `{Kairos, Chronos, Drift}` | GR-1, GR-2 |
| **B — Write-Lock** | `write_lock == True` AND `gate_type == One-Way` | GR-6 |

**Path B rationale:** A write-lock signals an identity-level, future-binding, or coherence-sensitive commit (ROM GR-6). These blocks qualify regardless of raw elapsed time because their irreversibility and coherence weight make duration a misleading judge.

## Usage
```bash
# 1. Drop time-quality-attribution-rom.json into /origins
# 2. Run Track 2 first:
python indexer/index_creative_files.py
# 3. Run:
python time-filter/filter_by_time.py
# 4. Output: output/time_filtered_index.csv
```

## Configuration
| Variable | Default | Description |
|----------|---------|-------------|
| `TIME_THRESHOLD_MINUTES` | **30** | Minimum minutes (Path A) |
| `ALLOWED_MODES` | Kairos, Chronos, Drift | Modes that count for Path A |
| `WRITE_LOCK_GATE` | One-Way | Gate type required for Path B |

## Output CSV Columns
| Column | Description |
|--------|-------------|
| `filename` | File name |
| `char_count` | Character count |
| `creative` | Creative flag (Track 2) |
| `created` | Creation timestamp |
| `time_minutes` | Minutes logged in ROM |
| `time_mode` | ARCS time mode (Chronos/Kairos/Drift/Shavasana) |
| `quality` | Block quality (Productive/Generative/Restorative/Neutral/Dissolutive) |
| `jurisdiction` | Evaluative authority (Clock/Compass/Court/Sanctuary) |
| `write_lock` | True if write-lock was engaged |
| `gate_type` | One-Way or Two-Way |
| `qualification_path` | `A (time)` / `B (write-lock)` / `A+B` |

## Failure Modes Guarded Against
- **FM-7** (Write-Lock Failure): Path B catches blocks that required atomicity
- **FM-3** (Jurisdiction Failure): Drift now included in Path A (discovery-yield blocks not penalized by Clock metrics)
- **FM-2** (Time Quality Attribution Failure): quality + jurisdiction fields surfaced in output for human review
