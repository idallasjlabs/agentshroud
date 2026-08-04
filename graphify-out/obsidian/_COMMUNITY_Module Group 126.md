---
type: community
cohesion: 0.09
members: 37
---

# Module Group 126

**Cohesion:** 0.09 - loosely connected
**Members:** 37 nodes

## Members
- [[.test_auto_revert_restores_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_critical_logged_when_setting_non_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_custom_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_default_mode_is_enforce()_3]] - code - gateway/tests/test_observatory_mode.py
- [[.test_default_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_mode_default_enforce()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_mode_request_defaults()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_no_critical_when_setting_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_response_includes_timestamp()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_returns_monitor_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_returns_observatory_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_revert_task_created_on_put()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_second_put_cancels_previous_task()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_set_mode_cancels_previous_revert_task()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_set_mode_clamps_high_revert()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_set_mode_enforce_revert_task_is_noop()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_set_mode_invalid_returns_400()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_set_mode_monitor_auto_reverts()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_valid_modes_constant()]] - code - gateway/tests/test_observatory_mode.py
- [[A revert task is created (and is an asyncio.Task).]] - rationale - gateway/tests/test_observatory_mode.py
- [[Auto-revert task sets mode back to enforce after delay.]] - rationale - gateway/tests/test_observatory_mode.py
- [[FastAPI_2]] - code - gateway/tests/test_observatory_mode.py
- [[Minimal FastAPI app that mounts the management router with auth bypassed.]] - rationale - gateway/tests/test_observatory_mode.py
- [[ModeRequest]] - code - gateway/web/api.py
- [[Reset AGENTSHROUD_MODE and cancel any revert task between tests.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Second PUT cancels the first revert task.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Set AGENTSHROUD_MODE at runtime with automatic revert to 'enforce'.]] - rationale - gateway/web/api.py
- [[TestAutoRevert]] - code - gateway/tests/test_observatory_mode.py
- [[TestCriticalLogging]] - code - gateway/tests/test_observatory_mode.py
- [[TestGetMode]] - code - gateway/tests/test_observatory_mode.py
- [[TestMode]] - code - gateway/tests/test_web_api_coverage.py
- [[TestModeRequestModel]] - code - gateway/tests/test_observatory_mode.py
- [[_make_app()]] - code - gateway/tests/test_observatory_mode.py
- [[client()_8]] - code - gateway/tests/test_observatory_mode.py
- [[reset_env_and_task()]] - code - gateway/tests/test_observatory_mode.py
- [[set_mode()_1]] - code - gateway/web/api.py
- [[test_observatory_mode.py]] - code - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_126
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_Module Group 70]]
- 9 edges to [[_COMMUNITY_Module Group 98]]
- 6 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 6 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 6 edges to [[_COMMUNITY_Module Group 85]]
- 4 edges to [[_COMMUNITY_Module Group 146]]
- 3 edges to [[_COMMUNITY_Module Group 74]]
- 2 edges to [[_COMMUNITY_Module Group 233]]
- 2 edges to [[_COMMUNITY_Module Group 488]]
- 2 edges to [[_COMMUNITY_Module Group 336]]
- 2 edges to [[_COMMUNITY_Web API & Dashboard UI]]
- 1 edge to [[_COMMUNITY_Module Group 83]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 310]]

## Top bridge nodes
- [[ModeRequest]] - degree 43, connects to 9 communities
- [[test_observatory_mode.py]] - degree 20, connects to 9 communities
- [[TestGetMode]] - degree 10, connects to 4 communities
- [[TestAutoRevert]] - degree 9, connects to 4 communities
- [[TestModeRequestModel]] - degree 9, connects to 4 communities
