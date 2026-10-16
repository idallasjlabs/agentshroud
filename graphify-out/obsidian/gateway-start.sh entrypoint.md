---
source_file: "docker/scripts/gateway-start.sh"
type: "code"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# gateway-start.sh entrypoint

## Connections
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - `shares_data_with` [EXTRACTED]
- [[security-entrypoint.sh boot scan flow]] - `calls` [EXTRACTED]
- [[wazuh-agent sidecar (root moment for privilege drop, then uid 1000)]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
