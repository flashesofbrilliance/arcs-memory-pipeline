# DEWY Macro — Folksonomy, Dewey Classification, Etymology, Wiki-Links

> DEWY-TAG: `007.1/macro-dewy` `003.1/folksonomy` `001.3/classification`  
> FOLKSONOMY: `dewy` `folksonomy` `dewey-decimal` `etymology` `wiki-links` `tagging` `classification` `canon-macro`  
> ETYMOLOGY: *Dewey* (Melvil Dewey, 1876 — decimal classification system). *Folksonomy* (Thomas Vander Wal, 2004 — folk + taxonomy; collaborative tagging). *Etymology* (Gk. etymon — true sense + logos — study of).  
> WIKI-LINKS: [[ARCS-v8.3-Canon]] [[Field-OS-Init]] [[Decision-Receipts]] [[BAR-KKL-LAB]]  
> VERSION: v1.0 | NCI: 94/100 | SOURCE-GRADE: A  
> LAST-UPDATED: 2026-04-26

---

## What Is DEWY?

DEWY is the **4th always-on macro** in the ARCS v8.5 stack (alongside BAR, KKL, LAB).
It runs **after** every significant output to tag, classify, and cross-link artifacts for the braided monorepo.

---

## Acronym

| Letter | Stands For | Function |
|---|---|---|
| **D** | Dewey Decimal | Classify artifact by ARCS Dewey code |
| **E** | Etymology | Trace key term origins → semantic roots |
| **W** | Wiki-links | Cross-reference to related ARCS primitives |
| **Y** | Yours (folksonomy) | Apply user-defined tags (kairos-canon, partner-axiom, etc.) |

---

## ARCS Dewey Code System

```
001.x — Canon Primitives
  001.1  Canon spine (L0–L5 pipeline)
  001.2  NCI self-grading
  001.3  Classification + folksonomy
  001.4  Source grading (A–F)

002.x — Decision Infrastructure
  002.1  Decision receipts
  002.2  Prediction logs
  002.3  Outcome tracking

003.x — Folksonomy + Memory
  003.1  Folksonomy tags
  003.2  Memory export
  003.3  Time-filter artifacts

004.x — ROM Candidates (v9 Firmware)
  004.1  Field OS + v9 ROM defaults
  004.2  Diamond Protocol
  004.3  Hypersphere + Hyperstition
  004.4  Golden Inchworm
  004.5  Funhouse Optics

005.x — Runtime Primitives
  005.1  Kairos Lock + Sync
  005.2  Kintsugi Immune
  005.3  Energy tracking
  005.4  Drift Sentinel
  005.5  NOTOMATION

006.x — Output Artifacts
  006.1  Job recon outputs
  006.2  Grant outputs
  006.3  Trade signals
  006.4  Business/MVP opportunities

007.x — Macros
  007.1  DEWY
  007.2  BAR (Baseline Asymmetric Ruin)
  007.3  KKL (Kairos vs. Chronos Lock)
  007.4  LAB (Loki / Advisors / Bayes)
  007.5  CUR (Curator)
  007.6  ALC (Alchemist)
```

---

## Invocation

```bash
# Tag a specific artifact
init arcs config=DEWY,domain=folksonomy,target=<artifact-id>

# Recursive tag entire folder
init arcs config=DEWY,domain=folksonomy,target=<folder>,recursive=true

# Dry run (preview tags, no write)
init arcs config=DEWY,domain=folksonomy,target=<artifact-id>,mode=dry-run
```

---

## Output Format

Every DEWY-tagged file receives a header block:

```markdown
> DEWY-TAG: `<code>/<domain>` `<code>/<domain>`  
> FOLKSONOMY: `tag1` `tag2` `tag3`  
> ETYMOLOGY: <key term origin notes>  
> WIKI-LINKS: [[Related-1]] [[Related-2]]  
> VERSION: <version> | NCI: <score>/100 | SOURCE-GRADE: <A-F>  
> LAST-UPDATED: <ISO date>
```

---

## DEWY Run Log Format (for `folksonomy/` folder)

```markdown
# DEWY Run — <artifact-id>
Date: <ISO>
Target: <file path>
Dewey Codes: <list>
Folksonomy Tags: <list>
Etymology Notes: <key terms>
Wiki-Links Added: <list>
NCI Score: <score>/100
Patterns Detected: <list>
Decision Receipt ID: <dr-YYYY-MM-DD-NNN>
```

---

## Recursive DEWY Protocol

When `recursive=true`:
1. Walk all files in target folder (depth-first)
2. For each file: run D + E + W + Y passes
3. Write/update DEWY header block in-place
4. Append entry to `folksonomy/DEWY-index.md`
5. Update `data-model/arcs-graph.json` with new nodes + edges
6. Commit with standard DEWY commit message:
   ```
   feat(dewy): recursive tag <folder> — <N> files, <M> new tags
   DEWY-TAG: <top codes>
   FOLKSONOMY: <top tags>
   DECISION-RECEIPT: <dr-id>
   ```

---

## Integration With Data Model

Every DEWY run updates `data-model/arcs-graph.json`:
- Each artifact becomes a **node** (id, path, dewey_codes, folksonomy, nci_score)
- Each wiki-link becomes an **edge** (source → target, relationship type)
- The graph is queryable for pattern detection, coherence scoring, drift analysis

---

## NCI Breakdown (This Doc)

| Dimension | Score | Notes |
|---|---|---|
| Factual | 38/40 | Dewey system well-defined; folksonomy codes ARCS-native |
| Sources | 18/20 | Primary (Dewey 1876, Vander Wal 2004 cited) |
| Honesty | 19/20 | Notes ARCS codes are non-standard extension |
| Action | 19/20 | CLI examples + integration path clear |
| **Total** | **94/100** | |

---

## Change Log

| Date | Version | Change |
|---|---|---|
| 2026-04-26 | v1.0 | Initial DEWY macro spec — 4th always-on macro in ARCS v8.5 stack |
