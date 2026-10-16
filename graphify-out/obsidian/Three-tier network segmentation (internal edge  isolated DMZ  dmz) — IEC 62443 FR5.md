---
source_file: "docker/docker-compose.yml"
type: "rationale"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "1004"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# Three-tier network segmentation (internal edge / isolated DMZ / dmz) — IEC 62443 FR5

## Connections
- [[Compose-version label mismatch forces network recreation + stale endpoint records]] - `references` [EXTRACTED]
- [[Devprod coexistence on one host offset ports (908018790) and subnets (172.20-2224)]] - `references` [EXTRACTED]
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - `rationale_for` [EXTRACTED]
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - `rationale_for` [EXTRACTED]
- [[hermes-dashboard-relay container (9119 Tailscale bypass of gateway)]] - `conceptually_related_to` [INFERRED]
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - `rationale_for` [EXTRACTED]
- [[wazuh-manager service (4.14.8, isolated-network only, open enrollment)]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
