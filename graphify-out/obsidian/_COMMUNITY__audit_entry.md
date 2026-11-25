---
type: community
members: 11
---

# _audit_entry

**Members:** 11 nodes

## Members
- [[dot-test_full_context_summary_from_details()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_missing_timestamp_uses_now()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_block_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_event_type()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_falls_back_to_message()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_from_agent_id()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_summary_from_non_allowed_action()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_user_key_fallback()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[SimpleNamespace]] - code
- [[TestFromAuditChainEntry]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_audit_entry()]] - code - gateway/tests/test_soc_realtime_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_audit_entry
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_Severity]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_dot-verify_export_integrity]]

## Top bridge nodes
- [[TestFromAuditChainEntry]] - degree 12, connects to 3 communities
- [[_audit_entry()]] - degree 12, connects to 2 communities
