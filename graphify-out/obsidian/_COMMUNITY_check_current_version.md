---
type: community
members: 6
---

# check_current_version

**Members:** 6 nodes

## Members
- [[dot-test_after_upgrade()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_no_history_unknown()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_with_env_var()]] - code - gateway/tests/test_agentshroud_manager.py
- [[Check the currently installed OpenClaw version.]] - rationale - gateway/tools/agentshroud_manager.py
- [[TestCheckCurrentVersion]] - code - gateway/tests/test_agentshroud_manager.py
- [[check_current_version()]] - code - gateway/tools/agentshroud_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_current_version
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_upgrade]]
- 3 edges to [[_COMMUNITY_test_agentshroud_manager.py]]
- 2 edges to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_downgrade]]

## Top bridge nodes
- [[check_current_version()]] - degree 12, connects to 4 communities
- [[TestCheckCurrentVersion]] - degree 4, connects to 1 community
- [[dot-test_after_upgrade()]] - degree 3, connects to 1 community
