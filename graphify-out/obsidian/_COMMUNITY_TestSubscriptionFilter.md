---
type: community
cohesion: 0.35
members: 11
---

# TestSubscriptionFilter

**Cohesion:** 0.35 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-_make_handler()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-_matches()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_instantiate()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_multi_subscription()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_no_subscription_accepts_log_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_no_subscription_accepts_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_subscription_filters_correctly()]] - code - gateway/tests/test_soc_websocket.py
- [[Replicate the filter logic from _event_fan_out.]] - rationale - gateway/tests/test_soc_websocket.py
- [[SOCWebSocketHandler_2]] - code - gateway/tests/test_soc_websocket.py
- [[Test event filtering via the subscriptions set (mirrors _event_fan_out logic).]] - rationale - gateway/tests/test_soc_websocket.py
- [[TestSubscriptionFilter]] - code - gateway/tests/test_soc_websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSubscriptionFilter
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[TestSubscriptionFilter]] - degree 9, connects to 1 community
- [[dot-_matches()]] - degree 8, connects to 1 community
- [[SOCWebSocketHandler_2]] - degree 4, connects to 1 community
- [[dot-test_instantiate()]] - degree 2, connects to 1 community
