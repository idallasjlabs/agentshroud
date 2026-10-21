---
type: community
members: 76
---

# _wrap_response() (3)

**Members:** 76 nodes

## Members
- [[dot-check_anomalies()]] - code - gateway/security/egress_monitor.py
- [[dot-daily_summary()]] - code - gateway/security/egress_monitor.py
- [[dot-get_events()_2]] - code - gateway/security/egress_monitor.py
- [[dot-record()_2]] - code - gateway/security/egress_monitor.py
- [[dot-test_alert_has_description()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_has_severity()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_monitor_mode_no_block()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_binary_data_in_text_fields()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_crlf_in_prompt_guard()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_deeply_nested_context_attacks()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_deeply_nested_json()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_default_mode_is_enforce()_6]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_empty_inputs_everywhere()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_empty_summary()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_generous_baselines()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_high_volume_triggers_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_json_injection_in_context()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_many_pii_entities()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_normal_multi_channel_not_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_normal_volume_no_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_null_byte_in_prompt()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_oversized_json_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_polyglot_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_rapid_fire_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_record_dns_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_file_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_http_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_mcp_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_regex_redos_email()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_regex_redos_ssn()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_slow_drip_across_channels()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_summary_report()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_unicode_normalization_bypass()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_unusual_destination_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_very_long_message()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_xml_entity_expansion()]] - code - gateway/tests/test_security_audit_advanced.py
- [[AlertSeverity]] - code - gateway/security/egress_monitor.py
- [[Alerts in monitor mode should never block.]] - rationale - gateway/tests/test_egress_monitor.py
- [[AnomalyAlert]] - code - gateway/security/egress_monitor.py
- [[Binary data in text fields shouldn't crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[CRLF injection in prompt shouldn't bypass detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Deeply nested JSON shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Default mode is enforce after v0.8.0 enforcement hardening._2]] - rationale - gateway/tests/test_egress_monitor.py
- [[EgressChannel]] - code - gateway/security/egress_monitor.py
- [[EgressEvent]] - code - gateway/security/egress_monitor.py
- [[EgressSummary]] - code - gateway/security/egress_monitor.py
- [[Email regex should not be vulnerable to ReDoS.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Empty strings shouldn't crash any module.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[JSON injection in message shouldn't manipulate context.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Message with hundreds of PII entities should complete.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Nested context attacks shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Null bytes shouldn't bypass prompt guard.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Polyglot (valid as multiple formats) shouldn't bypass checks.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Rapid scanning shouldn't degrade or crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[SSN regex should not be vulnerable to ReDoS.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Small amounts across multiple channels should be detected.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Test HTTP-level security CRLF, header injection, content types.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test resilience against denial of service patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestAlertGeneration]] - code - gateway/tests/test_egress_monitor.py
- [[TestAnomalyDetection_1]] - code - gateway/tests/test_egress_monitor.py
- [[TestDailySummary]] - code - gateway/tests/test_egress_monitor.py
- [[TestDoSPrevention]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestEgressMonitorConfig]] - code - gateway/tests/test_egress_monitor.py
- [[TestEventRecording]] - code - gateway/tests/test_egress_monitor.py
- [[TestHTTPSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestSlowDripDetection]] - code - gateway/tests/test_egress_monitor.py
- [[Unicode tricks shouldn't bypass PII detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Very large JSON shouldn't crash the parser.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Very long messages should be handled without crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[XXE-style payloads shouldn't crash processing.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[default_config()_4]] - code - gateway/tests/test_egress_monitor.py
- [[egress_monitor.py]] - code - gateway/security/egress_monitor.py
- [[monitor()_1]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_2]] - code - gateway/tests/test_egress_monitor.py
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_wrap_response_3
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_MiddlewareManager]]
- 17 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 10 edges to [[_COMMUNITY__wrap_response()]]
- 6 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 6 edges to [[_COMMUNITY_PortManager]]
- 4 edges to [[_COMMUNITY__wrap_response() (4)]]
- 3 edges to [[_COMMUNITY_test_playback_state.c]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy (2)_1]]
- 3 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 2 edges to [[_COMMUNITY_asyncio]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_SecureBrowser (3)]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 2 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 2 edges to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY__wrap_response() (5)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]

## Top bridge nodes
- [[TestDoSPrevention]] - degree 32, connects to 16 communities
- [[TestHTTPSecurity]] - degree 32, connects to 16 communities
- [[EgressEvent]] - degree 47, connects to 11 communities
- [[EgressChannel]] - degree 22, connects to 5 communities
- [[egress_monitor.py]] - degree 11, connects to 5 communities
