---
type: community
members: 47
---

# Community 1002

**Members:** 47 nodes

## Members
- [[.test_get_module_mode_enforce_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_no_env_override()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_get_module_mode_no_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_respect_global_override()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_module_mode_with_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_global_monitor_override_downgrades_all()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_monitor_mode_warning_message_format()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_monitor_mode_warnings_all_modules()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_monitor_mode_warnings_no_warnings_in_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_pii_sanitizer_default_action()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_security_config_all_defaults_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_security_config_dns_filter_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_egress_filter_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_egress_monitor_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_killswitch_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_mcp_proxy_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_pii_sanitizer_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_prompt_guard_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_subagent_monitor_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_module_config_default_mode()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_module_config_defaults()]] - code - gateway/tests/test_enforce_defaults.py
- [[AGENTSHROUD_MODE=monitor must downgrade ALL modules to monitor.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Complete security configuration]] - rationale - gateway/ingest_api/config.py
- [[Log warnings for any core modules running in monitor mode.]] - rationale - gateway/ingest_api/config.py
- [[Return module mode, respecting the global permissive override.]] - rationale - gateway/ingest_api/config.py
- [[Security module configuration]] - rationale - gateway/ingest_api/config.py
- [[SecurityConfig_3]] - code - gateway/ingest_api/config.py
- [[SecurityModuleConfig]] - code - gateway/ingest_api/config.py
- [[Test get_module_mode returns enforce when explicitly set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns enforce when no override set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns monitor when AGENTSHROUD_MODE=monitor.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that PII sanitizer defaults to redact action.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that SecurityModuleConfig defaults to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that all core modules default to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that core security modules default to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that get_module_mode respects AGENTSHROUD_MODE env var.]] - rationale - gateway/tests/test_observatory_mode.py
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
TABLE source_file, type FROM #community/Community_1002
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Community 72]]
- 13 edges to [[_COMMUNITY_Community 7]]
- 12 edges to [[_COMMUNITY_Community 50]]
- 3 edges to [[_COMMUNITY_Community 9]]
- 2 edges to [[_COMMUNITY_Community 10]]
- 2 edges to [[_COMMUNITY_Community 1119]]
- 1 edge to [[_COMMUNITY_Community 0]]
- 1 edge to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 344]]

## Top bridge nodes
- [[TestSecurityConfigDefaults]] - degree 30, connects to 10 communities
- [[get_module_mode()]] - degree 14, connects to 4 communities
- [[SecurityConfig_3]] - degree 30, connects to 3 communities
- [[SecurityModuleConfig]] - degree 15, connects to 3 communities
- [[TestEnforceDefaults]] - degree 16, connects to 2 communities