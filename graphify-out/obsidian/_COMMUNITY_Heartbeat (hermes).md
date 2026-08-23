---
type: community
cohesion: 1.00
members: 3
---

# Heartbeat (hermes)

**Cohesion:** 1.00 - tightly connected
**Members:** 3 nodes

## Members
- [[_log()_1]] - code - docker/bots/hermes/heartbeat.sh
- [[heartbeat.sh]] - code - docker/bots/hermes/heartbeat.sh
- [[heartbeat.sh script]] - code - docker/bots/hermes/heartbeat.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Heartbeat_hermes
SORT file.name ASC
```
