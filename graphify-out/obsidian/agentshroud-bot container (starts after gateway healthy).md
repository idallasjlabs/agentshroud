---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.svg"
type: "concept"
community: "Control Center"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Control_Center
---

# agentshroud-bot container (starts after gateway healthy)

## Connections
- [[agentshroud-gateway container (starts first)]] - `calls` [EXTRACTED]
- [[docker-agentshroud image (FROM node22-bookworm-slim)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Control_Center