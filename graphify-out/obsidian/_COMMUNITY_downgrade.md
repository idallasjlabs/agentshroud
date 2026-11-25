---
type: community
members: 6
---

# downgrade

**Members:** 6 nodes

## Members
- [[dot-test_blocked_on_invalid()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_dry_run()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_successful_downgrade()]] - code - gateway/tests/test_agentshroud_manager.py
- [[Downgrade OpenClaw to a previous version. Requires security review (risk of…]] - rationale - gateway/tools/agentshroud_manager.py
- [[TestDowngrade]] - code - gateway/tests/test_agentshroud_manager.py
- [[downgrade()]] - code - gateway/tools/agentshroud_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/downgrade
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_agentshroud_manager.py]]
- 3 edges to [[_COMMUNITY_upgrade]]
- 2 edges to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_check_current_version]]
- 1 edge to [[_COMMUNITY_rollback]]

## Top bridge nodes
- [[downgrade()]] - degree 13, connects to 5 communities
- [[TestDowngrade]] - degree 4, connects to 1 community
- [[dot-test_successful_downgrade()]] - degree 3, connects to 1 community
