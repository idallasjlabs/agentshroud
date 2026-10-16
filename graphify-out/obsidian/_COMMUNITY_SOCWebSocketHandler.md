---
type: community
cohesion: 0.14
members: 23
---

# SOCWebSocketHandler

**Cohesion:** 0.14 - loosely connected
**Members:** 23 nodes

## Members
- [[dot-__init__()_138]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-_handler()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-subscribe()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_command_invalid_json_ignored()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_command_message_updates_subscription()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_fan_out_filters_and_forwards()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_fan_out_survives_coerce_exception()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_initial_invalid_json_ignored()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_initial_subscribe_message_sets_filter()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_initial_timeout_subscribes_to_all()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_inner_timeout_continues_loop()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_keepalive_breaks_on_construction_error()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_keepalive_sends_pings()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_none_bus_returns_immediately()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_send_event_serializes()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_send_event_swallows_transport_error()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-unsubscribe()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[SOCWebSocketHandler_2]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestEventFanOut]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestHandlerRun]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSendEventAndKeepalive]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_FakeBus]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_spin()]] - code - gateway/tests/test_soc_realtime_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SOCWebSocketHandler
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Action]]
- 12 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 10 edges to [[_COMMUNITY_RBACConfig]]
- 7 edges to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[SOCWebSocketHandler_2]] - degree 14, connects to 3 communities
- [[TestHandlerRun]] - degree 14, connects to 3 communities
- [[_FakeBus]] - degree 12, connects to 3 communities
- [[TestSendEventAndKeepalive]] - degree 11, connects to 3 communities
- [[TestEventFanOut]] - degree 10, connects to 3 communities
