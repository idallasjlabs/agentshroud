---
type: community
cohesion: 0.06
members: 39
---

# test_observatory_mode.py

**Cohesion:** 0.06 - loosely connected
**Members:** 39 nodes

## Members
- [[dot-test_auto_revert_restores_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_mode_is_enforce()_7]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_revert_minutes_is_30()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_get_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_invalid_mode_returns_400()]] - code - gateway/tests/test_observatory_mode.py
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
- [[dot-test_set_monitor_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_observatory_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[A revert task is created (and is an asyncio.Task).]] - rationale - gateway/tests/test_observatory_mode.py
- [[Auto-revert task sets mode back to enforce after delay.]] - rationale - gateway/tests/test_observatory_mode.py
- [[FastAPI_4]] - code - gateway/tests/test_observatory_mode.py
- [[Integration tests for Observatory Mode API endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Minimal FastAPI app that mounts the management router with auth bypassed.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Reset AGENTSHROUD_MODE and cancel any revert task between tests.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Second PUT cancels the first revert task.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Set AGENTSHROUD_MODE at runtime with automatic revert to 'enforce'.]] - rationale - gateway/web/api.py
- [[Test GET managemode endpoint returns correct structure.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test POST managemode endpoint requestresponse.]] - rationale - gateway/tests/test_observatory_mode.py
- [[TestAutoRevert]] - code - gateway/tests/test_observatory_mode.py
- [[TestGetMode]] - code - gateway/tests/test_observatory_mode.py
- [[TestObservatoryModeAPI]] - code - gateway/tests/test_observatory_mode.py
- [[TestSetMode]] - code - gateway/tests/test_observatory_mode.py
- [[_make_app()]] - code - gateway/tests/test_observatory_mode.py
- [[client()_19]] - code - gateway/tests/test_observatory_mode.py
- [[reset_env_and_task()]] - code - gateway/tests/test_observatory_mode.py
- [[revert_after_minutes above 480 is clamped to 480.]] - rationale - gateway/tests/test_observatory_mode.py
- [[revert_after_minutes below 1 is clamped to 1.]] - rationale - gateway/tests/test_observatory_mode.py
- [[set_mode()_1]] - code - gateway/web/api.py
- [[test_observatory_mode.py]] - code - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_observatory_modepy
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 12 edges to [[_COMMUNITY_ModeRequest]]
- 6 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_load_config]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_TestObservatoryMode]]
- 1 edge to [[_COMMUNITY_TestKillSwitchVerification]]

## Top bridge nodes
- [[test_observatory_mode.py]] - degree 19, connects to 6 communities
- [[TestSetMode]] - degree 14, connects to 3 communities
- [[TestGetMode]] - degree 9, connects to 3 communities
- [[TestAutoRevert]] - degree 8, connects to 3 communities
- [[TestObservatoryModeAPI]] - degree 8, connects to 3 communities
