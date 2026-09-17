---
source_file: "docker-compose.secure.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# wazuh service (proxy-mode HIDS sidecar)

## Connections
- [[internal network (isolated, internaltrue)]] - `shares_data_with` [EXTRACTED]
- [[wazuh-agent service (standalone sidecar, split from gateway 2026-09-06)]] - `semantically_similar_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod