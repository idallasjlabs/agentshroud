---
type: community
cohesion: 0.10
members: 34
---

# Community 215

**Cohesion:** 0.10 - loosely connected
**Members:** 34 nodes

## Members
- [[.test_custom_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_default_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_log_dir_created_if_missing()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_affected_packages()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_counts_by_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_has_timestamp()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_no_results_key()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_scanner_name()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_top_cves_limited()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_top_cves_ordered_by_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_total_vulnerabilities()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_unknown_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_report_content_persisted()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_critical()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_top_cves_ids()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_warning_high_only()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_64]] - code - gateway/security/trivy_report.py
- [[Custom report_prefix is used verbatim.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Default report_prefix produces a 'trivy-' filename.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/trivy_report.py
- [[Parse raw Trivy JSON output into a structured summary.      Args         raw R]] - rationale - gateway/security/trivy_report.py
- [[Path_19]] - code - gateway/security/trivy_report.py
- [[Save a Trivy report to the log directory.      Args         report Parsed repo]] - rationale - gateway/security/trivy_report.py
- [[Saved file is valid JSON containing the report keys.]] - rationale - gateway/tests/test_security_toolchain.py
- [[TestTrivyParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySaveReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[generate_summary()_2]] - code - gateway/security/trivy_report.py
- [[parse_trivy_output()]] - code - gateway/security/trivy_report.py
- [[save_report creates the log directory if it does not exist.]] - rationale - gateway/tests/test_security_toolchain.py
- [[save_report()_1]] - code - gateway/security/trivy_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_215
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 112]]
- 4 edges to [[_COMMUNITY_Community 122]]
- 4 edges to [[_COMMUNITY_Community 640]]
- 3 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 3 edges to [[_COMMUNITY_Community 410]]
- 2 edges to [[_COMMUNITY_Community 100]]
- 1 edge to [[_COMMUNITY_Community 347]]
- 1 edge to [[_COMMUNITY_Community 72]]

## Top bridge nodes
- [[generate_summary()_2]] - degree 16, connects to 7 communities
- [[save_report()_1]] - degree 11, connects to 4 communities
- [[parse_trivy_output()]] - degree 23, connects to 3 communities
- [[TestTrivyParser]] - degree 12, connects to 2 communities
- [[TestTrivySummary_1]] - degree 7, connects to 2 communities