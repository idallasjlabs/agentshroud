---
type: community
cohesion: 1.00
members: 2
---

# Check Status (scripts)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[check-status.sh]] - code - docker/scripts/check-status.sh
- [[check-status.sh script]] - code - docker/scripts/check-status.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Check_Status_scripts
SORT file.name ASC
```
