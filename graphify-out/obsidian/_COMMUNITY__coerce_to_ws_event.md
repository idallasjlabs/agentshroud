---
type: community
members: 39
---

# _coerce_to_ws_event

**Members:** 39 nodes

## Members
- [[dot-test_construction()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_details_excludes_reserved_keys()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_edge_gateway_event_is_forwarded()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_egress_denied()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_event_type_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_import()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_instantiate()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_invalid_dict_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_keepalive_breaks_on_construction_error()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_legacy_inbound_blocked()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_message_fallback_for_summary()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_preserves_severity()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_returns_none_on_bad_input()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_security_event()]] - code - gateway/tests/test_soc_websocket.py
- [[dot-test_send_event_serializes()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_send_event_swallows_transport_error()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_severity_enum_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_source_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_string_mapping()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_type_mapping()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_unknown_severity_defaults_to_info()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_unmapped_gateway_event_still_dropped()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_wsevent_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Convert an EventBus item to WSEvent, return None if conversion fails.]] - rationale - gateway/soc/websocket.py
- [[SOC unified WebSocket stream — wssoc. Replaces the 5 separate ws endpoints…]] - rationale - gateway/soc/websocket.py
- [[TestCoerceToWSEvent]] - code - gateway/tests/test_soc_websocket.py
- [[TestCoerceToWSEventExtra]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestEdgeEventOverWebSocket]] - code - gateway/tests/test_soc_edge.py
- [[TestMapSeverity]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSOCWebSocketHandlerImport]] - code - gateway/tests/test_soc_websocket.py
- [[TestSendEventAndKeepalive]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSEvent]] - code - gateway/tests/test_soc_models.py
- [[Tests for gatewaysocwebsocket.py — SOCWebSocketHandler unit tests.]] - rationale - gateway/tests/test_soc_websocket.py
- [[WSEvent]] - code - gateway/soc/models.py
- [[_coerce_to_ws_event()]] - code - gateway/soc/websocket.py
- [[boom()_5]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[parametrize_12]] - code
- [[test_soc_websocket.py]] - code - gateway/tests/test_soc_websocket.py
- [[websocket.py]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_coerce_to_ws_event
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_socmodels.py]]
- 11 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 9 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 6 edges to [[_COMMUNITY_Severity]]
- 3 edges to [[_COMMUNITY_EventBus]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY_test_soc_edge.py]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY__FakeBus]]
- 1 edge to [[_COMMUNITY_fastapi]]

## Top bridge nodes
- [[websocket.py]] - degree 18, connects to 9 communities
- [[_coerce_to_ws_event()]] - degree 26, connects to 6 communities
- [[TestSendEventAndKeepalive]] - degree 8, connects to 4 communities
- [[TestEdgeEventOverWebSocket]] - degree 7, connects to 4 communities
- [[WSEvent]] - degree 15, connects to 3 communities
