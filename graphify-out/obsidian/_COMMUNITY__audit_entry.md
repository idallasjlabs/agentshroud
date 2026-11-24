---
type: community
members: 16
---

# _audit_entry

**Members:** 16 nodes

## Members
- [[dot-test_collects_and_converts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_full_context_summary_from_details()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_missing_timestamp_uses_now()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_none_store_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_severity_filter_drops_lower()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_store_error_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_block_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_event_type()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_message()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_from_agent_id()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_from_non_allowed_action()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_user_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[SimpleNamespace]] - code
- [[TestCollectRecentEvents]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestFromAuditChainEntry]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_audit_entry()]] - code - gateway/tests/test_soc_realtime_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_audit_entry
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_dot-verify_export_integrity]]

## Top bridge nodes
- [[TestFromAuditChainEntry]] - degree 12, connects to 2 communities
- [[_audit_entry()]] - degree 12, connects to 1 community
- [[TestCollectRecentEvents]] - degree 7, connects to 1 community
- [[dot-test_collects_and_converts()]] - degree 3, connects to 1 community
- [[dot-test_severity_filter_drops_lower()]] - degree 3, connects to 1 community
