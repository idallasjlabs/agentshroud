---
type: community
cohesion: 0.19
members: 16
---

# TestFromAuditChainEntry

**Cohesion:** 0.19 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_collects_and_converts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_conversion_error_path()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
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
TABLE source_file, type FROM #community/TestFromAuditChainEntry
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 1 edge to [[_COMMUNITY_SecurityEvent]]

## Top bridge nodes
- [[TestCollectRecentEvents]] - degree 12, connects to 5 communities
- [[TestFromAuditChainEntry]] - degree 16, connects to 4 communities
- [[_audit_entry()]] - degree 12, connects to 2 communities
- [[.test_collects_and_converts()]] - degree 3, connects to 1 community
- [[.test_severity_filter_drops_lower()]] - degree 3, connects to 1 community