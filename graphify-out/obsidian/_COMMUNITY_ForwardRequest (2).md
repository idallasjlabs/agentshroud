---
type: community
members: 5
---

# ForwardRequest (2)

**Members:** 5 nodes

## Members
- [[dot-test_dashboard_cookie_auth_serves_html()]] - code - gateway/tests/test_security_fixes.py
- [[GET dashboard with valid cookie auth returns HTML.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboard with valid cookie serves HTML]] - rationale - gateway/tests/test_security_fixes.py
- [[test_dashboard_returns_html()]] - code - gateway/tests/test_e2e.py
- [[test_dashboard_serves_html()]] - code - gateway/tests/test_dashboard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ForwardRequest_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_dashboard.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]

## Top bridge nodes
- [[dot-test_dashboard_cookie_auth_serves_html()]] - degree 3, connects to 1 community
- [[test_dashboard_serves_html()]] - degree 2, connects to 1 community
- [[test_dashboard_returns_html()]] - degree 2, connects to 1 community
