---
type: community
cohesion: 0.07
members: 30
---

# Layer-by-Layer Breakdown

**Cohesion:** 0.07 - loosely connected
**Members:** 30 nodes

## Members
- [[1. Container Isolation]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[1. MCP Proxy Wrapper (Bot Side)]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[10. Approval Queue]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[11. Ledger Recording]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[2. Authentication (Gateway Entry)]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[2. Capability Dropping]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[2. Network Isolation]] - document - docs/security/container-policy.md
- [[2.1 Docker Networks]] - document - docs/security/container-policy.md
- [[2.2 Exposed Ports]] - document - docs/security/container-policy.md
- [[2.3 Tailscale Network]] - document - docs/security/container-policy.md
- [[3. Middleware Manager]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[3. Resource Limits]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[4. Input Normalization]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[5. Audit Ledger]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[5. PII Sanitization]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[6. DNS Filter]] - document - docs/security/security-architecture.md
- [[6. Prompt Injection Defense]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[7. Secrets Management]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[7. TLS Termination and Inspection]] - document - docs/security/security-architecture.md
- [[8. Bot Identity Separation]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[8. Network Rate Limiter]] - document - docs/security/security-architecture.md
- [[9. Proxy Routing]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Data Flow]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Layer 2 Network Security (4 Modules)]] - document - docs/security/security-architecture.md
- [[Layer-by-Layer Breakdown]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Overview_22]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Related Notes_45]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Request Flow Diagram]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Response Path]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Security Controls_2]] - document - docs/security/SECURITY_ARCHITECTURE.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Layer-by-Layer_Breakdown
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Architecture]]
- 1 edge to [[_COMMUNITY_Security Module Inventory]]
- 1 edge to [[_COMMUNITY_Container Security Policy — AgentShroud]]
- 1 edge to [[_COMMUNITY_main.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_`SecurityPipeline`]]

## Top bridge nodes
- [[Layer-by-Layer Breakdown]] - degree 13, connects to 3 communities
- [[Security Controls_2]] - degree 10, connects to 2 communities
- [[Data Flow]] - degree 6, connects to 1 community
- [[2. Network Isolation]] - degree 6, connects to 1 community
- [[Layer 2 Network Security (4 Modules)]] - degree 5, connects to 1 community
