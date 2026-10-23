---
type: community
cohesion: 1.00
members: 2
---

# run-tests-batched.sh

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[export-openapi.sh]] - code - scripts/export-openapi.sh
- [[export-openapi.sh script]] - code - scripts/export-openapi.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run-tests-batchedsh
SORT file.name ASC
```
