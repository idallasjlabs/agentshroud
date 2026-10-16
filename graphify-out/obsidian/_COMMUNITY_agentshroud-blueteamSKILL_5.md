---
type: community
cohesion: 0.29
members: 7
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-guard()_3]] - code - gateway/tests/test_context_guard.py
- [[dot-test_empty_provenance_for_unknown_session()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_hash_integrity()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_provenance_ordering()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_tagging_basic()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_separate_sessions_isolated()]] - code - gateway/tests/test_context_guard.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]
- 1 edge to [[_COMMUNITY_ContextSegment]]

## Top bridge nodes
- [[TestSourceTagging]] - degree 9, connects to 3 communities
- [[dot-guard()_3]] - degree 2, connects to 1 community
