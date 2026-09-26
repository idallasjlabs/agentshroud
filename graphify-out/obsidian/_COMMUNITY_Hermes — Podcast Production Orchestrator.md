---
type: community
cohesion: 0.50
members: 4
---

# Hermes — Podcast Production Orchestrator

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[Test status endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test basic status endpoint functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestStatusEndpoint]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Hermes__Podcast_Production_Orchestrator
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_InjectionSeverity]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]

## Top bridge nodes
- [[TestStatusEndpoint]] - degree 4, connects to 2 communities
- [[.test_status_endpoint()]] - degree 3, connects to 1 community