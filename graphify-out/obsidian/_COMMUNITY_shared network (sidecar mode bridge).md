---
type: community
cohesion: 0.67
members: 3
---

# shared network (sidecar mode bridge)

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[agentshroud-gateway service (sidecar mode, optional scan)]] - code - docker-compose.sidecar.yml
- [[openclaw service (sidecar mode, exposed normally)]] - code - docker-compose.sidecar.yml
- [[shared network (sidecar mode bridge)]] - code - docker-compose.sidecar.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/shared_network_sidecar_mode_bridge
SORT file.name ASC
```
