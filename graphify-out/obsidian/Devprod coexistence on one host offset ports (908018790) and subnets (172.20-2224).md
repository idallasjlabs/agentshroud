---
source_file: "docker/docker-compose.agentshroud-bot.marvin.yml"
type: "rationale"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "1"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# Dev/prod coexistence on one host: offset ports (9080/18790) and subnets (172.20-22/24)

## Connections
- [[Dev override gateway (agentshroud-dev-gateway, 9080, dev Hermes upstreams)]] - `rationale_for` [EXTRACTED]
- [[Dev override voice-gateway on 127.0.0.18766]] - `rationale_for` [EXTRACTED]
- [[Three-tier network segmentation (internal edge  isolated DMZ  dmz) — IEC 62443 FR5]] - `references` [EXTRACTED]
- [[dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
