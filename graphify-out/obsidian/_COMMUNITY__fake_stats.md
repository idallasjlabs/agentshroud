---
type: community
members: 12
---

# _fake_stats

**Members:** 12 nodes

## Members
- [[dot-test_excessive_requests_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_excessive_tokens_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_excessive_tool_calls_flagged_and_alerted()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_failure_increments_and_alerts_at_threshold()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_healthy_resets_miss_counter()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_no_anomaly_when_within_limits()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_slow_when_response_exceeds_timeout()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_system_resource_cpu_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_system_resource_memory_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestAnomalyDetection]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestHeartbeat]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[_fake_stats()]] - code - gateway/tests/test_killswitch_monitor_behavior.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_fake_stats
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 3 edges to [[_COMMUNITY_KillSwitchConfig]]

## Top bridge nodes
- [[_fake_stats()]] - degree 10, connects to 2 communities
- [[TestAnomalyDetection]] - degree 8, connects to 2 communities
- [[TestHeartbeat]] - degree 5, connects to 2 communities
- [[dot-test_excessive_requests_flagged()]] - degree 3, connects to 1 community
- [[dot-test_excessive_tokens_flagged()]] - degree 3, connects to 1 community
