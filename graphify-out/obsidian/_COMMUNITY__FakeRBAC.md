---
type: community
cohesion: 0.29
members: 11
---

# _FakeRBAC

**Cohesion:** 0.29 - loosely connected
**Members:** 11 nodes

## Members
- [[.check_permission()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_get_rbac_manager_builds_real_manager()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_group_admin_with_teams_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_group_admin_without_teams_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_owner_delegates_to_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_require_allowed_does_not_raise()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_require_denied_raises_403_with_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_require_denied_without_reason_uses_forbidden()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Minimal RBAC stand-in with controllable check_permission results.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[TestSCLCaller]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_FakeRBAC]] - code - gateway/tests/test_soc_realtime_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeRBAC
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_ingest_apimain.py]]
- 6 edges to [[_COMMUNITY_BaseModel]]
- 3 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_SOCWebSocketHandler]]

## Top bridge nodes
- [[_FakeRBAC]] - degree 17, connects to 4 communities
- [[TestSCLCaller]] - degree 14, connects to 4 communities
- [[.test_is_group_admin_with_teams_config()]] - degree 4, connects to 2 communities
- [[.test_get_rbac_manager_builds_real_manager()]] - degree 3, connects to 1 community
- [[.test_is_group_admin_without_teams_config()]] - degree 3, connects to 1 community