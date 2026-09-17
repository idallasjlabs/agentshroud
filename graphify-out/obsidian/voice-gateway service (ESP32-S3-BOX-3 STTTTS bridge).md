---
source_file: "docker/docker-compose.yml"
type: "code"
community: "gateway service (prod, sole egress point, 75-mod"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# voice-gateway service (ESP32-S3-BOX-3 STT/TTS bridge)

## Connections
- [[agentshroud-internal network (EDGE tier, internet-facing)]] - `shares_data_with` [EXTRACTED]
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - `shares_data_with` [EXTRACTED]
- [[voice-gateway override (port 8766 — avoids prod SSH-forwarder port race)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod