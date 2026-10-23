---
type: community
cohesion: 0.09
members: 43
---

# TestEgressApprovalQueue

**Cohesion:** 0.09 - loosely connected
**Members:** 43 nodes

## Members
- [[dot-setup_method()_9]] - code - gateway/tests/test_soc_auth.py
- [[dot-setup_method()_10]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_bearer_header_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_different_keys_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_different_owners_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_empty_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_expired_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_handler_exception_is_swallowed()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_invalid_token_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_invalid_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_and_redeem()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_returns_hex_string()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_session_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_issue_ws_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_multiple_tokens_independent()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_raw_gateway_password_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_redeem_expired_ws_token_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_single_use()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_unauthorized_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_valid_ws_token_accepts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_verify_after_clear_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_expired_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_unknown_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_valid_token()]] - code - gateway/tests/test_soc_auth.py
- [[Clear token store before each test.]] - rationale - gateway/tests/test_soc_auth.py
- [[Consume a WS token and return the user_id, or None if invalidexpired.]] - rationale - gateway/soc/auth.py
- [[Derive an HMAC session token and register it in the session store.]] - rationale - gateway/soc/auth.py
- [[FastAPI WebSocket route handler for wssoc.]] - rationale - gateway/soc/websocket.py
- [[Issue a short-lived, single-use WebSocket token for a user.]] - rationale - gateway/soc/auth.py
- [[Make runsecrets reads deterministic (raise OSError) on any host.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Return user_id if token is a valid unexpired session token, else None.]] - rationale - gateway/soc/auth.py
- [[TestSessionTokens]] - code - gateway/tests/test_soc_auth.py
- [[TestWSSOCEndpoint]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSTokens]] - code - gateway/tests/test_soc_auth.py
- [[_block_run_secrets()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_make_ws()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_verify_session_token()]] - code - gateway/soc/auth.py
- [[issue_session_token()]] - code - gateway/soc/auth.py
- [[issue_ws_token()]] - code - gateway/soc/auth.py
- [[redeem_ws_token()]] - code - gateway/soc/auth.py
- [[soc_websocket()]] - code - gateway/soc/router.py
- [[test_soc_auth.py]] - code - gateway/tests/test_soc_auth.py
- [[ws_soc_endpoint()]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 3 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY__coerce_to_ws_event()]]

## Top bridge nodes
- [[ws_soc_endpoint()]] - degree 18, connects to 4 communities
- [[issue_ws_token()]] - degree 15, connects to 2 communities
- [[issue_session_token()]] - degree 14, connects to 2 communities
- [[redeem_ws_token()]] - degree 14, connects to 2 communities
- [[_make_ws()]] - degree 8, connects to 2 communities
