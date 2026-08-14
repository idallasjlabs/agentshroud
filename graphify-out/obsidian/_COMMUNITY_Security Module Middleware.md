---
type: community
members: 34
---

# Security Module Middleware

**Members:** 34 nodes

## Members
- [[.get_events()_1]] - code - gateway/security/egress_monitor.py
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
- [[Default mode is enforce after v0.8.0 enforcement hardening._1]] - rationale - gateway/tests/test_egress_monitor.py
- [[EgressEvent]] - code - gateway/security/egress_monitor.py
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Small amounts across multiple channels should be detected.]] - rationale - gateway/tests/test_egress_monitor.py
- [[TestAlertGeneration]] - code - gateway/tests/test_egress_monitor.py
- [[TestAnomalyDetection]] - code - gateway/tests/test_egress_monitor.py
- [[TestDailySummary]] - code - gateway/tests/test_egress_monitor.py
- [[TestEgressMonitorConfig]] - code - gateway/tests/test_egress_monitor.py
- [[TestEventRecording]] - code - gateway/tests/test_egress_monitor.py
- [[TestSlowDripDetection]] - code - gateway/tests/test_egress_monitor.py
- [[default_config()_2]] - code - gateway/tests/test_egress_monitor.py
- [[monitor()]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Module_Middleware
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_Auth & Exception Types]]
- 22 edges to [[_COMMUNITY_Egress & RBAC Security Core]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]

## Top bridge nodes
- [[EgressEvent]] - degree 48, connects to 4 communities
- [[test_egress_monitor.py]] - degree 14, connects to 2 communities
- [[TestEventRecording]] - degree 10, connects to 2 communities
- [[AlertSeverity]] - degree 9, connects to 2 communities
- [[TestAnomalyDetection]] - degree 9, connects to 2 communities