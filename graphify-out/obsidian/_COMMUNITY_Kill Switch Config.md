---
type: community
cohesion: 0.04
members: 101
---

# Kill Switch Config

**Cohesion:** 0.04 - loosely connected
**Members:** 101 nodes

## Members
- [[.__init__()_89]] - code - gateway/security/killswitch_monitor.py
- [[._check_request_rate()]] - code - gateway/security/killswitch_monitor.py
- [[._check_system_resources()]] - code - gateway/security/killswitch_monitor.py
- [[._check_token_usage()]] - code - gateway/security/killswitch_monitor.py
- [[._check_tool_call_rate()]] - code - gateway/security/killswitch_monitor.py
- [[._clean_old_metrics()]] - code - gateway/security/killswitch_monitor.py
- [[._count_recent_events()]] - code - gateway/security/killswitch_monitor.py
- [[._get_system_stats()]] - code - gateway/security/killswitch_monitor.py
- [[._log_heartbeat_result()]] - code - gateway/security/killswitch_monitor.py
- [[._log_verification_result()]] - code - gateway/security/killswitch_monitor.py
- [[._send_anomaly_alert()]] - code - gateway/security/killswitch_monitor.py
- [[._send_heartbeat_alert()]] - code - gateway/security/killswitch_monitor.py
- [[._send_verification_alert()]] - code - gateway/security/killswitch_monitor.py
- [[._test_docker_available()]] - code - gateway/security/killswitch_monitor.py
- [[._test_killswitch_mode()]] - code - gateway/security/killswitch_monitor.py
- [[._test_script_exists()]] - code - gateway/security/killswitch_monitor.py
- [[._test_script_permissions()]] - code - gateway/security/killswitch_monitor.py
- [[._test_script_syntax()]] - code - gateway/security/killswitch_monitor.py
- [[.anomaly_detection()]] - code - gateway/security/killswitch_monitor.py
- [[.get_status()]] - code - gateway/security/killswitch_monitor.py
- [[.heartbeat_check()]] - code - gateway/security/killswitch_monitor.py
- [[.test_all_pass_when_script_valid()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_anomaly_detection_excessive_tool_calls()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_anomaly_detection_normal()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_clean_old_metrics_drops_stale_entries()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_default_config()_3]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_docker_unavailable_is_fail()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_dry_run_exercises_enabled_modes()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_excessive_requests_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_excessive_tokens_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_excessive_tool_calls_flagged_and_alerted()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_fail_when_script_missing_triggers_alert()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_failure_increments_and_alerts_at_threshold()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_get_status()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_get_status_reports_verification_due()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_get_system_stats_handles_psutil_error()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_healthy_resets_miss_counter()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_heartbeat_check()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_init()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_killswitch_dry_run_disabled()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_no_anomaly_when_within_limits()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_slow_when_response_exceeds_timeout()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_system_resource_cpu_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_system_resource_memory_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_verify_killswitch_script_not_exists()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.to_dict()_9]] - code - gateway/security/killswitch_config.py
- [[.verify_killswitch()]] - code - gateway/security/killswitch_monitor.py
- [[Any_41]] - code - gateway/security/killswitch_config.py
- [[Any_42]] - code - gateway/security/killswitch_monitor.py
- [[Check if request rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if system resource usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if the agent is responding within expected parameters.          Returns]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if token usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if tool call rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Configuration for kill switch monitoring and verification.]] - rationale - gateway/security/killswitch_config.py
- [[Convert configuration to dictionary for serialization.]] - rationale - gateway/security/killswitch_config.py
- [[Count events in the last N seconds.]] - rationale - gateway/security/killswitch_monitor.py
- [[Detect unusual patterns that might indicate rogue behavior.          Args]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current kill switch monitor status.          Returns             Dict conta]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current system statistics.]] - rationale - gateway/security/killswitch_monitor.py
- [[Kill switch dry_run must be False — real termination on anomaly.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[KillSwitchConfig_1]] - code - gateway/security/killswitch_monitor.py
- [[KillSwitchConfig]] - code - gateway/security/killswitch_config.py
- [[KillSwitchMonitor]] - code - gateway/security/killswitch_monitor.py
- [[Log heartbeat result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Log verification result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Monitor and verify kill switch functionality.      Provides automated verificati]] - rationale - gateway/security/killswitch_monitor.py
- [[Remove metrics older than cutoff_time.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for anomaly detection.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for heartbeat failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for verification failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test a specific kill switch mode.          Args             mode The kill swit]] - rationale - gateway/security/killswitch_monitor.py
- [[Test anomaly detection with excessive tool calls.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test anomaly detection with normal metrics.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test basic heartbeat functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test default configuration values._2]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test if Docker is available.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script exists.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script has correct permissions.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script has valid syntax.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test kill switch configuration.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test kill switch monitor functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test monitor initialization.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test status retrieval.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test verification when kill switch script does not exist.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[TestAnomalyDetection_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestHeartbeat]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestKillSwitchConfig_1]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchMonitor]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestStatusAndStats]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestVerifyKillswitch]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[Verify that the kill switch mechanism works without actually killing.          A]] - rationale - gateway/security/killswitch_monitor.py
- [[_fake_stats()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[config()_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dispatcher()_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[killswitch_config.py]] - code - gateway/security/killswitch_config.py
- [[killswitch_config.py (KillSwitchConfig)]] - code - gateway/security/killswitch_config.py
- [[killswitch_monitor.py]] - code - gateway/security/killswitch_monitor.py
- [[killswitch_monitor.py (KillSwitchMonitor)]] - code - gateway/security/killswitch_monitor.py
- [[test_killswitch_monitor.py]] - code - gateway/tests/test_killswitch_monitor.py
- [[test_killswitch_monitor_behavior.py]] - code - gateway/tests/test_killswitch_monitor_behavior.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Kill_Switch_Config
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Egress & RBAC Security Core]]
- 16 edges to [[_COMMUNITY_Gateway Test Suite]]
- 5 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 5 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_Security Pipeline Core]]
- 2 edges to [[_COMMUNITY_Forward Routing & Approval]]
- 2 edges to [[_COMMUNITY_Enforce-Mode Auto-Revert]]
- 1 edge to [[_COMMUNITY_Security Module Middleware]]
- 1 edge to [[_COMMUNITY_Gateway Security Module]]
- 1 edge to [[_COMMUNITY_Gateway Security Module]]

## Top bridge nodes
- [[KillSwitchMonitor]] - degree 81, connects to 7 communities
- [[KillSwitchConfig]] - degree 43, connects to 7 communities
- [[killswitch_monitor.py]] - degree 6, connects to 2 communities
- [[KillSwitchConfig_1]] - degree 12, connects to 1 community
- [[._count_recent_events()]] - degree 7, connects to 1 community