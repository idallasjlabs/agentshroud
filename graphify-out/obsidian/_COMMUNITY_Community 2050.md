---
type: community
members: 8
---

# Community 2050

**Members:** 8 nodes

## Members
- [[._page()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[._run()_2]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_known_cves_matched_by_cve_id_not_id()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_never_writes_and_says_so()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_persistent_failure_exits_non_zero()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_transient_read_timeout_is_retried()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestNvdReportOnly]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[The NVD path emits the pre-migration schema (id=CVE-…, no ghsa_idcve_id).]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2050
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 55]]
- 1 edge to [[_COMMUNITY_Community 1342]]

## Top bridge nodes
- [[TestNvdReportOnly]] - degree 8, connects to 1 community
- [[._run()_2]] - degree 4, connects to 1 community
- [[.test_known_cves_matched_by_cve_id_not_id()]] - degree 3, connects to 1 community
- [[.test_transient_read_timeout_is_retried()]] - degree 2, connects to 1 community
- [[.test_persistent_failure_exits_non_zero()]] - degree 2, connects to 1 community