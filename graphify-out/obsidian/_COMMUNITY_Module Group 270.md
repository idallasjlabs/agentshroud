---
type: community
cohesion: 0.20
members: 17
---

# Module Group 270

**Cohesion:** 0.20 - loosely connected
**Members:** 17 nodes

## Members
- [[.test_details_excludes_reserved_keys()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_egress_denied()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_event_type_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_invalid_dict_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_legacy_inbound_blocked()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_message_fallback_for_summary()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_preserves_severity()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_returns_none_on_bad_input()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[.test_source_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_type_mapping()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_unknown_severity_defaults_to_info()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_wsevent_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Convert an EventBus item to WSEvent, return None if conversion fails.]] - rationale - gateway/soc/websocket.py
- [[TestCoerceToWSEvent]] - code - gateway/tests/test_soc_websocket.py
- [[TestCoerceToWSEventExtra]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_coerce_to_ws_event()]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_270
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_RBAC Configuration]]
- 3 edges to [[_COMMUNITY_SOC Services & Health Status]]
- 3 edges to [[_COMMUNITY_Module Group 120]]
- 3 edges to [[_COMMUNITY_Module Group 83]]
- 2 edges to [[_COMMUNITY_SOC Authentication]]
- 1 edge to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 1 edge to [[_COMMUNITY_Module Group 315]]

## Top bridge nodes
- [[_coerce_to_ws_event()]] - degree 21, connects to 5 communities
- [[TestCoerceToWSEventExtra]] - degree 15, connects to 4 communities
- [[TestCoerceToWSEvent]] - degree 7, connects to 2 communities
- [[.test_wsevent_passthrough()]] - degree 3, connects to 1 community
