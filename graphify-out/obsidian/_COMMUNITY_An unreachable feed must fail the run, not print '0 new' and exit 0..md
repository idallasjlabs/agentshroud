---
type: community
members: 10
---

# An unreachable feed must fail the run, not print '0 new' and exit 0.

**Members:** 10 nodes

## Members
- [[dot-test_append_on_unlocatable_list_exits_nonzero()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_edit_that_does_not_add_n_entries_is_rejected()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_feed_fetch_failure_is_not_reported_as_zero_new()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_main_exits_nonzero_when_an_agent_fails()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_nvd_layout_failure_exits_nonzero()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[An unreachable feed must fail the run, not print '0 new' and exit 0.]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestFailsLoudly]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_boom()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_boom()_1]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_timeout()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/An_unreachable_feed_must_fail_the_run_not_print_0_new_and_exit_0
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers (2)]]
- 1 edge to [[_COMMUNITY_ControlCenter]]
- 1 edge to [[_COMMUNITY__adv()]]

## Top bridge nodes
- [[dot-test_append_on_unlocatable_list_exits_nonzero()]] - degree 3, connects to 2 communities
- [[TestFailsLoudly]] - degree 6, connects to 1 community
- [[dot-test_feed_fetch_failure_is_not_reported_as_zero_new()]] - degree 4, connects to 1 community
- [[dot-test_main_exits_nonzero_when_an_agent_fails()]] - degree 4, connects to 1 community
- [[dot-test_nvd_layout_failure_exits_nonzero()]] - degree 3, connects to 1 community
