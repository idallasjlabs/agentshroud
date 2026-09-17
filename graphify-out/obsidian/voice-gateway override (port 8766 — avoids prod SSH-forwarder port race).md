---
source_file: "docker/docker-compose.agentshroud-bot.marvin.yml"
type: "rationale"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# voice-gateway override (port 8766 — avoids prod SSH-forwarder port race)

## Connections
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge)]] - `shares_data_with` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod