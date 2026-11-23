---
type: community
members: 21
---

# get_trivy_summary

**Members:** 21 nodes

## Members
- [[dot-test_clean_when_installed_but_no_report()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_report_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_prefix_filter()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_generate_summary_output()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_most_recent_file()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_empty_directory()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_missing_directory()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_on_invalid_json()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_when_all_files_empty()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_skips_empty_files_returns_next_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[Load the most recent JSON report file from a directory. Args directory…]] - rationale - gateway/security/scanner_integration.py
- [[Path_35]] - code
- [[Return True if the most recent report file was written within max_age_hours.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Trivy scan summary from saved reports. When Trivy is installed…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 29 AI Model & Supply Chain Integrity (0-5). MITRE ATLAS, OWASP…]] - rationale - gateway/security/scanner_integration.py
- [[TestGetTrivySummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestLoadLatestJson_1]] - code - gateway/tests/test_scanner_integration.py
- [[_is_fresh()]] - code - gateway/security/scanner_integration.py
- [[_load_latest_json()]] - code - gateway/security/scanner_integration.py
- [[_score_ai_model_supply_chain()]] - code - gateway/security/scanner_integration.py
- [[get_trivy_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_trivy_summary
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 6 edges to [[_COMMUNITY_scanner_integration.py]]
- 5 edges to [[_COMMUNITY_Any]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 1 edge to [[_COMMUNITY_get_sbom]]
- 1 edge to [[_COMMUNITY_get_wazuh_summary]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[get_trivy_summary()]] - degree 16, connects to 7 communities
- [[_load_latest_json()]] - degree 15, connects to 3 communities
- [[_is_fresh()]] - degree 8, connects to 3 communities
- [[TestLoadLatestJson_1]] - degree 8, connects to 1 community
- [[_score_ai_model_supply_chain()]] - degree 5, connects to 1 community
