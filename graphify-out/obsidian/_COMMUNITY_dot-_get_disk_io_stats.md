---
type: community
members: 19
---

# ._get_disk_io_stats

**Members:** 19 nodes

## Members
- [[dot-_alert_high_usage()]] - code - gateway/security/resource_guard.py
- [[dot-_check_system_resources()]] - code - gateway/security/resource_guard.py
- [[dot-_cleanup_expired_usage()]] - code - gateway/security/resource_guard.py
- [[dot-_get_disk_io_stats()]] - code - gateway/security/resource_guard.py
- [[dot-_monitor_resources()]] - code - gateway/security/resource_guard.py
- [[dot-add_alert_callback()]] - code - gateway/security/resource_guard.py
- [[dot-check_disk_write_limit()]] - code - gateway/security/resource_guard.py
- [[dot-get_usage_stats()]] - code - gateway/security/resource_guard.py
- [[Add a callback function to be called when resource alerts are triggered.]] - rationale - gateway/security/resource_guard.py
- [[Any_12]] - code
- [[Background task to monitor resource usage and trigger alerts.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded disk write limit.]] - rationale - gateway/security/resource_guard.py
- [[Check system-wide resource usage for anomalies (synchronous).]] - rationale - gateway/security/resource_guard.py
- [[Clean up old usage data (older than 5 minutes).]] - rationale - gateway/security/resource_guard.py
- [[Current resource usage metrics.]] - rationale - gateway/security/resource_guard.py
- [[Get current disk IO statistics.]] - rationale - gateway/security/resource_guard.py
- [[Get current usage statistics.]] - rationale - gateway/security/resource_guard.py
- [[ResourceUsage]] - code - gateway/security/resource_guard.py
- [[Trigger a resource usage alert synchronously.]] - rationale - gateway/security/resource_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_get_disk_io_stats
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_ResourceGuard]]

## Top bridge nodes
- [[dot-_get_disk_io_stats()]] - degree 5, connects to 1 community
- [[dot-_monitor_resources()]] - degree 5, connects to 1 community
- [[dot-_alert_high_usage()]] - degree 4, connects to 1 community
- [[dot-_check_system_resources()]] - degree 4, connects to 1 community
- [[dot-get_usage_stats()]] - degree 4, connects to 1 community
