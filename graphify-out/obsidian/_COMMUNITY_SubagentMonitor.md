---
type: community
members: 47
---

# SubagentMonitor

**Members:** 47 nodes

## Members
- [[dot-__init__()_67]] - code - gateway/security/subagent_monitor.py
- [[dot-_log_event()]] - code - gateway/security/subagent_monitor.py
- [[dot-check_tool_usage()]] - code - gateway/security/subagent_monitor.py
- [[dot-deregister()]] - code - gateway/security/subagent_monitor.py
- [[dot-get_active()]] - code - gateway/security/subagent_monitor.py
- [[dot-get_audit_log()_3]] - code - gateway/security/subagent_monitor.py
- [[dot-get_flagged_events()]] - code - gateway/security/subagent_monitor.py
- [[dot-kill_agent()]] - code - gateway/security/subagent_monitor.py
- [[dot-kill_all()]] - code - gateway/security/subagent_monitor.py
- [[dot-register_spawn()]] - code - gateway/security/subagent_monitor.py
- [[dot-test_audit_filterable_by_agent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_audit_has_timestamps()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_deregister_frees_slot()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_deregister_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_enforce_mode_blocks_over_limit()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_enforce_mode_blocks_trust_violation()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_kill_logs_event()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_kill_specific_agent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_kill_switch_marks_all_for_termination()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_kill_switch_propagates_to_children()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_monitor_mode_allows_all_tools()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_monitor_mode_allows_over_limit()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_spawn_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_tool_usage_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[Enum_18]] - code
- [[In monitor mode, even trust violations are allowed (just flagged).]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Monitor mode flags but allows.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[SubagentEvent]] - code - gateway/security/subagent_monitor.py
- [[SubagentEventType]] - code - gateway/security/subagent_monitor.py
- [[SubagentInfo]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitorConfig]] - code - gateway/security/subagent_monitor.py
- [[TestAuditTrail_2]] - code - gateway/tests/test_subagent_monitor.py
- [[TestConcurrentLimits]] - code - gateway/tests/test_subagent_monitor.py
- [[TestKillSwitch_1]] - code - gateway/tests/test_subagent_monitor.py
- [[TestPermissionMonitoring]] - code - gateway/tests/test_subagent_monitor.py
- [[Tests for sub-agent oversight and monitoring.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[ToolCheckResult]] - code - gateway/security/subagent_monitor.py
- [[default_config()_2]] - code - gateway/tests/test_subagent_monitor.py
- [[fixture_44]] - code
- [[monitor()_1]] - code - gateway/tests/test_subagent_monitor.py
- [[monitor_config()_2]] - code - gateway/tests/test_subagent_monitor.py
- [[str_12]] - code
- [[strict_config()_1]] - code - gateway/tests/test_subagent_monitor.py
- [[strict_monitor()]] - code - gateway/tests/test_subagent_monitor.py
- [[subagent_monitor.py_2]] - code - gateway/security/subagent_monitor.py
- [[test_subagent_monitor.py]] - code - gateway/tests/test_subagent_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SubagentMonitor
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_TestModuleConfigDefaults]]
- 2 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_TestAuth_1]]
- 1 edge to [[_COMMUNITY_TestTrustInheritance]]
- 1 edge to [[_COMMUNITY_TestSubagentMonitorConfig]]
- 1 edge to [[_COMMUNITY_TestSubagentTracking]]

## Top bridge nodes
- [[SubagentMonitor]] - degree 20, connects to 5 communities
- [[SubagentMonitorConfig]] - degree 12, connects to 4 communities
- [[test_subagent_monitor.py]] - degree 17, connects to 3 communities
- [[subagent_monitor.py_2]] - degree 10, connects to 2 communities
- [[SubagentEvent]] - degree 6, connects to 2 communities
