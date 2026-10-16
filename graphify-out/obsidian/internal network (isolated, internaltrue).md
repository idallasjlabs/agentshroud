---
source_file: "docker-compose.secure.yml"
type: "code"
community: "agentshroud-gateway service (proxy mode)"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/agentshroud-gateway_service_proxy_mode
---

# internal network (isolated, internal:true)

## Connections
- [[agentshroud-gateway service (proxy mode)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (proxy mode, internal-only network)]] - `shares_data_with` [EXTRACTED]
- [[wazuh service (proxy-mode HIDS sidecar)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/agentshroud-gateway_service_proxy_mode
