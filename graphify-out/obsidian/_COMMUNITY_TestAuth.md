---
type: community
cohesion: 0.03
members: 79
---

# TestAuth

**Cohesion:** 0.03 - loosely connected
**Members:** 79 nodes

## Members
- [[.__init__()_21]] - code - gateway/security/subagent_monitor.py
- [[._log_event()]] - code - gateway/security/subagent_monitor.py
- [[.check_tool_usage()]] - code - gateway/security/subagent_monitor.py
- [[.deregister()]] - code - gateway/security/subagent_monitor.py
- [[.get_active()]] - code - gateway/security/subagent_monitor.py
- [[.get_audit_log()_5]] - code - gateway/security/subagent_monitor.py
- [[.get_flagged_events()]] - code - gateway/security/subagent_monitor.py
- [[.kill_agent()]] - code - gateway/security/subagent_monitor.py
- [[.kill_all()]] - code - gateway/security/subagent_monitor.py
- [[.register_spawn()]] - code - gateway/security/subagent_monitor.py
- [[.test_agent_registry_module()]] - code - gateway/tests/test_security_audit.py
- [[.test_audit_filterable_by_agent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_audit_has_timestamps()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_consent_framework_loads()]] - code - gateway/tests/test_security_audit.py
- [[.test_default_mode_is_enforce()_1]] - code - gateway/tests/test_subagent_monitor.py
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
- [[.test_oauth_confused_deputy()]] - code - gateway/tests/test_security_audit.py
- [[.test_oauth_pkce_violation()]] - code - gateway/tests/test_security_audit.py
- [[.test_register_subagent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_reject_empty_token()]] - code - gateway/tests/test_security_audit.py
- [[.test_reject_garbage_token()]] - code - gateway/tests/test_security_audit.py
- [[.test_reject_malformed_jwt()]] - code - gateway/tests/test_security_audit.py
- [[.test_reject_none_algorithm()]] - code - gateway/tests/test_security_audit.py
- [[.test_session_binding()]] - code - gateway/tests/test_security_audit.py
- [[.test_session_different_fingerprints()]] - code - gateway/tests/test_security_audit.py
- [[.test_spawn_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_cannot_exceed_parent()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_info_has_spawn_time()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_subagent_inherits_parent_trust()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_tool_usage_logged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_tool_within_trust_allowed()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_trust_inheritance_default_on()]] - code - gateway/tests/test_subagent_monitor.py
- [[.test_trust_level_enforcement()]] - code - gateway/tests/test_security_audit.py
- [[.test_trust_recovery()]] - code - gateway/tests/test_security_audit.py
- [[.test_trust_violation_flagged()]] - code - gateway/tests/test_subagent_monitor.py
- [[.token_validator()]] - code - gateway/tests/test_security_audit.py
- [[Agent registry should be importable.]] - rationale - gateway/tests/test_security_audit.py
- [[Default mode is enforce after v0.8.0 enforcement hardening.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Different fingerprints should create different sessions.]] - rationale - gateway/tests/test_security_audit.py
- [[If sub-agent tries tool above its trust, flag it.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[In monitor mode, even trust violations are allowed (just flagged).]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Low-trust agents should be blocked from high-risk actions.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor mode flags but allows.]] - rationale - gateway/tests/test_subagent_monitor.py
- [[Reject JWTs with alg=none (classic attack).]] - rationale - gateway/tests/test_security_audit.py
- [[Session must bind to user identity.]] - rationale - gateway/tests/test_security_audit.py
- [[SubagentEvent]] - code - gateway/security/subagent_monitor.py
- [[SubagentInfo]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor]] - code - gateway/security/subagent_monitor.py
- [[Test authentication and authorization enforcement.]] - rationale - gateway/tests/test_security_audit.py
- [[TestAuditTrail_1]] - code - gateway/tests/test_subagent_monitor.py
- [[TestAuth]] - code - gateway/tests/test_security_audit.py
- [[TestConcurrentLimits]] - code - gateway/tests/test_subagent_monitor.py
- [[TestKillSwitch]] - code - gateway/tests/test_subagent_monitor.py
- [[TestPermissionMonitoring]] - code - gateway/tests/test_subagent_monitor.py
- [[TestSubagentMonitorConfig]] - code - gateway/tests/test_subagent_monitor.py
- [[TestSubagentTracking]] - code - gateway/tests/test_subagent_monitor.py
- [[TestTrustInheritance]] - code - gateway/tests/test_subagent_monitor.py
- [[ToolCheckResult]] - code - gateway/security/subagent_monitor.py
- [[Trust should recover after good behavior.]] - rationale - gateway/tests/test_security_audit.py
- [[default_config()]] - code - gateway/tests/test_subagent_monitor.py
- [[monitor()]] - code - gateway/tests/test_subagent_monitor.py
- [[monitor_config()]] - code - gateway/tests/test_subagent_monitor.py
- [[strict_config()]] - code - gateway/tests/test_subagent_monitor.py
- [[strict_monitor()]] - code - gateway/tests/test_subagent_monitor.py
- [[subagent_monitor.py]] - code - gateway/security/subagent_monitor.py
- [[test_subagent_monitor.py]] - code - gateway/tests/test_subagent_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAuth
SORT file.name ASC
```

## Connections to other communities
- 52 edges to [[_COMMUNITY_lifespan.py]]
- 14 edges to [[_COMMUNITY_test_security_audit.py]]
- 8 edges to [[_COMMUNITY_EncryptedStore]]
- 6 edges to [[_COMMUNITY_TrustManager]]
- 5 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_TestFileSandbox]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_KeyVault]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_falco_monitor.py]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[TestAuth]] - degree 48, connects to 12 communities
- [[SubagentMonitor]] - degree 47, connects to 8 communities
- [[subagent_monitor.py]] - degree 12, connects to 7 communities
- [[SubagentEvent]] - degree 17, connects to 5 communities
- [[test_subagent_monitor.py]] - degree 15, connects to 1 community