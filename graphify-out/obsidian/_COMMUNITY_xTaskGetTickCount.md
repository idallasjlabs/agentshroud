---
type: community
members: 3
---

# xTaskGetTickCount

**Members:** 3 nodes

## Members
- [[agentshroud-gateway service (sidecar mode, optional scan)]] - code - docker-compose.sidecar.yml
- [[openclaw service (sidecar mode, exposed normally)]] - code - docker-compose.sidecar.yml
- [[shared network (sidecar mode bridge)]] - code - docker-compose.sidecar.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/xTaskGetTickCount
SORT file.name ASC
```
