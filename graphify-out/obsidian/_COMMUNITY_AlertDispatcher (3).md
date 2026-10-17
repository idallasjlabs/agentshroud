---
type: community
members: 65
---

# AlertDispatcher (3)

**Members:** 65 nodes

## Members
- [[dot-__init__()_177]] - code - gateway/security/egress_monitor.py
- [[dot-__init__()_178]] - code - gateway/security/log_sanitizer.py
- [[dot-_compile_patterns()]] - code - gateway/security/log_sanitizer.py
- [[dot-check_anomalies()]] - code - gateway/security/egress_monitor.py
- [[dot-check_value_match()]] - code - gateway/security/key_vault.py
- [[dot-daily_summary()]] - code - gateway/security/egress_monitor.py
- [[dot-get_events()_2]] - code - gateway/security/egress_monitor.py
- [[dot-record()_2]] - code - gateway/security/egress_monitor.py
- [[dot-scan_outbound()]] - code - gateway/security/key_vault.py
- [[dot-store_key()]] - code - gateway/security/key_vault.py
- [[dot-test_alert_has_description()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_has_severity()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_monitor_mode_no_block()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_default_mode_is_enforce()_7]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_empty_summary()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_generous_baselines()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_high_volume_triggers_alert()]] - code - gateway/tests/test_egress_monitor.py
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
- [[Alerts in monitor mode should never block.]] - rationale - gateway/tests/test_egress_monitor.py
- [[AnomalyAlert]] - code - gateway/security/egress_monitor.py
- [[Any_74]] - code - gateway/security/log_sanitizer.py
- [[Check if any stored key values appear in text. Returns matching key names.]] - rationale - gateway/security/key_vault.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Default mode is enforce after v0.8.0 enforcement hardening._2]] - rationale - gateway/tests/test_egress_monitor.py
- [[EgressChannel]] - code - gateway/security/egress_monitor.py
- [[EgressEvent]] - code - gateway/security/egress_monitor.py
- [[EgressMonitor]] - code - gateway/security/egress_monitor.py
- [[EgressSummary]] - code - gateway/security/egress_monitor.py
- [[Encrypted Store Module Badge Icon]] - image - branding/icons/modules/encrypted-store-256x256.png
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[KeyEntry]] - code - gateway/security/key_vault.py
- [[KeyScope]] - code - gateway/security/key_vault.py
- [[LeakScanResult]] - code - gateway/security/key_vault.py
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Pattern_2]] - code - gateway/security/log_sanitizer.py
- [[Slow-drip  coordinated multi-channel exfiltration anomaly detection]] - concept - gateway/tests/test_egress_monitor.py
- [[Small amounts across multiple channels should be detected.]] - rationale - gateway/tests/test_egress_monitor.py
- [[TestAlertGeneration]] - code - gateway/tests/test_egress_monitor.py
- [[TestAnomalyDetection_1]] - code - gateway/tests/test_egress_monitor.py
- [[TestDailySummary]] - code - gateway/tests/test_egress_monitor.py
- [[TestEgressMonitorConfig]] - code - gateway/tests/test_egress_monitor.py
- [[TestEventRecording]] - code - gateway/tests/test_egress_monitor.py
- [[TestSlowDripDetection]] - code - gateway/tests/test_egress_monitor.py
- [[default_config()_4]] - code - gateway/tests/test_egress_monitor.py
- [[egress_monitor.py_2]] - code - gateway/security/egress_monitor.py
- [[encrypted_store.py_2]] - code - gateway/security/encrypted_store.py
- [[env_guard.py_2]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[get_sanitizer_stats()_1]] - code - gateway/security/log_sanitizer.py
- [[key_vault.py_2]] - code - gateway/security/key_vault.py
- [[log_sanitizer.py_2]] - code - gateway/security/log_sanitizer.py
- [[monitor()_1]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_2]] - code - gateway/tests/test_egress_monitor.py
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher_3
SORT file.name ASC
```

## Connections to other communities
- 48 edges to [[_COMMUNITY_AlertDispatcher]]
- 22 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 4 edges to [[_COMMUNITY_check_command]]
- 3 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_ProxyAction]]
- 2 edges to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (2)]]
- 1 edge to [[_COMMUNITY_TestLogSanitizer]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py (2)]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_egress_filter.py (3)]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]

## Top bridge nodes
- [[FR4 Data Confidentiality]] - degree 8, connects to 6 communities
- [[env_guard.py_2]] - degree 10, connects to 4 communities
- [[EgressEvent]] - degree 47, connects to 3 communities
- [[EgressChannel]] - degree 22, connects to 3 communities
- [[egress_monitor.py_2]] - degree 11, connects to 3 communities
