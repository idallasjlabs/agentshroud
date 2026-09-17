---
source_file: "docker/docker-compose.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# docker-socket-proxy service (scoped, no image-pull, digest-pinned)

## Connections
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - `shares_data_with` [EXTRACTED]
- [[hermes service (prod, profiles hermesfull — service block is dead code, see run-standalone.sh)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (prod, isolated network only)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod