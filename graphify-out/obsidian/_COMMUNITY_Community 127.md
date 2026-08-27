---
type: community
members: 51
---

# Community 127

**Members:** 51 nodes

## Members
- [[.setup_method()_34]] - code - gateway/tests/test_soc_auth.py
- [[.setup_method()_35]] - code - gateway/tests/test_soc_auth.py
- [[.test_bearer_header_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_different_keys_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[.test_different_owners_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[.test_empty_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_empty_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[.test_expired_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[.test_explicit_env_wins()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_handler_exception_is_swallowed()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_invalid_token_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_invalid_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_and_redeem()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_returns_hex_string()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_session_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_issue_ws_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_legacy_env_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_missing_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_multiple_tokens_independent()]] - code - gateway/tests/test_soc_auth.py
- [[.test_no_sources_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_raw_gateway_password_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_redeem_expired_ws_token_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_single_use()]] - code - gateway/tests/test_soc_auth.py
- [[.test_token_file_env()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_unauthorized_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_valid_ws_token_accepts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_verify_after_clear_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_expired_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_unknown_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_valid_token()]] - code - gateway/tests/test_soc_auth.py
- [[Clear token store before each test.]] - rationale - gateway/tests/test_soc_auth.py
- [[Consume a WS token and return the user_id, or None if invalidexpired.]] - rationale - gateway/soc/auth.py
- [[Derive an HMAC session token and register it in the session store.]] - rationale - gateway/soc/auth.py
- [[FastAPI WebSocket route handler for wssoc.]] - rationale - gateway/soc/websocket.py
- [[Issue a short-lived, single-use WebSocket token for a user.]] - rationale - gateway/soc/auth.py
- [[Make runsecrets reads deterministic (raise OSError) on any host.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Read the gateway auth token from envsecret.      Resolution order (matches inge]] - rationale - gateway/soc/auth.py
- [[Return user_id if token is a valid unexpired session token, else None.]] - rationale - gateway/soc/auth.py
- [[TestGetConfigToken]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSessionTokens]] - code - gateway/tests/test_soc_auth.py
- [[TestWSSOCEndpoint]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSTokens]] - code - gateway/tests/test_soc_auth.py
- [[_block_run_secrets()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_get_config_token()]] - code - gateway/soc/auth.py
- [[_make_ws()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_verify_session_token()]] - code - gateway/soc/auth.py
- [[issue_session_token()]] - code - gateway/soc/auth.py
- [[issue_ws_token()]] - code - gateway/soc/auth.py
- [[redeem_ws_token()]] - code - gateway/soc/auth.py
- [[test_soc_auth.py]] - code - gateway/tests/test_soc_auth.py
- [[ws_soc_endpoint()]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_127
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Community 15]]
- 5 edges to [[_COMMUNITY_Community 19]]
- 4 edges to [[_COMMUNITY_Community 27]]
- 2 edges to [[_COMMUNITY_Community 109]]
- 1 edge to [[_COMMUNITY_Community 18]]
- 1 edge to [[_COMMUNITY_Community 144]]

## Top bridge nodes
- [[ws_soc_endpoint()]] - degree 18, connects to 5 communities
- [[issue_ws_token()]] - degree 15, connects to 2 communities
- [[issue_session_token()]] - degree 14, connects to 2 communities
- [[redeem_ws_token()]] - degree 14, connects to 2 communities
- [[_get_config_token()]] - degree 12, connects to 2 communities