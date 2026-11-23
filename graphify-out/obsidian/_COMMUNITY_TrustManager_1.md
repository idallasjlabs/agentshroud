---
type: community
members: 17
---

# TrustManager

**Members:** 17 nodes

## Members
- [[ADR-008 Progressive Trust Level System]] - concept - docs/architecture/adr/ADR-008-progressive-trust-levels.md
- [[Approval DB (SQLiteaiosqlite)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[Approval Queue (SQLite)]] - concept - docs/architecture/system-architecture.md
- [[Approval Queue (gateway diagram)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[ApprovalRequest (data entity)]] - concept - docs/data/data-dictionary.md
- [[Dashboard (WebSocket)]] - concept - docs/architecture/system-architecture.md
- [[Kill Switch (MonitorBlockIsolate)]] - concept - docs/architecture/system-architecture.md
- [[Monitoring System Integration (WebhooksPrometheus)]] - document - docs/api/integration-guide.md
- [[RateLimitBucket (data entity)]] - concept - docs/data/data-dictionary.md
- [[Security Modules (30+, gateway diagram)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[TrustLevel (data entity)]] - concept - docs/data/data-dictionary.md
- [[TrustManager_1]] - concept - docker/config/hermes/SOUL.md
- [[agent_trust SQLite table]] - code - docs/data/schema-documentation.md
- [[agentshroud.yaml (main config schema)]] - code - docs/data/schema-documentation.md
- [[approval_requests SQLite table]] - code - docs/data/schema-documentation.md
- [[prompt_guard (prompt injection)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[trust_manager (trust levels)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustManager
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_hermesSOUL]]
- 1 edge to [[_COMMUNITY_Gateway ManagementControl-Plane API (v1.3.0)]]
- 1 edge to [[_COMMUNITY_Proxy Layer]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context)]]

## Top bridge nodes
- [[TrustManager_1]] - degree 6, connects to 3 communities
- [[Security Modules (30+, gateway diagram)]] - degree 3, connects to 1 community
- [[Approval DB (SQLiteaiosqlite)]] - degree 2, connects to 1 community
