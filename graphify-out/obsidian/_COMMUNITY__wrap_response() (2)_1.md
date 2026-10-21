---
type: community
members: 110
---

# _wrap_response() (2)

**Members:** 110 nodes

## Members
- [[dot-__init__()_111]] - code - gateway/security/drift_detector.py
- [[dot-_init_db()_2]] - code - gateway/security/drift_detector.py
- [[dot-acknowledge_alert()]] - code - gateway/security/drift_detector.py
- [[dot-check_drift()]] - code - gateway/security/drift_detector.py
- [[dot-close()_8]] - code - gateway/security/drift_detector.py
- [[dot-config_hash()]] - code - gateway/security/drift_detector.py
- [[dot-from_dict()_3]] - code - gateway/security/drift_detector.py
- [[dot-get_alerts()]] - code - gateway/security/drift_detector.py
- [[dot-get_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-set_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-setup_method()_20]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_6]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_acknowledge_alert()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_alert_dedup()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_alert_dispatcher_concurrent_dispatch()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_alert_dispatcher_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_alert_dispatcher_write()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_alerts_persisted()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_canary_system_importable()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_config_hash_changes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_hash_consistency()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_consent_required_for_sensitive_ops()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_context_guard_session_isolation_under_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_context_guard_tool_manipulation()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_dashboard_has_csp_meta()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_dashboard_html_exists()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_dashboard_no_inline_secrets()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_drift_detector_baseline()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_drift_detector_concurrent_writes()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_drift_detector_detects_change()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_drift_no_false_positive()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_health_report_importable()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_image_change()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_mcp_proxy_module_exists()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_new_capability()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_env_var()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_mount()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_baseline_no_alerts()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_drift()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_mixed_content()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_pickle_in_security_modules()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_shell_true_in_subprocess()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_yaml_unsafe_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_privileged_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_prompt_guard_catches_tool_injection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_prompt_guard_concurrent_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_read_only_disabled()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_removed_capability()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_requirements_pinned()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_seccomp_drift()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_set_and_get_baseline()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_simultaneous_baseline_and_config_change()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_subagent_monitor_tracks_events()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_trust_cannot_exceed_max()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_trust_manager_rapid_updates()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_unregistered_agent_blocked()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_violation_drops_trust_significantly()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_xss_in_dashboard_inputs()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-to_dict()_6]] - code - gateway/security/drift_detector.py
- [[A single violation should meaningfully impact trust.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Compare current config against baseline, return any drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[Concurrent alert dispatch shouldn't lose or corrupt alerts.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Concurrent baseline updates — SQLite is single-threaded by default.         This]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Concurrent prompt scans shouldn't interfere with each other.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Consent framework should be available for gating.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[ContainerSnapshot]] - code - gateway/security/drift_detector.py
- [[Context guard should detect tool result manipulation.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should escape user inputs (no raw innerHTML from API).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should have Content-Security-Policy or mention it.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should have an HTML file.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should not contain hardcoded secrets.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should not load HTTP resources.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Detect configuration drift from known-good baselines.]] - rationale - gateway/security/drift_detector.py
- [[Drift detector catches container config changes during operation.]] - rationale - gateway/tests/test_security_integration.py
- [[DriftAlert]] - code - gateway/security/drift_detector.py
- [[DriftDetector]] - code - gateway/security/drift_detector.py
- [[Duplicate alerts should be deduplicated.]] - rationale - gateway/tests/test_security_audit.py
- [[MCP proxy module should be importable.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Mark an alert as acknowledged.]] - rationale - gateway/security/drift_detector.py
- [[No yaml.load() without Loader (arbitrary code execution).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Prompt guard should catch tool-call injection attempts.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Rapid trust score updates shouldn't corrupt state.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Requirements should have pinned versions.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Retrieve baseline snapshot for a container.]] - rationale - gateway/security/drift_detector.py
- [[Retrieve stored drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[SHA-256 hash of the config for quick comparison.]] - rationale - gateway/security/drift_detector.py
- [[Security modules should not use pickle (deserialization attack).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Sessions shouldn't leak data under concurrent access.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Store a known-good baseline configuration. Returns config hash.]] - rationale - gateway/security/drift_detector.py
- [[Subagent events should be trackable.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Subprocess calls should not pass shell=True.          Uses AST analysis to flag]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test MCP tool proxy security controls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test audit chain integrity and tamper detection.]] - rationale - gateway/tests/test_security_audit.py
- [[Test dependency and supply chain security.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test thread safety and race conditions in security modules.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test trust boundaries and privilege escalation prevention.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test web dashboard and API security headers.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestAuditTrail_1]] - code - gateway/tests/test_security_audit.py
- [[TestConcurrency]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestDependencySecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestDriftDetector]] - code - gateway/tests/test_security_hardening.py
- [[TestMCPSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestPrivilegeEscalation_1]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestWebSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[Trust score should have an upper bound.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Unregistered agents should not be trusted.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Verify drift is detected even with rapid changes.]] - rationale - gateway/tests/test_security_hardening.py
- [[drift_detector.py]] - code - gateway/security/drift_detector.py
- [[test_drift_detection_in_pipeline()]] - code - gateway/tests/test_security_integration.py
- [[test_security_audit_advanced.py]] - code - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_wrap_response_2
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_MiddlewareManager]]
- 29 edges to [[_COMMUNITY__wrap_response()]]
- 17 edges to [[_COMMUNITY__wrap_response() (3)_1]]
- 16 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 16 edges to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 15 edges to [[_COMMUNITY_PortManager]]
- 9 edges to [[_COMMUNITY_socrouter.py]]
- 9 edges to [[_COMMUNITY_test_playback_state.c]]
- 9 edges to [[_COMMUNITY_TelegramAPIProxy (2)_1]]
- 8 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 8 edges to [[_COMMUNITY__wrap_response() (4)]]
- 8 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 8 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 7 edges to [[_COMMUNITY_asyncio]]
- 7 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 6 edges to [[_COMMUNITY_SecureBrowser (3)]]
- 6 edges to [[_COMMUNITY_EgressFilterConfig]]
- 6 edges to [[_COMMUNITY_SessionManager]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 4 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 3 edges to [[_COMMUNITY_Common Queries]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY__wrap_response() (5)]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (3)_1]]
- 2 edges to [[_COMMUNITY_socrouter.py (2)]]
- 2 edges to [[_COMMUNITY_WebProxy]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 1 edge to [[_COMMUNITY_AgentShroud™ README]]
- 1 edge to [[_COMMUNITY_KeyRotationManager (2)]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer (3)]]

## Top bridge nodes
- [[TestAuditTrail_1]] - degree 43, connects to 21 communities
- [[DriftDetector]] - degree 66, connects to 18 communities
- [[ContainerSnapshot]] - degree 63, connects to 16 communities
- [[TestPrivilegeEscalation_1]] - degree 30, connects to 16 communities
- [[TestConcurrency]] - degree 29, connects to 16 communities
