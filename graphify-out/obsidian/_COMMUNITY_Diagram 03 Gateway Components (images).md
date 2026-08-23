---
type: community
cohesion: 0.22
members: 9
---

# Diagram 03 Gateway Components (images)

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[MCP Proxy]] - concept - docs/architecture/system-architecture.md
- [[MCP Server Integration Guide]] - document - docs/api/integration-guide.md
- [[Op-Proxy (Credential Gateway)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[Proxy Layer_1]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[Web Proxy]] - concept - docs/architecture/system-architecture.md
- [[http_proxy.py (HTTP CONNECT 8181, domain allowlist)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[mcp-config.yml]] - code - docs/data/schema-documentation.md
- [[mcp_proxy.py (MCP tool call gate)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[web_proxy.py (domain allowlist engine)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Diagram_03_Gateway_Components_images
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Trust Manager.py (Security Modules)]]
- 1 edge to [[_COMMUNITY_Adr 005 Sha256 Hash (adr)]]
- 1 edge to [[_COMMUNITY_Diagram 07 Data Flow (images)]]

## Top bridge nodes
- [[Proxy Layer_1]] - degree 5, connects to 1 community
- [[MCP Proxy]] - degree 4, connects to 1 community
- [[Op-Proxy (Credential Gateway)]] - degree 2, connects to 1 community