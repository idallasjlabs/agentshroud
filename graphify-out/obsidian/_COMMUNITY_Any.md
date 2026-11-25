---
type: community
members: 30
---

# Any

**Members:** 30 nodes

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
- [[Any_61]] - code
- [[Load the most recent JSON report file from a directory. Args directory…]] - rationale - gateway/security/scanner_integration.py
- [[Return Fluent Bit log collector status. Fluent Bit is a log shipper, not a…]] - rationale - gateway/security/scanner_integration.py
- [[Return True if clamd Unix socket tmpclamd.ctl is connectable.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if fluent-bit pidfile tmpfluent-bit.pid exists with a live PID.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest ClamAV scan summary from saved reports. When ClamAV is installed…]] - rationale - gateway/security/scanner_integration.py
- [[Return latest OpenSCAP compliance summary from saved reports.]] - rationale - gateway/security/scanner_integration.py
- [[TestGetClamavSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetOpenscapSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestLoadLatestJson_1]] - code - gateway/tests/test_scanner_integration.py
- [[_is_clamd_running()]] - code - gateway/security/scanner_integration.py
- [[_is_fluent_bit_running()]] - code - gateway/security/scanner_integration.py
- [[_load_latest_json()]] - code - gateway/security/scanner_integration.py
- [[get_clamav_summary()]] - code - gateway/security/scanner_integration.py
- [[get_fluent_bit_summary()]] - code - gateway/security/scanner_integration.py
- [[get_openscap_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Any
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 8 edges to [[_COMMUNITY_scanner_integration.py]]
- 5 edges to [[_COMMUNITY_aggregate_results]]
- 3 edges to [[_COMMUNITY_get_trivy_summary]]
- 3 edges to [[_COMMUNITY_compute_scorecard]]
- 3 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 2 edges to [[_COMMUNITY_generate_summary]]
- 1 edge to [[_COMMUNITY_get_wazuh_summary]]
- 1 edge to [[_COMMUNITY_get_trivy_image_summaries]]
- 1 edge to [[_COMMUNITY_test_soc_bots.py]]

## Top bridge nodes
- [[Any_61]] - degree 22, connects to 10 communities
- [[get_clamav_summary()]] - degree 12, connects to 5 communities
- [[_load_latest_json()]] - degree 15, connects to 4 communities
- [[get_openscap_summary()]] - degree 11, connects to 4 communities
- [[get_fluent_bit_summary()]] - degree 5, connects to 2 communities
