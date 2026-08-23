---
type: community
cohesion: 1.00
members: 2
---

# Hermes Cron Dedup (scripts)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[hermes-cron-dedup.sh]] - code - docker/scripts/hermes-cron-dedup.sh
- [[hermes-cron-dedup.sh script]] - code - docker/scripts/hermes-cron-dedup.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Hermes_Cron_Dedup_scripts
SORT file.name ASC
```
