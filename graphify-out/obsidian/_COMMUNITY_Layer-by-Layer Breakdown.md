---
type: community
members: 25
---

# Layer-by-Layer Breakdown

**Members:** 25 nodes

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
- [[Data Flow]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Layer-by-Layer Breakdown]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Overview_12]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Related Notes_38]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Request Flow Diagram]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Response Path]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Security Controls_1]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[Telegram API_1]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[approval_queue.py]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Layer-by-Layer_Breakdown
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Architecture]]
- 1 edge to [[_COMMUNITY_Container Security Policy — AgentShroud]]
- 1 edge to [[_COMMUNITY_`SecurityPipeline`]]
- 1 edge to [[_COMMUNITY_hermesSOUL]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only) (2)]]
- 1 edge to [[_COMMUNITY_Slack Channel Setup (2)]]
- 1 edge to [[_COMMUNITY_main.py_1]]
- 1 edge to [[_COMMUNITY_EgressFilter]]

## Top bridge nodes
- [[approval_queue.py]] - degree 7, connects to 4 communities
- [[Layer-by-Layer Breakdown]] - degree 13, connects to 2 communities
- [[Security Controls_1]] - degree 10, connects to 2 communities
- [[Data Flow]] - degree 6, connects to 1 community
- [[Approval Queue (human gate)]] - degree 3, connects to 1 community
