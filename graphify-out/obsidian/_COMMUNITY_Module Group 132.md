---
type: community
cohesion: 0.05
members: 37
---

# Module Group 132

**Cohesion:** 0.05 - loosely connected
**Members:** 37 nodes

## Members
- [[.test_cookie_not_secure_on_http()]] - code - gateway/tests/test_security_fixes.py
- [[.test_dashboard_bad_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[.test_dashboard_bad_token_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[.test_dashboard_cookie_auth_serves_html()]] - code - gateway/tests/test_security_fixes.py
- [[.test_dashboard_no_auth_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[.test_dashboard_token_sets_cookie_and_redirects()]] - code - gateway/tests/test_security_fixes.py
- [[.test_json_api_has_cache_control()]] - code - gateway/tests/test_security_fixes.py
- [[.test_status_has_security_headers()]] - code - gateway/tests/test_security_fixes.py
- [[.test_status_returns_current_version()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_rejects_empty_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_rejects_master_token()]] - code - gateway/tests/test_security_fixes.py
- [[All API responses should include basic security headers.]] - rationale - gateway/tests/test_security_fixes.py
- [[ClientDisconnect mid-body-read must not crash the gateway process.]] - rationale - gateway/tests/test_security_fixes.py
- [[Cookie secure=False on HTTP requests]] - rationale - gateway/tests/test_security_fixes.py
- [[Dashboard cookie secure flag is dynamic based on request scheme]] - rationale - gateway/tests/test_security_fixes.py
- [[Dashboard should set httpOnly cookie and redirect to clean URL]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with invalid cookie returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with no auth returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with valid cookie serves HTML_1]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=valid sets cookie and redirects to dashboard]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=wrong returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET status should include security headers]] - rationale - gateway/tests/test_security_fixes.py
- [[GET status should return current version]] - rationale - gateway/tests/test_security_fixes.py
- [[JSON API responses should have Cache-Control no-store]] - rationale - gateway/tests/test_security_fixes.py
- [[Management WebSocket endpoints should use scoped tokens, not master auth.]] - rationale - gateway/tests/test_security_fixes.py
- [[Sync TestClient for WebSocket tests_1]] - rationale - gateway/tests/test_security_fixes.py
- [[TestDashboardCookieAuth]] - code - gateway/tests/test_security_fixes.py
- [[TestDashboardSecureCookie]] - code - gateway/tests/test_security_fixes.py
- [[TestGlobalSecurityHeaders]] - code - gateway/tests/test_security_fixes.py
- [[TestManagementWSTokenScoping]] - code - gateway/tests/test_security_fixes.py
- [[TestTelegramProxyClientDisconnect]] - code - gateway/tests/test_security_fixes.py
- [[TestVersionConsistency]] - code - gateway/tests/test_security_fixes.py
- [[Version strings should be consistent across the codebase.]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity should reject empty token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity should reject master auth token (R3-L4)]] - rationale - gateway/tests/test_security_fixes.py
- [[sync_client()_1]] - code - gateway/tests/test_security_fixes.py
- [[test_security_fixes.py]] - code - gateway/tests/test_security_fixes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_132
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 7 edges to [[_COMMUNITY_Module Group 94]]
- 3 edges to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 311]]
- 1 edge to [[_COMMUNITY_Module Group 444]]
- 1 edge to [[_COMMUNITY_Module Group 495]]
- 1 edge to [[_COMMUNITY_Module Group 337]]
- 1 edge to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[test_security_fixes.py]] - degree 17, connects to 8 communities
- [[TestManagementWSTokenScoping]] - degree 9, connects to 3 communities
- [[TestTelegramProxyClientDisconnect]] - degree 6, connects to 3 communities
- [[TestDashboardCookieAuth]] - degree 10, connects to 2 communities
- [[TestGlobalSecurityHeaders]] - degree 7, connects to 2 communities
