---
source_file: "docker-compose.secure.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
location: "L111-118"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# agentshroud-internal network (no external access)

## Connections
- [[MCP servers confined to the internal network]] - `rationale_for` [EXTRACTED]
- [[agentshroud-gateway service (proxy mode)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (internal network only)]] - `shares_data_with` [EXTRACTED]
- [[wazuh-agent sidecar (pinned 4.14.7)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod