---
type: community
cohesion: 0.21
members: 13
---

# AgentShroud (system, C4 context)

**Cohesion:** 0.21 - loosely connected
**Members:** 13 nodes

## Members
- [[1Password (credential vault)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[1Password Integration (service account)]] - document - docs/api/integration-guide.md
- [[AgentShroud (system, C4 context)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[AgentShroud Bot Container (Node.js 22OpenClaw 18789)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[Anthropic API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Brave Search API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[External Collaborators]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Gateway Container (Python 3.11FastAPI 8080)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[GitHub (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Isaiah Jefferson (ArchitectOwner)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[OpenAI API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Running Containers (gateway + bot, healthy)]] - image - docs/diagrams/images/diagram-06-cicd-deployment.svg
- [[Telegram (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_system_C4_context
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ADR-008 Progressive Trust Level System]]
- 1 edge to [[_COMMUNITY_ADR-001 Transparent Proxy Decision]]
- 1 edge to [[_COMMUNITY_ADR-006 Multi-Runtime Container Support]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]

## Top bridge nodes
- [[Gateway Container (Python 3.11FastAPI 8080)]] - degree 9, connects to 3 communities
- [[AgentShroud (system, C4 context)]] - degree 9, connects to 1 community
