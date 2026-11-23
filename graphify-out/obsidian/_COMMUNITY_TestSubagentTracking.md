---
type: community
members: 5
---

# TestSubagentTracking

**Members:** 5 nodes

## Members
- [[dot-test_deregister_subagent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_list_active_subagents()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_register_subagent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_subagent_info_has_spawn_time()]] - code - gateway/tests/test_subagent_monitor.py
- [[TestSubagentTracking]] - code - gateway/tests/test_subagent_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSubagentTracking
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_SubagentMonitor]]

## Top bridge nodes
- [[TestSubagentTracking]] - degree 5, connects to 1 community
