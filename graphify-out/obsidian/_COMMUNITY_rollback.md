---
type: community
members: 6
---

# rollback

**Members:** 6 nodes

## Members
- [[dot-test_no_history()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_no_previous_version()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_successful_rollback()]] - code - gateway/tests/test_agentshroud_manager.py
- [[Rollback to the previous version.]] - rationale - gateway/tools/agentshroud_manager.py
- [[TestRollback]] - code - gateway/tests/test_agentshroud_manager.py
- [[rollback()]] - code - gateway/tools/agentshroud_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/rollback
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_upgrade]]
- 3 edges to [[_COMMUNITY_test_agentshroud_manager.py]]
- 2 edges to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_downgrade]]

## Top bridge nodes
- [[rollback()]] - degree 11, connects to 4 communities
- [[TestRollback]] - degree 4, connects to 1 community
- [[dot-test_no_previous_version()]] - degree 3, connects to 1 community
- [[dot-test_successful_rollback()]] - degree 3, connects to 1 community
