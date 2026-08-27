---
type: community
members: 8
---

# Community 1002

**Members:** 8 nodes

## Members
- [[.test_clean_when_installed_but_no_report()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_infected_report()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_not_run_when_no_report()]] - code - gateway/tests/test_scanner_integration.py
- [[Return True if clamd Unix socket tmpclamd.ctl is connectable.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest ClamAV scan summary from saved reports.      When ClamAV is instal]] - rationale - gateway/security/scanner_integration.py
- [[TestGetClamavSummary]] - code - gateway/tests/test_scanner_integration.py
- [[_is_clamd_running()]] - code - gateway/security/scanner_integration.py
- [[get_clamav_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1002
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 123]]
- 3 edges to [[_COMMUNITY_Community 59]]
- 2 edges to [[_COMMUNITY_Community 261]]
- 1 edge to [[_COMMUNITY_Community 541]]
- 1 edge to [[_COMMUNITY_Community 125]]
- 1 edge to [[_COMMUNITY_Community 85]]

## Top bridge nodes
- [[get_clamav_summary()]] - degree 13, connects to 5 communities
- [[TestGetClamavSummary]] - degree 4, connects to 1 community
- [[_is_clamd_running()]] - degree 3, connects to 1 community
- [[.test_not_run_when_no_report()]] - degree 3, connects to 1 community
- [[.test_clean_when_installed_but_no_report()_1]] - degree 3, connects to 1 community