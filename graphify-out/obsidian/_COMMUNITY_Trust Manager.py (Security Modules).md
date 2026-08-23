---
type: community
cohesion: 0.09
members: 23
---

# Trust Manager.py (Security Modules)

**Cohesion:** 0.09 - loosely connected
**Members:** 23 nodes

## Members
- [[Approval Queue (SQLite)]] - concept - docs/architecture/system-architecture.md
- [[Approval Queue (gateway diagram)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[Configuration (TrustConfig)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Dashboard (WebSocket)]] - concept - docs/architecture/system-architecture.md
- [[Database Schema_2]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Default Action Trust Requirements]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Environment Variables_16]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Function Details_50]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Key Classes  Functions_53]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Kill Switch (MonitorBlockIsolate)]] - concept - docs/architecture/system-architecture.md
- [[Mode Enforce vs Monitor_11]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Monitoring System Integration (WebhooksPrometheus)]] - document - docs/api/integration-guide.md
- [[Purpose_171]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Related_57]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Responsibilities_55]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[Threat Model_26]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager_5]] - concept - docker/config/hermes/SOUL.md
- [[TrustManager._apply_decay(score, last_action_time)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager._update_score(agent_id, delta, event_type, details)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.get_history(agent_id, limit)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.get_trust(agent_id)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[TrustManager.is_action_allowed(agent_id, action)]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md
- [[trust_manager.py_1]] - document - docs/vault/02 - Modules/Security Modules/trust_manager.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Trust_Managerpy_Security_Modules
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Soul (hermes)]]
- 1 edge to [[_COMMUNITY_Diagram 01 C4 Context (images)]]
- 1 edge to [[_COMMUNITY_Diagram 03 Gateway Components (images)]]
- 1 edge to [[_COMMUNITY_Adr 009 Enforce By (adr)]]
- 1 edge to [[_COMMUNITY_Diagram 07 Data Flow (images)]]

## Top bridge nodes
- [[TrustManager_5]] - degree 18, connects to 5 communities