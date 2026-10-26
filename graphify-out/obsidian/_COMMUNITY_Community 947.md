---
type: community
members: 22
---

# Community 947

**Members:** 22 nodes

## Members
- [[ADR-001 Transparent Proxy Decision]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[ADR-004 Proxy-Side API Key Management]] - concept - docs/architecture/adr/ADR-004-api-keys-never-in-agent-container.md
- [[Agent Modification Approach (rejected alternative)]] - concept - docs/architecture/adr/ADR-001-transparent-proxy-vs-agent-modification.md
- [[Audit Ledger (SHA-256 hash only)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Deployment Modes]] - document - docs/architecture/deployment-diagram.md
- [[Gateway (FastAPI)]] - concept - docs/architecture/system-architecture.md
- [[MCP Proxy]] - concept - docs/architecture/system-architecture.md
- [[MCP Server Integration Guide]] - document - docs/api/integration-guide.md
- [[Op-Proxy (Credential Gateway)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[PII Sanitizer (Presidio + Regex)]] - concept - docs/architecture/system-architecture.md
- [[Proxy Layer_1]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[Proxy Mode (Recommended)]] - document - docs/architecture/deployment-diagram.md
- [[SSH Proxy]] - concept - docs/architecture/system-architecture.md
- [[Sidecar Mode (Performance Optimized)]] - document - docs/architecture/deployment-diagram.md
- [[Web Proxy]] - concept - docs/architecture/system-architecture.md
- [[http_proxy.py (HTTP CONNECT 8181, domain allowlist)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[ledger.db (90-day retention)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[mcp-config.yml]] - code - docs/data/schema-documentation.md
- [[mcp_proxy.py (MCP tool call gate)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[sanitizer.py (PII redaction, Presidioregex)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[ssh_proxy (approved hosts only)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[web_proxy.py (domain allowlist engine)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_947
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 392]]
- 2 edges to [[_COMMUNITY_Community 487]]
- 1 edge to [[_COMMUNITY_Community 418]]
- 1 edge to [[_COMMUNITY_Community 630]]
- 1 edge to [[_COMMUNITY_Community 637]]
- 1 edge to [[_COMMUNITY_Community 747]]

## Top bridge nodes
- [[Audit Ledger (SHA-256 hash only)]] - degree 7, connects to 3 communities
- [[Gateway (FastAPI)]] - degree 4, connects to 1 community
- [[MCP Proxy]] - degree 4, connects to 1 community
- [[Deployment Modes]] - degree 3, connects to 1 community
- [[Op-Proxy (Credential Gateway)]] - degree 2, connects to 1 community