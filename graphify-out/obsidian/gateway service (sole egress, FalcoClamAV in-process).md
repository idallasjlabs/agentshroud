---
source_file: "docker/docker-compose.yml"
type: "code"
community: "_wrap_response() (2)"
location: "L19"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_wrap_response_2
---

# gateway service (sole egress, Falco/ClamAV in-process)

## Connections
- [[AgentShroud production compose stack]] - `references` [EXTRACTED]
- [[CI DAST scan job (Nuclei)]] - `references` [EXTRACTED]
- [[ClamAV upstream vs Debian finding]] - `references` [INFERRED]
- [[Gateway Python requirements]] - `references` [INFERRED]
- [[Marvin dev compose override (agentshroud-bot)]] - `references` [EXTRACTED]
- [[container macro (always-true placeholder inside the gateway)]] - `references` [EXTRACTED]
- [[falco-alerts  security-reports shared volumes]] - `shares_data_with` [EXTRACTED]
- [[gateway-start.sh entrypoint]] - `shares_data_with` [EXTRACTED]
- [[hermes service (agentshroud-hermes-v2)]] - `calls` [EXTRACTED]
- [[openclaw service_1]] - `calls` [EXTRACTED]
- [[voice-gateway service]] - `calls` [EXTRACTED]
- [[wazuh-agent sidecar]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_wrap_response_2
