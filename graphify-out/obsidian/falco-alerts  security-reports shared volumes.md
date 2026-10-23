---
source_file: "docker/docker-compose.yml"
type: "code"
community: "run-standalone.sh"
location: "L1086"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run-standalonesh
---

# falco-alerts / security-reports shared volumes

## Connections
- [[AgentShroud production compose stack]] - `references` [EXTRACTED]
- [[gateway service (sole egress, FalcoClamAV in-process)]] - `shares_data_with` [EXTRACTED]
- [[wazuh-agent sidecar]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run-standalonesh
