---
type: community
cohesion: 0.83
members: 4
---

# Health Check (scripts)

**Cohesion:** 0.83 - tightly connected
**Members:** 4 nodes

## Members
- [[check_fail()]] - code - docker/scripts/health-check.sh
- [[check_pass()]] - code - docker/scripts/health-check.sh
- [[health-check.sh]] - code - docker/scripts/health-check.sh
- [[health-check.sh script]] - code - docker/scripts/health-check.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Health_Check_scripts
SORT file.name ASC
```
