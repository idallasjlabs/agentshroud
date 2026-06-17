---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.svg"
type: "image"
community: "Module Group 112"
tags:
  - graphify/image
  - graphify/EXPLICIT
  - community/Module_Group_112
---

# HTTP_PROXY set? (http://gateway:8181)

## Connections
- [[Bot Makes Outbound Request (any HTTPS connection)]] - `flows_to` [EXPLICIT]
- [[Direct Connection (would bypass all controls) — NOT CONFIGURED]] - `flows_to` [EXPLICIT]
- [[HTTP CONNECT Tunnel — request to gateway8181]] - `flows_to` [EXPLICIT]

#graphify/image #graphify/EXPLICIT #community/Module_Group_112