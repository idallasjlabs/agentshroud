---
type: community
cohesion: 0.08
members: 46
---

# Module Group 85

**Cohesion:** 0.08 - loosely connected
**Members:** 46 nodes

## Members
- [[.__init__()_73]] - code - gateway/security/killswitch_monitor.py
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
- [[.verify_killswitch()]] - code - gateway/security/killswitch_monitor.py
- [[Any_40]] - code - gateway/security/killswitch_monitor.py
- [[Check if request rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if system resource usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if the agent is responding within expected parameters.          Returns]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if token usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if tool call rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Count events in the last N seconds.]] - rationale - gateway/security/killswitch_monitor.py
- [[Detect unusual patterns that might indicate rogue behavior.          Args]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current kill switch monitor status.          Returns             Dict conta]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current system statistics.]] - rationale - gateway/security/killswitch_monitor.py
- [[KillSwitchMonitor]] - code - gateway/security/killswitch_monitor.py
- [[Log heartbeat result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Log verification result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Monitor and verify kill switch functionality.      Provides automated verificati]] - rationale - gateway/security/killswitch_monitor.py
- [[Remove metrics older than cutoff_time.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for anomaly detection.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for heartbeat failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Send alert for verification failure.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test a specific kill switch mode.          Args             mode The kill swit]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if Docker is available.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script exists.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script has correct permissions.]] - rationale - gateway/security/killswitch_monitor.py
- [[Test if the kill switch script has valid syntax.]] - rationale - gateway/security/killswitch_monitor.py
- [[Verify that the kill switch mechanism works without actually killing.          A]] - rationale - gateway/security/killswitch_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_85
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Module Group 98]]
- 10 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 6 edges to [[_COMMUNITY_Module Group 126]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 505]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 233]]
- 1 edge to [[_COMMUNITY_Module Group 488]]
- 1 edge to [[_COMMUNITY_Module Group 336]]

## Top bridge nodes
- [[KillSwitchMonitor]] - degree 59, connects to 8 communities
- [[.__init__()_73]] - degree 4, connects to 2 communities
- [[Any_40]] - degree 21, connects to 1 community
- [[._count_recent_events()]] - degree 7, connects to 1 community