---
type: community
cohesion: 0.07
members: 43
---

# Module Group 98

**Cohesion:** 0.07 - loosely connected
**Members:** 43 nodes

## Members
- [[._make_monitor()]] - code - gateway/tests/test_observatory_mode.py
- [[.from_env()_1]] - code - gateway/security/killswitch_config.py
- [[.test_anomaly_detection_excessive_tool_calls()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_anomaly_detection_normal()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_default_config()_3]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_dry_run_true_does_not_kill()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_duration_is_non_negative()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_status()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_heartbeat_check()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_init()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.test_killswitch_dry_run_disabled()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_overall_status_is_valid_value()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_result_has_required_fields()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_script_exists_test_is_present()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_verification_log_written()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_verify_killswitch_script_not_exists()]] - code - gateway/tests/test_killswitch_monitor.py
- [[.to_dict()_9]] - code - gateway/security/killswitch_config.py
- [[Any_39]] - code - gateway/security/killswitch_config.py
- [[Automated verification that verify_killswitch() returns required fields.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Configuration for kill switch monitoring and verification.]] - rationale - gateway/security/killswitch_config.py
- [[Convert configuration to dictionary for serialization.]] - rationale - gateway/security/killswitch_config.py
- [[Kill switch dry_run must be False — real termination on anomaly.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[KillSwitchConfig_1]] - code - gateway/security/killswitch_monitor.py
- [[KillSwitchConfig]] - code - gateway/security/killswitch_config.py
- [[Load configuration from environment variables._1]] - rationale - gateway/security/killswitch_config.py
- [[Path_27]] - code - gateway/tests/test_observatory_mode.py
- [[Test anomaly detection with excessive tool calls.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test anomaly detection with normal metrics.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test basic heartbeat functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test default configuration values._2]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test kill switch configuration.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test kill switch monitor functionality.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test monitor initialization.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test status retrieval.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[Test verification when kill switch script does not exist.]] - rationale - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchConfig_1]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchMonitor]] - code - gateway/tests/test_killswitch_monitor.py
- [[TestKillSwitchVerification]] - code - gateway/tests/test_observatory_mode.py
- [[dry_run=True must never trigger actual kill switch execution.]] - rationale - gateway/tests/test_observatory_mode.py
- [[killswitch_config.py]] - code - gateway/security/killswitch_config.py
- [[killswitch_monitor.py]] - code - gateway/security/killswitch_monitor.py
- [[test_killswitch_monitor.py]] - code - gateway/tests/test_killswitch_monitor.py
- [[verify_killswitch() must write a log entry for auditability.]] - rationale - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_98
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Module Group 85]]
- 9 edges to [[_COMMUNITY_Module Group 126]]
- 6 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 2 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 2 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 505]]
- 1 edge to [[_COMMUNITY_Module Group 233]]
- 1 edge to [[_COMMUNITY_Module Group 488]]
- 1 edge to [[_COMMUNITY_Module Group 336]]

## Top bridge nodes
- [[KillSwitchConfig]] - degree 37, connects to 7 communities
- [[TestKillSwitchVerification]] - degree 14, connects to 4 communities
- [[Path_27]] - degree 6, connects to 4 communities
- [[killswitch_monitor.py]] - degree 5, connects to 3 communities
- [[TestKillSwitchMonitor]] - degree 10, connects to 1 community
