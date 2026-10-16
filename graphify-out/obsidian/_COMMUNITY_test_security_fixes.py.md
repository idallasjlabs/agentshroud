---
type: community
cohesion: 0.03
members: 60
---

# test_security_fixes.py

**Cohesion:** 0.03 - loosely connected
**Members:** 60 nodes

## Members
- [[dot-test_cookie_not_secure_on_http()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_bad_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_bad_token_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_no_auth_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_token_sets_cookie_and_redirects()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_json_api_has_cache_control()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ssh_command_uses_strict_checking()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_status_has_security_headers()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_status_returns_current_version()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_strict_host_key_checking_in_source()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_activity_rejects_bad_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_activity_rejects_empty_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_activity_rejects_master_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_activity_rejects_no_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_approvals_rejects_bad_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_approvals_rejects_master_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_approvals_rejects_no_token()]] - code - gateway/tests/test_security_fixes.py
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
- [[GET dashboardws-token with valid cookie returns token]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=valid sets cookie and redirects to dashboard]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=wrong returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET status should include security headers]] - rationale - gateway/tests/test_security_fixes.py
- [[GET status should return current version]] - rationale - gateway/tests/test_security_fixes.py
- [[JSON API responses should have Cache-Control no-store]] - rationale - gateway/tests/test_security_fixes.py
- [[Management WebSocket endpoints should use scoped tokens, not master auth.]] - rationale - gateway/tests/test_security_fixes.py
- [[SSH execute builds command with StrictHostKeyChecking=yes]] - rationale - gateway/tests/test_security_fixes.py
- [[Source code uses StrictHostKeyChecking=yes]] - rationale - gateway/tests/test_security_fixes.py
- [[Sync TestClient for WebSocket tests_1]] - rationale - gateway/tests/test_security_fixes.py
- [[TestDashboardCookieAuth]] - code - gateway/tests/test_security_fixes.py
- [[TestDashboardSecureCookie]] - code - gateway/tests/test_security_fixes.py
- [[TestDashboardWSToken]] - code - gateway/tests/test_security_fixes.py
- [[TestGlobalSecurityHeaders]] - code - gateway/tests/test_security_fixes.py
- [[TestManagementWSTokenScoping]] - code - gateway/tests/test_security_fixes.py
- [[TestSSHStrictHostKeyChecking]] - code - gateway/tests/test_security_fixes.py
- [[TestTelegramProxyClientDisconnect]] - code - gateway/tests/test_security_fixes.py
- [[TestVersionConsistency]] - code - gateway/tests/test_security_fixes.py
- [[TestWebSocketHandshakeAuth]] - code - gateway/tests/test_security_fixes.py
- [[Verify SSH proxy uses StrictHostKeyChecking=yes, not accept-new]] - rationale - gateway/tests/test_security_fixes.py
- [[Version strings should be consistent across the codebase.]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity closes immediately without token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity closes with bad token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity should reject empty token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity should reject master auth token (R3-L4)]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals closes immediately without token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals closes with bad token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals rejects the master auth token -- R3-L4 removed the         mast]] - rationale - gateway/tests/test_security_fixes.py
- [[WebSocket endpoints must validate token during handshake, not first message]] - rationale - gateway/tests/test_security_fixes.py
- [[gatewayingest_apiroutesdashboard.py (_create_ws_token)]] - code - gateway/ingest_api/routes/dashboard.py
- [[sync_client()_1]] - code - gateway/tests/test_security_fixes.py
- [[test_security_fixes.py]] - code - gateway/tests/test_security_fixes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_fixespy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_SSHHostConfig]]
- 11 edges to [[_COMMUNITY_SSHProxy]]
- 11 edges to [[_COMMUNITY_DataLedger]]
- 5 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_BotConfig]]
- 2 edges to [[_COMMUNITY_test_e2e.py]]

## Top bridge nodes
- [[test_security_fixes.py]] - degree 18, connects to 6 communities
- [[TestWebSocketHandshakeAuth]] - degree 12, connects to 4 communities
- [[TestDashboardCookieAuth]] - degree 10, connects to 4 communities
- [[TestManagementWSTokenScoping]] - degree 9, connects to 4 communities
- [[TestTelegramProxyClientDisconnect]] - degree 6, connects to 4 communities
