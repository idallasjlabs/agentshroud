---
type: community
cohesion: 0.08
members: 39
---

# Module Group 120

**Cohesion:** 0.08 - loosely connected
**Members:** 39 nodes

## Members
- [[.__init__()_103]] - code - gateway/soc/auth.py
- [[.__init__()_133]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[._event_fan_out()]] - code - gateway/soc/websocket.py
- [[._keepalive_loop()]] - code - gateway/soc/websocket.py
- [[._send_event()]] - code - gateway/soc/websocket.py
- [[.check_permission()_2]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.run()_5]] - code - gateway/soc/websocket.py
- [[.test_allowed()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_blocked()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_conversion_error_path()_3]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_conversion_error_path()_2]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_conversion_error_path()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_dict_allowed_without_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_dict_blocked_with_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_dict_form()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_get_rbac_manager_builds_real_manager()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_group_admin_with_teams_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_group_admin_without_teams_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_owner_delegates_to_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_object_form()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_object_form_with_defaults()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_require_allowed_does_not_raise()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_require_denied_raises_403_with_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_require_denied_without_reason_uses_forbidden()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_sanitized()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Main connection loop.]] - rationale - gateway/soc/websocket.py
- [[Manages a single wssoc client connection.]] - rationale - gateway/soc/websocket.py
- [[Minimal RBAC stand-in with controllable check_permission results.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[RBACManager_2]] - code - gateway/soc/auth.py
- [[Role_2]] - code - gateway/soc/auth.py
- [[SOCWebSocketHandler]] - code - gateway/soc/websocket.py
- [[SimpleNamespace]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Subscribe to EventBus and forward matching events to the client.]] - rationale - gateway/soc/websocket.py
- [[TestFromAnomalyAlert]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestFromEgressAttempt]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestFromPipelineResult]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestSCLCaller]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_get_rbac_manager()]] - code - gateway/soc/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_120
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_RBAC Configuration]]
- 16 edges to [[_COMMUNITY_SOC Authentication]]
- 13 edges to [[_COMMUNITY_Module Group 83]]
- 7 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 5 edges to [[_COMMUNITY_Module Group 207]]
- 3 edges to [[_COMMUNITY_Module Group 315]]
- 3 edges to [[_COMMUNITY_Module Group 270]]
- 3 edges to [[_COMMUNITY_Module Group 296]]
- 2 edges to [[_COMMUNITY_SOC Services & Health Status]]

## Top bridge nodes
- [[SOCWebSocketHandler]] - degree 39, connects to 8 communities
- [[_FakeRBAC_1]] - degree 17, connects to 3 communities
- [[SimpleNamespace]] - degree 14, connects to 3 communities
- [[TestSCLCaller]] - degree 14, connects to 3 communities
- [[TestFromEgressAttempt]] - degree 11, connects to 3 communities
