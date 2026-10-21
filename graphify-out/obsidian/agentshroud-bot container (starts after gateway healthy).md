---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.svg"
type: "concept"
community: "AgentShroud Incident Response Plan (2)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AgentShroud_Incident_Response_Plan_2
---

# agentshroud-bot container (starts after gateway healthy)

## Connections
- [[agentshroud-gateway container (starts first)]] - `calls` [EXTRACTED]
- [[docker-agentshroud image (FROM node22-bookworm-slim)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/AgentShroud_Incident_Response_Plan_2
