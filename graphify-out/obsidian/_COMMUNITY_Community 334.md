---
type: community
cohesion: 0.16
members: 26
---

# Community 334

**Cohesion:** 0.16 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-__init__()_134]] - code - gateway/soc/websocket.py
- [[dot-test_minimal_construction()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_optional_fields_default_none()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_severity_ordering()_1]] - code - gateway/tests/test_soc_models.py
- [[Any_46]] - code - gateway/soc/event_adapter.py
- [[Best-effort conversion of arbitrary event dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Best-effort mapping of arbitrary severity strings to Severity enum.]] - rationale - gateway/soc/event_adapter.py
- [[Collect recent SecurityEvents from AuditStore (async-safe read).]] - rationale - gateway/soc/event_adapter.py
- [[Convert AuditEvent (from AuditStore) to SecurityEvent.      AuditEvent fields e]] - rationale - gateway/soc/event_adapter.py
- [[Convert a PipelineResult to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an AnomalyAlert (from EgressMonitorSOCCorrelation) to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an EgressAttempt or egress dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[SecurityEvent]] - code - gateway/soc/event_adapter.py
- [[SecurityEvent_1]] - code - gateway/soc/models.py
- [[Severity_1]] - code - gateway/soc/event_adapter.py
- [[Severity_2]] - code - gateway/soc/models.py
- [[TestSecurityEvent]] - code - gateway/tests/test_soc_models.py
- [[WebSocket_5]] - code - gateway/soc/websocket.py
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
TABLE source_file, type FROM #community/Community_334
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 7 edges to [[_COMMUNITY_Community 68]]
- 6 edges to [[_COMMUNITY_Community 66]]
- 4 edges to [[_COMMUNITY_SOC Correlation & Router]]
- 3 edges to [[_COMMUNITY_Voice Gateway STT & Browser Security]]
- 2 edges to [[_COMMUNITY_Community 187]]
- 1 edge to [[_COMMUNITY_Community 153]]
- 1 edge to [[_COMMUNITY_Community 159]]
- 1 edge to [[_COMMUNITY_Community 67]]

## Top bridge nodes
- [[SecurityEvent_1]] - degree 20, connects to 5 communities
- [[Severity_2]] - degree 15, connects to 5 communities
- [[collect_recent_events()]] - degree 10, connects to 3 communities
- [[WebSocket_5]] - degree 5, connects to 3 communities
- [[event_adapter.py]] - degree 11, connects to 2 communities