---
type: community
cohesion: 0.24
members: 13
---

# export_bot

**Cohesion:** 0.24 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-test_collects_and_converts()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_conversion_error_path()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_full_context_summary_from_details()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_missing_timestamp_uses_now()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_severity_filter_drops_lower()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_block_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_event_type()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_message()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_from_agent_id()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_from_non_allowed_action()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_user_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestFromAuditChainEntry]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_audit_entry()]] - code - gateway/tests/test_soc_realtime_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/export_bot
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_AsyncMock_1]]
- 1 edge to [[_COMMUNITY_test_soc_realtime_coverage.py]]

## Top bridge nodes
- [[TestFromAuditChainEntry]] - degree 16, connects to 2 communities
- [[dot-test_collects_and_converts()]] - degree 3, connects to 2 communities
- [[dot-test_severity_filter_drops_lower()]] - degree 3, connects to 2 communities
- [[_audit_entry()]] - degree 12, connects to 1 community
