---
type: community
members: 11
---

# cmd_start

**Members:** 11 nodes

## Members
- [[Funnel hermes via gateway (Hermes isolation boundary)]] - rationale - scripts/tailscale-serve.sh
- [[Funnel root path  - gateway hermes-dashboard]] - rationale - scripts/tailscale-serve.sh
- [[Gateway hermes-dashboard reverse proxy 502 from hostTailscale]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Temporary Funnel stopgap for ESP32 voice terminal]] - rationale - scripts/tailscale-serve.sh
- [[cmd_persist]] - code - scripts/tailscale-serve.sh
- [[cmd_start]] - code - scripts/tailscale-serve.sh
- [[cmd_status]] - code - scripts/tailscale-serve.sh
- [[cmd_stop]] - code - scripts/tailscale-serve.sh
- [[hermes-dashboard-relay container (9119 Tailscale bypass of gateway)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[tailscale-serve.sh]] - code - scripts/tailscale-serve.sh
- [[tailscale-serve.sh script]] - code - scripts/tailscale-serve.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/cmd_start
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Request]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[cmd_start]] - degree 8, connects to 1 community
- [[Gateway hermes-dashboard reverse proxy 502 from hostTailscale]] - degree 2, connects to 1 community
