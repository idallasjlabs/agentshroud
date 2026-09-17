---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.svg"
type: "concept"
community: "agentshroud-gateway container (starts first)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/agentshroud-gateway_container_starts_first
---

# agentshroud-bot container (starts after gateway healthy)

## Connections
- [[agentshroud-gateway container (starts first)]] - `calls` [EXTRACTED]
- [[docker-agentshroud image (FROM node22-bookworm-slim)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/agentshroud-gateway_container_starts_first