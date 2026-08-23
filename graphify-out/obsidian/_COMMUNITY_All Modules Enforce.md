---
type: community
cohesion: 0.08
members: 34
---

# All Modules Enforce

**Cohesion:** 0.08 - loosely connected
**Members:** 34 nodes

## Members
- [[.test_get_module_mode_enforce_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_no_env_override()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_get_module_mode_no_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_respect_global_override()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_module_mode_with_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_global_monitor_override_downgrades_all()]] - code - gateway/tests/test_all_modules_enforce.py
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
- [[Test that get_module_mode respects AGENTSHROUD_MODE env var.]] - rationale - gateway/tests/test_observatory_mode.py
- [[TestSecurityConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[Verify SecurityConfig and SecurityModuleConfig default to enforce.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[get_module_mode()]] - code - gateway/ingest_api/config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/All_Modules_Enforce
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 19 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 6 edges to [[_COMMUNITY_Config]]
- 5 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 3 edges to [[_COMMUNITY_Killswitch Monitor & Observatory Mode]]
- 2 edges to [[_COMMUNITY_Router (soc)]]
- 2 edges to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 1 edge to [[_COMMUNITY_Dns Filter]]
- 1 edge to [[_COMMUNITY_Egress Filter (security)]]
- 1 edge to [[_COMMUNITY_Git Guard (security)]]
- 1 edge to [[_COMMUNITY_Multi Turn Tracker (security)]]

## Top bridge nodes
- [[TestSecurityConfigDefaults]] - degree 30, connects to 9 communities
- [[SecurityConfig_3]] - degree 30, connects to 5 communities
- [[SecurityModuleConfig]] - degree 15, connects to 5 communities
- [[get_module_mode()]] - degree 13, connects to 4 communities
- [[.test_global_monitor_override_downgrades_all()]] - degree 4, connects to 2 communities