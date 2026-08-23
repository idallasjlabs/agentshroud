---
type: community
cohesion: 0.50
members: 4
---

# Logs (scripts)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[logs.sh]] - code - docker/scripts/logs.sh
- [[logs.sh script]] - code - docker/scripts/logs.sh
- [[restart.sh]] - code - docker/scripts/restart.sh
- [[restart.sh script]] - code - docker/scripts/restart.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Logs_scripts
SORT file.name ASC
```
