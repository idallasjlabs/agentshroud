---
type: community
members: 22
---

# TestAgentsRegistry

**Members:** 22 nodes

## Members
- [[dot-test_agent_ids_are_unique()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_bad_mode_rejected()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_derived_hosted_local()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_derived_hosted_when_no_local_bots()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_edge_disabled_local_only_derived()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_edge_rows_carry_connection_and_support()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_explicit_mode_filters_rows()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_health_timeout_reads_unknown()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_hosted_rows_listed_from_disk_when_edge_disabled()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_local_health_from_service_manager()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_no_lockdown_module_reads_unknown()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_requires_read_system()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_suspended_client_marks_vendor_suspended()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_unhooked_hosted_agents_never_ok()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_unreadable_profiles_with_edge_off_list_no_vendor_rows()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_vendor_rows_carry_edge_counters()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_vendor_status_values_are_honest()]] - code - gateway/tests/test_soc_edge.py
- [[TestAgentsRegistry]] - code - gateway/tests/test_soc_edge.py
- [[_bad()]] - code - gateway/tests/test_soc_edge.py
- [[_bot()_1]] - code - gateway/tests/test_soc_edge.py
- [[_rows()]] - code - gateway/tests/test_soc_edge.py
- [[_timeout()_1]] - code - gateway/tests/test_soc_edge.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAgentsRegistry
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_soc_edge.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_LockdownLevel]]
- 1 edge to [[_COMMUNITY_TestEdgeKill]]

## Top bridge nodes
- [[TestAgentsRegistry]] - degree 22, connects to 4 communities
- [[_rows()]] - degree 8, connects to 1 community
- [[_bot()_1]] - degree 6, connects to 1 community
