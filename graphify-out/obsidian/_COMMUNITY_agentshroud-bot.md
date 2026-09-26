---
type: community
cohesion: 0.19
members: 16
---

# agentshroud-bot

**Cohesion:** 0.19 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_clean_when_installed_but_no_report()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_not_run_when_no_report_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_prefix_filter()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_generate_summary_output()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_most_recent_file()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_none_for_empty_directory()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_none_for_missing_directory()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_none_on_invalid_json()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_none_when_all_files_empty()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_skips_empty_files_returns_next_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[Load the most recent JSON report file from a directory.      Args         direc]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Trivy scan summary from saved reports.      When Trivy is installe]] - rationale - gateway/security/scanner_integration.py
- [[TestGetTrivySummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestLoadLatestJson]] - code - gateway/tests/test_scanner_integration.py
- [[_load_latest_json()]] - code - gateway/security/scanner_integration.py
- [[get_trivy_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-bot
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 4 edges to [[_COMMUNITY_Canvas Skill]]
- 4 edges to [[_COMMUNITY_A2AMethod]]
- 3 edges to [[_COMMUNITY_Step-by-Step Installation]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_🟢 INFO (nice to have)]]

## Top bridge nodes
- [[get_trivy_summary()]] - degree 16, connects to 8 communities
- [[_load_latest_json()]] - degree 15, connects to 4 communities
- [[TestLoadLatestJson]] - degree 8, connects to 1 community
- [[TestGetTrivySummary]] - degree 4, connects to 1 community
- [[.test_clean_when_installed_but_no_report()]] - degree 3, connects to 1 community