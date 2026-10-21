---
source_file: "docker-compose.secure.yml"
type: "code"
community: "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
location: "L23-58"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Required__45_for_text__30_for_UI_elements
---

# agentshroud-gateway service (proxy mode)

## Connections
- [[Proxy mode — full network isolation + egress control]] - `implements` [EXTRACTED]
- [[agentshroud-external network]] - `shares_data_with` [EXTRACTED]
- [[agentshroud-internal network (no external access)]] - `shares_data_with` [EXTRACTED]
- [[external network (gateway host-facing bridge)]] - `shares_data_with` [EXTRACTED]
- [[internal network (isolated, internaltrue)]] - `shares_data_with` [EXTRACTED]
- [[openclaw service (internal network only)]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Required__45_for_text__30_for_UI_elements
