---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.svg"
type: "concept"
community: "Diagram 22 Dependency Graph (images)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Diagram_22_Dependency_Graph_images
---

# agentshroud-bot container (starts after gateway healthy)

## Connections
- [[agentshroud-gateway container (starts first)]] - `calls` [EXTRACTED]
- [[docker-agentshroud image (FROM node22-bookworm-slim)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Diagram_22_Dependency_Graph_images