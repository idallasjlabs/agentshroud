---
source_file: "docker/docker-compose.yml"
type: "code"
community: "Sunday Upgrade prompt"
location: "L331"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Sunday_Upgrade_prompt
---

# wazuh-agent sidecar service

## Connections
- [[Base docker-compose stack]] - `references` [EXTRACTED]
- [[Marvin dev compose override (agentshroud-bot)]] - `references` [EXTRACTED]
- [[falco-alerts  clamav-db volumes (in-gateway sidecars)]] - `shares_data_with` [EXTRACTED]
- [[gateway service (agentshroud-gateway)]] - `references` [EXTRACTED]
- [[gateway-start.sh entrypoint]] - `references` [EXTRACTED]
- [[wazuh-manager service (wazuh 4.14.8)]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Sunday_Upgrade_prompt
