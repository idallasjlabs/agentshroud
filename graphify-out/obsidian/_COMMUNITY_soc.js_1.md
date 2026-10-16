---
type: community
cohesion: 0.40
members: 6
---

# soc.js

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Members
- [[dot-to_dict()_5]] - code - gateway/security/soc_correlation.py
- [[Any_12]] - code - gateway/security/soc_correlation.py
- [[CorrelationSummary]] - code - gateway/security/soc_correlation.py
- [[_renderCorrelation()]] - code - gateway/soc/static/soc.js
- [[build_correlation_summary()]] - code - gateway/security/soc_correlation.py
- [[soc_correlation.py]] - code - gateway/security/soc_correlation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/socjs
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_soc.js]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_migrate-cve-registry-ghsa.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[build_correlation_summary()]] - degree 10, connects to 4 communities
- [[CorrelationSummary]] - degree 5, connects to 1 community
- [[_renderCorrelation()]] - degree 3, connects to 1 community
