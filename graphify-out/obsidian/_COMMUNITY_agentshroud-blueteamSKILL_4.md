---
type: community
cohesion: 0.33
members: 10
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.33 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-test_few_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_normal_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_normal_sized_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_oversized_message_blocked()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_repeated_pattern_flagged()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_short_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[Check if message should be allowed, with detailed findings.      Args         t]] - rationale - gateway/security/context_guard.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[check_message()]] - code - gateway/security/context_guard.py
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_6]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_5]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_3]]

## Top bridge nodes
- [[test_context_guard.py]] - degree 5, connects to 3 communities
- [[check_message()]] - degree 11, connects to 2 communities
- [[TestCheckMessage]] - degree 9, connects to 2 communities
