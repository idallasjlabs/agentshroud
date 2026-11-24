---
type: community
members: 35
---

# ModeRequest

**Members:** 35 nodes

## Members
- [[dot-test_auto_revert_restores_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_auto_revert_timer_logic()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_custom_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_get_mode_default_enforce()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_get_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_mode_request_defaults()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_revert_task_created_on_put()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_second_put_cancels_previous_task()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_mode_cancels_previous_revert_task()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_mode_clamps_high_revert()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_mode_enforce_revert_task_is_noop()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_mode_invalid_returns_400()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_mode_monitor_auto_reverts()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_set_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_valid_modes_constant()]] - code - gateway/tests/test_observatory_mode.py
- [[A revert task is created (and is an asyncio.Task).]] - rationale - gateway/tests/test_observatory_mode.py
- [[Auto-revert task sets mode back to enforce after delay.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Integration tests for Observatory Mode API endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[ModeRequest]] - code - gateway/web/api.py
- [[Second PUT cancels the first revert task.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Set AGENTSHROUD_MODE at runtime with automatic revert to 'enforce'.]] - rationale - gateway/web/api.py
- [[Test GET managemode endpoint returns correct structure.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test POST managemode endpoint requestresponse.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test auto-revert timer functionality.]] - rationale - gateway/tests/test_observatory_mode.py
- [[TestAutoRevert]] - code - gateway/tests/test_observatory_mode.py
- [[TestMode]] - code - gateway/tests/test_web_api_coverage.py
- [[TestModeRequestModel]] - code - gateway/tests/test_observatory_mode.py
- [[TestObservatoryModeAPI]] - code - gateway/tests/test_observatory_mode.py
- [[_auto_revert()]] - code - gateway/web/api.py
- [[asyncio_55]] - code
- [[fake_sleep()_2]] - code - gateway/tests/test_web_api_coverage.py
- [[fast_sleep()]] - code - gateway/tests/test_observatory_mode.py
- [[put_2]] - code
- [[set_mode()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ModeRequest
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_observatory_mode.py]]
- 4 edges to [[_COMMUNITY_api.py]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY__engine]]
- 2 edges to [[_COMMUNITY_TestObservatoryMode]]

## Top bridge nodes
- [[ModeRequest]] - degree 18, connects to 3 communities
- [[set_mode()]] - degree 9, connects to 2 communities
- [[asyncio_55]] - degree 8, connects to 2 communities
- [[TestMode]] - degree 9, connects to 1 community
- [[dot-test_revert_task_created_on_put()]] - degree 6, connects to 1 community
