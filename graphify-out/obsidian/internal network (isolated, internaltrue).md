---
source_file: "docker-compose.secure.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# internal network (isolated, internal:true)

## Connections
- [[agentshroud-gateway service (proxy mode)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (proxy mode, internal-only network)]] - `shares_data_with` [EXTRACTED]
- [[wazuh service (proxy-mode HIDS sidecar)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod