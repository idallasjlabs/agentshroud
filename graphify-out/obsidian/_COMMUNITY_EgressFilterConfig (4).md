---
type: community
members: 84
---

# EgressFilterConfig (4)

**Members:** 84 nodes

## Members
- [[dot-from_env()]] - code - gateway/security/killswitch_config.py
- [[dot-test_anomaly_detection_excessive_tool_calls()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_anomaly_detection_normal()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_auto_revert_restores_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_auto_revert_timer_logic()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_critical_logged_when_setting_non_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_custom_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_config()_7]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_default_mode_is_enforce()_4]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_default_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_get_module_mode_pinned_modules()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_get_module_mode_respect_global_override()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_get_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_get_status()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_heartbeat_check()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_init()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-test_killswitch_dry_run_disabled()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_module_mode_resolution()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_no_critical_when_setting_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_observatory_mode_state_initialization()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_observatory_mode_validation()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_pinned_modules_validation()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_response_includes_timestamp()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_returns_monitor_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_returns_observatory_when_set()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_revert_task_created_on_put()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_second_put_cancels_previous_task()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_security_pipeline_set_global_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_security_pipeline_set_global_mode_missing_components()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_observatory_mode_endpoint()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_valid_modes_constant()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_verify_killswitch_script_not_exists()]] - code - gateway/tests/test_killswitch_monitor.py
- [[dot-to_dict()_9]] - code - gateway/security/killswitch_config.py
- [[A revert task is created (and is an asyncio.Task).]] - rationale - gateway/tests/test_observatory_mode.py
- [[Any_54]] - code - gateway/security/killswitch_config.py
- [[Auto-revert task sets mode back to enforce after delay.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Configuration for kill switch monitoring and verification.]] - rationale - gateway/security/killswitch_config.py
- [[Convert configuration to dictionary for serialization.]] - rationale - gateway/security/killswitch_config.py
- [[FastAPI_3]] - code - gateway/tests/test_observatory_mode.py
- [[Integration tests for Observatory Mode API endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Kill switch dry_run must be False — real termination on anomaly.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[KillSwitchConfig]] - code - gateway/security/killswitch_config.py
- [[Load configuration from environment variables.]] - rationale - gateway/security/killswitch_config.py
- [[Minimal FastAPI app that mounts the management router with auth bypassed.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Reset AGENTSHROUD_MODE and cancel any revert task between tests.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Second PUT cancels the first revert task.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Set AGENTSHROUD_MODE at runtime with automatic revert to 'enforce'.]] - rationale - gateway/web/api.py
- [[Test GET managemode endpoint returns correct structure.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test Observatory Mode configuration and endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test POST managemode endpoint requestresponse.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test SecurityPipeline.set_global_mode method.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test anomaly detection with excessive tool calls.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test anomaly detection with normal metrics.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test auto-revert timer functionality.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test basic heartbeat functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test default configuration values._5]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test kill switch configuration.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test kill switch monitor functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test module mode resolution with pinned modules.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test monitor initialization.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test set_global_mode handles missing components gracefully.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test status retrieval.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test that get_module_mode respects AGENTSHROUD_MODE env var.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test that observatory mode state is properly initialized.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test that pinned modules always return enforce even in monitor mode.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test validation of observatory mode parameters.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test validation of pinned module names.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test verification when kill switch script does not exist.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[TestAutoRevert]] - code - gateway/tests/test_observatory_mode.py
- [[TestCriticalLogging]] - code - gateway/tests/test_observatory_mode.py
- [[TestGetMode]] - code - gateway/tests/test_observatory_mode.py
- [[TestKillSwitchConfig_1]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchMonitor]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestModeRequestModel]] - code - gateway/tests/test_observatory_mode.py
- [[TestObservatoryMode]] - code - gateway/tests/test_observatory_mode.py
- [[TestObservatoryModeAPI]] - code - gateway/tests/test_observatory_mode.py
- [[_make_app()]] - code - gateway/tests/test_observatory_mode.py
- [[client()_18]] - code - gateway/tests/test_observatory_mode.py
- [[killswitch_config.py]] - code - gateway/security/killswitch_config.py
- [[killswitch_monitor.py]] - code - gateway/security/killswitch_monitor.py
- [[reset_env_and_task()]] - code - gateway/tests/test_observatory_mode.py
- [[set_mode()]] - code - gateway/web/api.py
- [[test_killswitch_monitor.py]] - code - gateway/tests/test_killswitch_monitor.py
- [[test_observatory_mode.py]] - code - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig_4
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_AgentTarget (3)]]
- 15 edges to [[_COMMUNITY_AsyncMock]]
- 10 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 6 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig (4) (2)]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_TestWebSearchLog]]
- 1 edge to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (3)]]
- 1 edge to [[_COMMUNITY_DelegationManager]]

## Top bridge nodes
- [[test_observatory_mode.py]] - degree 19, connects to 6 communities
- [[KillSwitchConfig]] - degree 43, connects to 4 communities
- [[killswitch_monitor.py]] - degree 6, connects to 4 communities
- [[TestObservatoryMode]] - degree 15, connects to 3 communities
- [[TestGetMode]] - degree 9, connects to 3 communities
