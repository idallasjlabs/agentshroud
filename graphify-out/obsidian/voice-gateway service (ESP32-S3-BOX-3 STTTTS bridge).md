---
source_file: "docker/docker-compose.yml"
type: "code"
community: "docker/docker-compose.yml"
location: "docker/docker-compose.yml:510"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/docker-composeyml
---

# voice-gateway service (ESP32-S3-BOX-3 STT/TTS bridge)

## Connections
- [[agentshroud-internal network (edge tier, internet-facing)]] - `shares_data_with` [EXTRACTED]
- [[agentshroud-isolated network (DMZ tier, internaltrue)]] - `shares_data_with` [EXTRACTED]
- [[gateway POST emailsend-owner endpoint]] - `conceptually_related_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/docker/docker-composeyml