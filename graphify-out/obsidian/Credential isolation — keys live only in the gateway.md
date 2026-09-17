---
source_file: "docker-compose.secure.yml"
type: "rationale"
community: "gateway service (prod, sole egress point, 75-mod"
location: "L42-45, L77"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# Credential isolation — keys live only in the gateway

## Connections
- [[direnv-based environment variable management]] - `semantically_similar_to` [INFERRED]
- [[openclaw service (internal network only)]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod