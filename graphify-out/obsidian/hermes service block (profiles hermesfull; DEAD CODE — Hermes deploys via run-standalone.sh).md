---
source_file: "docker/docker-compose.yml"
type: "code"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "664"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# hermes service block (profiles hermes/full; DEAD CODE — Hermes deploys via run-standalone.sh)

## Connections
- [[Compose secrets block (file fallbacks; asb extracts from credential backend at runtime)]] - `shares_data_with` [EXTRACTED]
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - `rationale_for` [EXTRACTED]
- [[Multi-Agent Orchestration (specialized agents, per-agent isolation)]] - `semantically_similar_to` [INFERRED]
- [[Sunday upgrade mission every component in dev and prod to latest stable, resolve every finding, dev first]] - `references` [EXTRACTED]
- [[Three-tier network segmentation (internal edge  isolated DMZ  dmz) — IEC 62443 FR5]] - `rationale_for` [EXTRACTED]
- [[docker-socket-proxy service (digest-pinned tecnativa, narrow allowlist)]] - `references` [EXTRACTED]
- [[dockerbotshermesagentshroud-secrets.sh (s6 cont-init secret injection)]] - `references` [EXTRACTED]
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - `references` [EXTRACTED]
- [[run-standalone.sh]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
