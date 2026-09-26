---
type: community
cohesion: 1.00
members: 1
---

# Drift Detection in Pipeline

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[SOUL.md Freshness Check Job]] - code - .github/workflows/ci.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Drift_Detection_in_Pipeline
SORT file.name ASC
```
