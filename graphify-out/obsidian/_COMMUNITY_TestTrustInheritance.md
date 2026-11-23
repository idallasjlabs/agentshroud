---
type: community
members: 7
---

# TestTrustInheritance

**Members:** 7 nodes

## Members
- [[dot-test_nested_subagent_inherits_chain()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_subagent_cannot_exceed_parent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_subagent_inherits_parent_trust()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_tool_within_trust_allowed()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_trust_violation_flagged()]] - code - gateway/tests/test_subagent_monitor.py
- [[If sub-agent tries tool above its trust, flag it.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[TestTrustInheritance]] - code - gateway/tests/test_subagent_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTrustInheritance
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_SubagentMonitor]]

## Top bridge nodes
- [[TestTrustInheritance]] - degree 6, connects to 1 community
