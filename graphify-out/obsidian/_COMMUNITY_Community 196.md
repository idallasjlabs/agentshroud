---
type: community
members: 26
---

# Community 196

**Members:** 26 nodes

## Members
- [[.test_get_module_mode_enforce_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_no_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_with_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_global_monitor_override_downgrades_all()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_monitor_mode_warning_message_format()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_monitor_mode_warnings_all_modules()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_monitor_mode_warnings_no_warnings_in_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_pii_sanitizer_default_action()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_security_config_all_defaults_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_security_module_config_defaults()]] - code - gateway/tests/test_enforce_defaults.py
- [[AGENTSHROUD_MODE=monitor must downgrade ALL modules to monitor.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Log warnings for any core modules running in monitor mode.]] - rationale - gateway/ingest_api/config.py
- [[Return module mode, respecting the global permissive override.]] - rationale - gateway/ingest_api/config.py
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
- [[check_monitor_mode_warnings()]] - code - gateway/ingest_api/config.py
- [[get_module_mode()]] - code - gateway/ingest_api/config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_196
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Community 72]]
- 5 edges to [[_COMMUNITY_Community 84]]
- 4 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 104]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 103]]
- 1 edge to [[_COMMUNITY_Community 1002]]
- 1 edge to [[_COMMUNITY_Community 68]]

## Top bridge nodes
- [[get_module_mode()]] - degree 14, connects to 7 communities
- [[TestEnforceDefaults]] - degree 16, connects to 3 communities
- [[check_monitor_mode_warnings()]] - degree 9, connects to 3 communities
- [[.test_global_monitor_override_downgrades_all()]] - degree 4, connects to 2 communities
- [[.test_get_module_mode_no_override()]] - degree 4, connects to 1 community