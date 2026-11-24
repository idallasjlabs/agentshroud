---
type: community
members: 34
---

# SecurityConfig

**Members:** 34 nodes

## Members
- [[dot-test_get_module_mode_enforce_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_get_module_mode_no_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_get_module_mode_with_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_monitor_mode_warning_message_format()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_monitor_mode_warnings_all_modules()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_monitor_mode_warnings_no_warnings_in_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[dot-test_pii_sanitizer_default_action()]] - code - gateway/tests/test_enforce_defaults.py
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
- [[Complete security configuration]] - rationale - gateway/ingest_api/config.py
- [[SecurityConfig_1]] - code - gateway/ingest_api/config.py
- [[Test get_module_mode returns enforce when explicitly set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns enforce when no override set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns monitor when AGENTSHROUD_MODE=monitor.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that PII sanitizer defaults to redact action.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that SecurityModuleConfig defaults to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that all core modules default to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that core security modules default to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that monitor mode warnings contain required information.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that no warnings are logged when all modules are in enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that warnings are logged for all core modules in monitor mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[TestEnforceDefaults]] - code - gateway/tests/test_enforce_defaults.py
- [[TestSecurityConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[Verify SecurityConfig and SecurityModuleConfig default to enforce.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[dict]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecurityConfig
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]

## Top bridge nodes
- [[SecurityConfig_1]] - degree 24, connects to 3 communities
- [[TestSecurityConfigDefaults]] - degree 13, connects to 1 community
- [[TestEnforceDefaults]] - degree 13, connects to 1 community
- [[dot-test_get_module_mode_enforce_override()]] - degree 5, connects to 1 community
- [[dot-test_get_module_mode_no_override()]] - degree 5, connects to 1 community
