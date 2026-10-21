---
source_file: "docker/docker-compose.yml"
type: "code"
community: "Sunday Upgrade prompt"
location: "L19"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Sunday_Upgrade_prompt
---

# gateway service (agentshroud-gateway)

## Connections
- [[Base docker-compose stack]] - `references` [EXTRACTED]
- [[CI DAST scan job (Nuclei)]] - `references` [EXTRACTED]
- [[Marvin dev compose override (agentshroud-bot)]] - `references` [EXTRACTED]
- [[container macro (always-true placeholder inside the gateway)]] - `references` [EXTRACTED]
- [[falco-alerts  clamav-db volumes (in-gateway sidecars)]] - `shares_data_with` [EXTRACTED]
- [[gateway-start.sh entrypoint]] - `shares_data_with` [EXTRACTED]
- [[hermes bot service (profile hermesfull)]] - `references` [EXTRACTED]
- [[openclaw bot service]] - `references` [EXTRACTED]
- [[voice-gateway service]] - `references` [EXTRACTED]
- [[wazuh-agent sidecar service]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Sunday_Upgrade_prompt
