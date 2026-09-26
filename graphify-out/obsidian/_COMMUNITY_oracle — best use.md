---
type: community
cohesion: 0.27
members: 13
---

# oracle — best use

**Cohesion:** 0.27 - loosely connected
**Members:** 13 nodes

## Members
- [[._make_handler()]] - code - gateway/tests/test_soc_websocket.py
- [[._matches()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_import()_1]] - code - gateway/tests/test_soc_websocket.py
- [[.test_instantiate()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_multi_subscription()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_no_subscription_accepts_log_event()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_no_subscription_accepts_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_subscription_filters_correctly()]] - code - gateway/tests/test_soc_websocket.py
- [[Replicate the filter logic from _event_fan_out.]] - rationale - gateway/tests/test_soc_websocket.py
- [[SOCWebSocketHandler_2]] - code - gateway/tests/test_soc_websocket.py
- [[Test event filtering via the subscriptions set (mirrors _event_fan_out logic).]] - rationale - gateway/tests/test_soc_websocket.py
- [[TestSOCWebSocketHandlerImport]] - code - gateway/tests/test_soc_websocket.py
- [[TestSubscriptionFilter]] - code - gateway/tests/test_soc_websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/oracle__best_use
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_EncryptedStore]]

## Top bridge nodes
- [[TestSubscriptionFilter]] - degree 9, connects to 2 communities
- [[TestSOCWebSocketHandlerImport]] - degree 4, connects to 2 communities
- [[._matches()]] - degree 8, connects to 1 community
- [[SOCWebSocketHandler_2]] - degree 4, connects to 1 community