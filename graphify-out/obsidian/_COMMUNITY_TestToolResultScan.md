---
type: community
members: 9
---

# TestToolResultScan

**Members:** 9 nodes

## Members
- [[dot-test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[Explicit ignore-instructions payload embedded in a tool result.]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestToolResultScan]] - code - gateway/tests/test_prompt_guard.py
- [[Tests for indirect prompt injection detection in tool results.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Tool result scan blocks at score ≥ 0.6 vs direct scan threshold of 0.8.]] - rationale - gateway/tests/test_prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestToolResultScan
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_PromptGuard]]

## Top bridge nodes
- [[TestToolResultScan]] - degree 9, connects to 1 community
