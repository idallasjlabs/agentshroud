---
source_file: "docker/docker-compose.yml"
type: "code"
community: "run-standalone.sh"
location: "L335"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run-standalonesh
---

# wazuh-agent sidecar

## Connections
- [[AgentShroud production compose stack]] - `references` [EXTRACTED]
- [[Marvin dev compose override (agentshroud-bot)]] - `references` [EXTRACTED]
- [[falco-alerts  security-reports shared volumes]] - `shares_data_with` [EXTRACTED]
- [[gateway service (sole egress, FalcoClamAV in-process)]] - `shares_data_with` [EXTRACTED]
- [[gateway-start.sh entrypoint]] - `references` [EXTRACTED]
- [[wazuh-manager service (4.14.8)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run-standalonesh
