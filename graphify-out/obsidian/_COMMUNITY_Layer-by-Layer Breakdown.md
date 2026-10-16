---
type: community
cohesion: 0.06
members: 35
---

# Layer-by-Layer Breakdown

**Cohesion:** 0.06 - loosely connected
**Members:** 35 nodes

## Members
- [[1. Container Isolation]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[1. MCP Proxy Wrapper (Bot Side)]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[10. Approval Queue]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[11. Ledger Recording]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[2. Authentication (Gateway Entry)]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[2. Capability Dropping]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[3. Middleware Manager]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[3. Resource Limits]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[4. Input Normalization]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[5. Audit Ledger]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[5. PII Sanitization]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[6. Prompt Injection Defense]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[7. Secrets Management]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[8. Bot Identity Separation]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[9. Proxy Routing]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Approval Queue (human gate)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Data Flow_1]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[EnhancedApprovalQueue (`enhanced_queue.py`)]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Environment Variables Used]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Key Class `EnhancedApprovalQueue`]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Layer-by-Layer Breakdown]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Overview_3]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Persistence]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Purpose_68]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Related Notes_20]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Related Notes_21]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Request Flow Diagram]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Response Path]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Responsibilities]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Security Controls_1]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[Telegram API_1]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Timeout Behavior]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Tool Risk Tiers]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[WebSocket Notifications]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[approval_queue.py]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Layer-by-Layer_Breakdown
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Architecture]]
- 1 edge to [[_COMMUNITY_main.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_`SecurityPipeline`]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_34 Security Modules Pipeline (P0-P3)]]
- 1 edge to [[_COMMUNITY_hermesSOUL]]
- 1 edge to [[_COMMUNITY_Container Security Policy — AgentShroud]]

## Top bridge nodes
- [[approval_queue.py]] - degree 7, connects to 3 communities
- [[Layer-by-Layer Breakdown]] - degree 13, connects to 2 communities
- [[Security Controls_1]] - degree 10, connects to 2 communities
- [[Data Flow_1]] - degree 6, connects to 1 community
- [[Approval Queue (human gate)]] - degree 3, connects to 1 community
