---
type: community
cohesion: 0.29
members: 7
---

# TestToolAuthorization

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-test_allowed_tool()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_in_monitor_still_allows()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_tool_cronjob()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_tool_delegate_task()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_tool_memory()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_tool_send_message()]] - code - gateway/tests/test_subagent_governance.py
- [[TestToolAuthorization]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestToolAuthorization
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_SubagentGovernance]]
- 2 edges to [[_COMMUNITY_GovernanceAction]]
- 1 edge to [[_COMMUNITY_dot-_check_budget]]

## Top bridge nodes
- [[TestToolAuthorization]] - degree 12, connects to 3 communities
