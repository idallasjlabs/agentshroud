---
type: community
members: 7
---

# Community 2073

**Members:** 7 nodes

## Members
- [[._nvd_entry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.registry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_dry_run_reports_count_and_writes_nothing()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_empty_input_is_a_no_op()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_openclaw_and_hermes_lists_each_get_their_own_entry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestNvdAppend]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[The NVD source appends to the OpenClaw  Hermes lists through the same locator.]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2073
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 55]]
- 2 edges to [[_COMMUNITY_Community 1342]]

## Top bridge nodes
- [[.test_openclaw_and_hermes_lists_each_get_their_own_entry()]] - degree 4, connects to 2 communities
- [[TestNvdAppend]] - degree 7, connects to 1 community
- [[.test_dry_run_reports_count_and_writes_nothing()]] - degree 3, connects to 1 community
- [[.registry()]] - degree 2, connects to 1 community
- [[.test_empty_input_is_a_no_op()]] - degree 2, connects to 1 community