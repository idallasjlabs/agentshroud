---
type: community
members: 11
---

# _FakeBus

**Members:** 11 nodes

## Members
- [[dot-__init__()_24]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-subscribe()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_fan_out_filters_and_forwards()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_fan_out_survives_coerce_exception()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_keepalive_sends_pings()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_none_bus_returns_immediately()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-unsubscribe()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestEventFanOut]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_FakeBus]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_spin()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[fragile()]] - code - gateway/tests/test_soc_realtime_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeBus
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_SOCWebSocketHandler]]
- 1 edge to [[_COMMUNITY__coerce_to_ws_event]]

## Top bridge nodes
- [[TestEventFanOut]] - degree 5, connects to 2 communities
- [[dot-test_keepalive_sends_pings()]] - degree 3, connects to 2 communities
- [[_FakeBus]] - degree 6, connects to 1 community
- [[dot-test_fan_out_survives_coerce_exception()]] - degree 5, connects to 1 community
- [[_spin()]] - degree 4, connects to 1 community
