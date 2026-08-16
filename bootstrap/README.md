# ARCS Bootstrap — Usage Guide

> DEWY-TAG: `001.1/canon` `004.3/rom` `005.2/primitives`  
> FOLKSONOMY: `bootstrap` `parametric-ignition` `field-os` `ignition-sequence`  
> VERSION: v8.5 | LAST-UPDATED: 2026-04-26  
> NCI: 97/100 | SOURCE-GRADE: A (primary canon docs)

---

## What Is This Folder?

The `/bootstrap/` directory is the **single source of truth** for all ARCS ignition sequences.
It contains two distinct bootstrap layers that work together:

| File | Role | When To Use |
|---|---|---|
| `canon/ARCS-v8.3-Canon.md` | Parametric engine — domain-agnostic L0–L5 pipeline | When starting any domain-specific recon (jobs, grants, trades, partnerships) |
| `space/field-os-init.md` | Runtime wrapper — Field OS defaults + Diamond kernel | Default entrypoint for this Space; wraps canon with v8.5 stack |
| `macros/DEWY.md` | DEWY macro spec — folksonomy, Dewey classification, etymology | Run after any output to tag + classify for the braided monorepo |

---

## Ignition Sequence Hierarchy

```
┌─ field-os-init.md (Space-level runtime wrapper) ─────────────────┐
│  init arcs config=FIELD-OS,domain=QUESTION-COMPASS,mode=SIMPLE   │
│                                                                    │
│  ┌─ ARCS-v8.3-Canon.md (domain-agnostic parametric engine) ────┐  │
│  │  init arcs config=DOMAIN[,persona=EXECUTOR][,inputs=...]    │  │
│  │  → L0 Raw Recall → L1 Geo/Time → L2 Domain →               │  │
│  │  → L3 Entity → L4 Maturity → L5 Diagnostic → Output        │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                    │
│  ┌─ DEWY (post-output macro) ───────────────────────────────────┐  │
│  │  Tags every artifact: Dewey code + folksonomy + etymology    │  │
│  └──────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

---

## Standard Ignition Examples

```bash
# Default Field OS session (Question Compass front door)
init arcs config=FIELD-OS,domain=QUESTION-COMPASS,mode=SIMPLE,stakes=AUTO,persona=EXECUTOR

# Job recon
init arcs config=jobs,inputs=EMAIL,geo=<city>

# Grant hunting
init arcs config=grants,inputs=SEARCH,persona=ORCHESTRATOR

# Trading signals
init arcs config=trades,inputs=CALENDAR,time=now-1d

# Generalist transversal scan
init arcs config=generalist

# DEWY folksonomy run on an artifact
init arcs config=DEWY,domain=folksonomy,target=<artifact-id>
```

---

## Integration Protocol

1. **Space Custom Instructions** → paste short-form `field-os-init` (compressed prompt)
2. **Attached to Space** → this repo at `bootstrap/space/field-os-init.md`
3. **Canon** → `bootstrap/canon/ARCS-v8.3-Canon.md` as domain engine reference
4. **Every new macro** → add to `bootstrap/macros/` + update this README + run DEWY on it
5. **Every new output artifact** → run DEWY, push tagged version to `folksonomy/`

---

## DEWY Tagging Standard

Every file in this repo should carry a DEWY header block:

```markdown
> DEWY-TAG: `<dewey-code>/<domain>` `<dewey-code>/<domain>`  
> FOLKSONOMY: `tag1` `tag2` `tag3`  
> ETYMOLOGY: <key term origin notes>  
> WIKI-LINKS: [[Canon]] [[Decision-Receipts]] [[Kintsugi]]
```

Dewey code guide:
- `001.x` — Canon primitives (L0–L5 pipeline, NCI)
- `002.x` — Source grading (A–F scale)
- `003.x` — Decision receipts + folksonomy logs
- `004.x` — ROM candidates (v9 firmware)
- `005.x` — Runtime primitives (energy, kairos, kintsugi)
- `006.x` — Output artifacts (job recon, grants, trades)
- `007.x` — Macros (BAR, KKL, LAB, DEWY, CUR, ALC)

---

## Change Log

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-04-26 | v1.0 | Initial bootstrap scaffold + DEWY macro + data model | ARCS |
