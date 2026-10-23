---
source_file: "docker/docker-compose.yml"
type: "code"
community: "run-standalone.sh"
location: "L9"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run-standalonesh
---

# AgentShroud production compose stack

## Connections
- [[AgentShroud Infrastructure (own images reported in full)]] - `conceptually_related_to` [INFERRED]
- [[agentshroud-dmz network (IEC 62443 FR5 SL2)]] - `references` [EXTRACTED]
- [[agentshroud-isolated network (internal)]] - `references` [EXTRACTED]
- [[docker-socket-proxy (digest pinned)]] - `references` [EXTRACTED]
- [[falco-alerts  security-reports shared volumes]] - `references` [EXTRACTED]
- [[gateway service (sole egress, FalcoClamAV in-process)]] - `references` [EXTRACTED]
- [[hermes service (agentshroud-hermes-v2)]] - `references` [EXTRACTED]
- [[openclaw service]] - `references` [EXTRACTED]
- [[voice-gateway service]] - `references` [EXTRACTED]
- [[wazuh-agent sidecar]] - `references` [EXTRACTED]
- [[wazuh-manager service (4.14.8)]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run-standalonesh
