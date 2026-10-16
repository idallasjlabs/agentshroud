---
source_file: "docker/docker-compose.yml"
type: "concept"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "179"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)

## Connections
- [[Dev override gateway (agentshroud-dev-gateway, 9080, dev Hermes upstreams)]] - `references` [EXTRACTED]
- [[TestHermesDashboardBridgeReachability]] - `references` [EXTRACTED]
- [[dashboard_bridge.py]] - `references` [EXTRACTED]
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - `rationale_for` [EXTRACTED]
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - `rationale_for` [EXTRACTED]
- [[hermes-dashboard-relay container (9119 Tailscale bypass of gateway)]] - `references` [EXTRACTED]
- [[lifespan.py]] - `references` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
