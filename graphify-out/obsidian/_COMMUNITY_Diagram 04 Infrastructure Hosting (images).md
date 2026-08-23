---
type: community
cohesion: 0.29
members: 7
---

# Diagram 04 Infrastructure Hosting (images)

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[Docker Compose (infra diagram)]] - image - docs/diagrams/images/diagram-04-infrastructure-hosting.svg
- [[Docker Secrets (infra diagram)]] - image - docs/diagrams/images/diagram-04-infrastructure-hosting.svg
- [[Docker Secrets Management (deployment doc)]] - concept - docs/architecture/deployment-diagram.md
- [[Docker Secrets Structure (runsecrets)]] - concept - docs/data/schema-documentation.md
- [[Named Docker Volumes]] - image - docs/diagrams/images/diagram-04-infrastructure-hosting.svg
- [[agentshroud-internal network (172.20.0.016)]] - image - docs/diagrams/images/diagram-04-infrastructure-hosting.svg
- [[agentshroud-isolated network (172.21.0.016)]] - image - docs/diagrams/images/diagram-04-infrastructure-hosting.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Diagram_04_Infrastructure_Hosting_images
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Adr 003 Two Network (adr)]]

## Top bridge nodes
- [[agentshroud-isolated network (172.21.0.016)]] - degree 2, connects to 1 community