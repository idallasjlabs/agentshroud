---
type: community
cohesion: 0.07
members: 29
---

# EgressFilter

**Cohesion:** 0.07 - loosely connected
**Members:** 29 nodes

## Members
- [[1. MCP Proxy Wrapper (Bot Side)]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[11. Ledger Recording]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[2. Authentication (Gateway Entry)]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[3. Middleware Manager]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[4. Input Normalization]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[5. PII Sanitization]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[6. Prompt Injection Defense]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[9. Proxy Routing]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Configuration_3]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Data Flow_1]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[EgressFilter_3]] - concept - docker/config/hermes/SOUL.md
- [[EgressFilter._is_private_ip(host)]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[EgressFilter._record(agent_id, dest, port, action, rule)]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[EgressFilter.check(agent_id, destination, port)]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[EgressPolicy.matches_domain(domain)]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Environment Variables_2]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Function Details]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Key Classes  Functions]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Layer-by-Layer Breakdown]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Mode Enforce vs Monitor]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Overview_12]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Purpose_71]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Related]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Related Notes_30]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Request Flow Diagram]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Response Path]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Responsibilities_1]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[Threat Model_1]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md
- [[egress_filter.py]] - document - docs/vault/02 - Modules/Security Modules/egress_filter.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilter
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_system-requirements]]
- 1 edge to [[_COMMUNITY_main.py]]
- 1 edge to [[_COMMUNITY_`SecurityPipeline`]]
- 1 edge to [[_COMMUNITY_Security Controls]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_hermesSOUL]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.8.0 Watchtower — Execution Summary (Draft)]]

## Top bridge nodes
- [[EgressFilter_3]] - degree 16, connects to 3 communities
- [[Layer-by-Layer Breakdown]] - degree 13, connects to 3 communities
- [[Data Flow_1]] - degree 6, connects to 1 community
