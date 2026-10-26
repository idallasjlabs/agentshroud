---
source_file: "docker-compose.secure.yml"
type: "code"
community: "Community 636"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_636
---

# internal network (isolated, internal:true)

## Connections
- [[openclaw service (proxy mode, internal-only network)]] - `shares_data_with` [EXTRACTED]
- [[wazuh service (proxy-mode HIDS sidecar)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_636