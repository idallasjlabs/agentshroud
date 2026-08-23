---
type: community
cohesion: 1.00
members: 1
---

# Forward (routes)

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[POST forwardstream (streaming voice pipeline)]] - code - gateway/ingest_api/routes/forward.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Forward_routes
SORT file.name ASC
```
