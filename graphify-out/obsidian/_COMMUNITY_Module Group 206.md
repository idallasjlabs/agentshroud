---
type: community
cohesion: 0.19
members: 23
---

# Module Group 206

**Cohesion:** 0.19 - loosely connected
**Members:** 23 nodes

## Members
- [[.test_minimal_construction()]] - code - gateway/tests/test_soc_models.py
- [[.test_optional_fields_default_none()]] - code - gateway/tests/test_soc_models.py
- [[.test_severity_ordering()]] - code - gateway/tests/test_soc_models.py
- [[Any_59]] - code - gateway/soc/event_adapter.py
- [[Best-effort conversion of arbitrary event dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Best-effort mapping of arbitrary severity strings to Severity enum.]] - rationale - gateway/soc/event_adapter.py
- [[Collect recent SecurityEvents from AuditStore (async-safe read).]] - rationale - gateway/soc/event_adapter.py
- [[Convert AuditEvent (from AuditStore) to SecurityEvent.      AuditEvent fields e]] - rationale - gateway/soc/event_adapter.py
- [[Convert a PipelineResult to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an AnomalyAlert (from EgressMonitorSOCCorrelation) to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an EgressAttempt or egress dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[SecurityEvent]] - code - gateway/soc/event_adapter.py
- [[SecurityEvent_1]] - code - gateway/soc/models.py
- [[Severity]] - code - gateway/soc/event_adapter.py
- [[TestSecurityEvent]] - code - gateway/tests/test_soc_models.py
- [[_map_severity()]] - code - gateway/soc/event_adapter.py
- [[collect_recent_events()]] - code - gateway/soc/event_adapter.py
- [[event_adapter.py]] - code - gateway/soc/event_adapter.py
- [[from_anomaly_alert()]] - code - gateway/soc/event_adapter.py
- [[from_audit_chain_entry()]] - code - gateway/soc/event_adapter.py
- [[from_dict()]] - code - gateway/soc/event_adapter.py
- [[from_egress_attempt()]] - code - gateway/soc/event_adapter.py
- [[from_pipeline_result()]] - code - gateway/soc/event_adapter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_206
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Module Group 83]]
- 5 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 4 edges to [[_COMMUNITY_SOC Services & Health Status]]
- 4 edges to [[_COMMUNITY_SOC Bots & CVE Management]]
- 2 edges to [[_COMMUNITY_SOC Authentication]]

## Top bridge nodes
- [[SecurityEvent_1]] - degree 19, connects to 4 communities
- [[event_adapter.py]] - degree 11, connects to 3 communities
- [[Any_59]] - degree 9, connects to 1 community
- [[collect_recent_events()]] - degree 9, connects to 1 community
- [[SecurityEvent]] - degree 8, connects to 1 community
