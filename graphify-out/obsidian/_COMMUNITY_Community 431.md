---
type: community
members: 46
---

# Community 431

**Members:** 46 nodes

## Members
- [[.__init__()_76]] - code - gateway/security/egress_monitor.py
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
- [[Default mode is enforce after v0.8.0 enforcement hardening._1]] - rationale - gateway/tests/test_egress_monitor.py
- [[EgressChannel]] - code - gateway/security/egress_monitor.py
- [[EgressEvent]] - code - gateway/security/egress_monitor.py
- [[EgressMonitor]] - code - gateway/security/egress_monitor.py
- [[EgressMonitorConfig]] - code - gateway/security/egress_monitor.py
- [[EgressSummary]] - code - gateway/security/egress_monitor.py
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
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
- [[monitor()]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py
- [[web_proxy.py]] - code - gateway/proxy/web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_431
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Community 0]]
- 34 edges to [[_COMMUNITY_Community 72]]
- 6 edges to [[_COMMUNITY_Community 8]]
- 5 edges to [[_COMMUNITY_Community 120]]
- 4 edges to [[_COMMUNITY_Community 27]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 562]]
- 2 edges to [[_COMMUNITY_Community 71]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 152]]
- 1 edge to [[_COMMUNITY_Community 281]]
- 1 edge to [[_COMMUNITY_Community 5]]

## Top bridge nodes
- [[web_proxy.py]] - degree 27, connects to 10 communities
- [[egress_monitor.py]] - degree 12, connects to 4 communities
- [[EgressChannel]] - degree 23, connects to 3 communities
- [[EgressEvent]] - degree 49, connects to 2 communities
- [[EgressMonitorConfig]] - degree 30, connects to 1 community