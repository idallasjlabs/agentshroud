---
type: community
members: 31
---

# SOCWebSocketHandler

**Members:** 31 nodes

## Members
- [[dot-__init__()_57]] - code - gateway/soc/websocket.py
- [[dot-_event_fan_out()]] - code - gateway/soc/websocket.py
- [[dot-_handler()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-_keepalive_loop()]] - code - gateway/soc/websocket.py
- [[dot-_make_handler()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-_matches()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-_send_event()]] - code - gateway/soc/websocket.py
- [[dot-run()_1]] - code - gateway/soc/websocket.py
- [[dot-test_command_invalid_json_ignored()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_command_message_updates_subscription()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_fan_out_honours_edge_subscription()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_initial_invalid_json_ignored()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_initial_subscribe_message_sets_filter()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_initial_timeout_subscribes_to_all()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_inner_timeout_continues_loop()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_multi_subscription()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_no_subscription_accepts_log_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_no_subscription_accepts_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_subscription_filters_correctly()]] - code - gateway/tests/test_soc_websocket.py
- [[Any_26]] - code
- [[Main connection loop.]] - rationale - gateway/soc/websocket.py
- [[Manages a single wssoc client connection.]] - rationale - gateway/soc/websocket.py
- [[Replicate the filter logic from _event_fan_out.]] - rationale - gateway/tests/test_soc_websocket.py
- [[SOCWebSocketHandler]] - code - gateway/soc/websocket.py
- [[Subscribe to EventBus and forward matching events to the client.]] - rationale - gateway/soc/websocket.py
- [[Test event filtering via the subscriptions set (mirrors _event_fan_out logic).]] - rationale - gateway/tests/test_soc_websocket.py
- [[TestHandlerRun]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSubscriptionFilter]] - code - gateway/tests/test_soc_websocket.py
- [[WebSocket_1]] - code
- [[_on_event()]] - code - gateway/soc/websocket.py
- [[_send()_1]] - code - gateway/tests/test_soc_edge.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SOCWebSocketHandler
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY__coerce_to_ws_event]]
- 5 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_EventBus]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY__FakeBus]]
- 1 edge to [[_COMMUNITY_test_soc_edge.py]]
- 1 edge to [[_COMMUNITY_socmodels.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[SOCWebSocketHandler]] - degree 24, connects to 5 communities
- [[dot-test_fan_out_honours_edge_subscription()]] - degree 5, connects to 3 communities
- [[dot-_handler()]] - degree 10, connects to 1 community
- [[TestHandlerRun]] - degree 9, connects to 1 community
- [[TestSubscriptionFilter]] - degree 9, connects to 1 community
