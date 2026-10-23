---
source_file: "docker/docker-compose.yml"
type: "code"
community: "run-standalone.sh"
location: "L19"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run-standalonesh
---

# gateway service (sole egress, Falco/ClamAV in-process)

## Connections
- [[AgentShroud production compose stack]] - `references` [EXTRACTED]
- [[CI DAST scan job (Nuclei)]] - `references` [EXTRACTED]
- [[Marvin dev compose override (agentshroud-bot)]] - `references` [EXTRACTED]
- [[container macro (always-true placeholder inside the gateway)]] - `references` [EXTRACTED]
- [[falco-alerts  security-reports shared volumes]] - `shares_data_with` [EXTRACTED]
- [[gateway-start.sh entrypoint]] - `shares_data_with` [EXTRACTED]
- [[hermes service (agentshroud-hermes-v2)]] - `calls` [EXTRACTED]
- [[openclaw service]] - `calls` [EXTRACTED]
- [[voice-gateway service]] - `calls` [EXTRACTED]
- [[wazuh-agent sidecar]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run-standalonesh
