---
type: community
cohesion: 0.22
members: 18
---

# Event Adapter (soc)

**Cohesion:** 0.22 - loosely connected
**Members:** 18 nodes

## Members
- [[Any_66]] - code - gateway/soc/event_adapter.py
- [[Best-effort conversion of arbitrary event dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Best-effort mapping of arbitrary severity strings to Severity enum.]] - rationale - gateway/soc/event_adapter.py
- [[Collect recent SecurityEvents from AuditStore (async-safe read).]] - rationale - gateway/soc/event_adapter.py
- [[Convert AuditEvent (from AuditStore) to SecurityEvent.      AuditEvent fields e]] - rationale - gateway/soc/event_adapter.py
- [[Convert a PipelineResult to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an AnomalyAlert (from EgressMonitorSOCCorrelation) to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an EgressAttempt or egress dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[SecurityEvent]] - code - gateway/soc/event_adapter.py
- [[Severity_1]] - code - gateway/soc/event_adapter.py
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
TABLE source_file, type FROM #community/Event_Adapter_soc
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Soc Bots]]
- 4 edges to [[_COMMUNITY_Soc Websocket]]
- 4 edges to [[_COMMUNITY_SOC Router (Collaborator Mgmt)]]
- 1 edge to [[_COMMUNITY_Soc Models]]
- 1 edge to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 1 edge to [[_COMMUNITY_Soc Realtime Coverage]]

## Top bridge nodes
- [[event_adapter.py]] - degree 11, connects to 4 communities
- [[collect_recent_events()]] - degree 10, connects to 3 communities
- [[Any_66]] - degree 9, connects to 2 communities
- [[SecurityEvent]] - degree 8, connects to 2 communities
- [[from_dict()]] - degree 8, connects to 2 communities