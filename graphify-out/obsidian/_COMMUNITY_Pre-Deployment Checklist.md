---
type: community
cohesion: 0.13
members: 15
---

# Pre-Deployment Checklist

**Cohesion:** 0.13 - loosely connected
**Members:** 15 nodes

## Members
- [[11 Cron Jobs]] - document - docs/architecture/agentic-os.md
- [[11. Automated Operations]] - document - docs/architecture/agentic-os.md
- [[Approval Queue (human-in-the-loop)]] - concept - docs/architecture/agentic-os.md
- [[Blocked by default (private RFC1918 ranges)]] - image - docs/diagrams/images/diagram-05-network-topology.svg
- [[DNS Filter]] - concept - docs/architecture/system-architecture.md
- [[Egress Monitor]] - concept - docs/architecture/system-architecture.md
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - document - docs/api/api-reference.md
- [[InspectionResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[OpenClaw Integration Guide (v0.9.0)]] - document - docs/api/integration-guide.md
- [[SOC Dashboard]] - document - docs/architecture/agentic-os.md
- [[SecurityFinding (data entity)]] - concept - docs/data/data-dictionary.md
- [[URLAnalysisResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[egress-config.yml]] - code - docs/data/schema-documentation.md
- [[gatewaysocrouter.py (SOC Shared Command Layer)]] - code - docs/api/api-reference.md
- [[gatewaywebapi.py (Web control center)]] - code - docs/api/api-reference.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Pre-Deployment_Checklist
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY_AgentShroud Color Palette]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]
- 1 edge to [[_COMMUNITY_Proxy Layer]]

## Top bridge nodes
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - degree 7, connects to 3 communities
- [[11. Automated Operations]] - degree 3, connects to 1 community
- [[Approval Queue (human-in-the-loop)]] - degree 2, connects to 1 community
