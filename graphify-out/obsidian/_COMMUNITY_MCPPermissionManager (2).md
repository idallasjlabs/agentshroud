---
type: community
cohesion: 0.02
members: 121
---

# MCPPermissionManager (2)

**Cohesion:** 0.02 - loosely connected
**Members:** 121 nodes

## Members
- [[dot-execute()]] - code - gateway/ssh_proxy/proxy.py
- [[dot-expand_key_path()]] - code - gateway/ingest_api/ssh_config.py
- [[dot-expand_known_hosts()]] - code - gateway/ingest_api/ssh_config.py
- [[dot-test_cookie_not_secure_on_http()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_bad_cookie_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_bad_token_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_no_auth_returns_403()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dashboard_token_sets_cookie_and_redirects()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_execute_nonzero_exit()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_execute_success()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_execute_timeout()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_execute_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_is_auto_approved_no()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_is_auto_approved_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_is_auto_approved_yes()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_json_api_has_cache_control()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_non_auto_approved_executes_directly()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_approval_sanitizes_command_pii()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ssh_command_uses_strict_checking()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ssh_disabled_config()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_ssh_exec_auto_approved()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_cwd_accepted_and_forwarded()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_exec_cwd_none_forwards_none()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_ssh_history()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_status_has_security_headers()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_status_returns_current_version()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_strict_host_key_checking_in_source()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_validate_auto_approve_exact_only()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_allowed()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_backslash_n_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_carriage_return_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_denied()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_dollar_brace_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_dollar_var_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_global_denied()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_and()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_backticks()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_dollar_paren()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_or()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_pipe()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_injection_blocked_semicolon()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_newline_injection()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_not_in_allowlist()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_command_unknown_host()]] - code - gateway/tests/test_ssh_proxy.py
- [[dot-test_validate_empty_command()]] - code - gateway/tests/test_ssh_proxy.py
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
- [[Approval queue details must be PII-sanitized before storage]] - rationale - gateway/tests/test_security_fixes.py
- [[Auto-approve must be exact match, not prefix (Finding 3)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[ClientDisconnect mid-body-read must not crash the gateway process.]] - rationale - gateway/tests/test_security_fixes.py
- [[Configuration for a single SSH host]] - rationale - gateway/ingest_api/ssh_config.py
- [[Cookie secure=False on HTTP requests]] - rationale - gateway/tests/test_security_fixes.py
- [[Dashboard cookie secure flag is dynamic based on request scheme]] - rationale - gateway/tests/test_security_fixes.py
- [[Dashboard should set httpOnly cookie and redirect to clean URL]] - rationale - gateway/tests/test_security_fixes.py
- [[Dashboard ws-token endpoint returns token only for cookie-authed sessions]] - rationale - gateway/tests/test_security_fixes.py
- [[Execute a command on a remote host via SSH.]] - rationale - gateway/ssh_proxy/proxy.py
- [[GET dashboard with invalid cookie returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard with no auth returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardws-token with valid cookie returns token]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=valid sets cookie and redirects to dashboard]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboardtoken=wrong returns 403]] - rationale - gateway/tests/test_security_fixes.py
- [[GET status should include security headers]] - rationale - gateway/tests/test_security_fixes.py
- [[GET status should return current version]] - rationale - gateway/tests/test_security_fixes.py
- [[JSON API responses should have Cache-Control no-store]] - rationale - gateway/tests/test_security_fixes.py
- [[Management WebSocket endpoints should use scoped tokens, not master auth.]] - rationale - gateway/tests/test_security_fixes.py
- [[Omitting cwd passes cwd=None to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Result of an SSH command execution]] - rationale - gateway/ssh_proxy/proxy.py
- [[SSH exec requiring approval sanitizes PII in command before storing]] - rationale - gateway/tests/test_security_fixes.py
- [[SSH execute builds command with StrictHostKeyChecking=yes]] - rationale - gateway/tests/test_security_fixes.py
- [[SSHConfig]] - code - gateway/tests/test_ssh_proxy.py
- [[SSHHostConfig]] - code - gateway/ingest_api/ssh_config.py
- [[SSHProxy]] - code - gateway/tests/test_ssh_proxy.py
- [[SSHResult]] - code - gateway/ssh_proxy/proxy.py
- [[Source code uses StrictHostKeyChecking=yes]] - rationale - gateway/tests/test_security_fixes.py
- [[Sync TestClient for WebSocket tests]] - rationale - gateway/tests/test_security_fixes.py
- [[Test SSH disabled returns 503 (Finding 12)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[Test newline-based injection attempts (Finding 11)]] - rationale - gateway/tests/test_ssh_proxy.py
- [[TestApprovalQueuePIISanitization]] - code - gateway/tests/test_security_fixes.py
- [[TestDashboardCookieAuth]] - code - gateway/tests/test_security_fixes.py
- [[TestDashboardSecureCookie]] - code - gateway/tests/test_security_fixes.py
- [[TestDashboardWSToken]] - code - gateway/tests/test_security_fixes.py
- [[TestExecute]] - code - gateway/tests/test_ssh_proxy.py
- [[TestGlobalSecurityHeaders]] - code - gateway/tests/test_security_fixes.py
- [[TestInjectionNewline]] - code - gateway/tests/test_ssh_proxy.py
- [[TestIsAutoApproved]] - code - gateway/tests/test_ssh_proxy.py
- [[TestManagementWSTokenScoping]] - code - gateway/tests/test_security_fixes.py
- [[TestSSHDisabled]] - code - gateway/tests/test_ssh_proxy.py
- [[TestSSHStrictHostKeyChecking]] - code - gateway/tests/test_security_fixes.py
- [[TestTelegramProxyClientDisconnect]] - code - gateway/tests/test_security_fixes.py
- [[TestValidateCommand]] - code - gateway/tests/test_ssh_proxy.py
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
- [[When require_approval=false, non-auto-approved commands execute directly.]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[cwd is validated and passed to proxy.execute().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[gatewayingest_apiroutesdashboard.py (_create_ws_token)]] - code - gateway/ingest_api/routes/dashboard.py
- [[proxy()_1]] - code - gateway/tests/test_ssh_proxy.py
- [[ssh_config()]] - code - gateway/tests/test_ssh_proxy.py
- [[ssh_config()_1]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[ssh_config.py]] - code - gateway/ingest_api/ssh_config.py
- [[sync_client()]] - code - gateway/tests/test_security_fixes.py
- [[test_security_fixes.py]] - code - gateway/tests/test_security_fixes.py
- [[test_ssh_proxy.py]] - code - gateway/tests/test_ssh_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager_2
SORT file.name ASC
```

## Connections to other communities
- 45 edges to [[_COMMUNITY_MCPPermissionManager]]
- 32 edges to [[_COMMUNITY_SSHProxy]]
- 5 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 4 edges to [[_COMMUNITY_api.py (2)]]
- 2 edges to [[_COMMUNITY_UserSessionManager (3)]]
- 1 edge to [[_COMMUNITY__make_cve]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_GroupConfig]]

## Top bridge nodes
- [[test_security_fixes.py]] - degree 18, connects to 5 communities
- [[SSHHostConfig]] - degree 44, connects to 3 communities
- [[TestWebSocketHandshakeAuth]] - degree 12, connects to 3 communities
- [[TestDashboardCookieAuth]] - degree 10, connects to 3 communities
- [[TestManagementWSTokenScoping]] - degree 9, connects to 3 communities
