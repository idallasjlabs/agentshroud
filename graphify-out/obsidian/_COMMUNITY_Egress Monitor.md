---
type: community
cohesion: 0.07
members: 47
---

# Egress Monitor

**Cohesion:** 0.07 - loosely connected
**Members:** 47 nodes

## Members
- [[.__init__()_93]] - code - gateway/security/log_sanitizer.py
- [[._compile_patterns()]] - code - gateway/security/log_sanitizer.py
- [[.check_anomalies()]] - code - gateway/security/egress_monitor.py
- [[.daily_summary()]] - code - gateway/security/egress_monitor.py
- [[.get_events()_2]] - code - gateway/security/egress_monitor.py
- [[.record()_1]] - code - gateway/security/egress_monitor.py
- [[.test_alert_has_description()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_alert_has_severity()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_alert_monitor_mode_no_block()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_default_mode_is_enforce()_1]] - code - gateway/tests/test_egress_monitor.py
- [[.test_empty_summary()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_generous_baselines()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_high_volume_triggers_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_normal_multi_channel_not_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_normal_volume_no_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_record_dns_event()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_record_file_event()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_record_http_event()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_record_mcp_event()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_slow_drip_across_channels()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_summary_report()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_unusual_destination_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[AlertSeverity]] - code - gateway/security/egress_monitor.py
- [[Alerts in monitor mode should never block.]] - rationale - gateway/tests/test_egress_monitor.py
- [[AnomalyAlert]] - code - gateway/security/egress_monitor.py
- [[Any_46]] - code - gateway/security/log_sanitizer.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Default mode is enforce after v0.8.0 enforcement hardening._1]] - rationale - gateway/tests/test_egress_monitor.py
- [[EgressEvent]] - code - gateway/security/egress_monitor.py
- [[EgressSummary]] - code - gateway/security/egress_monitor.py
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Pattern_1]] - code - gateway/security/log_sanitizer.py
- [[Small amounts across multiple channels should be detected.]] - rationale - gateway/tests/test_egress_monitor.py
- [[TestAlertGeneration]] - code - gateway/tests/test_egress_monitor.py
- [[TestAnomalyDetection]] - code - gateway/tests/test_egress_monitor.py
- [[TestDailySummary]] - code - gateway/tests/test_egress_monitor.py
- [[TestEgressMonitorConfig]] - code - gateway/tests/test_egress_monitor.py
- [[TestEventRecording]] - code - gateway/tests/test_egress_monitor.py
- [[TestSlowDripDetection]] - code - gateway/tests/test_egress_monitor.py
- [[default_config()_2]] - code - gateway/tests/test_egress_monitor.py
- [[egress_monitor.py]] - code - gateway/security/egress_monitor.py
- [[get_sanitizer_stats()]] - code - gateway/security/log_sanitizer.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py
- [[monitor()]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Egress_Monitor
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 21 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 6 edges to [[_COMMUNITY_OAuth & Metadata Guard]]
- 3 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 2 edges to [[_COMMUNITY_Web Proxy Security]]
- 2 edges to [[_COMMUNITY_Key Vault]]
- 2 edges to [[_COMMUNITY_Resource Guard & Local Model Parity]]
- 2 edges to [[_COMMUNITY_Git Guard (security)]]
- 1 edge to [[_COMMUNITY_Skill Guard]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 1 edge to [[_COMMUNITY_Security Audit]]
- 1 edge to [[_COMMUNITY_Log Sanitizer]]
- 1 edge to [[_COMMUNITY_Session Security]]

## Top bridge nodes
- [[EgressEvent]] - degree 49, connects to 9 communities
- [[egress_monitor.py]] - degree 13, connects to 6 communities
- [[log_sanitizer.py]] - degree 7, connects to 5 communities
- [[test_egress_monitor.py]] - degree 14, connects to 2 communities
- [[TestEventRecording]] - degree 10, connects to 2 communities