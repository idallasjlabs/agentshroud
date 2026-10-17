---
type: community
members: 9
---

# AgentShroud (system, C4 context) (3)

**Members:** 9 nodes

## Members
- [[ADR-001 Transparent Proxy Decision]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[ADR-004 Proxy-Side API Key Management]] - concept - docs/architecture/adr/ADR-004-api-keys-never-in-agent-container.md
- [[Agent Modification Approach (rejected alternative)]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[Deployment Modes_1]] - document - docs/architecture/deployment-diagram.md
- [[Gateway (FastAPI)]] - concept - docs/architecture/system-architecture.md
- [[PII Sanitizer (Presidio + Regex)]] - concept - docs/architecture/system-architecture.md
- [[Proxy Mode (Recommended)_1]] - document - docs/architecture/deployment-diagram.md
- [[Sidecar Mode (Performance Optimized)]] - document - docs/architecture/deployment-diagram.md
- [[sanitizer.py (PII redaction, Presidioregex)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_system_C4_context_3
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Deployment Architecture]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context)]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]

## Top bridge nodes
- [[Gateway (FastAPI)]] - degree 4, connects to 1 community
- [[Deployment Modes_1]] - degree 3, connects to 1 community
- [[PII Sanitizer (Presidio + Regex)]] - degree 3, connects to 1 community
