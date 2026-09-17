---
source_file: "docker-compose.secure.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# openclaw service (proxy mode, internal-only network)

## Connections
- [[internal network (isolated, internaltrue)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (prod, isolated network only)]] - `semantically_similar_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod