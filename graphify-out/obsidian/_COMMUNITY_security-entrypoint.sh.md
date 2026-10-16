---
type: community
cohesion: 0.43
members: 7
---

# security-entrypoint.sh

**Cohesion:** 0.43 - moderately connected
**Members:** 7 nodes

## Members
- [[120s freshclam timeout rationale (bounded failure over outage)]] - rationale - docker/scripts/security-entrypoint.sh
- [[alert_critical()]] - code - docker/scripts/security-entrypoint.sh
- [[gateway-start.sh]] - code - docker/scripts/gateway-start.sh
- [[gateway-start.sh script]] - code - docker/scripts/gateway-start.sh
- [[log()_3]] - code - docker/scripts/security-entrypoint.sh
- [[security-entrypoint.sh]] - code - docker/scripts/security-entrypoint.sh
- [[security-entrypoint.sh script]] - code - docker/scripts/security-entrypoint.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/security-entrypointsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Falco Rules]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_dockerscriptssecurity-scan.sh]]

## Top bridge nodes
- [[security-entrypoint.sh]] - degree 7, connects to 2 communities
- [[gateway-start.sh]] - degree 3, connects to 1 community
