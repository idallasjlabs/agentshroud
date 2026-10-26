---
type: community
members: 45
---

# Community 5

**Members:** 45 nodes

## Members
- [[.__del__()]] - code - gateway/security/resource_guard.py
- [[.__init__()_114]] - code - gateway/security/resource_guard.py
- [[._alert_high_usage()]] - code - gateway/security/resource_guard.py
- [[._check_system_resources()_1]] - code - gateway/security/resource_guard.py
- [[._cleanup_expired_usage()]] - code - gateway/security/resource_guard.py
- [[._get_disk_io_stats()]] - code - gateway/security/resource_guard.py
- [[._monitor_resources()]] - code - gateway/security/resource_guard.py
- [[._start_monitoring_task()]] - code - gateway/security/resource_guard.py
- [[.add_alert_callback()_1]] - code - gateway/security/resource_guard.py
- [[.check_cpu_limit()]] - code - gateway/security/resource_guard.py
- [[.check_disk_write_limit()]] - code - gateway/security/resource_guard.py
- [[.check_memory_limit()]] - code - gateway/security/resource_guard.py
- [[.check_resource()]] - code - gateway/security/resource_guard.py
- [[.cleanup_temp_files()]] - code - gateway/security/resource_guard.py
- [[.get_usage_stats()]] - code - gateway/security/resource_guard.py
- [[.register_temp_file()]] - code - gateway/security/resource_guard.py
- [[.start_request_tracking()]] - code - gateway/security/resource_guard.py
- [[.stop()_11]] - code - gateway/security/resource_guard.py
- [[.stop_monitoring()]] - code - gateway/security/resource_guard.py
- [[.test_check_cpu_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_check_disk_write_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_check_memory_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[Add a callback function to be called when resource alerts are triggered.]] - rationale - gateway/security/resource_guard.py
- [[Any_57]] - code - gateway/security/resource_guard.py
- [[Background task to monitor resource usage and trigger alerts.]] - rationale - gateway/security/resource_guard.py
- [[Best-effort cleanup for test contexts that don't call stop().]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded CPU time limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded disk write limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded memory limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if resource usage is allowed for an agent.          Args             agen]] - rationale - gateway/security/resource_guard.py
- [[Check system-wide resource usage for anomalies (synchronous).]] - rationale - gateway/security/resource_guard.py
- [[Clean up old usage data (older than 5 minutes).]] - rationale - gateway/security/resource_guard.py
- [[Clean up temporary files for an agent.]] - rationale - gateway/security/resource_guard.py
- [[Get current disk IO statistics.]] - rationale - gateway/security/resource_guard.py
- [[Get current usage statistics.]] - rationale - gateway/security/resource_guard.py
- [[Monitor and limit resource usage per agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Register a temporary file for tracking.]] - rationale - gateway/security/resource_guard.py
- [[ResourceGuard]] - code - gateway/security/resource_guard.py
- [[Start background monitoring task.]] - rationale - gateway/security/resource_guard.py
- [[Start tracking resources for a specific agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring task cleanly.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring.]] - rationale - gateway/security/resource_guard.py
- [[TestResourceGuardFailClosed]] - code - gateway/tests/test_round2_hardening.py
- [[Trigger a resource usage alert synchronously.]] - rationale - gateway/security/resource_guard.py
- [[Verify resource check methods return False (deny) on exception.]] - rationale - gateway/tests/test_round2_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_5
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Community 0]]
- 16 edges to [[_COMMUNITY_Community 434]]
- 12 edges to [[_COMMUNITY_Community 2324]]
- 10 edges to [[_COMMUNITY_Community 72]]
- 3 edges to [[_COMMUNITY_Community 1945]]
- 3 edges to [[_COMMUNITY_Community 479]]
- 3 edges to [[_COMMUNITY_Community 2030]]
- 2 edges to [[_COMMUNITY_Community 506]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 14]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 208]]
- 1 edge to [[_COMMUNITY_Community 2049]]
- 1 edge to [[_COMMUNITY_Community 2004]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 41]]
- 1 edge to [[_COMMUNITY_Community 509]]
- 1 edge to [[_COMMUNITY_Community 431]]

## Top bridge nodes
- [[ResourceGuard]] - degree 95, connects to 16 communities
- [[TestResourceGuardFailClosed]] - degree 11, connects to 4 communities
- [[.__init__()_114]] - degree 4, connects to 1 community
- [[.get_usage_stats()]] - degree 4, connects to 1 community
- [[.test_check_cpu_limit_returns_false_on_exception()]] - degree 3, connects to 1 community