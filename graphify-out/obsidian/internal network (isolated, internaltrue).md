---
source_file: "docker-compose.secure.yml"
type: "code"
community: "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Required__45_for_text__30_for_UI_elements
---

# internal network (isolated, internal:true)

## Connections
- [[agentshroud-gateway service (proxy mode)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (proxy mode, internal-only network)]] - `shares_data_with` [EXTRACTED]
- [[wazuh service (proxy-mode HIDS sidecar)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Required__45_for_text__30_for_UI_elements
