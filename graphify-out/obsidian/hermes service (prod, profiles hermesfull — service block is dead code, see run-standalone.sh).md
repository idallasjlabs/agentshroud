---
source_file: "docker/docker-compose.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# hermes service (prod, profiles hermes/full — service block is dead code, see run-standalone.sh)

## Connections
- [[agentshroud-isolated network (DMZ tier, internaltrue)]] - `shares_data_with` [EXTRACTED]
- [[docker-socket-proxy service (scoped, no image-pull, digest-pinned)]] - `shares_data_with` [EXTRACTED]
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - `shares_data_with` [EXTRACTED]
- [[hermes override (marvin dev host, dashboard port 9119)]] - `shares_data_with` [EXTRACTED]
- [[init-config.sh (Hermes first-boot config materialisation)]] - `shares_data_with` [INFERRED]
- [[run-standalone.sh — launches Hermes via `docker run`, bypassing compose restart-storm bug]] - `semantically_similar_to` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod