---
source_file: "docker/scripts/gateway-start.sh"
type: "code"
community: "run-standalone.sh"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run-standalonesh
---

# gateway-start.sh entrypoint

## Connections
- [[gateway service (sole egress, FalcoClamAV in-process)]] - `shares_data_with` [EXTRACTED]
- [[security-entrypoint.sh boot scan flow]] - `calls` [EXTRACTED]
- [[wazuh-agent sidecar]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run-standalonesh
