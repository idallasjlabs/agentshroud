---
type: community
members: 9
---

# Community 864

**Members:** 9 nodes

## Members
- [[ADR-001 Transparent Proxy Decision]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[ADR-004 Proxy-Side API Key Management]] - concept - docs/architecture/adr/ADR-004-api-keys-never-in-agent-container.md
- [[Agent Modification Approach (rejected alternative)]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[Deployment Modes]] - document - docs/architecture/deployment-diagram.md
- [[Gateway (FastAPI)]] - concept - docs/architecture/system-architecture.md
- [[PII Sanitizer (Presidio + Regex)]] - concept - docs/architecture/system-architecture.md
- [[Proxy Mode (Recommended)]] - document - docs/architecture/deployment-diagram.md
- [[Sidecar Mode (Performance Optimized)]] - document - docs/architecture/deployment-diagram.md
- [[sanitizer.py (PII redaction, Presidioregex)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_864
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 238]]
- 1 edge to [[_COMMUNITY_Community 407]]
- 1 edge to [[_COMMUNITY_Community 409]]

## Top bridge nodes
- [[Gateway (FastAPI)]] - degree 4, connects to 1 community
- [[Deployment Modes]] - degree 3, connects to 1 community
- [[PII Sanitizer (Presidio + Regex)]] - degree 3, connects to 1 community