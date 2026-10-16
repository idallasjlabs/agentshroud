---
type: community
cohesion: 0.04
members: 98
---

# test_soc_realtime_coverage.py

**Cohesion:** 0.04 - loosely connected
**Members:** 98 nodes

## Members
- [[dot-__init__()_36]] - code - gateway/soc/websocket.py
- [[dot-_event_fan_out()]] - code - gateway/soc/websocket.py
- [[dot-_keepalive_loop()]] - code - gateway/soc/websocket.py
- [[dot-_make_handler()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-_matches()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-_send_event()]] - code - gateway/soc/websocket.py
- [[dot-run()]] - code - gateway/soc/websocket.py
- [[dot-setup_method()_4]] - code - gateway/tests/test_soc_auth.py
- [[dot-setup_method()_5]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_bearer_header_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_details_excludes_reserved_keys()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_different_keys_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_different_owners_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_egress_denied()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_empty_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_empty_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_event_type_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_expired_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_explicit_env_wins()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_handler_exception_is_swallowed()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_import()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_instantiate()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_invalid_dict_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_invalid_token_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_invalid_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_and_redeem()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_returns_hex_string()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_session_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_issue_ws_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_legacy_env_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_legacy_inbound_blocked()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_message_fallback_for_summary()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_missing_first_file_falls_to_second()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_multi_subscription()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_multiple_tokens_independent()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_no_sources_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_no_subscription_accepts_log_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_no_subscription_accepts_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_preserves_severity()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_raw_gateway_password_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_redeem_expired_ws_token_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_returns_none_on_bad_input()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_single_use()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_source_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_subscription_filters_correctly()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_token_file_env()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_type_mapping()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_unauthorized_closes_4003()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_unknown_severity_defaults_to_info()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_valid_ws_token_accepts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_verify_after_clear_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_expired_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_unknown_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_valid_token()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_wsevent_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Clear token store before each test.]] - rationale - gateway/tests/test_soc_auth.py
- [[Consume a WS token and return the user_id, or None if invalidexpired.]] - rationale - gateway/soc/auth.py
- [[Convert an EventBus item to WSEvent, return None if conversion fails.]] - rationale - gateway/soc/websocket.py
- [[Derive an HMAC session token and register it in the session store.]] - rationale - gateway/soc/auth.py
- [[FastAPI WebSocket route handler for wssoc.]] - rationale - gateway/soc/websocket.py
- [[Issue a short-lived, single-use WebSocket token for a user.]] - rationale - gateway/soc/auth.py
- [[Main connection loop.]] - rationale - gateway/soc/websocket.py
- [[Make runsecrets reads deterministic (raise OSError) on any host.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Manages a single wssoc client connection.]] - rationale - gateway/soc/websocket.py
- [[Read the gateway auth token from envsecret.      Resolution order (matches inge]] - rationale - gateway/soc/auth.py
- [[Replicate the filter logic from _event_fan_out.]] - rationale - gateway/tests/test_soc_websocket.py
- [[Return user_id if token is a valid unexpired session token, else None.]] - rationale - gateway/soc/auth.py
- [[SOCWebSocketHandler]] - code - gateway/tests/test_soc_websocket.py
- [[SOCWebSocketHandler_1]] - code - gateway/soc/websocket.py
- [[Severity]] - code - gateway/soc/models.py
- [[Subscribe to EventBus and forward matching events to the client.]] - rationale - gateway/soc/websocket.py
- [[Test event filtering via the subscriptions set (mirrors _event_fan_out logic).]] - rationale - gateway/tests/test_soc_websocket.py
- [[TestCoerceToWSEvent]] - code - gateway/tests/test_soc_websocket.py
- [[TestCoerceToWSEventExtra]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestGetConfigToken]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSOCWebSocketHandlerImport]] - code - gateway/tests/test_soc_websocket.py
- [[TestSessionTokens]] - code - gateway/tests/test_soc_auth.py
- [[TestSubscriptionFilter]] - code - gateway/tests/test_soc_websocket.py
- [[TestWSSOCEndpoint]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSTokens]] - code - gateway/tests/test_soc_auth.py
- [[WSEvent]] - code - gateway/soc/models.py
- [[WSEvent_1]] - code - gateway/soc/websocket.py
- [[WSEventType]] - code - gateway/soc/models.py
- [[WebSocket]] - code - gateway/soc/websocket.py
- [[_block_run_secrets()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_coerce_to_ws_event()]] - code - gateway/soc/websocket.py
- [[_get_config_token()]] - code - gateway/soc/auth.py
- [[_make_ws()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_verify_session_token()]] - code - gateway/soc/auth.py
- [[issue_session_token()]] - code - gateway/soc/auth.py
- [[issue_ws_token()]] - code - gateway/soc/auth.py
- [[redeem_ws_token()]] - code - gateway/soc/auth.py
- [[soc_websocket()]] - code - gateway/soc/router.py
- [[test_soc_auth.py]] - code - gateway/tests/test_soc_auth.py
- [[test_soc_websocket.py]] - code - gateway/tests/test_soc_websocket.py
- [[websocket.py]] - code - gateway/soc/websocket.py
- [[ws_soc_endpoint()]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_realtime_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 68 edges to [[_COMMUNITY_MiddlewareManager]]
- 8 edges to [[_COMMUNITY__FakeRBAC_1]]
- 6 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_SlackAPIProxy]]
- 2 edges to [[_COMMUNITY_AsyncMock_1]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY__FakeRBAC]]
- 2 edges to [[_COMMUNITY_soc.js]]
- 1 edge to [[_COMMUNITY_export_bot_1]]
- 1 edge to [[_COMMUNITY_test_soc_bots.py]]

## Top bridge nodes
- [[Severity]] - degree 15, connects to 5 communities
- [[WSEvent]] - degree 14, connects to 4 communities
- [[WSEventType]] - degree 11, connects to 4 communities
- [[SOCWebSocketHandler_1]] - degree 40, connects to 2 communities
- [[ws_soc_endpoint()]] - degree 18, connects to 2 communities
