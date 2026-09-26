---
type: community
cohesion: 0.18
members: 11
---

# ADR-007: Zero-Config Security (docker-compose up

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[MCP Proxy]] - concept - docs/architecture/system-architecture.md
- [[MCP Server Integration Guide]] - document - docs/api/integration-guide.md
- [[Op-Proxy (Credential Gateway)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[Proxy Layer_1]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[SSH Proxy]] - concept - docs/architecture/system-architecture.md
- [[Web Proxy]] - concept - docs/architecture/system-architecture.md
- [[http_proxy.py (HTTP CONNECT 8181, domain allowlist)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[mcp-config.yml]] - code - docs/data/schema-documentation.md
- [[mcp_proxy.py (MCP tool call gate)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[ssh_proxy (approved hosts only)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[web_proxy.py (domain allowlist engine)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ADR-007_Zero-Config_Security_docker-compose_up
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_container-net-diag.sh]]
- 1 edge to [[_COMMUNITY_test_claude_via_openai_path.py]]
- 1 edge to [[_COMMUNITY_Mode A — Single task]]

## Top bridge nodes
- [[MCP Proxy]] - degree 4, connects to 1 community
- [[SSH Proxy]] - degree 2, connects to 1 community
- [[Op-Proxy (Credential Gateway)]] - degree 2, connects to 1 community