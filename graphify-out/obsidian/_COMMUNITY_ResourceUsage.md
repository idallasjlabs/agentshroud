---
type: community
cohesion: 0.29
members: 10
---

# ResourceUsage

**Cohesion:** 0.29 - loosely connected
**Members:** 10 nodes

## Members
- [[check()_12]] - code - scripts/preflight-check.sh
- [[fail()_6]] - code - scripts/tailscale-check.sh
- [[infra-check.sh]] - code - scripts/infra-check.sh
- [[infra-check.sh script]] - code - scripts/infra-check.sh
- [[ok()_2]] - code - scripts/tailscale-check.sh
- [[preflight-check.sh]] - code - scripts/preflight-check.sh
- [[preflight-check.sh script]] - code - scripts/preflight-check.sh
- [[tailscale-check.sh]] - code - scripts/tailscale-check.sh
- [[tailscale-check.sh script]] - code - scripts/tailscale-check.sh
- [[warn()_6]] - code - scripts/tailscale-check.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ResourceUsage
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]

## Top bridge nodes
- [[preflight-check.sh]] - degree 4, connects to 1 community
