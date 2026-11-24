---
type: community
members: 15
---

# ._monitor_resources

**Members:** 15 nodes

## Members
- [[dot-_alert_high_usage()]] - code - gateway/security/resource_guard.py
- [[dot-_check_system_resources()]] - code - gateway/security/resource_guard.py
- [[dot-_cleanup_expired_usage()]] - code - gateway/security/resource_guard.py
- [[dot-_monitor_resources()]] - code - gateway/security/resource_guard.py
- [[dot-add_alert_callback()]] - code - gateway/security/resource_guard.py
- [[dot-get_usage_stats()]] - code - gateway/security/resource_guard.py
- [[Add a callback function to be called when resource alerts are triggered.]] - rationale - gateway/security/resource_guard.py
- [[Any_17]] - code
- [[Background task to monitor resource usage and trigger alerts.]] - rationale - gateway/security/resource_guard.py
- [[Check system-wide resource usage for anomalies (synchronous).]] - rationale - gateway/security/resource_guard.py
- [[Clean up old usage data (older than 5 minutes).]] - rationale - gateway/security/resource_guard.py
- [[Current resource usage metrics.]] - rationale - gateway/security/resource_guard.py
- [[Get current usage statistics.]] - rationale - gateway/security/resource_guard.py
- [[ResourceUsage]] - code - gateway/security/resource_guard.py
- [[Trigger a resource usage alert synchronously.]] - rationale - gateway/security/resource_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_monitor_resources
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ResourceGuard]]

## Top bridge nodes
- [[dot-_monitor_resources()]] - degree 5, connects to 1 community
- [[dot-_alert_high_usage()]] - degree 4, connects to 1 community
- [[dot-_check_system_resources()]] - degree 4, connects to 1 community
- [[dot-get_usage_stats()]] - degree 4, connects to 1 community
- [[Any_17]] - degree 4, connects to 1 community
