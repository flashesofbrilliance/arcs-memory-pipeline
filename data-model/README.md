# ARCS Data Model

> DEWY-TAG: `003.1/data-model` `003.2/graph-schema`  
> FOLKSONOMY: `data-model` `graph` `arcs-graph` `schema` `interactive` `progressive`  
> VERSION: v1.0 | LAST-UPDATED: 2026-04-26

---

## Overview

The `data-model/` folder contains the **progressively-updating ARCS knowledge graph** — a machine-readable mirror of everything in the repo, updated by every DEWY run.

---

## Files

| File | Purpose |
|---|---|
| `arcs-graph.json` | Master knowledge graph — nodes (artifacts) + edges (wiki-links) + tag cloud + decision receipts |
| `README.md` | This file — schema docs + query examples |

---

## Schema

### Node

```json
{
  "id": "<slug>",
  "path": "<repo-relative path>",
  "type": "canon | macro | runtime-wrapper | documentation | folksonomy-run | registry | output",
  "dewey_codes": ["001.1", "004.3"],
  "folksonomy": ["tag1", "tag2"],
  "nci_score": 95,
  "source_grade": "A",
  "version": "1.0",
  "last_updated": "YYYY-MM-DD",
  "dewy_run": "DEWY-NNN"
}
```

### Edge

```json
{
  "source": "<node-id>",
  "target": "<node-id>",
  "relationship": "references | wraps | includes | writes-to | tags | cites | produced-by | registered-in",
  "label": "<human description>"
}
```

### Decision Receipt

```json
{
  "id": "dr-YYYY-MM-DD-NNN",
  "date": "YYYY-MM-DD",
  "question": "...",
  "horizon": "today | this-week | this-quarter | 1-3-years",
  "stakes": "low | medium | high",
  "mode": "QUICKMOVE | PLAN | COURT",
  "clarity_mode": "SIMPLE | RICH | DEEP",
  "macros_used": ["BAR", "KKL", "LAB", "DEWY"],
  "true_north": "...",
  "rationale": "...",
  "outcome": "PENDING | CONFIRMED | REVISED"
}
```

---

## How To Query

### Find all artifacts by Dewey code
```js
graph.nodes.filter(n => n.dewey_codes.includes('001.1'))
```

### Find all artifacts by folksonomy tag
```js
graph.nodes.filter(n => n.folksonomy.includes('kairos'))
```

### Get all edges from a node
```js
graph.edges.filter(e => e.source === 'field-os-init')
```

### Get top tags
```js
Object.entries(graph.tag_cloud).sort((a,b) => b[1]-a[1]).slice(0,10)
```

### Get open decision receipts
```js
graph.decision_receipts.filter(r => r.outcome === 'PENDING')
```

---

## Update Protocol

Every DEWY run **must** update `arcs-graph.json`:
1. Add new nodes for any new files tagged
2. Add new edges for any new wiki-links discovered
3. Recalculate `tag_cloud` counts
4. Append new decision receipt if triggered
5. Bump `meta.last_updated`

This keeps the graph **progressively accurate** — it grows with every commit.

---

## Roadmap

- [ ] v1.1: Add `confidence_score` to edges
- [ ] v1.2: Auto-generate graph from DEWY-index via CI action
- [ ] v1.3: Interactive graph viewer (D3.js) as GitHub Pages
- [ ] v2.0: Semantic similarity edges (cosine distance between folksonomy embeddings)
