---
type: community
members: 28
---

# KillSwitchMonitor

**Members:** 28 nodes

## Members
- [[dot-test_all_pass_when_script_valid()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_clean_old_metrics_drops_stale_entries()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_docker_unavailable_is_fail()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_dry_run_exercises_enabled_modes()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_excessive_requests_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_excessive_tokens_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_excessive_tool_calls_flagged_and_alerted()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_fail_when_script_missing_triggers_alert()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_failure_increments_and_alerts_at_threshold()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_get_status_reports_verification_due()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_get_system_stats_handles_psutil_error()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_healthy_resets_miss_counter()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_no_anomaly_when_within_limits()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_slow_when_response_exceeds_timeout()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_system_resource_cpu_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_system_resource_memory_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[Behavior tests for KillSwitchMonitor verifyheartbeatanomaly paths. The…]] - rationale - gateway/tests/test_killswitch_monitor_behavior.py
- [[KillSwitchMonitor]] - code - gateway/security/killswitch_monitor.py
- [[Monitor and verify kill switch functionality. Provides automated verification…]] - rationale - gateway/security/killswitch_monitor.py
- [[TestAnomalyDetection]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestHeartbeat]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestStatusAndStats]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestVerifyKillswitch]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[_fake_stats()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[config()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dispatcher()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[fixture_22]] - code
- [[test_killswitch_monitor_behavior.py]] - code - gateway/tests/test_killswitch_monitor_behavior.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KillSwitchMonitor
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Any_3]]
- 15 edges to [[_COMMUNITY_KillSwitchConfig]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestKillSwitchVerification]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_test_observatory_mode.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[KillSwitchMonitor]] - degree 62, connects to 8 communities
- [[test_killswitch_monitor_behavior.py]] - degree 12, connects to 1 community
- [[config()]] - degree 3, connects to 1 community
