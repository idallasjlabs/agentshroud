---
type: community
members: 48
---

# EgressEvent

**Members:** 48 nodes

## Members
- [[dot-__init__()_61]] - code - gateway/security/egress_monitor.py
- [[dot-check_anomalies()]] - code - gateway/security/egress_monitor.py
- [[dot-daily_summary()]] - code - gateway/security/egress_monitor.py
- [[dot-get_events()_1]] - code - gateway/security/egress_monitor.py
- [[dot-record()]] - code - gateway/security/egress_monitor.py
- [[dot-test_alert_has_description()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_has_severity()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_monitor_mode_no_block()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_default_mode_is_enforce()]] - code - gateway/tests/test_egress_monitor.py
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
- [[Default mode is enforce after v0.8.0 enforcement hardening.]] - rationale - gateway/tests/test_egress_monitor.py
- [[EgressChannel]] - code - gateway/security/egress_monitor.py
- [[EgressEvent]] - code - gateway/security/egress_monitor.py
- [[EgressMonitor]] - code - gateway/security/egress_monitor.py
- [[EgressMonitorConfig]] - code - gateway/security/egress_monitor.py
- [[EgressSummary]] - code - gateway/security/egress_monitor.py
- [[Enum_16]] - code
- [[IntEnum]] - code
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Small amounts across multiple channels should be detected.]] - rationale - gateway/tests/test_egress_monitor.py
- [[TestAlertGeneration]] - code - gateway/tests/test_egress_monitor.py
- [[TestAnomalyDetection_1]] - code - gateway/tests/test_egress_monitor.py
- [[TestDailySummary]] - code - gateway/tests/test_egress_monitor.py
- [[TestEgressMonitorConfig]] - code - gateway/tests/test_egress_monitor.py
- [[TestEventRecording]] - code - gateway/tests/test_egress_monitor.py
- [[TestSlowDripDetection]] - code - gateway/tests/test_egress_monitor.py
- [[Tests for unified egress monitoring.]] - rationale - gateway/tests/test_egress_monitor.py
- [[default_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[egress_monitor.py_2]] - code - gateway/security/egress_monitor.py
- [[fixture_38]] - code
- [[monitor()]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[str_11]] - code
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressEvent
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_WebProxy]]
- 5 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestExfiltrationDetection]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_TestModuleConfigDefaults]]
- 2 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 1 edge to [[_COMMUNITY_WebProxyResult]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_MetadataGuard]]

## Top bridge nodes
- [[EgressMonitorConfig]] - degree 14, connects to 6 communities
- [[EgressEvent]] - degree 28, connects to 5 communities
- [[EgressMonitor]] - degree 14, connects to 4 communities
- [[egress_monitor.py_2]] - degree 12, connects to 3 communities
- [[EgressChannel]] - degree 13, connects to 2 communities
