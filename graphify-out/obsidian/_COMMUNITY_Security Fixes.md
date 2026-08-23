---
type: community
cohesion: 0.47
members: 6
---

# Security Fixes

**Cohesion:** 0.47 - moderately connected
**Members:** 6 nodes

## Members
- [[.test_ws_token_with_bad_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_token_with_valid_cookie()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_token_without_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[Dashboard ws-token endpoint returns token only for cookie-authed sessions]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardws-token with valid cookie returns token]] - rationale - gateway/tests/test_security_fixes.py
- [[TestDashboardWSToken]] - code - gateway/tests/test_security_fixes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Fixes
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 1 edge to [[_COMMUNITY_Ssh Write File Endpoint]]

## Top bridge nodes
- [[TestDashboardWSToken]] - degree 8, connects to 2 communities