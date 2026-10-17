---
type: community
members: 18
---

# ADR-009: Enforce-by-Default Security Philosophy

**Members:** 18 nodes

## Members
- [[ADR-002 Default-Allow with Comprehensive Logging]] - concept - docs/architecture/adr/ADR-002-default-allow-security-philosophy.md
- [[ADR-009-enforce-by-default]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[ADR-009 Enforce-by-Default Security Philosophy]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Compliance Alignment (9 standards)]] - concept - docs/architecture/agentic-os.md
- [[Configuration_10]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Consequences_2]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Context_4]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Decision_4]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Migration from ADR-002]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Negative Consequences_1]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Policy Table]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Positive Consequences_1]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Related_5]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[Security Modules (30+, gateway diagram)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[SecurityPipeline (75 modules, 7 layers)]] - concept - docs/architecture/agentic-os.md
- [[Status_4]] - document - docs/architecture/adr/ADR-009-enforce-by-default.md
- [[prompt_guard (prompt injection)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[trust_manager (trust levels)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ADR-009_Enforce-by-Default_Security_Philosophy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]
- 1 edge to [[_COMMUNITY_TrustManager]]

## Top bridge nodes
- [[SecurityPipeline (75 modules, 7 layers)]] - degree 4, connects to 1 community
- [[trust_manager (trust levels)]] - degree 2, connects to 1 community
