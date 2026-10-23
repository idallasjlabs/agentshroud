---
type: community
cohesion: 0.32
members: 8
---

# fixture (2)

**Cohesion:** 0.32 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-_nvd_entry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-registry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_dry_run_reports_count_and_writes_nothing()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_empty_input_is_a_no_op()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_openclaw_and_hermes_lists_each_get_their_own_entry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestNvdAppend]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[The NVD source appends to the OpenClaw  Hermes lists through the same locator.]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[fixture]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/fixture_2
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers (2)_1]]
- 1 edge to [[_COMMUNITY_ControlCenter]]

## Top bridge nodes
- [[TestNvdAppend]] - degree 7, connects to 1 community
- [[dot-test_openclaw_and_hermes_lists_each_get_their_own_entry()]] - degree 4, connects to 1 community
- [[dot-registry()]] - degree 3, connects to 1 community
- [[dot-test_dry_run_reports_count_and_writes_nothing()]] - degree 3, connects to 1 community
- [[dot-test_empty_input_is_a_no_op()]] - degree 2, connects to 1 community
