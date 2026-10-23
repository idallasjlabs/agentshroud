---
type: community
cohesion: 0.12
members: 25
---

# _load_latest_json

**Cohesion:** 0.12 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-test_clean_report()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_clean_when_installed_but_no_report()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_critical_on_critical_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_infected_report()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_report()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_report()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_prefix_filter()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_most_recent_file()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_empty_directory()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_missing_directory()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_on_invalid_json()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_when_all_files_empty()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_skips_empty_files_returns_next_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_warning_on_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[Load the most recent JSON report file from a directory.      Args         direc]] - rationale - gateway/security/scanner_integration.py
- [[Return True if clamd Unix socket tmpclamd.ctl is connectable.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest ClamAV scan summary from saved reports.      When ClamAV is instal]] - rationale - gateway/security/scanner_integration.py
- [[Return latest OpenSCAP compliance summary from saved reports.]] - rationale - gateway/security/scanner_integration.py
- [[TestGetClamavSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetOpenscapSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestLoadLatestJson_1]] - code - gateway/tests/test_scanner_integration.py
- [[_is_clamd_running()]] - code - gateway/security/scanner_integration.py
- [[_load_latest_json()]] - code - gateway/security/scanner_integration.py
- [[get_clamav_summary()]] - code - gateway/security/scanner_integration.py
- [[get_openscap_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_load_latest_json
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_parse_clamscan_output]]
- 8 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 4 edges to [[_COMMUNITY_OpenClaw Skill Metadata Schema (frontmatter convention)]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]

## Top bridge nodes
- [[_load_latest_json()]] - degree 15, connects to 3 communities
- [[get_clamav_summary()]] - degree 13, connects to 3 communities
- [[get_openscap_summary()]] - degree 11, connects to 2 communities
- [[TestLoadLatestJson_1]] - degree 8, connects to 1 community
- [[TestGetOpenscapSummary]] - degree 5, connects to 1 community
