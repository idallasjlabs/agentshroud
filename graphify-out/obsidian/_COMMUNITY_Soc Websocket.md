---
type: community
cohesion: 0.09
members: 46
---

# Soc Websocket

**Cohesion:** 0.09 - loosely connected
**Members:** 46 nodes

## Members
- [[.__init__()_132]] - code - gateway/soc/websocket.py
- [[._event_fan_out()]] - code - gateway/soc/websocket.py
- [[._keepalive_loop()]] - code - gateway/soc/websocket.py
- [[._make_handler()]] - code - gateway/tests/test_soc_websocket.py
- [[._matches()]] - code - gateway/tests/test_soc_websocket.py
- [[._send_event()]] - code - gateway/soc/websocket.py
- [[.run()_5]] - code - gateway/soc/websocket.py
- [[.test_details_excludes_reserved_keys()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_egress_denied()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_event_type_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_import()_1]] - code - gateway/tests/test_soc_websocket.py
- [[.test_instantiate()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_invalid_dict_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_legacy_inbound_blocked()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_message_fallback_for_summary()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_multi_subscription()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_no_subscription_accepts_log_event()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_no_subscription_accepts_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_preserves_severity()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_returns_none_on_bad_input()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_source_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_subscription_filters_correctly()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_type_mapping()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_unknown_severity_defaults_to_info()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_wsevent_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Convert an EventBus item to WSEvent, return None if conversion fails.]] - rationale - gateway/soc/websocket.py
- [[Main connection loop.]] - rationale - gateway/soc/websocket.py
- [[Manages a single wssoc client connection.]] - rationale - gateway/soc/websocket.py
- [[Replicate the filter logic from _event_fan_out.]] - rationale - gateway/tests/test_soc_websocket.py
- [[SOCWebSocketHandler_2]] - code - gateway/tests/test_soc_websocket.py
- [[SOCWebSocketHandler]] - code - gateway/soc/websocket.py
- [[Severity_2]] - code - gateway/soc/models.py
- [[Subscribe to EventBus and forward matching events to the client.]] - rationale - gateway/soc/websocket.py
- [[Test event filtering via the subscriptions set (mirrors _event_fan_out logic).]] - rationale - gateway/tests/test_soc_websocket.py
- [[TestCoerceToWSEvent]] - code - gateway/tests/test_soc_websocket.py
- [[TestCoerceToWSEventExtra]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSOCWebSocketHandlerImport]] - code - gateway/tests/test_soc_websocket.py
- [[TestSubscriptionFilter]] - code - gateway/tests/test_soc_websocket.py
- [[WSEvent]] - code - gateway/soc/models.py
- [[WSEvent_1]] - code - gateway/soc/websocket.py
- [[WSEventType]] - code - gateway/soc/models.py
- [[WebSocket_6]] - code - gateway/soc/websocket.py
- [[_coerce_to_ws_event()]] - code - gateway/soc/websocket.py
- [[test_soc_websocket.py]] - code - gateway/tests/test_soc_websocket.py
- [[websocket.py]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Soc_Websocket
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 9 edges to [[_COMMUNITY_Soc Realtime Coverage]]
- 8 edges to [[_COMMUNITY_Soc Models]]
- 4 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 4 edges to [[_COMMUNITY_Event Adapter (soc)]]
- 3 edges to [[_COMMUNITY_Router (soc)]]
- 2 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 2 edges to [[_COMMUNITY_Soc (static)]]
- 2 edges to [[_COMMUNITY_Soc Realtime Coverage]]
- 1 edge to [[_COMMUNITY_Soc Bots]]

## Top bridge nodes
- [[Severity_2]] - degree 15, connects to 5 communities
- [[SOCWebSocketHandler]] - degree 40, connects to 4 communities
- [[WSEvent]] - degree 14, connects to 4 communities
- [[WSEventType]] - degree 11, connects to 4 communities
- [[websocket.py]] - degree 11, connects to 4 communities