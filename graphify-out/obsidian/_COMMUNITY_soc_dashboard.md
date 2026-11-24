---
type: community
members: 6
---

# soc_dashboard

**Members:** 6 nodes

## Members
- [[Fallback minimal dashboard when template file is missing.]] - rationale - gateway/soc/router.py
- [[Request_4]] - code
- [[Serve the unified SOC web dashboard.]] - rationale - gateway/soc/router.py
- [[_minimal_dashboard_html()]] - code - gateway/soc/router.py
- [[soc_dashboard()]] - code - gateway/soc/router.py
- [[test_minimal_dashboard_html_contents()]] - code - gateway/tests/test_soc_router_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/soc_dashboard
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]

## Top bridge nodes
- [[soc_dashboard()]] - degree 5, connects to 1 community
- [[_minimal_dashboard_html()]] - degree 4, connects to 1 community
- [[test_minimal_dashboard_html_contents()]] - degree 2, connects to 1 community
