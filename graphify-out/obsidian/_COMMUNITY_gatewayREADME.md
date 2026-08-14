---
type: community
members: 17
---

# gateway/README.md

**Members:** 17 nodes

## Members
- [[.guard()]] - code - gateway/tests/test_context_guard.py
- [[.test_empty_provenance_for_unknown_session()]] - code - gateway/tests/test_context_guard.py
- [[.test_few_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_normal_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_normal_sized_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_oversized_message_blocked()]] - code - gateway/tests/test_context_guard.py
- [[.test_repeated_pattern_flagged()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_hash_integrity()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_provenance_ordering()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_tagging_basic()]] - code - gateway/tests/test_context_guard.py
- [[.test_separate_sessions_isolated()]] - code - gateway/tests/test_context_guard.py
- [[.test_short_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[Check if message should be allowed, with detailed findings.      Args         t]] - rationale - gateway/security/context_guard.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py
- [[check_message()]] - code - gateway/security/context_guard.py
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gateway/READMEmd
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Egress & RBAC Security Core]]
- 3 edges to [[_COMMUNITY_Planning Docs]]
- 3 edges to [[_COMMUNITY_Audit Export Pipeline]]

## Top bridge nodes
- [[TestCheckMessage]] - degree 9, connects to 2 communities
- [[TestSourceTagging]] - degree 9, connects to 2 communities
- [[test_context_guard.py]] - degree 5, connects to 2 communities
- [[check_message()]] - degree 11, connects to 1 community
- [[.guard()]] - degree 2, connects to 1 community