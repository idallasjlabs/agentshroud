---
type: community
cohesion: 0.02
members: 159
---

# Killswitch Monitor & Observatory Mode

**Cohesion:** 0.02 - loosely connected
**Members:** 159 nodes

## Members
- [[.__init__()_25]] - code - gateway/proxy/mcp_audit.py
- [[.__init__()_32]] - code - gateway/proxy/pipeline.py
- [[.__init__()_53]] - code - gateway/security/alert_dispatcher.py
- [[.__init__()_92]] - code - gateway/security/killswitch_monitor.py
- [[._check_request_rate()]] - code - gateway/security/killswitch_monitor.py
- [[._check_system_resources()]] - code - gateway/security/killswitch_monitor.py
- [[._check_token_usage()]] - code - gateway/security/killswitch_monitor.py
- [[._check_tool_call_rate()]] - code - gateway/security/killswitch_monitor.py
- [[._clean_old_metrics()]] - code - gateway/security/killswitch_monitor.py
- [[._count_recent_events()]] - code - gateway/security/killswitch_monitor.py
- [[._get_system_stats()]] - code - gateway/security/killswitch_monitor.py
- [[._log_heartbeat_result()]] - code - gateway/security/killswitch_monitor.py
- [[._log_verification_result()]] - code - gateway/security/killswitch_monitor.py
- [[._make_monitor()]] - code - gateway/tests/test_observatory_mode.py
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
- [[.test_auto_revert_timer_logic()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_clean_old_metrics_drops_stale_entries()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_critical_logged_when_setting_non_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_default_config()_3]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_default_mode_is_enforce()_3]] - code - gateway/tests/test_observatory_mode.py
- [[.test_docker_unavailable_is_fail()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_dry_run_exercises_enabled_modes()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_dry_run_true_does_not_kill()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_duration_is_non_negative()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_excessive_requests_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_excessive_tokens_flagged()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_excessive_tool_calls_flagged_and_alerted()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_fail_when_script_missing_triggers_alert()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_failure_increments_and_alerts_at_threshold()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_get_module_mode_pinned_modules()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_status()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_get_status_reports_verification_due()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_get_system_stats_handles_psutil_error()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_healthy_resets_miss_counter()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_heartbeat_check()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_init()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_killswitch_dry_run_disabled()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_module_mode_resolution()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_no_anomaly_when_within_limits()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_no_critical_when_setting_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_observatory_mode_state_initialization()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_observatory_mode_validation()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_overall_status_is_valid_value()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_pinned_modules_validation()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_response_includes_timestamp()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_result_has_required_fields()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_returns_monitor_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_returns_observatory_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_script_exists_test_is_present()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_security_pipeline_set_global_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_security_pipeline_set_global_mode_missing_components()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_set_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_slow_when_response_exceeds_timeout()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_system_resource_cpu_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_system_resource_memory_anomaly()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[.test_verification_log_written()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_verify_killswitch_script_not_exists()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.to_dict()_10]] - code - gateway/security/killswitch_config.py
- [[.verify_killswitch()]] - code - gateway/security/killswitch_monitor.py
- [[Any_44]] - code - gateway/security/killswitch_config.py
- [[Any_45]] - code - gateway/security/killswitch_monitor.py
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
- [[FastAPI_2]] - code - gateway/tests/test_observatory_mode.py
- [[Get current kill switch monitor status.          Returns             Dict conta]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current system statistics.]] - rationale - gateway/security/killswitch_monitor.py
- [[Integration tests for Observatory Mode API endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Kill switch dry_run must be False — real termination on anomaly.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[KillSwitchConfig_1]] - code - gateway/security/killswitch_monitor.py
- [[KillSwitchConfig]] - code - gateway/security/killswitch_config.py
- [[KillSwitchMonitor]] - code - gateway/security/killswitch_monitor.py
- [[Log heartbeat result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Log verification result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Minimal FastAPI app that mounts the management router with auth bypassed.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Monitor and verify kill switch functionality.      Provides automated verificati]] - rationale - gateway/security/killswitch_monitor.py
- [[Path_5]] - code - gateway/security/alert_dispatcher.py
- [[Path_35]] - code - gateway/tests/test_observatory_mode.py
- [[Remove metrics older than cutoff_time.]] - rationale - gateway/security/killswitch_monitor.py
- [[Reset AGENTSHROUD_MODE and cancel any revert task between tests.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Send alert for anomaly detection.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for heartbeat failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for verification failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test GET managemode endpoint returns correct structure.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test Observatory Mode configuration and endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test POST managemode endpoint requestresponse.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test SecurityPipeline.set_global_mode method.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test a specific kill switch mode.          Args             mode The kill swit]] - rationale - gateway/security/killswitch_monitor.py
- [[Test anomaly detection with excessive tool calls.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test anomaly detection with normal metrics.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test auto-revert timer functionality.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test basic heartbeat functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test default configuration values._2]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test if Docker is available.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script exists.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script has correct permissions.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script has valid syntax.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test kill switch configuration.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test kill switch monitor functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test module mode resolution with pinned modules.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test monitor initialization.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test set_global_mode handles missing components gracefully.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test status retrieval.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test that observatory mode state is properly initialized.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test that pinned modules always return enforce even in monitor mode.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test validation of observatory mode parameters.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test validation of pinned module names.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test verification when kill switch script does not exist.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[TestAnomalyDetection_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestCriticalLogging]] - code - gateway/tests/test_observatory_mode.py
- [[TestGetMode]] - code - gateway/tests/test_observatory_mode.py
- [[TestHeartbeat]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestKillSwitchConfig_1]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchMonitor]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchVerification]] - code - gateway/tests/test_observatory_mode.py
- [[TestObservatoryMode]] - code - gateway/tests/test_observatory_mode.py
- [[TestObservatoryModeAPI]] - code - gateway/tests/test_observatory_mode.py
- [[TestStatusAndStats]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[TestVerifyKillswitch]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[Verify that the kill switch mechanism works without actually killing.          A]] - rationale - gateway/security/killswitch_monitor.py
- [[_fake_stats()]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[_make_app()]] - code - gateway/tests/test_observatory_mode.py
- [[client()_11]] - code - gateway/tests/test_observatory_mode.py
- [[config()_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[deque]] - code - gateway/security/killswitch_monitor.py
- [[dispatcher()_1]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[dry_run=True must never trigger actual kill switch execution.]] - rationale - gateway/tests/test_observatory_mode.py
- [[killswitch_config.py]] - code - gateway/security/killswitch_config.py
- [[killswitch_config.py (KillSwitchConfig)]] - code - gateway/security/killswitch_config.py
- [[killswitch_monitor.py]] - code - gateway/security/killswitch_monitor.py
- [[killswitch_monitor.py (KillSwitchMonitor)]] - code - gateway/security/killswitch_monitor.py
- [[progressive_lockdown.py]] - code - gateway/security/progressive_lockdown.py
- [[reset_env_and_task()]] - code - gateway/tests/test_observatory_mode.py
- [[test_killswitch_monitor.py]] - code - gateway/tests/test_killswitch_monitor.py
- [[test_killswitch_monitor_behavior.py]] - code - gateway/tests/test_killswitch_monitor_behavior.py
- [[test_observatory_mode.py]] - code - gateway/tests/test_observatory_mode.py
- [[verify_killswitch() must write a log entry for auditability.]] - rationale - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Killswitch_Monitor__Observatory_Mode
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 14 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 11 edges to [[_COMMUNITY_Web Api Coverage]]
- 5 edges to [[_COMMUNITY_Observatory Mode]]
- 4 edges to [[_COMMUNITY_Progressive Lockdown]]
- 3 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 3 edges to [[_COMMUNITY_All Modules Enforce]]
- 3 edges to [[_COMMUNITY_Observatory Mode]]
- 1 edge to [[_COMMUNITY_Mcp Audit (proxy)]]
- 1 edge to [[_COMMUNITY_Pipeline Unit]]
- 1 edge to [[_COMMUNITY_Context Guard (security)]]
- 1 edge to [[_COMMUNITY_Cross Bot Trust Ledger]]
- 1 edge to [[_COMMUNITY_Delegation]]
- 1 edge to [[_COMMUNITY_Manifest (skills)]]
- 1 edge to [[_COMMUNITY_Icon 64x64 (app)]]
- 1 edge to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 1 edge to [[_COMMUNITY_Dashboard Endpoints (web)]]
- 1 edge to [[_COMMUNITY_Iec 62443 Matrix (compliance)]]
- 1 edge to [[_COMMUNITY_Phase 3a 3b Implementation (architecture)]]
- 1 edge to [[_COMMUNITY_05 Behavior (diagrams)]]

## Top bridge nodes
- [[KillSwitchConfig]] - degree 43, connects to 6 communities
- [[test_observatory_mode.py]] - degree 19, connects to 6 communities
- [[FR2 Use Control]] - degree 8, connects to 6 communities
- [[KillSwitchMonitor]] - degree 80, connects to 5 communities
- [[TestObservatoryMode]] - degree 15, connects to 3 communities