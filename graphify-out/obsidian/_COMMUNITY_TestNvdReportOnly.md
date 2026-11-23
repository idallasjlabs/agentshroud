---
type: community
members: 8
---

# TestNvdReportOnly

**Members:** 8 nodes

## Members
- [[dot-_run()_1]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_known_cves_matched_by_cve_id_not_id()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_never_writes_and_says_so()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_persistent_failure_exits_non_zero()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestNvdReportOnly]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[The NVD path emits the pre-migration schema (id=CVE-…, no ghsa_idcve_id).…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_fake_urlopen()_2]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_no_write()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestNvdReportOnly
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_dot-test_fetch_paginates_via_link_cursor]]
- 3 edges to [[_COMMUNITY__sync]]
- 1 edge to [[_COMMUNITY_test_sync_cve_registry_ghsa.py]]

## Top bridge nodes
- [[TestNvdReportOnly]] - degree 8, connects to 2 communities
- [[dot-test_persistent_failure_exits_non_zero()]] - degree 4, connects to 2 communities
- [[dot-_run()_1]] - degree 5, connects to 1 community
- [[dot-test_known_cves_matched_by_cve_id_not_id()]] - degree 3, connects to 1 community
