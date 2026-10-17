---
type: community
members: 55
---

# test_prompt_guard.py

**Members:** 55 nodes

## Members
- [[dot-test_auto_revert_restores_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_critical_logged_when_setting_non_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_custom_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_mode_is_enforce()_1]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_revert_minutes_is_30()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_get_mode_default_enforce()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_get_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_invalid_mode_returns_400()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_mode_request_defaults()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_no_critical_when_setting_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_response_includes_previous_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_response_includes_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_response_includes_timestamp()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_returns_monitor_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_returns_observatory_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_revert_minutes_clamped_max()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_revert_minutes_clamped_min()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_revert_task_created_on_put()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_second_put_cancels_previous_task()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_enforce_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_mode_cancels_previous_revert_task()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_mode_clamps_high_revert()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_mode_enforce_revert_task_is_noop()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_mode_invalid_returns_400()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_mode_monitor_auto_reverts()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_monitor_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_observatory_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_valid_modes_constant()]] - code - gateway/tests/test_observatory_mode.py
- [[A revert task is created (and is an asyncio.Task).]] - rationale - gateway/tests/test_observatory_mode.py
- [[Auto-revert task sets mode back to enforce after delay.]] - rationale - gateway/tests/test_observatory_mode.py
- [[FastAPI_1]] - code - gateway/tests/test_observatory_mode.py
- [[Integration tests for Observatory Mode API endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Minimal FastAPI app that mounts the management router with auth bypassed.]] - rationale - gateway/tests/test_observatory_mode.py
- [[ModeRequest]] - code - gateway/web/api.py
- [[Reset AGENTSHROUD_MODE and cancel any revert task between tests.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Second PUT cancels the first revert task.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Set AGENTSHROUD_MODE at runtime with automatic revert to 'enforce'.]] - rationale - gateway/web/api.py
- [[Test GET managemode endpoint returns correct structure.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test POST managemode endpoint requestresponse.]] - rationale - gateway/tests/test_observatory_mode.py
- [[TestAutoRevert]] - code - gateway/tests/test_observatory_mode.py
- [[TestCriticalLogging]] - code - gateway/tests/test_observatory_mode.py
- [[TestGetMode]] - code - gateway/tests/test_observatory_mode.py
- [[TestMode]] - code - gateway/tests/test_web_api_coverage.py
- [[TestModeRequestModel]] - code - gateway/tests/test_observatory_mode.py
- [[TestObservatoryModeAPI]] - code - gateway/tests/test_observatory_mode.py
- [[TestSetMode]] - code - gateway/tests/test_observatory_mode.py
- [[_make_app()]] - code - gateway/tests/test_observatory_mode.py
- [[client()_4]] - code - gateway/tests/test_observatory_mode.py
- [[reset_env_and_task()]] - code - gateway/tests/test_observatory_mode.py
- [[revert_after_minutes above 480 is clamped to 480.]] - rationale - gateway/tests/test_observatory_mode.py
- [[revert_after_minutes below 1 is clamped to 1.]] - rationale - gateway/tests/test_observatory_mode.py
- [[set_mode()]] - code - gateway/web/api.py
- [[test_observatory_mode.py]] - code - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_prompt_guardpy
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_ModeRequest]]
- 19 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 8 edges to [[_COMMUNITY_AuditChain]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_KillSwitchMonitor (3)]]
- 2 edges to [[_COMMUNITY_api.py (2)_1]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 1 edge to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_ModeRequest (3)]]

## Top bridge nodes
- [[ModeRequest]] - degree 47, connects to 8 communities
- [[test_observatory_mode.py]] - degree 19, connects to 5 communities
- [[TestSetMode]] - degree 14, connects to 2 communities
- [[TestGetMode]] - degree 9, connects to 2 communities
- [[TestModeRequestModel]] - degree 8, connects to 2 communities
