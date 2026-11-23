---
type: community
members: 39
---

# asyncio

**Members:** 39 nodes

## Members
- [[dot-test_client_disconnect_returns_499()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_cookie_not_secure_on_http()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_bad_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_bad_token_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_cookie_auth_serves_html()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_no_auth_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_token_sets_cookie_and_redirects()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_json_api_has_cache_control()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_status_has_security_headers()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_status_returns_current_version()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_token_with_bad_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_token_with_valid_cookie()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_token_without_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[All API responses should include basic security headers.]] - rationale - gateway/tests/test_security_fixes.py
- [[ClientDisconnect mid-body-read must not crash the gateway process.]] - rationale - gateway/tests/test_security_fixes.py
- [[Cookie secure=False on HTTP requests]] - rationale - gateway/tests/test_security_fixes.py
- [[Dashboard cookie secure flag is dynamic based on request scheme]] - rationale - gateway/tests/test_security_fixes.py
- [[Dashboard should set httpOnly cookie and redirect to clean URL]] - rationale - gateway/tests/test_security_fixes.py
- [[Dashboard ws-token endpoint returns token only for cookie-authed sessions]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with invalid cookie returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with no auth returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with valid cookie serves HTML]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardws-token with bad cookie returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardws-token with valid cookie returns token]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardws-token without cookie returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=valid sets cookie and redirects to dashboard]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=wrong returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET status should include security headers]] - rationale - gateway/tests/test_security_fixes.py
- [[GET status should return current version]] - rationale - gateway/tests/test_security_fixes.py
- [[JSON API responses should have Cache-Control no-store]] - rationale - gateway/tests/test_security_fixes.py
- [[TestDashboardCookieAuth]] - code - gateway/tests/test_security_fixes.py
- [[TestDashboardSecureCookie]] - code - gateway/tests/test_security_fixes.py
- [[TestDashboardWSToken]] - code - gateway/tests/test_security_fixes.py
- [[TestGlobalSecurityHeaders]] - code - gateway/tests/test_security_fixes.py
- [[TestTelegramProxyClientDisconnect]] - code - gateway/tests/test_security_fixes.py
- [[TestVersionConsistency]] - code - gateway/tests/test_security_fixes.py
- [[Version strings should be consistent across the codebase.]] - rationale - gateway/tests/test_security_fixes.py
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - rationale - gateway/tests/test_security_fixes.py
- [[asyncio_47]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_BotConfig]]

## Top bridge nodes
- [[dot-test_client_disconnect_returns_499()]] - degree 5, connects to 2 communities
- [[asyncio_47]] - degree 15, connects to 1 community
- [[TestDashboardCookieAuth]] - degree 7, connects to 1 community
- [[TestDashboardWSToken]] - degree 5, connects to 1 community
- [[TestGlobalSecurityHeaders]] - degree 4, connects to 1 community
