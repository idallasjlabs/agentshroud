---
type: community
cohesion: 0.20
members: 10
---

# TestDashboardCookieAuth

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_dashboard_bad_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[.test_dashboard_bad_token_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[.test_dashboard_no_auth_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[.test_dashboard_token_sets_cookie_and_redirects()]] - code - gateway/tests/test_security_fixes.py
- [[Dashboard should set httpOnly cookie and redirect to clean URL]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with invalid cookie returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with no auth returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=valid sets cookie and redirects to dashboard]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=wrong returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[TestDashboardCookieAuth]] - code - gateway/tests/test_security_fixes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDashboardCookieAuth
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_test_e2e.py]]

## Top bridge nodes
- [[TestDashboardCookieAuth]] - degree 10, connects to 2 communities