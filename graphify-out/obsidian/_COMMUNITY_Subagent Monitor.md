---
type: community
cohesion: 0.05
members: 58
---

# Subagent Monitor

**Cohesion:** 0.05 - loosely connected
**Members:** 58 nodes

## Members
- [[.__init__()_120]] - code - gateway/security/subagent_monitor.py
- [[._log_event()_1]] - code - gateway/security/subagent_monitor.py
- [[.check_tool_usage()]] - code - gateway/security/subagent_monitor.py
- [[.deregister()_1]] - code - gateway/security/subagent_monitor.py
- [[.get_active()]] - code - gateway/security/subagent_monitor.py
- [[.get_audit_log()_6]] - code - gateway/security/subagent_monitor.py
- [[.get_flagged_events()]] - code - gateway/security/subagent_monitor.py
- [[.kill_agent()]] - code - gateway/security/subagent_monitor.py
- [[.kill_all()]] - code - gateway/security/subagent_monitor.py
- [[.register_spawn()]] - code - gateway/security/subagent_monitor.py
- [[.test_audit_filterable_by_agent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_audit_has_timestamps()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_default_mode_is_enforce()_7]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_deregister_frees_slot()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_deregister_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_deregister_subagent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_enforce_mode_blocks_over_limit()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_enforce_mode_blocks_trust_violation()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_generous_concurrent_default()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_kill_logs_event()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_kill_specific_agent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_kill_switch_marks_all_for_termination()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_kill_switch_propagates_to_children()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_list_active_subagents()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_monitor_mode_allows_all_tools()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_monitor_mode_allows_over_limit()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_nested_subagent_inherits_chain()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_register_subagent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_spawn_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_cannot_exceed_parent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_info_has_spawn_time()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_inherits_parent_trust()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_tool_usage_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_tool_within_trust_allowed()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_trust_inheritance_default_on()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_trust_violation_flagged()]] - code - gateway/tests/test_subagent_monitor.py
- [[Default mode is enforce after v0.8.0 enforcement hardening._2]] - rationale - gateway/tests/test_subagent_monitor.py
- [[If sub-agent tries tool above its trust, flag it.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[In monitor mode, even trust violations are allowed (just flagged).]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Monitor mode flags but allows.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[SubagentEvent]] - code - gateway/security/subagent_monitor.py
- [[SubagentInfo]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor]] - code - gateway/security/subagent_monitor.py
- [[TestAuditTrail_2]] - code - gateway/tests/test_subagent_monitor.py
- [[TestConcurrentLimits]] - code - gateway/tests/test_subagent_monitor.py
- [[TestKillSwitch]] - code - gateway/tests/test_subagent_monitor.py
- [[TestPermissionMonitoring]] - code - gateway/tests/test_subagent_monitor.py
- [[TestSubagentMonitorConfig]] - code - gateway/tests/test_subagent_monitor.py
- [[TestSubagentTracking]] - code - gateway/tests/test_subagent_monitor.py
- [[TestTrustInheritance]] - code - gateway/tests/test_subagent_monitor.py
- [[ToolCheckResult]] - code - gateway/security/subagent_monitor.py
- [[default_config()_4]] - code - gateway/tests/test_subagent_monitor.py
- [[monitor()_1]] - code - gateway/tests/test_subagent_monitor.py
- [[monitor_config()_2]] - code - gateway/tests/test_subagent_monitor.py
- [[strict_config()_2]] - code - gateway/tests/test_subagent_monitor.py
- [[strict_monitor()]] - code - gateway/tests/test_subagent_monitor.py
- [[subagent_monitor.py]] - code - gateway/security/subagent_monitor.py
- [[test_subagent_monitor.py]] - code - gateway/tests/test_subagent_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Subagent_Monitor
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 14 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 12 edges to [[_COMMUNITY_OAuth & Metadata Guard]]
- 3 edges to [[_COMMUNITY_Resource Guard & Local Model Parity]]
- 2 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 2 edges to [[_COMMUNITY_Security Hardening]]
- 2 edges to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 2 edges to [[_COMMUNITY_Git Guard (security)]]
- 2 edges to [[_COMMUNITY_Security Audit]]
- 1 edge to [[_COMMUNITY_A2a Integration]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Scanner Integration Coverage]]
- 1 edge to [[_COMMUNITY_Session Security]]
- 1 edge to [[_COMMUNITY_Security Regressions V1 2]]

## Top bridge nodes
- [[SubagentMonitor]] - degree 47, connects to 10 communities
- [[SubagentEvent]] - degree 17, connects to 7 communities
- [[subagent_monitor.py]] - degree 12, connects to 7 communities
- [[test_subagent_monitor.py]] - degree 15, connects to 2 communities
- [[TestTrustInheritance]] - degree 9, connects to 2 communities