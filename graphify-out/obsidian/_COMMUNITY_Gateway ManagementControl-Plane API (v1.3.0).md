---
type: community
cohesion: 0.08
members: 26
---

# Gateway Management/Control-Plane API (v1.3.0)

**Cohesion:** 0.08 - loosely connected
**Members:** 26 nodes

## Members
- [[11 Cron Jobs]] - document - docs/architecture/agentic-os.md
- [[11. Automated Operations]] - document - docs/architecture/agentic-os.md
- [[Approval Queue (human-in-the-loop)]] - concept - docs/architecture/agentic-os.md
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
- [[SOC Dashboard]] - document - docs/architecture/agentic-os.md
- [[SSH Proxy]] - concept - docs/architecture/system-architecture.md
- [[SecurityFinding (data entity)]] - concept - docs/data/data-dictionary.md
- [[URLAnalysisResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[Web Proxy]] - concept - docs/architecture/system-architecture.md
- [[egress-config.yml]] - code - docs/data/schema-documentation.md
- [[gatewaysocrouter.py (SOC Shared Command Layer)]] - code - docs/api/api-reference.md
- [[gatewaywebapi.py (Web control center)]] - code - docs/api/api-reference.md
- [[http_proxy.py (HTTP CONNECT 8181, domain allowlist)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[mcp-config.yml]] - code - docs/data/schema-documentation.md
- [[mcp_proxy.py (MCP tool call gate)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[ssh_proxy (approved hosts only)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[web_proxy.py (domain allowlist engine)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gateway_Management/Control-Plane_API_v130
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Agentic OS]]
- 1 edge to [[_COMMUNITY_ADR-009 Enforce-by-Default Security Philosophy]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]

## Top bridge nodes
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - degree 7, connects to 2 communities
- [[MCP Proxy]] - degree 4, connects to 1 community
- [[11. Automated Operations]] - degree 3, connects to 1 community
- [[Approval Queue (human-in-the-loop)]] - degree 2, connects to 1 community
- [[SSH Proxy]] - degree 2, connects to 1 community