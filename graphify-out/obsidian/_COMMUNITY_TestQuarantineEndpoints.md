---
type: community
cohesion: 0.40
members: 5
---

# TestQuarantineEndpoints

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[Test quarantine management endpoints in main.py.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestQuarantineEndpoints
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[TestQuarantineEndpoints]] - degree 6, connects to 2 communities