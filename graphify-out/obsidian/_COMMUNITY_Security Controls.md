---
type: community
cohesion: 0.12
members: 16
---

# Security Controls

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[1. Container Isolation]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[10. Approval Queue]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[2. Capability Dropping]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[2. Network Isolation]] - document - docs/security/container-policy.md
- [[2.1 Docker Networks]] - document - docs/security/container-policy.md
- [[2.2 Exposed Ports]] - document - docs/security/container-policy.md
- [[2.3 Tailscale Network]] - document - docs/security/container-policy.md
- [[3. Resource Limits]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[5. Audit Ledger]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[6. DNS Filter]] - document - docs/security/security-architecture.md
- [[7. Secrets Management]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[7. TLS Termination and Inspection]] - document - docs/security/security-architecture.md
- [[8. Bot Identity Separation]] - document - docs/security/SECURITY_ARCHITECTURE.md
- [[8. Network Rate Limiter]] - document - docs/security/security-architecture.md
- [[Layer 2 Network Security (4 Modules)]] - document - docs/security/security-architecture.md
- [[Security Controls_2]] - document - docs/security/SECURITY_ARCHITECTURE.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Controls
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Security Architecture]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_Security Module Inventory]]
- 1 edge to [[_COMMUNITY_Container Security Policy — AgentShroud]]
- 1 edge to [[_COMMUNITY_Layer-by-Layer Breakdown]]

## Top bridge nodes
- [[Security Controls_2]] - degree 10, connects to 2 communities
- [[2. Network Isolation]] - degree 6, connects to 1 community
- [[Layer 2 Network Security (4 Modules)]] - degree 5, connects to 1 community
- [[10. Approval Queue]] - degree 2, connects to 1 community