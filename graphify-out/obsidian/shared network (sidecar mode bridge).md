---
source_file: "docker-compose.sidecar.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# shared network (sidecar mode bridge)

## Connections
- [[agentshroud-gateway service (sidecar mode, optional scan)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (sidecar mode, exposed normally)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod