---
type: community
cohesion: 0.20
members: 10
---

# Prompt Guard

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.pg()_1]] - code - gateway/tests/test_prompt_guard.py
- [[.test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[Explicit ignore-instructions payload embedded in a tool result.]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestToolResultScan]] - code - gateway/tests/test_prompt_guard.py
- [[Tests for indirect prompt injection detection in tool results.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Tool result scan blocks at score ≥ 0.6 vs direct scan threshold of 0.8.]] - rationale - gateway/tests/test_prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Prompt_Guard
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Pipeline Unit]]
- 1 edge to [[_COMMUNITY_Context Integrity]]
- 1 edge to [[_COMMUNITY_Prompt Guard]]

## Top bridge nodes
- [[TestToolResultScan]] - degree 11, connects to 4 communities
- [[.pg()_1]] - degree 2, connects to 1 community