---
type: community
cohesion: 0.08
members: 33
---

# SecurityConfig

**Cohesion:** 0.08 - loosely connected
**Members:** 33 nodes

## Members
- [[.test_get_module_mode_enforce_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_no_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_with_override()]] - code - gateway/tests/test_enforce_defaults.py
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
- [[Complete security configuration]] - rationale - gateway/ingest_api/config.py
- [[Security module configuration]] - rationale - gateway/ingest_api/config.py
- [[SecurityConfig_4]] - code - gateway/ingest_api/config.py
- [[SecurityModuleConfig]] - code - gateway/ingest_api/config.py
- [[Test get_module_mode returns enforce when explicitly set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns enforce when no override set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns monitor when AGENTSHROUD_MODE=monitor.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that PII sanitizer defaults to redact action.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that SecurityModuleConfig defaults to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that all core modules default to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that monitor mode warnings contain required information.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that no warnings are logged when all modules are in enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that warnings are logged for all core modules in monitor mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[TestSecurityConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[Verify SecurityConfig and SecurityModuleConfig default to enforce.]] - rationale - gateway/tests/test_all_modules_enforce.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecurityConfig
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_lifespan.py]]
- 16 edges to [[_COMMUNITY_TrustManager]]
- 5 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_BaseModel]]
- 2 edges to [[_COMMUNITY_BotConfig]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_load_config()]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]

## Top bridge nodes
- [[TestSecurityConfigDefaults]] - degree 30, connects to 8 communities
- [[SecurityConfig_4]] - degree 30, connects to 6 communities
- [[SecurityModuleConfig]] - degree 15, connects to 5 communities
- [[.test_get_module_mode_enforce_override()]] - degree 4, connects to 2 communities
- [[.test_get_module_mode_no_override()]] - degree 4, connects to 2 communities