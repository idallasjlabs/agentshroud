---
type: community
cohesion: 0.13
members: 20
---

# AgentShroud (system, C4 context)

**Cohesion:** 0.13 - loosely connected
**Members:** 20 nodes

## Members
- [[1Password (credential vault)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[1Password Integration (service account)]] - document - docs/api/integration-guide.md
- [[ADR-001 Transparent Proxy Decision]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[ADR-004 Proxy-Side API Key Management]] - concept - docs/architecture/adr/ADR-004-api-keys-never-in-agent-container.md
- [[Agent Modification Approach (rejected alternative)]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[AgentShroud (system, C4 context)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[AgentShroud Bot Container (Node.js 22OpenClaw 18789)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[Anthropic API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Brave Search API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Deployment Modes_1]] - document - docs/architecture/deployment-diagram.md
- [[External Collaborators]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Gateway (FastAPI)]] - concept - docs/architecture/system-architecture.md
- [[Gateway Container (Python 3.11FastAPI 8080)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[GitHub (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Isaiah Jefferson (ArchitectOwner)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[OpenAI API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Proxy Mode (Recommended)_1]] - document - docs/architecture/deployment-diagram.md
- [[Running Containers (gateway + bot, healthy)]] - image - docs/diagrams/images/diagram-06-cicd-deployment.svg
- [[Sidecar Mode (Performance Optimized)]] - document - docs/architecture/deployment-diagram.md
- [[Telegram (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_system_C4_context
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Deployment Architecture]]
- 1 edge to [[_COMMUNITY_ADR-006 Multi-Runtime Container Support]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]

## Top bridge nodes
- [[Gateway Container (Python 3.11FastAPI 8080)]] - degree 9, connects to 2 communities
- [[AgentShroud (system, C4 context)]] - degree 9, connects to 1 community
- [[Gateway (FastAPI)]] - degree 4, connects to 1 community
- [[Deployment Modes_1]] - degree 3, connects to 1 community
