---
type: community
cohesion: 0.03
members: 121
---

# KillSwitchMonitor

**Cohesion:** 0.03 - loosely connected
**Members:** 121 nodes

## Members
- [[dot-__init__()_108]] - code - gateway/proxy/mcp_audit.py
- [[dot-__init__()_109]] - code - gateway/proxy/pipeline.py
- [[dot-__init__()_110]] - code - gateway/security/alert_dispatcher.py
- [[dot-__init__()_111]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-__init__()_112]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_request_rate()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_system_resources()_1]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_token_usage()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_tool_call_rate()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_clean_old_metrics()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_count_recent_events()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_get_system_stats()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_log_heartbeat_result()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_log_verification_result()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_make_monitor()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-_send_anomaly_alert()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_send_heartbeat_alert()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_send_verification_alert()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_docker_available()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_killswitch_mode()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_script_exists()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_script_permissions()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_test_script_syntax()]] - code - gateway/security/killswitch_monitor.py
- [[dot-anomaly_detection()]] - code - gateway/security/killswitch_monitor.py
- [[dot-get_status()_1]] - code - gateway/security/killswitch_monitor.py
- [[dot-heartbeat_check()]] - code - gateway/security/killswitch_monitor.py
- [[dot-test_all_pass_when_script_valid()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_anomaly_detection_excessive_tool_calls()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_anomaly_detection_normal()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_clean_old_metrics_drops_stale_entries()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_default_config()_2]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_docker_unavailable_is_fail()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_dry_run_exercises_enabled_modes()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_dry_run_true_does_not_kill()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_duration_is_non_negative()]] - code - gateway/tests/test_observatory_mode.py
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
- [[dot-test_overall_status_is_valid_value()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_result_has_required_fields()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_script_exists_test_is_present()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_slow_when_response_exceeds_timeout()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_system_resource_cpu_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_system_resource_memory_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dot-test_verification_log_written()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_verify_killswitch_script_not_exists()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-to_dict()_6]] - code - gateway/security/killswitch_config.py
- [[dot-verify_killswitch()]] - code - gateway/security/killswitch_monitor.py
- [[Any_41]] - code - gateway/security/killswitch_config.py
- [[Any_42]] - code - gateway/security/killswitch_monitor.py
- [[Automated verification that verify_killswitch() returns required fields.]] - rationale - gateway/tests/test_observatory_mode.py
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
- [[Log heartbeat result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Log verification result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Monitor and verify kill switch functionality.      Provides automated verificati]] - rationale - gateway/security/killswitch_monitor.py
- [[Path_29]] - code - gateway/security/alert_dispatcher.py
- [[Path_30]] - code - gateway/tests/test_observatory_mode.py
- [[Remove metrics older than cutoff_time.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for anomaly detection.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for heartbeat failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for verification failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test a specific kill switch mode.          Args             mode The kill swit]] - rationale - gateway/security/killswitch_monitor.py
- [[Test anomaly detection with excessive tool calls.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test anomaly detection with normal metrics.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test basic heartbeat functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test default configuration values._1]] - rationale - gateway/tests/test_killswitch_monitor.py
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
- [[TestKillSwitchConfig]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchMonitor]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchVerification]] - code - gateway/tests/test_observatory_mode.py
- [[TestStatusAndStats]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestVerifyKillswitch]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[Verify that the kill switch mechanism works without actually killing.          A]] - rationale - gateway/security/killswitch_monitor.py
- [[_fake_stats()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[config()_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[deque]] - code - gateway/security/killswitch_monitor.py
- [[dispatcher()_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dry_run=True must never trigger actual kill switch execution.]] - rationale - gateway/tests/test_observatory_mode.py
- [[killswitch_config.py]] - code - gateway/security/killswitch_config.py
- [[killswitch_config.py (KillSwitchConfig)]] - code - gateway/security/killswitch_config.py
- [[killswitch_monitor.py]] - code - gateway/security/killswitch_monitor.py
- [[killswitch_monitor.py (KillSwitchMonitor)]] - code - gateway/security/killswitch_monitor.py
- [[test_killswitch_monitor.py]] - code - gateway/tests/test_killswitch_monitor.py
- [[test_killswitch_monitor_behavior.py]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[verify_killswitch() must write a log entry for auditability.]] - rationale - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KillSwitchMonitor
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_MiddlewareManager]]
- 15 edges to [[_COMMUNITY_test_observatory_mode.py]]
- 4 edges to [[_COMMUNITY_ModeRequest]]
- 3 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 2 edges to [[_COMMUNITY_TestObservatoryMode]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_Path_3]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_05-behavior]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]

## Top bridge nodes
- [[FR2 Use Control]] - degree 7, connects to 6 communities
- [[KillSwitchConfig_1]] - degree 43, connects to 5 communities
- [[KillSwitchMonitor]] - degree 80, connects to 4 communities
- [[TestKillSwitchVerification]] - degree 13, connects to 3 communities
- [[killswitch_monitor.py]] - degree 8, connects to 2 communities
