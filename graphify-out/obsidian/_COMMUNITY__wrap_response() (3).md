---
type: community
cohesion: 0.11
members: 22
---

# _wrap_response() (3)

**Cohesion:** 0.11 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-test_alert_has_description()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_has_severity()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_monitor_mode_no_block()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_empty_summary()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_high_volume_triggers_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_normal_multi_channel_not_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_normal_volume_no_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_slow_drip_across_channels()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_summary_report()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_unusual_destination_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[AlertSeverity]] - code - gateway/security/egress_monitor.py
- [[Alerts in monitor mode should never block.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[Small amounts across multiple channels should be detected.]] - rationale - gateway/tests/test_egress_monitor.py
- [[TestAlertGeneration]] - code - gateway/tests/test_egress_monitor.py
- [[TestAnomalyDetection]] - code - gateway/tests/test_egress_monitor.py
- [[TestDailySummary]] - code - gateway/tests/test_egress_monitor.py
- [[TestSlowDripDetection]] - code - gateway/tests/test_egress_monitor.py
- [[default_config()_2]] - code - gateway/tests/test_egress_monitor.py
- [[monitor()_1]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_wrap_response_3
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_ContextGuard]]
- 16 edges to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]

## Top bridge nodes
- [[AlertSeverity]] - degree 9, connects to 3 communities
- [[test_egress_monitor.py]] - degree 14, connects to 2 communities
- [[TestAlertGeneration]] - degree 9, connects to 2 communities
- [[TestAnomalyDetection]] - degree 9, connects to 2 communities
- [[TestDailySummary]] - degree 8, connects to 2 communities
