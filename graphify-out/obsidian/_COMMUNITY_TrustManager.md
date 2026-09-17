---
type: community
cohesion: 0.09
members: 23
---

# TrustManager

**Cohesion:** 0.09 - loosely connected
**Members:** 23 nodes

## Members
- [[Approval Queue (SQLite)]] - concept - docs/architecture/system-architecture.md
- [[Approval Queue (gateway diagram)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
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
- [[Related]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Responsibilities_1]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Threat Model_1]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager_4]] - concept - docker/config/hermes/SOUL.md
- [[TrustManager._apply_decay(score, last_action_time)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager._update_score(agent_id, delta, event_type, details)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.get_history(agent_id, limit)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.get_trust(agent_id)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.is_action_allowed(agent_id, action)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[trust_manager.py]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustManager
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_hermesSOUL]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context)]]
- 1 edge to [[_COMMUNITY_Gateway ManagementControl-Plane API (v1.3.0)]]
- 1 edge to [[_COMMUNITY_ADR-009 Enforce-by-Default Security Philosophy]]

## Top bridge nodes
- [[TrustManager_4]] - degree 18, connects to 5 communities