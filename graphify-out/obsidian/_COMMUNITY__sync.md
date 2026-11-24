---
type: community
members: 15
---

# _sync

**Members:** 15 nodes

## Members
- [[dot-test_agent_var_resolved_from_registry_dict()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_append_targets_correct_agent_list()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_dry_run_writes_nothing()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_entry_to_py_handles_none_cvss()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_entry_to_py_roundtrips()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_insert_adds_exactly_n_entries_and_still_parses()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_missing_variable_raises()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_non_list_value_raises()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_string_literals_match_black_quote_preference()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[CI runs black on gateway; an appended registry block must already be clean.]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestListLocator]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestSerialization_1]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_exec_registry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_sync()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[parametrize_2]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_sync
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY__adv]]
- 6 edges to [[_COMMUNITY_test_sync_cve_registry_ghsa.py]]
- 5 edges to [[_COMMUNITY_TestNvdAppend]]
- 5 edges to [[_COMMUNITY_TestFailsLoudly]]
- 5 edges to [[_COMMUNITY_dot-test_fetch_paginates_via_link_cursor]]
- 3 edges to [[_COMMUNITY_TestNvdReportOnly]]
- 3 edges to [[_COMMUNITY_TestSnapshotSmoke]]

## Top bridge nodes
- [[_sync()]] - degree 41, connects to 7 communities
- [[_exec_registry()]] - degree 4, connects to 2 communities
- [[TestSerialization_1]] - degree 6, connects to 1 community
- [[TestListLocator]] - degree 5, connects to 1 community
- [[dot-test_append_targets_correct_agent_list()]] - degree 4, connects to 1 community
