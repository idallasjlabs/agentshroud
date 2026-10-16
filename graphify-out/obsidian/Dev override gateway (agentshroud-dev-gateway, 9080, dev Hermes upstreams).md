---
source_file: "docker/docker-compose.agentshroud-bot.marvin.yml"
type: "code"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "14"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# Dev override: gateway (agentshroud-dev-gateway, :9080, dev Hermes upstreams)

## Connections
- [[Dev gateway HERMES_DASHBOARD_UPSTREAM pointed at prod hostname (always 502)]] - `references` [EXTRACTED]
- [[Devprod coexistence on one host offset ports (908018790) and subnets (172.20-2224)]] - `rationale_for` [EXTRACTED]
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - `references` [EXTRACTED]
- [[dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]] - `references` [EXTRACTED]
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - `references` [EXTRACTED]
- [[gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]] - `references` [EXTRACTED]
- [[lifespan.py]] - `references` [EXTRACTED]
- [[pre-commit check-yaml hook (--unsafe)]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
