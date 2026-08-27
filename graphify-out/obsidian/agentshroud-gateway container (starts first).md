---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.svg"
type: "concept"
community: "Community 1106"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Community_1106
---

# agentshroud-gateway container (starts first)

## Connections
- [[1password_service_account Docker secret]] - `shares_data_with` [EXTRACTED]
- [[agentshroud-bot container (starts after gateway healthy)]] - `calls` [EXTRACTED]
- [[docker-gateway image (FROM python3.11-slim, gatewayDockerfile)]] - `calls` [EXTRACTED]
- [[gateway_password.txt Docker secret]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Community_1106