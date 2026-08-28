---
type: community
cohesion: 0.07
members: 58
---

# Community 95

**Cohesion:** 0.07 - loosely connected
**Members:** 58 nodes

## Members
- [[.__init__()_76]] - code - gateway/security/egress_monitor.py
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
- [[.test_egress_monitor_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_empty_summary()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_generous_baselines()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_high_volume_triggers_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[.test_install_log_sanitizer_no_error()]] - code - gateway/tests/test_log_sanitizer.py
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
- [[EgressChannel]] - code - gateway/security/egress_monitor.py
- [[EgressEvent]] - code - gateway/security/egress_monitor.py
- [[EgressMonitor]] - code - gateway/security/egress_monitor.py
- [[EgressMonitorConfig]] - code - gateway/security/egress_monitor.py
- [[EgressSummary]] - code - gateway/security/egress_monitor.py
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Install the log sanitizer on all existing loggers.]] - rationale - gateway/security/log_sanitizer.py
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Pattern_1]] - code - gateway/security/log_sanitizer.py
- [[Slow-drip  coordinated multi-channel exfiltration anomaly detection]] - concept - gateway/tests/test_egress_monitor.py
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
- [[install_log_sanitizer()]] - code - gateway/security/log_sanitizer.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py
- [[monitor()]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py
- [[test_log_sanitizer.py]] - code - gateway/tests/test_log_sanitizer.py
- [[web_proxy.py]] - code - gateway/proxy/web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_95
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 32 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 6 edges to [[_COMMUNITY_Community 48]]
- 5 edges to [[_COMMUNITY_Community 121]]
- 4 edges to [[_COMMUNITY_Community 19]]
- 3 edges to [[_COMMUNITY_Community 22]]
- 2 edges to [[_COMMUNITY_Middleware & Lifespan]]
- 2 edges to [[_COMMUNITY_Community 66]]
- 2 edges to [[_COMMUNITY_Key Vault & Audit Chain]]
- 2 edges to [[_COMMUNITY_Community 18]]
- 2 edges to [[_COMMUNITY_Community 644]]
- 1 edge to [[_COMMUNITY_Community 165]]
- 1 edge to [[_COMMUNITY_Community 410]]
- 1 edge to [[_COMMUNITY_Community 175]]
- 1 edge to [[_COMMUNITY_Community 102]]
- 1 edge to [[_COMMUNITY_Community 174]]
- 1 edge to [[_COMMUNITY_Community 225]]
- 1 edge to [[_COMMUNITY_Community 157]]
- 1 edge to [[_COMMUNITY_Community 474]]

## Top bridge nodes
- [[web_proxy.py]] - degree 27, connects to 9 communities
- [[egress_monitor.py]] - degree 13, connects to 4 communities
- [[log_sanitizer.py]] - degree 7, connects to 4 communities
- [[EgressEvent]] - degree 49, connects to 3 communities
- [[EgressMonitorConfig]] - degree 30, connects to 3 communities