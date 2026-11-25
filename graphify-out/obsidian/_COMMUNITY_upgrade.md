---
type: community
members: 16
---

# upgrade

**Members:** 16 nodes

## Members
- [[dot-test_after_operations()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_blocked_on_invalid_version()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_dry_run()_1]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_empty_history()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_sequential_upgrades()]] - code - gateway/tests/test_agentshroud_manager.py
- [[dot-test_successful_upgrade()]] - code - gateway/tests/test_agentshroud_manager.py
- [[Any_82]] - code
- [[Connection_3]] - code
- [[Get SQLite connection for version history.]] - rationale - gateway/tools/agentshroud_manager.py
- [[List all version history entries.]] - rationale - gateway/tools/agentshroud_manager.py
- [[TestListVersions]] - code - gateway/tests/test_agentshroud_manager.py
- [[TestUpgrade_1]] - code - gateway/tests/test_agentshroud_manager.py
- [[Upgrade OpenClaw to a target version. Requires a prior security review and…]] - rationale - gateway/tools/agentshroud_manager.py
- [[_get_db()]] - code - gateway/tools/agentshroud_manager.py
- [[list_versions()]] - code - gateway/tools/agentshroud_manager.py
- [[upgrade()]] - code - gateway/tools/agentshroud_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/upgrade
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_agentshroud_manager.py]]
- 4 edges to [[_COMMUNITY_check_current_version]]
- 4 edges to [[_COMMUNITY_rollback]]
- 4 edges to [[_COMMUNITY_version_routes.py]]
- 3 edges to [[_COMMUNITY_downgrade]]

## Top bridge nodes
- [[upgrade()]] - degree 18, connects to 5 communities
- [[_get_db()]] - degree 8, connects to 4 communities
- [[Any_82]] - degree 6, connects to 4 communities
- [[list_versions()]] - degree 10, connects to 2 communities
- [[TestUpgrade_1]] - degree 5, connects to 1 community
