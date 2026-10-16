---
type: community
cohesion: 0.07
members: 49
---

# MiddlewareManager

**Cohesion:** 0.07 - loosely connected
**Members:** 49 nodes

## Members
- [[dot-test_get_module_mode_enforce_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_get_module_mode_no_env_override()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_get_module_mode_no_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_get_module_mode_with_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_global_monitor_override_downgrades_all()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_monitor_mode_warning_message_format()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_monitor_mode_warnings_all_modules()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_monitor_mode_warnings_no_warnings_in_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_pii_sanitizer_default_action()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_pii_sanitizer_default_enforcement()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_pii_sanitizer_mode_param()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_security_config_all_defaults_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_security_config_dns_filter_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_config_egress_filter_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_config_egress_monitor_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_config_killswitch_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_config_mcp_proxy_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_config_pii_sanitizer_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_config_prompt_guard_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_config_subagent_monitor_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_module_config_default_mode()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_security_module_config_defaults()]] - code - gateway/tests/test_enforce_defaults.py
- [[AGENTSHROUD_MODE=monitor must downgrade ALL modules to monitor.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Complete security configuration]] - rationale - gateway/ingest_api/config.py
- [[Log warnings for any core modules running in monitor mode.]] - rationale - gateway/ingest_api/config.py
- [[Return module mode, respecting the global permissive override.]] - rationale - gateway/ingest_api/config.py
- [[Security module configuration]] - rationale - gateway/ingest_api/config.py
- [[SecurityConfig_4]] - code - gateway/ingest_api/config.py
- [[SecurityModuleConfig]] - code - gateway/ingest_api/config.py
- [[Test PIISanitizer accepts and stores mode parameter.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test PIISanitizer defaults to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns enforce when explicitly set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns enforce when no override set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns monitor when AGENTSHROUD_MODE=monitor.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that PII sanitizer defaults to redact action.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that SecurityModuleConfig defaults to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that all core modules default to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that core security modules default to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that individual modules respect the enforcemonitor mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that monitor mode warnings contain required information.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that no warnings are logged when all modules are in enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that warnings are logged for all core modules in monitor mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[TestEnforceDefaults]] - code - gateway/tests/test_enforce_defaults.py
- [[TestModuleEnforcement]] - code - gateway/tests/test_enforce_defaults.py
- [[TestSecurityConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[Verify SecurityConfig and SecurityModuleConfig default to enforce.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[check_monitor_mode_warnings()]] - code - gateway/ingest_api/config.py
- [[get_module_mode()]] - code - gateway/ingest_api/config.py
- [[test_enforce_defaults.py]] - code - gateway/tests/test_enforce_defaults.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_MiddlewareManager_8]]
- 10 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 7 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY__FakeRBAC]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_3]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_ResourceGuard_1]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_1]]
- 1 edge to [[_COMMUNITY_TrustConfig_1]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor_2]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py]]
- 1 edge to [[_COMMUNITY_ConsentFramework_1]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_3]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_MultiTurnTracker_1]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer]]

## Top bridge nodes
- [[TestSecurityConfigDefaults]] - degree 30, connects to 15 communities
- [[get_module_mode()]] - degree 14, connects to 6 communities
- [[SecurityConfig_4]] - degree 30, connects to 4 communities
- [[SecurityModuleConfig]] - degree 15, connects to 4 communities
- [[TestEnforceDefaults]] - degree 16, connects to 3 communities
