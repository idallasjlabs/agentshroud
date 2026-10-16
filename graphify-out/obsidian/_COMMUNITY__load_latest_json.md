---
type: community
cohesion: 0.19
members: 16
---

# _load_latest_json

**Cohesion:** 0.19 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-test_clean_when_installed_but_no_report()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_report_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_prefix_filter()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_generate_summary_output()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_most_recent_file()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_empty_directory()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_missing_directory()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_on_invalid_json()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_when_all_files_empty()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_skips_empty_files_returns_next_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[Load the most recent JSON report file from a directory.      Args         direc]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Trivy scan summary from saved reports.      When Trivy is installe]] - rationale - gateway/security/scanner_integration.py
- [[TestGetTrivySummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestLoadLatestJson_1]] - code - gateway/tests/test_scanner_integration.py
- [[_load_latest_json()]] - code - gateway/security/scanner_integration.py
- [[get_trivy_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_load_latest_json
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_scanner_integration.py]]
- 4 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 4 edges to [[_COMMUNITY_test_collaborator_greeter.py_1]]
- 3 edges to [[_COMMUNITY_Path_2]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_AgentTarget_4]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]

## Top bridge nodes
- [[get_trivy_summary()]] - degree 16, connects to 8 communities
- [[_load_latest_json()]] - degree 15, connects to 4 communities
- [[TestLoadLatestJson_1]] - degree 8, connects to 1 community
- [[TestGetTrivySummary]] - degree 4, connects to 1 community
- [[dot-test_clean_when_installed_but_no_report()_1]] - degree 3, connects to 1 community
