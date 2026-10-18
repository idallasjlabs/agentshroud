---
type: community
members: 82
---

# _FakeRBAC

**Members:** 82 nodes

## Members
- [[dot-_build_record()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_rbac()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_teams()]] - code - gateway/soc/contributors.py
- [[dot-_load_paused_ids()]] - code - gateway/soc/contributors.py
- [[dot-get_contributor()]] - code - gateway/soc/contributors.py
- [[dot-list_contributors()]] - code - gateway/soc/contributors.py
- [[dot-test_approved_status()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_confirmation_required()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()_1]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()_2]] - code - gateway/tests/test_soc_models.py
- [[dot-test_defaults()_1]] - code - gateway/tests/test_soc_models.py
- [[dot-test_destructive_requires_confirmation()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_error_model()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_pending_status_default()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_permission_denied_error()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_red_risk_high_threat()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_running_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_standby_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_stopped_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_unhealthy_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_with_resource_usage()]] - code - gateway/tests/test_soc_models.py
- [[Alarm]] - code - gateway/soc/models.py
- [[AlarmStatus]] - code - gateway/soc/models.py
- [[Any_60]] - code - gateway/soc/event_adapter.py
- [[Best-effort conversion of arbitrary event dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Best-effort mapping of arbitrary severity strings to Severity enum.]] - rationale - gateway/soc/event_adapter.py
- [[Collect recent SecurityEvents from AuditStore (async-safe read).]] - rationale - gateway/soc/event_adapter.py
- [[ContributorRecord]] - code - gateway/soc/contributors.py
- [[ContributorRecord_1]] - code - gateway/soc/models.py
- [[Convert AuditEvent (from AuditStore) to SecurityEvent.      AuditEvent fields e]] - rationale - gateway/soc/event_adapter.py
- [[Convert a PipelineResult to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an AnomalyAlert (from EgressMonitorSOCCorrelation) to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an EgressAttempt or egress dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[EgressRequest_1]] - code - gateway/soc/models.py
- [[EgressStatus]] - code - gateway/soc/models.py
- [[HealthStatus]] - code - gateway/soc/services.py
- [[HealthStatus_1]] - code - gateway/soc/models.py
- [[Platform]] - code - gateway/soc/models.py
- [[ResourceUsage_1]] - code - gateway/soc/models.py
- [[RiskLevel_6]] - code - gateway/soc/models.py
- [[SCLError]] - code - gateway/soc/models.py
- [[STANDBY = binary installed but cannot run in this environment; should be healthy]] - rationale - gateway/tests/test_soc_services.py
- [[SecurityEvent_1]] - code - gateway/soc/event_adapter.py
- [[ServiceDescriptor_1]] - code - gateway/soc/models.py
- [[ServiceStatus]] - code - gateway/soc/services.py
- [[ServiceStatus_1]] - code - gateway/soc/models.py
- [[Severity_1]] - code - gateway/soc/event_adapter.py
- [[Severity_2]] - code - gateway/soc/models.py
- [[TestConfirmationModel]] - code - gateway/tests/test_soc_egress.py
- [[TestContributorRecord]] - code - gateway/tests/test_soc_models.py
- [[TestEgressRequest]] - code - gateway/tests/test_soc_models.py
- [[TestEgressRequestModel]] - code - gateway/tests/test_soc_egress.py
- [[TestSCLError]] - code - gateway/tests/test_soc_models.py
- [[TestServiceDescriptor]] - code - gateway/tests/test_soc_models.py
- [[TestServiceDescriptorDefaults]] - code - gateway/tests/test_soc_services.py
- [[TestWSEvent]] - code - gateway/tests/test_soc_models.py
- [[UserRole]] - code - gateway/soc/models.py
- [[UserRole_1]] - code - gateway/soc/contributors.py
- [[Validate ServiceDescriptor model defaults — no real container calls.]] - rationale - gateway/tests/test_soc_services.py
- [[WSEvent]] - code - gateway/soc/models.py
- [[WSEvent_1]] - code - gateway/soc/websocket.py
- [[WSEventType]] - code - gateway/soc/models.py
- [[WebSocket_4]] - code - gateway/soc/websocket.py
- [[_map_severity()]] - code - gateway/soc/event_adapter.py
- [[_new_uuid()]] - code - gateway/soc/models.py
- [[_now_iso()]] - code - gateway/soc/models.py
- [[_role_enum()]] - code - gateway/soc/contributors.py
- [[collect_recent_events()]] - code - gateway/soc/event_adapter.py
- [[contributors.py]] - code - gateway/soc/contributors.py
- [[event_adapter.py]] - code - gateway/soc/event_adapter.py
- [[from_anomaly_alert()]] - code - gateway/soc/event_adapter.py
- [[from_audit_chain_entry()]] - code - gateway/soc/event_adapter.py
- [[from_dict()]] - code - gateway/soc/event_adapter.py
- [[from_egress_attempt()]] - code - gateway/soc/event_adapter.py
- [[from_pipeline_result()]] - code - gateway/soc/event_adapter.py
- [[socmodels.py]] - code - gateway/soc/models.py
- [[test_soc_egress.py]] - code - gateway/tests/test_soc_egress.py
- [[test_soc_models.py]] - code - gateway/tests/test_soc_models.py
- [[test_soc_services.py]] - code - gateway/tests/test_soc_services.py
- [[test_soc_websocket.py]] - code - gateway/tests/test_soc_websocket.py
- [[websocket.py]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeRBAC
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_socrouter.py]]
- 21 edges to [[_COMMUNITY_ServiceManager]]
- 19 edges to [[_COMMUNITY_test_soc_bots.py]]
- 18 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 10 edges to [[_COMMUNITY_SecurityPipeline]]
- 9 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 8 edges to [[_COMMUNITY_test_soc_realtime_coverage.py (2)]]
- 5 edges to [[_COMMUNITY_soc.js]]
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_export_bot]]

## Top bridge nodes
- [[socmodels.py]] - degree 29, connects to 4 communities
- [[ServiceDescriptor_1]] - degree 20, connects to 4 communities
- [[Severity_2]] - degree 15, connects to 4 communities
- [[WSEvent]] - degree 14, connects to 4 communities
- [[ServiceStatus_1]] - degree 13, connects to 4 communities
