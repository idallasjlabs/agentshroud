---
type: community
members: 6
---

# Community 2121

**Members:** 6 nodes

## Members
- [[.test_edit_that_does_not_add_n_entries_is_rejected()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_feed_fetch_failure_is_not_reported_as_zero_new()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_main_exits_nonzero_when_an_agent_fails()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_nvd_layout_failure_exits_nonzero()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[An unreachable feed must fail the run, not print '0 new' and exit 0.]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestFailsLoudly]] - code - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2121
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 55]]
- 1 edge to [[_COMMUNITY_Community 1342]]

## Top bridge nodes
- [[TestFailsLoudly]] - degree 6, connects to 2 communities
- [[.test_feed_fetch_failure_is_not_reported_as_zero_new()]] - degree 3, connects to 1 community
- [[.test_edit_that_does_not_add_n_entries_is_rejected()]] - degree 2, connects to 1 community
- [[.test_nvd_layout_failure_exits_nonzero()]] - degree 2, connects to 1 community
- [[.test_main_exits_nonzero_when_an_agent_fails()]] - degree 2, connects to 1 community