---
type: community
cohesion: 0.04
members: 73
---

# Subagent Monitor

**Cohesion:** 0.04 - loosely connected
**Members:** 73 nodes

## Members
- [[.__init__()_94]] - code - gateway/security/subagent_monitor.py
- [[._log_event()]] - code - gateway/security/subagent_monitor.py
- [[.check_tool_usage()]] - code - gateway/security/subagent_monitor.py
- [[.deregister()]] - code - gateway/security/subagent_monitor.py
- [[.get_active()]] - code - gateway/security/subagent_monitor.py
- [[.get_audit_log()_3]] - code - gateway/security/subagent_monitor.py
- [[.get_flagged_events()]] - code - gateway/security/subagent_monitor.py
- [[.kill_agent()]] - code - gateway/security/subagent_monitor.py
- [[.kill_all()]] - code - gateway/security/subagent_monitor.py
- [[.register_spawn()]] - code - gateway/security/subagent_monitor.py
- [[.test_audit_filterable_by_agent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_audit_has_timestamps()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_consent_required_for_sensitive_ops()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_default_mode_is_enforce()_6]] - code - gateway/tests/test_subagent_monitor.py
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
- [[.test_session_cannot_impersonate()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_spawn_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_cannot_exceed_parent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_info_has_spawn_time()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_inherits_parent_trust()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_monitor_tracks_events()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_tool_usage_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_tool_within_trust_allowed()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_trust_cannot_exceed_max()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_trust_inheritance_default_on()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_trust_violation_flagged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_unregistered_agent_blocked()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_violation_drops_trust_significantly()]] - code - gateway/tests/test_security_audit_advanced.py
- [[A single violation should meaningfully impact trust.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Consent framework should be available for gating.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Default mode is enforce after v0.8.0 enforcement hardening._2]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Different sessions should have different identities.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[If sub-agent tries tool above its trust, flag it.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[In monitor mode, even trust violations are allowed (just flagged).]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Monitor mode flags but allows.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Subagent events should be trackable.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[SubagentEvent]] - code - gateway/security/subagent_monitor.py
- [[SubagentEventType]] - code - gateway/security/subagent_monitor.py
- [[SubagentInfo]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor]] - code - gateway/security/subagent_monitor.py
- [[Test trust boundaries and privilege escalation prevention.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestAuditTrail_2]] - code - gateway/tests/test_subagent_monitor.py
- [[TestConcurrentLimits]] - code - gateway/tests/test_subagent_monitor.py
- [[TestKillSwitch]] - code - gateway/tests/test_subagent_monitor.py
- [[TestPermissionMonitoring]] - code - gateway/tests/test_subagent_monitor.py
- [[TestPrivilegeEscalation]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestSubagentMonitorConfig]] - code - gateway/tests/test_subagent_monitor.py
- [[TestSubagentTracking]] - code - gateway/tests/test_subagent_monitor.py
- [[TestTrustInheritance]] - code - gateway/tests/test_subagent_monitor.py
- [[ToolCheckResult]] - code - gateway/security/subagent_monitor.py
- [[Trust score should have an upper bound.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Unregistered agents should not be trusted.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[default_config()_3]] - code - gateway/tests/test_subagent_monitor.py
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
- 27 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 21 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 12 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 9 edges to [[_COMMUNITY_Alert Dispatcher]]
- 5 edges to [[_COMMUNITY_Module Group 110]]
- 3 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 3 edges to [[_COMMUNITY_Module Group 66]]
- 2 edges to [[_COMMUNITY_Module Group 258]]
- 2 edges to [[_COMMUNITY_Module Group 257]]
- 2 edges to [[_COMMUNITY_Module Group 137]]
- 1 edge to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Module Group 102]]
- 1 edge to [[_COMMUNITY_DNS Filter & Tunneling Detection]]
- 1 edge to [[_COMMUNITY_Module Group 88]]
- 1 edge to [[_COMMUNITY_Module Group 80]]
- 1 edge to [[_COMMUNITY_Context Guard & Integrity]]
- 1 edge to [[_COMMUNITY_Progressive Trust Levels]]

## Top bridge nodes
- [[TestPrivilegeEscalation]] - degree 31, connects to 13 communities
- [[SubagentMonitor]] - degree 54, connects to 9 communities
- [[SubagentEventType]] - degree 22, connects to 7 communities
- [[SubagentEvent]] - degree 17, connects to 5 communities
- [[subagent_monitor.py]] - degree 7, connects to 2 communities