"""Track 3: Filter creative files by time-quality threshold using ARCS ROM.

Dual-path qualification:
  PATH A (Time)       — minutes >= TIME_THRESHOLD_MINUTES AND mode in ALLOWED_MODES
  PATH B (Write-Lock) — write_lock == true AND gate_type == 'One-Way' (ROM GR-6 proxy)

A file qualifies if it passes EITHER path.
"""
import json
import csv
import os

ROM_PATH = "../origins/time-quality-attribution-rom.json"
INPUT_CSV = "../output/creative_index.csv"
OUTPUT_CSV = "../output/time_filtered_index.csv"

# --- Path A: Time threshold ---
TIME_THRESHOLD_MINUTES = 30          # Shorter default (was 120)
ALLOWED_MODES = {"Kairos", "Chronos", "Drift"}  # Drift included: discovery-yield blocks count

# --- Path B: Write-Lock proxy (ROM GR-6) ---
# A file qualifies if its ROM entry signals:
#   write_lock == True  AND  gate_type == 'One-Way'
# This captures identity-level, future-binding, or coherence-sensitive commits
# regardless of raw elapsed time.
WRITE_LOCK_GATE = "One-Way"


def load_rom(path: str) -> dict:
    if not os.path.exists(path):
        print(f"[WARN] ROM not found at {path}. Skipping time scoring.")
        return {}
    with open(path) as f:
        return json.load(f)


def load_creative_index(path: str) -> list[dict]:
    with open(path) as f:
        return list(csv.DictReader(f))


def score_file(filename: str, rom: dict) -> dict:
    """Look up the ROM entry for a file. Returns entry or a zero-state default."""
    for entry in rom.get("entries", []):
        if entry.get("file") == filename:
            return entry
    return {
        "file": filename,
        "mode": "UNKNOWN",
        "minutes": 0,
        "write_lock": False,
        "gate_type": "Two-Way",
        "quality": "Neutral",
        "jurisdiction": "Clock",
    }


def qualifies_path_a(entry: dict, threshold: int, modes: set) -> bool:
    """Path A: sufficient time in an allowed mode."""
    return int(entry.get("minutes", 0)) >= threshold and entry.get("mode", "UNKNOWN") in modes


def qualifies_path_b(entry: dict) -> bool:
    """Path B: write-lock + One-Way gate (ROM GR-6 proxy).
    Captures identity-level / future-binding commits regardless of duration.
    """
    return bool(entry.get("write_lock", False)) and entry.get("gate_type") == WRITE_LOCK_GATE


def filter_files(
    records: list[dict],
    rom: dict,
    threshold: int,
    modes: set,
) -> list[dict]:
    qualified = []
    for rec in records:
        if rec.get("creative", "False") != "True":
            continue
        entry = score_file(rec["filename"], rom)
        path_a = qualifies_path_a(entry, threshold, modes)
        path_b = qualifies_path_b(entry)
        if path_a or path_b:
            rec["time_minutes"] = entry.get("minutes", 0)
            rec["time_mode"] = entry.get("mode", "UNKNOWN")
            rec["quality"] = entry.get("quality", "Neutral")
            rec["jurisdiction"] = entry.get("jurisdiction", "Clock")
            rec["write_lock"] = entry.get("write_lock", False)
            rec["gate_type"] = entry.get("gate_type", "Two-Way")
            rec["qualification_path"] = (
                "A+B" if (path_a and path_b)
                else "A (time)" if path_a
                else "B (write-lock)"
            )
            qualified.append(rec)
    return qualified


def write_csv(records: list[dict], path: str):
    if not records:
        print("No files met the threshold.")
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)
    print(f"Output: {path} ({len(records)} files qualified)")
    path_a_count = sum(1 for r in records if "A" in r["qualification_path"])
    path_b_count = sum(1 for r in records if "B" in r["qualification_path"])
    print(f"  Path A (time >{threshold}min):  {path_a_count}")
    print(f"  Path B (write-lock One-Way): {path_b_count}")


if __name__ == "__main__":
    rom = load_rom(ROM_PATH)
    records = load_creative_index(INPUT_CSV)
    qualified = filter_files(records, rom, TIME_THRESHOLD_MINUTES, ALLOWED_MODES)
    write_csv(qualified, OUTPUT_CSV)
