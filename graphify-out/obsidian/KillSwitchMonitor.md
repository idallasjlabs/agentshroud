---
source_file: "gateway/security/killswitch_monitor.py"
type: "code"
community: "Module Group 85"
location: "L30"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_85
---

# KillSwitchMonitor

## Connections
- [[.__init__()_8]] - `calls` [EXTRACTED]
- [[.__init__()_73]] - `method` [EXTRACTED]
- [[._check_request_rate()]] - `method` [EXTRACTED]
- [[._check_system_resources()]] - `method` [EXTRACTED]
- [[._check_token_usage()]] - `method` [EXTRACTED]
- [[._check_tool_call_rate()]] - `method` [EXTRACTED]
- [[._clean_old_metrics()]] - `method` [EXTRACTED]
- [[._count_recent_events()]] - `method` [EXTRACTED]
- [[._get_system_stats()]] - `method` [EXTRACTED]
- [[._log_heartbeat_result()]] - `method` [EXTRACTED]
- [[._log_verification_result()]] - `method` [EXTRACTED]
- [[._make_monitor()]] - `calls` [EXTRACTED]
- [[._send_anomaly_alert()]] - `method` [EXTRACTED]
- [[._send_heartbeat_alert()]] - `method` [EXTRACTED]
- [[._send_verification_alert()]] - `method` [EXTRACTED]
- [[._test_docker_available()]] - `method` [EXTRACTED]
- [[._test_killswitch_mode()]] - `method` [EXTRACTED]
- [[._test_script_exists()]] - `method` [EXTRACTED]
- [[._test_script_permissions()]] - `method` [EXTRACTED]
- [[._test_script_syntax()]] - `method` [EXTRACTED]
- [[.anomaly_detection()]] - `method` [EXTRACTED]
- [[.get_status()]] - `method` [EXTRACTED]
- [[.heartbeat_check()]] - `method` [EXTRACTED]
- [[.test_anomaly_detection_excessive_tool_calls()]] - `calls` [EXTRACTED]
- [[.test_anomaly_detection_normal()]] - `calls` [EXTRACTED]
- [[.test_get_status()]] - `calls` [EXTRACTED]
- [[.test_heartbeat_check()]] - `calls` [EXTRACTED]
- [[.test_init()]] - `calls` [EXTRACTED]
- [[.test_verify_killswitch_script_not_exists()]] - `calls` [EXTRACTED]
- [[.verify_killswitch()]] - `method` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_6]] - `uses` [INFERRED]
- [[FastAPI_2]] - `uses` [INFERRED]
- [[KillSwitchConfig]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Monitor and verify kill switch functionality.      Provides automated verificati]] - `rationale_for` [EXTRACTED]
- [[Path_27]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestAutoRevert]] - `uses` [INFERRED]
- [[TestCriticalLogging]] - `uses` [INFERRED]
- [[TestGetMode]] - `uses` [INFERRED]
- [[TestKillSwitchConfig_1]] - `uses` [INFERRED]
- [[TestKillSwitchMonitor]] - `uses` [INFERRED]
- [[TestKillSwitchVerification]] - `uses` [INFERRED]
- [[TestModeRequestModel]] - `uses` [INFERRED]
- [[TestObservatoryMode]] - `uses` [INFERRED]
- [[TestObservatoryModeAPI]] - `uses` [INFERRED]
- [[TestSetMode]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[killswitch_monitor.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_killswitch_monitor.py]] - `imports` [EXTRACTED]
- [[test_observatory_mode.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_85
