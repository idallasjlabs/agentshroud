---
type: community
members: 4
---

# Startup Flow Diagram

**Members:** 4 nodes

## Members
- [[logs.sh]] - code - docker/scripts/logs.sh
- [[logs.sh script]] - code - docker/scripts/logs.sh
- [[restart.sh]] - code - docker/scripts/restart.sh
- [[restart.sh script]] - code - docker/scripts/restart.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Startup_Flow_Diagram
SORT file.name ASC
```
