---
type: community
members: 50
---

# KillSwitchMonitor (3)

**Members:** 50 nodes

## Members
- [[dot-__init__()_52]] - code - gateway/proxy/mcp_audit.py
- [[dot-__init__()_53]] - code - gateway/proxy/pipeline.py
- [[dot-__init__()_54]] - code - gateway/security/alert_dispatcher.py
- [[dot-__init__()_55]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_request_rate()]] - code - gateway/security/killswitch_monitor.py
- [[dot-_check_system_resources()]] - code - gateway/security/killswitch_monitor.py
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
- [[dot-get_status()]] - code - gateway/security/killswitch_monitor.py
- [[dot-heartbeat_check()]] - code - gateway/security/killswitch_monitor.py
- [[dot-verify_killswitch()]] - code - gateway/security/killswitch_monitor.py
- [[Any_13]] - code - gateway/security/killswitch_monitor.py
- [[Check if request rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if system resource usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if the agent is responding within expected parameters.          Returns]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if token usage is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Check if tool call rate is abnormal.]] - rationale - gateway/security/killswitch_monitor.py
- [[Count events in the last N seconds.]] - rationale - gateway/security/killswitch_monitor.py
- [[Detect unusual patterns that might indicate rogue behavior.          Args]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current kill switch monitor status.          Returns             Dict conta]] - rationale - gateway/security/killswitch_monitor.py
- [[Get current system statistics.]] - rationale - gateway/security/killswitch_monitor.py
- [[KillSwitchConfig]] - code - gateway/security/killswitch_monitor.py
- [[Log heartbeat result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Log verification result to file.]] - rationale - gateway/security/killswitch_monitor.py
- [[Path_12]] - code - gateway/security/alert_dispatcher.py
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
- [[deque]] - code - gateway/security/killswitch_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KillSwitchMonitor_3
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]

## Top bridge nodes
- [[deque]] - degree 8, connects to 3 communities
- [[Any_13]] - degree 21, connects to 1 community
- [[dot-anomaly_detection()]] - degree 11, connects to 1 community
- [[dot-verify_killswitch()]] - degree 10, connects to 1 community
- [[dot-_count_recent_events()]] - degree 7, connects to 1 community
