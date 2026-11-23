---
type: community
members: 18
---

# Gateway Management/Control-Plane API (v1.3.0)

**Members:** 18 nodes

## Members
- [[11 Cron Jobs]] - document - docs/architecture/agentic-os.md
- [[11. Automated Operations]] - document - docs/architecture/agentic-os.md
- [[ADR-002 Default-Allow with Comprehensive Logging]] - concept - docs/architecture/adr/ADR-002-default-allow-security-philosophy.md
- [[Approval Queue (human-in-the-loop)]] - concept - docs/architecture/agentic-os.md
- [[Blocked by default (private RFC1918 ranges)]] - image - docs/diagrams/images/diagram-05-network-topology.svg
- [[Compliance Alignment (9 standards)]] - concept - docs/architecture/agentic-os.md
- [[DNS Filter]] - concept - docs/architecture/system-architecture.md
- [[Egress Monitor]] - concept - docs/architecture/system-architecture.md
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - document - docs/api/api-reference.md
- [[InspectionResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[OpenClaw Integration Guide (v0.9.0)]] - document - docs/api/integration-guide.md
- [[SOC Dashboard]] - document - docs/architecture/agentic-os.md
- [[SecurityFinding (data entity)]] - concept - docs/data/data-dictionary.md
- [[SecurityPipeline (75 modules, 7 layers)]] - concept - docs/architecture/agentic-os.md
- [[URLAnalysisResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[egress-config.yml]] - code - docs/data/schema-documentation.md
- [[gatewaysocrouter.py (SOC Shared Command Layer)]] - code - docs/api/api-reference.md
- [[gatewaywebapi.py (Web control center)]] - code - docs/api/api-reference.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gateway_Management/Control-Plane_API_v130
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Agentic OS]]
- 1 edge to [[_COMMUNITY_TrustManager_1]]
- 1 edge to [[_COMMUNITY_Proxy Layer]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]

## Top bridge nodes
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - degree 6, connects to 2 communities
- [[SecurityPipeline (75 modules, 7 layers)]] - degree 4, connects to 1 community
- [[11. Automated Operations]] - degree 3, connects to 1 community
