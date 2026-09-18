---
type: community
cohesion: 0.33
members: 10
---

# check_message()

**Cohesion:** 0.33 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_few_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_normal_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_normal_sized_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_oversized_message_blocked()]] - code - gateway/tests/test_context_guard.py
- [[.test_repeated_pattern_flagged()]] - code - gateway/tests/test_context_guard.py
- [[.test_short_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[Check if message should be allowed, with detailed findings.      Args         t]] - rationale - gateway/security/context_guard.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[check_message()]] - code - gateway/security/context_guard.py
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_message
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_tool_result_injection.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_.analyze_message()]]
- 1 edge to [[_COMMUNITY_TestSourceTagging]]

## Top bridge nodes
- [[test_context_guard.py]] - degree 5, connects to 3 communities
- [[check_message()]] - degree 11, connects to 2 communities
- [[TestCheckMessage]] - degree 9, connects to 2 communities