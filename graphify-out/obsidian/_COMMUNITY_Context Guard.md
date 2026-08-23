---
type: community
cohesion: 0.29
members: 7
---

# Context Guard

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.guard()]] - code - gateway/tests/test_context_guard.py
- [[.test_empty_provenance_for_unknown_session()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_hash_integrity()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_provenance_ordering()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_tagging_basic()]] - code - gateway/tests/test_context_guard.py
- [[.test_separate_sessions_isolated()]] - code - gateway/tests/test_context_guard.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Context_Guard
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Context Integrity]]
- 1 edge to [[_COMMUNITY_Context Guard]]

## Top bridge nodes
- [[TestSourceTagging]] - degree 9, connects to 3 communities
- [[.guard()]] - degree 2, connects to 1 community