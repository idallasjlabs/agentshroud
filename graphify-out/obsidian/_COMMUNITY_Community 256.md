---
type: community
cohesion: 0.07
members: 31
---

# Community 256

**Cohesion:** 0.07 - loosely connected
**Members:** 31 nodes

## Members
- [[ADR-008 Progressive Trust Level System]] - concept - docs/architecture/adr/ADR-008-progressive-trust-levels.md
- [[Approval DB (SQLiteaiosqlite)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[Approval Queue (SQLite)]] - concept - docs/architecture/system-architecture.md
- [[Approval Queue (gateway diagram)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[ApprovalRequest (data entity)]] - concept - docs/data/data-dictionary.md
- [[Configuration (TrustConfig)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Dashboard (WebSocket)]] - concept - docs/architecture/system-architecture.md
- [[Database Schema]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Default Action Trust Requirements]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Environment Variables_2]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Function Details]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Key Classes  Functions]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Kill Switch (MonitorBlockIsolate)]] - concept - docs/architecture/system-architecture.md
- [[Mode Enforce vs Monitor]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Monitoring System Integration (WebhooksPrometheus)]] - document - docs/api/integration-guide.md
- [[Purpose_118]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[RateLimitBucket (data entity)]] - concept - docs/data/data-dictionary.md
- [[Related]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Responsibilities_2]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Threat Model_1]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustLevel (data entity)]] - concept - docs/data/data-dictionary.md
- [[TrustManager_4]] - concept - docker/config/hermes/SOUL.md
- [[TrustManager._apply_decay(score, last_action_time)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager._update_score(agent_id, delta, event_type, details)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.get_history(agent_id, limit)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.get_trust(agent_id)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.is_action_allowed(agent_id, action)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[agent_trust SQLite table]] - code - docs/data/schema-documentation.md
- [[agentshroud.yaml (main config schema)]] - code - docs/data/schema-documentation.md
- [[approval_requests SQLite table]] - code - docs/data/schema-documentation.md
- [[trust_manager.py]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_256
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 217]]
- 1 edge to [[_COMMUNITY_Community 357]]
- 1 edge to [[_COMMUNITY_Community 499]]
- 1 edge to [[_COMMUNITY_Community 420]]

## Top bridge nodes
- [[TrustManager_4]] - degree 18, connects to 4 communities
- [[Approval DB (SQLiteaiosqlite)]] - degree 2, connects to 1 community