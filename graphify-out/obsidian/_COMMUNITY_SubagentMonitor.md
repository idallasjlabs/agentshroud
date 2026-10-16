---
type: community
cohesion: 0.05
members: 57
---

# SubagentMonitor

**Cohesion:** 0.05 - loosely connected
**Members:** 57 nodes

## Members
- [[dot-__init__()_23]] - code - gateway/security/subagent_monitor.py
- [[dot-_log_event()]] - code - gateway/security/subagent_monitor.py
- [[dot-check_tool_usage()]] - code - gateway/security/subagent_monitor.py
- [[dot-deregister()]] - code - gateway/security/subagent_monitor.py
- [[dot-get_active()]] - code - gateway/security/subagent_monitor.py
- [[dot-get_audit_log()]] - code - gateway/security/subagent_monitor.py
- [[dot-get_flagged_events()]] - code - gateway/security/subagent_monitor.py
- [[dot-kill_agent()]] - code - gateway/security/subagent_monitor.py
- [[dot-kill_all()]] - code - gateway/security/subagent_monitor.py
- [[dot-register_spawn()]] - code - gateway/security/subagent_monitor.py
- [[dot-test_audit_filterable_by_agent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_audit_has_timestamps()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_default_mode_is_enforce()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_deregister_frees_slot()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_deregister_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_deregister_subagent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_enforce_mode_blocks_over_limit()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_enforce_mode_blocks_trust_violation()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_generous_concurrent_default()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_kill_logs_event()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_kill_specific_agent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_kill_switch_marks_all_for_termination()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_kill_switch_propagates_to_children()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_list_active_subagents()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_monitor_mode_allows_all_tools()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_monitor_mode_allows_over_limit()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_nested_subagent_inherits_chain()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_register_subagent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_spawn_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_subagent_cannot_exceed_parent()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_subagent_info_has_spawn_time()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_subagent_inherits_parent_trust()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_tool_usage_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_tool_within_trust_allowed()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_trust_inheritance_default_on()]] - code - gateway/tests/test_subagent_monitor.py
- [[dot-test_trust_violation_flagged()]] - code - gateway/tests/test_subagent_monitor.py
- [[Default mode is enforce after v0.8.0 enforcement hardening.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[If sub-agent tries tool above its trust, flag it.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[In monitor mode, even trust violations are allowed (just flagged).]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Monitor mode flags but allows.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[SubagentInfo]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor]] - code - gateway/security/subagent_monitor.py
- [[TestAuditTrail_1]] - code - gateway/tests/test_subagent_monitor.py
- [[TestConcurrentLimits]] - code - gateway/tests/test_subagent_monitor.py
- [[TestKillSwitch]] - code - gateway/tests/test_subagent_monitor.py
- [[TestPermissionMonitoring]] - code - gateway/tests/test_subagent_monitor.py
- [[TestSubagentMonitorConfig]] - code - gateway/tests/test_subagent_monitor.py
- [[TestSubagentTracking]] - code - gateway/tests/test_subagent_monitor.py
- [[TestTrustInheritance]] - code - gateway/tests/test_subagent_monitor.py
- [[ToolCheckResult]] - code - gateway/security/subagent_monitor.py
- [[default_config()]] - code - gateway/tests/test_subagent_monitor.py
- [[monitor()]] - code - gateway/tests/test_subagent_monitor.py
- [[monitor_config()]] - code - gateway/tests/test_subagent_monitor.py
- [[strict_config()_1]] - code - gateway/tests/test_subagent_monitor.py
- [[strict_monitor()]] - code - gateway/tests/test_subagent_monitor.py
- [[subagent_monitor.py]] - code - gateway/security/subagent_monitor.py
- [[test_subagent_monitor.py]] - code - gateway/tests/test_subagent_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SubagentMonitor
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_AlertDispatcher]]
- 24 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine]]

## Top bridge nodes
- [[subagent_monitor.py]] - degree 10, connects to 6 communities
- [[SubagentMonitor]] - degree 46, connects to 3 communities
- [[test_subagent_monitor.py]] - degree 15, connects to 2 communities
- [[TestTrustInheritance]] - degree 9, connects to 2 communities
- [[TestAuditTrail_1]] - degree 8, connects to 2 communities
