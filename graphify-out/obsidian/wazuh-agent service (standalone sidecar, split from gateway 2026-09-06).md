---
source_file: "docker/docker-compose.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# wazuh-agent service (standalone sidecar, split from gateway 2026-09-06)

## Connections
- [[Docker sidecar integrity — falcoclamavfluent-bit in-process, wazuh-agent standalone sidecar]] - `references` [EXTRACTED]
- [[agentshroud-isolated network (DMZ tier, internaltrue)]] - `shares_data_with` [EXTRACTED]
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - `references` [EXTRACTED]
- [[wazuh service (proxy-mode HIDS sidecar)]] - `semantically_similar_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod