---
source_file: "docker/docker-compose.yml"
type: "code"
community: "docker/docker-compose.yml"
location: "docker/docker-compose.yml:658"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/docker-composeyml
---

# agentshroud-internal network (edge tier, internet-facing)

## Connections
- [[gateway service (docker-compose.yml)]] - `shares_data_with` [EXTRACTED]
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docker/docker-composeyml