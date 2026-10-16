---
type: community
cohesion: 0.47
members: 6
---

# get_falco_summary

**Cohesion:** 0.47 - moderately connected
**Members:** 6 nodes

## Members
- [[dot-test_clean_when_installed_not_running()_2]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_alert_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_summary_for_empty_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[Return latest Falco alert summary from the local alert directory.      CC-20 If]] - rationale - gateway/security/scanner_integration.py
- [[TestGetFalcoSummary]] - code - gateway/tests/test_scanner_integration.py
- [[get_falco_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_falco_summary
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 4 edges to [[_COMMUNITY_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_Path_1]]

## Top bridge nodes
- [[get_falco_summary()]] - degree 13, connects to 3 communities
- [[TestGetFalcoSummary]] - degree 4, connects to 1 community
- [[dot-test_not_run_when_no_alert_dir()_1]] - degree 3, connects to 1 community
