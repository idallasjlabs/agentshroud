---
type: community
cohesion: 0.05
members: 75
---

# test_soc_realtime_coverage.py

**Cohesion:** 0.05 - loosely connected
**Members:** 75 nodes

## Members
- [[.setup_method()_8]] - code - gateway/tests/test_soc_auth.py
- [[.setup_method()_9]] - code - gateway/tests/test_soc_auth.py
- [[.test_bearer_header_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_bearer_header_valid()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_cookie_raw_bearer_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_different_keys_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[.test_different_owners_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[.test_empty_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_empty_token_or_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_empty_token_rejected()_1]] - code - gateway/tests/test_soc_auth.py
- [[.test_expired_token_rejected()_1]] - code - gateway/tests/test_soc_auth.py
- [[.test_explicit_env_wins()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_get_caller_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_handler_exception_is_swallowed()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_invalid_token_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_invalid_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_and_redeem()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_returns_hex_string()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_session_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_issue_ws_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_legacy_env_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_match()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_mismatch()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_missing_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_multiple_tokens_independent()]] - code - gateway/tests/test_soc_auth.py
- [[.test_no_credentials_raises_401()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_no_sources_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_raw_gateway_password_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_redeem_expired_ws_token_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_session_cookie_valid()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_single_use()]] - code - gateway/tests/test_soc_auth.py
- [[.test_token_file_env()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_unauthorized_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_valid_ws_token_accepts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_verify_after_clear_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_expired_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_unknown_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_valid_token()]] - code - gateway/tests/test_soc_auth.py
- [[.test_wrong_bearer_raises_401()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_x_soc_token_header_valid()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Clear token store before each test.]] - rationale - gateway/tests/test_soc_auth.py
- [[Constant-time comparison against the gateway shared secret.]] - rationale - gateway/soc/auth.py
- [[Consume a WS token and return the user_id, or None if invalidexpired.]] - rationale - gateway/soc/auth.py
- [[Derive an HMAC session token and register it in the session store.]] - rationale - gateway/soc/auth.py
- [[Exchange gateway token for a session cookie.]] - rationale - gateway/soc/router.py
- [[FastAPI WebSocket route handler for wssoc.]] - rationale - gateway/soc/websocket.py
- [[FastAPI dependency resolve Bearercookie token → user_id → role.]] - rationale - gateway/soc/auth.py
- [[Issue a short-lived, single-use WebSocket token for a user.]] - rationale - gateway/soc/auth.py
- [[Make runsecrets reads deterministic (raise OSError) on any host.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Public FastAPI dependency injected by SCL route handlers.]] - rationale - gateway/soc/auth.py
- [[Read the gateway auth token from envsecret.      Resolution order (matches inge]] - rationale - gateway/soc/auth.py
- [[Remove all gateway-password env vars and clear token stores.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Return user_id if token is a valid unexpired session token, else None.]] - rationale - gateway/soc/auth.py
- [[TestGetConfigToken]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestResolveCaller]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSessionTokens]] - code - gateway/tests/test_soc_auth.py
- [[TestVerifyBearer]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSSOCEndpoint]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSTokens]] - code - gateway/tests/test_soc_auth.py
- [[_block_run_secrets()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_get_config_token()]] - code - gateway/soc/auth.py
- [[_make_ws()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_resolve_caller()]] - code - gateway/soc/auth.py
- [[_verify_bearer()]] - code - gateway/soc/auth.py
- [[_verify_session_token()]] - code - gateway/soc/auth.py
- [[auth_login()]] - code - gateway/soc/router.py
- [[clean_auth_env()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[get_caller()]] - code - gateway/soc/auth.py
- [[issue_session_token()]] - code - gateway/soc/auth.py
- [[issue_ws_token()]] - code - gateway/soc/auth.py
- [[redeem_ws_token()]] - code - gateway/soc/auth.py
- [[soc_websocket()]] - code - gateway/soc/router.py
- [[test_soc_auth.py]] - code - gateway/tests/test_soc_auth.py
- [[test_soc_realtime_coverage.py]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[ws_soc_endpoint()]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_realtime_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 39 edges to [[_COMMUNITY_ingest_apimain.py]]
- 16 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 8 edges to [[_COMMUNITY_RBACConfig]]
- 8 edges to [[_COMMUNITY_socrouter.py]]
- 6 edges to [[_COMMUNITY_BaseModel]]
- 5 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 3 edges to [[_COMMUNITY_TestFromAuditChainEntry]]
- 3 edges to [[_COMMUNITY__FakeRBAC]]
- 2 edges to [[_COMMUNITY_SecurityEvent]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]

## Top bridge nodes
- [[test_soc_realtime_coverage.py]] - degree 47, connects to 8 communities
- [[get_caller()]] - degree 7, connects to 4 communities
- [[ws_soc_endpoint()]] - degree 18, connects to 3 communities
- [[TestResolveCaller]] - degree 15, connects to 3 communities
- [[TestWSSOCEndpoint]] - degree 14, connects to 3 communities