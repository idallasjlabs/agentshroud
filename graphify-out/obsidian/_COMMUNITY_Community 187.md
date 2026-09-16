---
type: community
cohesion: 0.09
members: 38
---

# Community 187

**Cohesion:** 0.09 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-_event_fan_out()]] - code - gateway/soc/websocket.py
- [[dot-_keepalive_loop()]] - code - gateway/soc/websocket.py
- [[dot-_make_handler()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-_matches()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-_send_event()]] - code - gateway/soc/websocket.py
- [[dot-run()_1]] - code - gateway/soc/websocket.py
- [[dot-test_details_excludes_reserved_keys()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_egress_denied()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_event_type_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_import()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_instantiate()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_invalid_dict_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_legacy_inbound_blocked()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_message_fallback_for_summary()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_multi_subscription()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_no_subscription_accepts_log_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_no_subscription_accepts_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_preserves_severity()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_returns_none_on_bad_input()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_source_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_subscription_filters_correctly()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_type_mapping()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_unknown_severity_defaults_to_info()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_wsevent_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Convert an EventBus item to WSEvent, return None if conversion fails.]] - rationale - gateway/soc/websocket.py
- [[Main connection loop.]] - rationale - gateway/soc/websocket.py
- [[Replicate the filter logic from _event_fan_out.]] - rationale - gateway/tests/test_soc_websocket.py
- [[SOCWebSocketHandler_2]] - code - gateway/tests/test_soc_websocket.py
- [[Subscribe to EventBus and forward matching events to the client.]] - rationale - gateway/soc/websocket.py
- [[Test event filtering via the subscriptions set (mirrors _event_fan_out logic).]] - rationale - gateway/tests/test_soc_websocket.py
- [[TestCoerceToWSEvent]] - code - gateway/tests/test_soc_websocket.py
- [[TestCoerceToWSEventExtra]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSOCWebSocketHandlerImport]] - code - gateway/tests/test_soc_websocket.py
- [[TestSubscriptionFilter]] - code - gateway/tests/test_soc_websocket.py
- [[WSEvent]] - code - gateway/soc/websocket.py
- [[_coerce_to_ws_event()]] - code - gateway/soc/websocket.py
- [[test_soc_websocket.py]] - code - gateway/tests/test_soc_websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_187
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 3 edges to [[_COMMUNITY_Community 68]]
- 2 edges to [[_COMMUNITY_Voice Gateway STT & Browser Security]]
- 2 edges to [[_COMMUNITY_Community 334]]
- 1 edge to [[_COMMUNITY_Community 159]]

## Top bridge nodes
- [[test_soc_websocket.py]] - degree 7, connects to 3 communities
- [[WSEvent]] - degree 6, connects to 3 communities
- [[_coerce_to_ws_event()]] - degree 22, connects to 2 communities
- [[dot-run()_1]] - degree 5, connects to 2 communities
- [[TestCoerceToWSEventExtra]] - degree 15, connects to 1 community