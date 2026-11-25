---
type: community
members: 51
---

# test_soc_realtime_coverage.py

**Members:** 51 nodes

## Members
- [[dot-setup_method()_30]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_bearer_header_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_conversion_error_path()_4]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_empty_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_empty_token_rejected()_1]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_expired_token_rejected()_1]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_explicit_env_wins()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_full_dict()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_handler_exception_is_swallowed()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_invalid_token_closes_4003()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_invalid_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_and_redeem()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_ws_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_legacy_env_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_minimal_dict_uses_fallbacks()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_missing_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_multiple_tokens_independent()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_no_sources_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_raw_gateway_password_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_redeem_expired_ws_token_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_single_use()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_token_file_env()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_unauthorized_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_valid_ws_token_accepts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Clear token store before each test.]] - rationale - gateway/tests/test_soc_auth.py
- [[Consume a WS token and return the user_id, or None if invalidexpired.]] - rationale - gateway/soc/auth.py
- [[Coverage tests for gatewaysocwebsocket.py, event_adapter.py and auth.py.…]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[FastAPI WebSocket route handler for wssoc.]] - rationale - gateway/soc/websocket.py
- [[Issue a short-lived, single-use WebSocket token for a user.]] - rationale - gateway/soc/auth.py
- [[Make runsecrets reads deterministic (raise OSError) on any host.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Read the gateway auth token from envsecret. Resolution order (matches…]] - rationale - gateway/soc/auth.py
- [[Remove all gateway-password env vars and clear token stores.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[TestFromDict]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestGetConfigToken]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestTokenStorePruning]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSSOCEndpoint]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSTokens]] - code - gateway/tests/test_soc_auth.py
- [[Tests for gatewaysocauth.py — SCL authentication and WS token issuance.]] - rationale - gateway/tests/test_soc_auth.py
- [[_block_run_secrets()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_get_config_token()]] - code - gateway/soc/auth.py
- [[_make_ws()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[clean_auth_env()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[fixture_114]] - code
- [[guarded_open()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[issue_ws_token()]] - code - gateway/soc/auth.py
- [[redeem_ws_token()]] - code - gateway/soc/auth.py
- [[soc_websocket()]] - code - gateway/soc/router.py
- [[test_soc_auth.py]] - code - gateway/tests/test_soc_auth.py
- [[test_soc_realtime_coverage.py]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[websocket_6]] - code
- [[ws_soc_endpoint()]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_realtime_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_RBACConfig]]
- 9 edges to [[_COMMUNITY__coerce_to_ws_event]]
- 7 edges to [[_COMMUNITY_socrouter.py]]
- 6 edges to [[_COMMUNITY_issue_session_token]]
- 5 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 4 edges to [[_COMMUNITY_Severity]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY__FakeBus]]
- 2 edges to [[_COMMUNITY__audit_entry]]
- 2 edges to [[_COMMUNITY__verify_bearer]]
- 2 edges to [[_COMMUNITY_socmodels.py]]
- 1 edge to [[_COMMUNITY_TestFromPipelineResult]]
- 1 edge to [[_COMMUNITY_TestFromAnomalyAlert]]
- 1 edge to [[_COMMUNITY_fastapi]]

## Top bridge nodes
- [[test_soc_realtime_coverage.py]] - degree 54, connects to 14 communities
- [[ws_soc_endpoint()]] - degree 16, connects to 4 communities
- [[issue_ws_token()]] - degree 15, connects to 2 communities
- [[redeem_ws_token()]] - degree 14, connects to 2 communities
- [[_get_config_token()]] - degree 12, connects to 2 communities
