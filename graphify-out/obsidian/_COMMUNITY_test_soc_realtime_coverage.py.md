---
type: community
cohesion: 0.04
members: 94
---

# test_soc_realtime_coverage.py

**Cohesion:** 0.04 - loosely connected
**Members:** 94 nodes

## Members
- [[dot-__init__()_72]] - code - gateway/soc/auth.py
- [[dot-__init__()_73]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-check_permission()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-setup_method()_12]] - code - gateway/tests/test_soc_auth.py
- [[dot-setup_method()_13]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_bearer_header_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_bearer_header_valid()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_conversion_error_path()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_cookie_raw_bearer_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_different_keys_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_different_owners_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_empty_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_empty_token_or_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_empty_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_expired_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_explicit_env_wins()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_full_dict()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_get_caller_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_get_rbac_manager_builds_real_manager()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_handler_exception_is_swallowed()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_invalid_token_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_invalid_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_is_group_admin_with_teams_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_is_group_admin_without_teams_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_is_owner_delegates_to_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_issue_and_redeem()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_returns_hex_string()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_session_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_issue_ws_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_legacy_env_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_match()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_minimal_dict_uses_fallbacks()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_mismatch()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_missing_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_multiple_tokens_independent()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_no_credentials_raises_401()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_no_sources_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_raw_gateway_password_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_redeem_expired_ws_token_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_require_allowed_does_not_raise()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_require_denied_raises_403_with_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_require_denied_without_reason_uses_forbidden()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_session_cookie_valid()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_single_use()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_token_file_env()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_unauthorized_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_valid_ws_token_accepts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_verify_after_clear_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_expired_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_unknown_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_valid_token()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_wrong_bearer_raises_401()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_x_soc_token_header_valid()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Clear token store before each test.]] - rationale - gateway/tests/test_soc_auth.py
- [[Constant-time comparison against the gateway shared secret.]] - rationale - gateway/soc/auth.py
- [[Consume a WS token and return the user_id, or None if invalidexpired.]] - rationale - gateway/soc/auth.py
- [[Derive an HMAC session token and register it in the session store.]] - rationale - gateway/soc/auth.py
- [[FastAPI WebSocket route handler for wssoc.]] - rationale - gateway/soc/websocket.py
- [[FastAPI dependency resolve Bearercookie token → user_id → role.]] - rationale - gateway/soc/auth.py
- [[Issue a short-lived, single-use WebSocket token for a user.]] - rationale - gateway/soc/auth.py
- [[Make runsecrets reads deterministic (raise OSError) on any host.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Minimal RBAC stand-in with controllable check_permission results.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Public FastAPI dependency injected by SCL route handlers.]] - rationale - gateway/soc/auth.py
- [[RBACManager]] - code - gateway/soc/auth.py
- [[Read the gateway auth token from envsecret.      Resolution order (matches inge]] - rationale - gateway/soc/auth.py
- [[Remove all gateway-password env vars and clear token stores.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Return user_id if token is a valid unexpired session token, else None.]] - rationale - gateway/soc/auth.py
- [[Role_20]] - code - gateway/soc/auth.py
- [[TestFromDict]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestGetConfigToken]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestResolveCaller]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSCLCaller]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSessionTokens]] - code - gateway/tests/test_soc_auth.py
- [[TestTokenStorePruning]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestVerifyBearer]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSSOCEndpoint]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSTokens]] - code - gateway/tests/test_soc_auth.py
- [[_FakeRBAC]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_block_run_secrets()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_get_config_token()]] - code - gateway/soc/auth.py
- [[_get_rbac_manager()]] - code - gateway/soc/auth.py
- [[_make_ws()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_resolve_caller()]] - code - gateway/soc/auth.py
- [[_verify_bearer()]] - code - gateway/soc/auth.py
- [[_verify_session_token()]] - code - gateway/soc/auth.py
- [[clean_auth_env()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[get_caller()]] - code - gateway/soc/auth.py
- [[issue_session_token()]] - code - gateway/soc/auth.py
- [[issue_ws_token()]] - code - gateway/soc/auth.py
- [[redeem_ws_token()]] - code - gateway/soc/auth.py
- [[socauth.py]] - code - gateway/soc/auth.py
- [[test_soc_auth.py]] - code - gateway/tests/test_soc_auth.py
- [[test_soc_realtime_coverage.py]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[ws_soc_endpoint()]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_realtime_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_Action]]
- 23 edges to [[_COMMUNITY_Enum]]
- 20 edges to [[_COMMUNITY_socrouter.py]]
- 13 edges to [[_COMMUNITY_RBACConfig]]
- 10 edges to [[_COMMUNITY_Role]]
- 8 edges to [[_COMMUNITY_TestFromAuditChainEntry]]
- 5 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_rbac_config.py]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]

## Top bridge nodes
- [[test_soc_realtime_coverage.py]] - degree 47, connects to 7 communities
- [[socauth.py]] - degree 19, connects to 6 communities
- [[_FakeRBAC]] - degree 17, connects to 4 communities
- [[TestResolveCaller]] - degree 15, connects to 4 communities
- [[TestSCLCaller]] - degree 14, connects to 4 communities
