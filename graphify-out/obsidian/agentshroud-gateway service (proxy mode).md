---
source_file: "docker-compose.secure.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
location: "L23-58"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# agentshroud-gateway service (proxy mode)

## Connections
- [[CI DAST scan job (Nuclei, self-hosted)]] - `references` [INFERRED]
- [[Proxy mode — full network isolation + egress control]] - `implements` [EXTRACTED]
- [[agentshroud-external network]] - `shares_data_with` [EXTRACTED]
- [[agentshroud-internal network (no external access)]] - `shares_data_with` [EXTRACTED]
- [[external network (gateway host-facing bridge)]] - `shares_data_with` [EXTRACTED]
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - `semantically_similar_to` [INFERRED]
- [[internal network (isolated, internaltrue)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (internal network only)]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod