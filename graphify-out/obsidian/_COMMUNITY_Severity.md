---
type: community
members: 32
---

# Severity

**Members:** 32 nodes

## Members
- [[dot-blocked()]] - code - gateway/security/skill_guard.py
- [[dot-severity()]] - code - gateway/security/skill_guard.py
- [[dot-test_conversion_error_path()_3]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_dict_allowed_without_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_dict_blocked_with_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_minimal_construction()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_object_form()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_optional_fields_default_none()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_severity_ordering()]] - code - gateway/tests/test_soc_models.py
- [[Any_35]] - code
- [[Best-effort conversion of arbitrary event dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Best-effort mapping of arbitrary severity strings to Severity enum.]] - rationale - gateway/soc/event_adapter.py
- [[Collect recent SecurityEvents from AuditStore (async-safe read).]] - rationale - gateway/soc/event_adapter.py
- [[Convert AuditEvent (from AuditStore) to SecurityEvent. AuditEvent fields…]] - rationale - gateway/soc/event_adapter.py
- [[Convert a PipelineResult to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an AnomalyAlert (from EgressMonitorSOCCorrelation) to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an EgressAttempt or egress dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Highest severity across all findings (``NONE`` when clean).]] - rationale - gateway/security/skill_guard.py
- [[SOC event adapter — normalises heterogeneous event sources into SecurityEvent.…]] - rationale - gateway/soc/event_adapter.py
- [[SecurityEvent]] - code - gateway/soc/models.py
- [[Severity]] - code - gateway/soc/models.py
- [[TestFromEgressAttempt]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSecurityEvent]] - code - gateway/tests/test_soc_models.py
- [[_map_severity()]] - code - gateway/soc/event_adapter.py
- [[collect_recent_events()]] - code - gateway/soc/event_adapter.py
- [[domain()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[event_adapter.py]] - code - gateway/soc/event_adapter.py
- [[from_anomaly_alert()]] - code - gateway/soc/event_adapter.py
- [[from_audit_chain_entry()]] - code - gateway/soc/event_adapter.py
- [[from_dict()]] - code - gateway/soc/event_adapter.py
- [[from_egress_attempt()]] - code - gateway/soc/event_adapter.py
- [[from_pipeline_result()]] - code - gateway/soc/event_adapter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Severity
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_soc_bots.py]]
- 9 edges to [[_COMMUNITY_socmodels.py]]
- 6 edges to [[_COMMUNITY__coerce_to_ws_event]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 3 edges to [[_COMMUNITY_SkillGuard]]
- 2 edges to [[_COMMUNITY__audit_entry]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_TestFromPipelineResult]]
- 1 edge to [[_COMMUNITY_TestFromAnomalyAlert]]
- 1 edge to [[_COMMUNITY_dot-verify_export_integrity]]
- 1 edge to [[_COMMUNITY_AlertTelegramRelay]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[Severity]] - degree 25, connects to 8 communities
- [[SecurityEvent]] - degree 22, connects to 5 communities
- [[event_adapter.py]] - degree 12, connects to 2 communities
- [[dot-severity()]] - degree 6, connects to 2 communities
- [[dot-blocked()]] - degree 5, connects to 2 communities
