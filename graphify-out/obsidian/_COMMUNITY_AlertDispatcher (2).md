---
type: community
members: 84
---

# AlertDispatcher (2)

**Members:** 84 nodes

## Members
- [[dot-__init__()_154]] - code - gateway/security/key_vault.py
- [[dot-__init__()_155]] - code - gateway/security/key_vault.py
- [[dot-__init__()_156]] - code - gateway/security/log_sanitizer.py
- [[dot-_agent_in_scope()]] - code - gateway/security/key_vault.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/log_sanitizer.py
- [[dot-_contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[dot-_log_audit()]] - code - gateway/security/key_vault.py
- [[dot-_looks_like_credential()]] - code - gateway/security/env_guard.py
- [[dot-_record_leakage()]] - code - gateway/security/env_guard.py
- [[dot-check_anomalies()]] - code - gateway/security/egress_monitor.py
- [[dot-check_command_execution()]] - code - gateway/security/env_guard.py
- [[dot-check_file_access()]] - code - gateway/security/env_guard.py
- [[dot-check_value_match()]] - code - gateway/security/key_vault.py
- [[dot-daily_summary()]] - code - gateway/security/egress_monitor.py
- [[dot-delete_key()]] - code - gateway/security/key_vault.py
- [[dot-get_audit_log()_6]] - code - gateway/security/key_vault.py
- [[dot-get_key()_1]] - code - gateway/security/key_vault.py
- [[dot-inject_for_request()]] - code - gateway/security/key_vault.py
- [[dot-list_keys()]] - code - gateway/security/key_vault.py
- [[dot-redact()]] - code - gateway/security/key_vault.py
- [[dot-rotate_key()]] - code - gateway/security/key_vault.py
- [[dot-scan_outbound()]] - code - gateway/security/key_vault.py
- [[dot-scrub_command_output()]] - code - gateway/security/env_guard.py
- [[dot-store_key()]] - code - gateway/security/key_vault.py
- [[dot-test_default_mode_is_enforce()_3]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_empty_summary()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_generous_baselines()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_high_volume_triggers_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_install_log_sanitizer_no_error()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_key_vault_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_normal_multi_channel_not_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_normal_volume_no_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_dns_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_file_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_http_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_mcp_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_slow_drip_across_channels()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_summary_report()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_unusual_destination_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[AlertSeverity]] - code - gateway/security/egress_monitor.py
- [[AnomalyAlert]] - code - gateway/security/egress_monitor.py
- [[Any_57]] - code - gateway/security/log_sanitizer.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Default mode is enforce after v0.8.0 enforcement hardening._1]] - rationale - gateway/tests/test_egress_monitor.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[EgressSummary]] - code - gateway/security/egress_monitor.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[Install the log sanitizer on all existing loggers.]] - rationale - gateway/security/log_sanitizer.py
- [[KeyAuditEvent]] - code - gateway/security/key_vault.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyScope]] - code - gateway/security/key_vault.py
- [[KeyVault]] - code - gateway/security/key_vault.py
- [[LeakScanResult]] - code - gateway/security/key_vault.py
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Pattern_2]] - code - gateway/security/log_sanitizer.py
- [[Per-agent API key scoping, redaction, leak detection, and rotation]] - concept - gateway/tests/test_key_vault.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py
- [[Small amounts across multiple channels should be detected.]] - rationale - gateway/tests/test_egress_monitor.py
- [[TestAnomalyDetection_1]] - code - gateway/tests/test_egress_monitor.py
- [[TestDailySummary]] - code - gateway/tests/test_egress_monitor.py
- [[TestEgressMonitorConfig]] - code - gateway/tests/test_egress_monitor.py
- [[TestEventRecording]] - code - gateway/tests/test_egress_monitor.py
- [[TestSlowDripDetection]] - code - gateway/tests/test_egress_monitor.py
- [[default_config()_2]] - code - gateway/tests/test_egress_monitor.py
- [[egress_monitor.py]] - code - gateway/security/egress_monitor.py
- [[env_guard.py_2]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[get_sanitizer_stats()]] - code - gateway/security/log_sanitizer.py
- [[install_log_sanitizer()]] - code - gateway/security/log_sanitizer.py
- [[key_vault.py]] - code - gateway/security/key_vault.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py
- [[monitor()_1]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py
- [[test_log_sanitizer.py]] - code - gateway/tests/test_log_sanitizer.py
- [[vault()]] - code - gateway/tests/test_key_vault.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher_2
SORT file.name ASC
```

## Connections to other communities
- 54 edges to [[_COMMUNITY_AlertDispatcher]]
- 34 edges to [[_COMMUNITY_SecurityPipeline]]
- 19 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_check_command]]
- 2 edges to [[_COMMUNITY_KillSwitchMonitor (2)]]
- 2 edges to [[_COMMUNITY_TestLogSanitizer]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_AgentRegistry (2)]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_SessionManager]]

## Top bridge nodes
- [[env_guard.py_2]] - degree 10, connects to 5 communities
- [[egress_monitor.py]] - degree 11, connects to 4 communities
- [[KeyVault]] - degree 53, connects to 2 communities
- [[test_egress_monitor.py]] - degree 14, connects to 2 communities
- [[key_vault.py]] - degree 12, connects to 2 communities
