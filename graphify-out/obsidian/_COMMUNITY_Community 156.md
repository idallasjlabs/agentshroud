---
type: community
cohesion: 0.05
members: 42
---

# Community 156

**Cohesion:** 0.05 - loosely connected
**Members:** 42 nodes

## Members
- [[.test_auto_revert_restores_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_critical_logged_when_setting_non_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_default_mode_is_enforce()_3]] - code - gateway/tests/test_observatory_mode.py
- [[.test_default_revert_minutes_is_30()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_invalid_mode_returns_400()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_no_critical_when_setting_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_response_includes_previous_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_response_includes_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_response_includes_timestamp()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_returns_monitor_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_returns_observatory_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_revert_minutes_clamped_max()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_revert_minutes_clamped_min()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_revert_task_created_on_put()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_second_put_cancels_previous_task()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_set_enforce_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_set_monitor_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_set_observatory_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_set_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[A revert task is created (and is an asyncio.Task).]] - rationale - gateway/tests/test_observatory_mode.py
- [[Auto-revert task sets mode back to enforce after delay.]] - rationale - gateway/tests/test_observatory_mode.py
- [[FastAPI_3]] - code - gateway/tests/test_observatory_mode.py
- [[Integration tests for Observatory Mode API endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Minimal FastAPI app that mounts the management router with auth bypassed.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Reset AGENTSHROUD_MODE and cancel any revert task between tests.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Second PUT cancels the first revert task.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Set AGENTSHROUD_MODE at runtime with automatic revert to 'enforce'.]] - rationale - gateway/web/api.py
- [[Test GET managemode endpoint returns correct structure.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test POST managemode endpoint requestresponse.]] - rationale - gateway/tests/test_observatory_mode.py
- [[TestAutoRevert]] - code - gateway/tests/test_observatory_mode.py
- [[TestCriticalLogging]] - code - gateway/tests/test_observatory_mode.py
- [[TestGetMode]] - code - gateway/tests/test_observatory_mode.py
- [[TestObservatoryModeAPI]] - code - gateway/tests/test_observatory_mode.py
- [[TestSetMode]] - code - gateway/tests/test_observatory_mode.py
- [[_make_app()]] - code - gateway/tests/test_observatory_mode.py
- [[client()_11]] - code - gateway/tests/test_observatory_mode.py
- [[reset_env_and_task()]] - code - gateway/tests/test_observatory_mode.py
- [[revert_after_minutes above 480 is clamped to 480.]] - rationale - gateway/tests/test_observatory_mode.py
- [[revert_after_minutes below 1 is clamped to 1.]] - rationale - gateway/tests/test_observatory_mode.py
- [[set_mode()_1]] - code - gateway/web/api.py
- [[test_observatory_mode.py]] - code - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_156
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 25]]
- 13 edges to [[_COMMUNITY_Community 29]]
- 7 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 1 edge to [[_COMMUNITY_Community 157]]
- 1 edge to [[_COMMUNITY_Community 457]]
- 1 edge to [[_COMMUNITY_Community 37]]

## Top bridge nodes
- [[test_observatory_mode.py]] - degree 19, connects to 5 communities
- [[TestSetMode]] - degree 14, connects to 3 communities
- [[TestGetMode]] - degree 9, connects to 3 communities
- [[TestAutoRevert]] - degree 8, connects to 3 communities
- [[TestObservatoryModeAPI]] - degree 8, connects to 3 communities