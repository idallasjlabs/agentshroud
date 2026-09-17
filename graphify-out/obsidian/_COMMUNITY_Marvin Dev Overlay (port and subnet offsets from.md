---
type: community
cohesion: 0.29
members: 7
---

# Marvin Dev Overlay (port and subnet offsets from

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[AGENTSHROUD_GATEWAY_CONTAINER Override (renamed container breaks CVE scan)]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[AgentShroud Daily Check-in (disabled — bot-identity-locked to dev)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Gateway Service]] - code - docker/docker-compose.yml
- [[Marvin Dev Overlay (port and subnet offsets from prod)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Wazuh Agent Service]] - code - docker/docker-compose.yml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[security-entrypoint.sh boot scan flow]] - code - docker/scripts/security-entrypoint.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Marvin_Dev_Overlay_port_and_subnet_offsets_from
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Falco Detection Rules]]

## Top bridge nodes
- [[Gateway Service]] - degree 3, connects to 1 community