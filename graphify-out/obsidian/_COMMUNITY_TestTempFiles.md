---
type: community
members: 5
---

# TestTempFiles

**Members:** 5 nodes

## Members
- [[dot-test_cleanup_tolerates_missing_file()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_cleanup_unlinks_existing_and_clears_registry()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_register_blocks_over_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_register_under_limit()]] - code - gateway/tests/test_resource_guard_limits.py
- [[TestTempFiles]] - code - gateway/tests/test_resource_guard_limits.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTempFiles
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ResourceGuard]]

## Top bridge nodes
- [[TestTempFiles]] - degree 5, connects to 1 community
