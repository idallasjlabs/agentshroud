---
type: community
cohesion: 0.22
members: 9
---

# Community 918

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[.test_cpu_limit_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cpu_limit_fails_closed_on_psutil_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_cpu_limit_ok_when_under()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_disk_write_limit_allows_when_no_baseline()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_disk_write_limit_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_disk_write_limit_under_threshold()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_memory_limit_fails_closed_on_error()]] - code - gateway/tests/test_resource_guard_limits.py
- [[.test_memory_limit_ok_and_exceeded()]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestCpuMemoryDiskLimits]] - code - gateway/tests/test_resource_guard_limits.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_918
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 225]]
- 1 edge to [[_COMMUNITY_Community 88]]

## Top bridge nodes
- [[TestCpuMemoryDiskLimits]] - degree 12, connects to 2 communities