---
type: community
members: 21
---

# ADR-005: SHA-256 Hash Chain Audit Integrity

**Members:** 21 nodes

## Members
- [[Blocked by default (private RFC1918 ranges)]] - image - docs/diagrams/images/diagram-05-network-topology.svg
- [[DNS Filter]] - concept - docs/architecture/system-architecture.md
- [[Egress Monitor]] - concept - docs/architecture/system-architecture.md
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - document - docs/api/api-reference.md
- [[InspectionResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[MCP Proxy]] - concept - docs/architecture/system-architecture.md
- [[MCP Server Integration Guide]] - document - docs/api/integration-guide.md
- [[Op-Proxy (Credential Gateway)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[OpenClaw Integration Guide (v0.9.0)]] - document - docs/api/integration-guide.md
- [[Proxy Layer_1]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[SSH Proxy]] - concept - docs/architecture/system-architecture.md
- [[SecurityFinding (data entity)]] - concept - docs/data/data-dictionary.md
- [[URLAnalysisResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[Web Proxy]] - concept - docs/architecture/system-architecture.md
- [[egress-config.yml]] - code - docs/data/schema-documentation.md
- [[gatewaywebapi.py (Web control center)]] - code - docs/api/api-reference.md
- [[http_proxy.py (HTTP CONNECT 8181, domain allowlist)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[mcp-config.yml]] - code - docs/data/schema-documentation.md
- [[mcp_proxy.py (MCP tool call gate)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[ssh_proxy (approved hosts only)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[web_proxy.py (domain allowlist engine)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ADR-005_SHA-256_Hash_Chain_Audit_Integrity
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_ADR-009 Enforce-by-Default Security Philosophy]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context) (3)]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity (2)]]

## Top bridge nodes
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - degree 7, connects to 3 communities
- [[MCP Proxy]] - degree 4, connects to 1 community
- [[SSH Proxy]] - degree 2, connects to 1 community
