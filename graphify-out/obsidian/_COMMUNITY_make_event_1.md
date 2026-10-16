---
type: community
cohesion: 0.11
members: 19
---

# make_event

**Cohesion:** 0.11 - loosely connected
**Members:** 19 nodes

## Members
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[test_async_subscriber()]] - code - gateway/tests/test_event_bus.py
- [[test_auth_failure_escalation()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_no_subscribers_no_error()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_to_multiple_subscribers()]] - code - gateway/tests/test_event_bus.py
- [[test_event_bus.py]] - code - gateway/tests/test_event_bus.py
- [[test_event_has_required_fields()]] - code - gateway/tests/test_event_bus.py
- [[test_get_recent()]] - code - gateway/tests/test_event_bus.py
- [[test_get_stats()_2]] - code - gateway/tests/test_event_bus.py
- [[test_subscribe_receive_events()]] - code - gateway/tests/test_event_bus.py
- [[test_unsubscribe_stops_events()]] - code - gateway/tests/test_event_bus.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/make_event
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_make_event]]

## Top bridge nodes
- [[test_event_bus.py]] - degree 12, connects to 2 communities
- [[test_auth_failure_escalation()]] - degree 3, connects to 1 community
- [[test_emit_no_subscribers_no_error()]] - degree 3, connects to 1 community
- [[test_emit_to_multiple_subscribers()]] - degree 3, connects to 1 community
- [[test_event_has_required_fields()]] - degree 3, connects to 1 community
