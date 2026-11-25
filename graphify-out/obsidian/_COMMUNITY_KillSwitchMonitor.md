---
type: community
members: 55
---

# KillSwitchMonitor

**Members:** 55 nodes

## Members
- [[dot-_check_request_rate()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_system_resources()_1]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_token_usage()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_tool_call_rate()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_clean_old_metrics()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_count_recent_events()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_get_system_stats()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_log_heartbeat_result()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_log_verification_result()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_send_anomaly_alert()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_send_heartbeat_alert()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_send_verification_alert()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_docker_available()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_killswitch_mode()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_script_exists()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_script_permissions()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_script_syntax()]] - code - gateway/security/killswitch_monitor.py
- [[dot-anomaly_detection()]] - code - gateway/security/killswitch_monitor.py
- [[dot-get_status()_3]] - code - gateway/security/killswitch_monitor.py
- [[dot-heartbeat_check()]] - code - gateway/security/killswitch_monitor.py
- [[dot-test_all_pass_when_script_valid()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_clean_old_metrics_drops_stale_entries()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_docker_unavailable_is_fail()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_dry_run_exercises_enabled_modes()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_fail_when_script_missing_triggers_alert()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_get_status_reports_verification_due()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_get_system_stats_handles_psutil_error()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-verify_killswitch()]] - code - gateway/security/killswitch_monitor.py
- [[Any_86]] - code
- [[Check if request rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if system resource usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if the agent is responding within expected parameters. Returns Dict…]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if token usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if tool call rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Count events in the last N seconds.]] - rationale - gateway/security/killswitch_monitor.py
- [[Detect unusual patterns that might indicate rogue behavior. Args tool_calls…]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current kill switch monitor status. Returns Dict containing current status…]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current system statistics.]] - rationale - gateway/security/killswitch_monitor.py
- [[KillSwitchMonitor]] - code - gateway/security/killswitch_monitor.py
- [[Log heartbeat result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Log verification result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Monitor and verify kill switch functionality. Provides automated verification…]] - rationale - gateway/security/killswitch_monitor.py
- [[Remove metrics older than cutoff_time.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for anomaly detection.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for heartbeat failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for verification failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test a specific kill switch mode. Args mode The kill switch mode to test…]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if Docker is available.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script exists.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script has correct permissions.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script has valid syntax.]] - rationale - gateway/security/killswitch_monitor.py
- [[TestStatusAndStats]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestVerifyKillswitch]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[Verify that the kill switch mechanism works without actually killing. Args…]] - rationale - gateway/security/killswitch_monitor.py
- [[deque]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KillSwitchMonitor
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_KillSwitchConfig]]
- 12 edges to [[_COMMUNITY__fake_stats]]
- 2 edges to [[_COMMUNITY_TestKillSwitchVerification]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_test_observatory_mode.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[KillSwitchMonitor]] - degree 62, connects to 9 communities
- [[Any_86]] - degree 20, connects to 1 community
- [[TestVerifyKillswitch]] - degree 6, connects to 1 community
- [[TestStatusAndStats]] - degree 5, connects to 1 community
- [[dot-test_get_status_reports_verification_due()]] - degree 3, connects to 1 community
