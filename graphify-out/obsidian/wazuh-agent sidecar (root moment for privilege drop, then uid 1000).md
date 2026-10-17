---
source_file: "docker/docker-compose.yml"
type: "code"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "330"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# wazuh-agent sidecar (root moment for privilege drop, then uid 1000)

## Connections
- [[Soak, not just boot (check-soak-status.sh SOAKED)]] - `semantically_similar_to` [INFERRED]
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - `shares_data_with` [EXTRACTED]
- [[gateway-start.sh entrypoint]] - `references` [EXTRACTED]
- [[wazuh-manager service (4.14.8, isolated-network only, open enrollment)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
