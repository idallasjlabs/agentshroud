---
type: community
cohesion: 0.38
members: 7
---

# init-openclaw-config.sh

**Cohesion:** 0.38 - loosely connected
**Members:** 7 nodes

## Members
- [[_oc_config_set]] - code - docker/scripts/init-openclaw-config.sh
- [[_sha256]] - code - docker/scripts/init-openclaw-config.sh
- [[agentshroud-isolated Network (DMZ tier)]] - code - docker/docker-compose.yml
- [[entrypoint-agentshroud.sh]] - code - docker/scripts/entrypoint-agentshroud.sh
- [[entrypoint-agentshroud.sh script]] - code - docker/scripts/entrypoint-agentshroud.sh
- [[init-openclaw-config.sh]] - code - docker/scripts/init-openclaw-config.sh
- [[init-openclaw-config.sh script]] - code - docker/scripts/init-openclaw-config.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/init-openclaw-configsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]

## Top bridge nodes
- [[entrypoint-agentshroud.sh]] - degree 3, connects to 1 community