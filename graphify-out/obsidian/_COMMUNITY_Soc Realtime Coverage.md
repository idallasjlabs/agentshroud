---
type: community
cohesion: 0.19
members: 16
---

# Soc Realtime Coverage

**Cohesion:** 0.19 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_collects_and_converts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_conversion_error_path()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_full_context_summary_from_details()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_missing_timestamp_uses_now()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_none_store_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_severity_filter_drops_lower()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_store_error_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_summary_falls_back_to_block_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_summary_falls_back_to_event_type()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_summary_falls_back_to_message()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_summary_from_agent_id()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_summary_from_non_allowed_action()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_user_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestCollectRecentEvents]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestFromAuditChainEntry]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_audit_entry()]] - code - gateway/tests/test_soc_realtime_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Soc_Realtime_Coverage
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 3 edges to [[_COMMUNITY_Slack Proxy Coverage]]
- 2 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 2 edges to [[_COMMUNITY_Soc Websocket]]
- 1 edge to [[_COMMUNITY_Event Adapter (soc)]]

## Top bridge nodes
- [[TestCollectRecentEvents]] - degree 12, connects to 4 communities
- [[TestFromAuditChainEntry]] - degree 16, connects to 3 communities
- [[_audit_entry()]] - degree 12, connects to 1 community
- [[.test_collects_and_converts()]] - degree 3, connects to 1 community
- [[.test_severity_filter_drops_lower()]] - degree 3, connects to 1 community