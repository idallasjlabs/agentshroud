---
source_file: "prompts/sunday-upgrade.md"
type: "rationale"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "294"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# Soak, not just boot: check-soak-status.sh must report SOAKED on dev OpenClaw

## Connections
- [[The run is judged on state change, not steps completed]] - `semantically_similar_to` [INFERRED]
- [[check-soak-status.sh]] - `references` [EXTRACTED]
- [[wazuh-agent sidecar (root moment for privilege drop, then uid 1000)]] - `semantically_similar_to` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
