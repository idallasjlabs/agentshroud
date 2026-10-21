---
source_file: "docker/docker-compose.yml"
type: "code"
community: "_wrap_response() (2)"
location: "L335"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_wrap_response_2
---

# wazuh-agent sidecar

## Connections
- [[AgentShroud production compose stack]] - `references` [EXTRACTED]
- [[Marvin dev compose override (agentshroud-bot)]] - `references` [EXTRACTED]
- [[falco-alerts  security-reports shared volumes]] - `shares_data_with` [EXTRACTED]
- [[gateway service (sole egress, FalcoClamAV in-process)]] - `shares_data_with` [EXTRACTED]
- [[gateway-start.sh entrypoint]] - `references` [EXTRACTED]
- [[wazuh-manager service (4.14.8)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_wrap_response_2
