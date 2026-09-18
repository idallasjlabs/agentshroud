---
source_file: "docker/docker-compose.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# openclaw service (prod, isolated network only)

## Connections
- [[agentshroud-isolated network (DMZ tier, internaltrue)]] - `shares_data_with` [EXTRACTED]
- [[docker-socket-proxy service (scoped, no image-pull, digest-pinned)]] - `shares_data_with` [EXTRACTED]
- [[openclaw override (marvin dev host, port 18790)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (proxy mode, internal-only network)]] - `semantically_similar_to` [INFERRED]
- [[openclaw service (sidecar mode, exposed normally)]] - `semantically_similar_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod