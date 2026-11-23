---
type: community
members: 15
---

# patch

**Members:** 15 nodes

## Members
- [[dot-test_cpu_limit_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cpu_limit_fails_closed_on_psutil_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cpu_limit_ok_when_under()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_disk_write_limit_allows_when_no_baseline()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_disk_write_limit_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_disk_write_limit_under_threshold()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_get_usage_stats_for_agent()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_get_usage_stats_system_wide()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_memory_limit_fails_closed_on_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_memory_limit_ok_and_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_start_request_tracking_records_baseline()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_start_request_tracking_survives_psutil_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestCpuMemoryDiskLimits]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestUsageStatsAndTracking]] - code - gateway/tests/test_resource_guard_limits.py
- [[patch_2]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/patch
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ResourceGuard]]

## Top bridge nodes
- [[TestCpuMemoryDiskLimits]] - degree 9, connects to 1 community
- [[TestUsageStatsAndTracking]] - degree 5, connects to 1 community
