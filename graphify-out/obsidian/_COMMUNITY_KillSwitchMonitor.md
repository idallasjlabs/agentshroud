---
type: community
cohesion: 0.03
members: 114
---

# KillSwitchMonitor

**Cohesion:** 0.03 - loosely connected
**Members:** 114 nodes

## Members
- [[dot-__init__()_93]] - code - gateway/proxy/mcp_audit.py
- [[dot-__init__()_94]] - code - gateway/proxy/pipeline.py
- [[dot-__init__()_95]] - code - gateway/security/alert_dispatcher.py
- [[dot-__init__()_96]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-__init__()_97]] - code - gateway/security/killswitch_monitor.py
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
- [[dot-from_env()_2]] - code - gateway/security/killswitch_config.py
- [[dot-get_status()]] - code - gateway/security/killswitch_monitor.py
- [[dot-heartbeat_check()]] - code - gateway/security/killswitch_monitor.py
- [[dot-test_all_pass_when_script_valid()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_anomaly_detection_excessive_tool_calls()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_anomaly_detection_normal()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_clean_old_metrics_drops_stale_entries()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_critical_logged_when_setting_non_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_config()_4]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_docker_unavailable_is_fail()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_dry_run_exercises_enabled_modes()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_excessive_requests_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_excessive_tokens_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_excessive_tool_calls_flagged_and_alerted()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_fail_when_script_missing_triggers_alert()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_failure_increments_and_alerts_at_threshold()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_get_status()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_get_status_reports_verification_due()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_get_system_stats_handles_psutil_error()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_healthy_resets_miss_counter()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_heartbeat_check()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_init()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_killswitch_dry_run_disabled()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_no_anomaly_when_within_limits()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_no_critical_when_setting_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_slow_when_response_exceeds_timeout()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_system_resource_cpu_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_system_resource_memory_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_verify_killswitch_script_not_exists()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-to_dict()_10]] - code - gateway/security/killswitch_config.py
- [[dot-verify_killswitch()]] - code - gateway/security/killswitch_monitor.py
- [[Any_39]] - code - gateway/security/killswitch_config.py
- [[Any_40]] - code - gateway/security/killswitch_monitor.py
- [[Check if request rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if system resource usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if the agent is responding within expected parameters.          Returns]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if token usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if tool call rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Configuration for kill switch monitoring and verification.]] - rationale - gateway/security/killswitch_config.py
- [[Convert configuration to dictionary for serialization.]] - rationale - gateway/security/killswitch_config.py
- [[Count events in the last N seconds.]] - rationale - gateway/security/killswitch_monitor.py
- [[Detect unusual patterns that might indicate rogue behavior.          Args]] - rationale - gateway/security/killswitch_monitor.py
- [[FR2 Use Control]] - concept - docs/compliance/iec-62443-matrix.md
- [[Get current kill switch monitor status.          Returns             Dict conta]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current system statistics.]] - rationale - gateway/security/killswitch_monitor.py
- [[Kill Switch Module Badge Icon]] - image - branding/icons/modules/kill-switch-256x256.png
- [[Kill switch dry_run must be False — real termination on anomaly.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[KillSwitchConfig]] - code - gateway/security/killswitch_monitor.py
- [[KillSwitchConfig_1]] - code - gateway/security/killswitch_config.py
- [[KillSwitchMonitor]] - code - gateway/security/killswitch_monitor.py
- [[Load configuration from environment variables._1]] - rationale - gateway/security/killswitch_config.py
- [[Log heartbeat result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Log verification result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Monitor and verify kill switch functionality.      Provides automated verificati]] - rationale - gateway/security/killswitch_monitor.py
- [[Path_34]] - code - gateway/security/alert_dispatcher.py
- [[Remove metrics older than cutoff_time.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for anomaly detection.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for heartbeat failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for verification failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test a specific kill switch mode.          Args             mode The kill swit]] - rationale - gateway/security/killswitch_monitor.py
- [[Test anomaly detection with excessive tool calls.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test anomaly detection with normal metrics.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test basic heartbeat functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test default configuration values._3]] - rationale - gateway/tests/test_killswitch_monitor.py
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
- [[TestCriticalLogging]] - code - gateway/tests/test_observatory_mode.py
- [[TestHeartbeat]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestKillSwitchConfig]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchMonitor]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestStatusAndStats]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestVerifyKillswitch]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[Verify that the kill switch mechanism works without actually killing.          A]] - rationale - gateway/security/killswitch_monitor.py
- [[_fake_stats()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[config()_2]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[deque]] - code - gateway/security/killswitch_monitor.py
- [[dispatcher()_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[killswitch_config.py]] - code - gateway/security/killswitch_config.py
- [[killswitch_config.py (KillSwitchConfig)]] - code - gateway/security/killswitch_config.py
- [[killswitch_monitor.py]] - code - gateway/security/killswitch_monitor.py
- [[killswitch_monitor.py (KillSwitchMonitor)]] - code - gateway/security/killswitch_monitor.py
- [[test_killswitch_monitor.py]] - code - gateway/tests/test_killswitch_monitor.py
- [[test_killswitch_monitor_behavior.py]] - code - gateway/tests/test_killswitch_monitor_behavior.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KillSwitchMonitor
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_MiddlewareManager]]
- 13 edges to [[_COMMUNITY_test_observatory_mode.py]]
- 6 edges to [[_COMMUNITY_TestKillSwitchVerification]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_ModeRequest]]
- 2 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 2 edges to [[_COMMUNITY_TestObservatoryMode]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_dot-analyze_message]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_05-behavior]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]

## Top bridge nodes
- [[KillSwitchMonitor]] - degree 80, connects to 6 communities
- [[FR2 Use Control]] - degree 7, connects to 6 communities
- [[KillSwitchConfig_1]] - degree 43, connects to 5 communities
- [[TestCriticalLogging]] - degree 7, connects to 3 communities
- [[killswitch_monitor.py]] - degree 8, connects to 2 communities
