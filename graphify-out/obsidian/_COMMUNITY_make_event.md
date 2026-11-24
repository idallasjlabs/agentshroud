---
type: community
members: 72
---

# make_event

**Members:** 72 nodes

## Members
- [[dot-__init__()_6]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-__init__()_7]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-__init__()_8]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_alert()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_authenticate()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_check_limits()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_p0()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_record()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_scrub()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_strike()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_visible_tools()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-call_tool()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-emit()]] - code - gateway/ingest_api/event_bus.py
- [[dot-enforcing()]] - code - gateway/inbound_edge/profiles.py
- [[dot-get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[dot-get_stats()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-hit()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-list_tools()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-principal_id()]] - code - gateway/inbound_edge/edge_jwt.py
- [[dot-profiles()]] - code - gateway/inbound_edge/service.py
- [[dot-run()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-to_dict()_1]] - code - gateway/ingest_api/event_bus.py
- [[dot-tool_access()]] - code - gateway/inbound_edge/profiles.py
- [[3+ auth failures in 5 min escalates to critical]] - rationale - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Any_9]] - code
- [[Any_10]] - code
- [[CallContext]] - code - gateway/inbound_edge/call_pipeline.py
- [[EdgeCallPipeline]] - code - gateway/inbound_edge/call_pipeline.py
- [[EdgePrincipal]] - code - gateway/inbound_edge/edge_jwt.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[Emitting with no subscribers doesn't raise]] - rationale - gateway/tests/test_event_bus.py
- [[Events have type, timestamp, summary, details, severity]] - rationale - gateway/tests/test_event_bus.py
- [[Exception_1]] - code
- [[Facade]] - code - gateway/inbound_edge/call_pipeline.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[Helper to create a GatewayEvent with current timestamp]] - rationale - gateway/ingest_api/event_bus.py
- [[Multiple subscribers all receive the same event]] - rationale - gateway/tests/test_event_bus.py
- [[Namespaced identity used by every downstream module. Never an owner ID.]] - rationale - gateway/inbound_edge/edge_jwt.py
- [[Protocol]] - code
- [[Recent events are returned in order]] - rationale - gateway/tests/test_event_bus.py
- [[Sliding one-minute window counter keyed by principal or vendor.]] - rationale - gateway/inbound_edge/call_pipeline.py
- [[Stats track event counts]] - rationale - gateway/tests/test_event_bus.py
- [[Subscriber receives emitted events]] - rationale - gateway/tests/test_event_bus.py
- [[The MCP ``Tool`` view of a descriptor (internal fields stripped).]] - rationale - gateway/inbound_edge/descriptors.py
- [[The validated vendor profiles the pipeline enforces (read by the Command…]] - rationale - gateway/inbound_edge/service.py
- [[Unsubscribed callback stops receiving events]] - rationale - gateway/tests/test_event_bus.py
- [[VendorProfile]] - code - gateway/inbound_edge/profiles.py
- [[_Denied]] - code - gateway/inbound_edge/call_pipeline.py
- [[_Window]] - code - gateway/inbound_edge/call_pipeline.py
- [[_rank()]] - code - gateway/inbound_edge/call_pipeline.py
- [[_result()]] - code - gateway/inbound_edge/call_pipeline.py
- [[_string_leaves()]] - code - gateway/inbound_edge/call_pipeline.py
- [[``read````write`` when the vendor may call ``tool``, else ``None``.]] - rationale - gateway/inbound_edge/profiles.py
- [[asyncio_4]] - code
- [[bus()]] - code - gateway/tests/test_event_bus.py
- [[call_pipeline.py]] - code - gateway/inbound_edge/call_pipeline.py
- [[cb()]] - code - gateway/tests/test_event_bus.py
- [[cb()_1]] - code - gateway/tests/test_event_bus.py
- [[fixture_7]] - code
- [[make_event()]] - code - gateway/ingest_api/event_bus.py
- [[mcp_tool()]] - code - gateway/inbound_edge/descriptors.py
- [[test_async_subscriber()]] - code - gateway/tests/test_event_bus.py
- [[test_auth_failure_escalation()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_no_subscribers_no_error()]] - code - gateway/tests/test_event_bus.py
- [[test_emit_to_multiple_subscribers()]] - code - gateway/tests/test_event_bus.py
- [[test_event_bus.py]] - code - gateway/tests/test_event_bus.py
- [[test_event_has_required_fields()]] - code - gateway/tests/test_event_bus.py
- [[test_get_recent()]] - code - gateway/tests/test_event_bus.py
- [[test_get_stats()]] - code - gateway/tests/test_event_bus.py
- [[test_subscribe_receive_events()]] - code - gateway/tests/test_event_bus.py
- [[test_unsubscribe_stops_events()]] - code - gateway/tests/test_event_bus.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/make_event
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 20 edges to [[_COMMUNITY_ingest_apimain.py]]
- 13 edges to [[_COMMUNITY_test_edge_approvals.py]]
- 6 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 5 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 5 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_test_dashboard.py]]
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_LockdownLevel]]
- 3 edges to [[_COMMUNITY_EdgeOAuthService]]
- 3 edges to [[_COMMUNITY_normalize_input]]
- 3 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 3 edges to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 2 edges to [[_COMMUNITY_load_profiles]]
- 2 edges to [[_COMMUNITY_GatewayConfig]]
- 2 edges to [[_COMMUNITY_decide_approval]]
- 2 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 2 edges to [[_COMMUNITY_egress_approval.py]]
- 1 edge to [[_COMMUNITY__client_info]]
- 1 edge to [[_COMMUNITY__token]]
- 1 edge to [[_COMMUNITY_EdgeStore]]
- 1 edge to [[_COMMUNITY_email_send]]
- 1 edge to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_dot-_extract_egress_targets]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_test_mcp_proxy.py]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[make_event()]] - degree 67, connects to 19 communities
- [[call_pipeline.py]] - degree 36, connects to 8 communities
- [[VendorProfile]] - degree 24, connects to 6 communities
- [[EdgeCallPipeline]] - degree 26, connects to 4 communities
- [[EdgePrincipal]] - degree 15, connects to 2 communities
