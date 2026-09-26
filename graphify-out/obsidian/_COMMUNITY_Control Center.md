---
type: community
cohesion: 0.33
members: 6
---

# Control Center

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[1password_service_account Docker secret]] - concept - docs/diagrams/images/diagram-22-dependency-graph.svg
- [[agentshroud-bot container (starts after gateway healthy)]] - concept - docs/diagrams/images/diagram-22-dependency-graph.svg
- [[agentshroud-gateway container (starts first)]] - concept - docs/diagrams/images/diagram-22-dependency-graph.svg
- [[docker-agentshroud image (FROM node22-bookworm-slim)]] - concept - docs/diagrams/images/diagram-22-dependency-graph.svg
- [[docker-gateway image (FROM python3.11-slim, gatewayDockerfile)]] - concept - docs/diagrams/images/diagram-22-dependency-graph.svg
- [[gateway_password.txt Docker secret]] - concept - docs/diagrams/images/diagram-22-dependency-graph.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Control_Center
SORT file.name ASC
```
