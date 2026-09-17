---
type: community
cohesion: 0.10
members: 34
---

# Community 220

**Cohesion:** 0.10 - loosely connected
**Members:** 34 nodes

## Members
- [[dot-test_custom_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_default_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_log_dir_created_if_missing()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_affected_packages()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_counts_by_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_output()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_has_timestamp()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_no_results_key()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_scanner_name()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_top_cves_limited()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_top_cves_ordered_by_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_total_vulnerabilities()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_unknown_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_report_content_persisted()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_critical()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_cves_ids()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_warning_high_only()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_37]] - code
- [[Custom report_prefix is used verbatim.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Default report_prefix produces a 'trivy-' filename.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Generate a summary dict suitable for the health report. Args report Parsed…]] - rationale - gateway/security/trivy_report.py
- [[Parse raw Trivy JSON output into a structured summary. Args raw Raw JSON…]] - rationale - gateway/security/trivy_report.py
- [[Path_22]] - code
- [[Save a Trivy report to the log directory. Args report Parsed report dict.…]] - rationale - gateway/security/trivy_report.py
- [[Saved file is valid JSON containing the report keys.]] - rationale - gateway/tests/test_security_toolchain.py
- [[TestTrivyParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySaveReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySummary]] - code - gateway/tests/test_security_toolchain.py
- [[generate_summary]] - code - gateway/security/trivy_report.py
- [[parse_trivy_output]] - code - gateway/security/trivy_report.py
- [[save_report]] - code - gateway/security/trivy_report.py
- [[save_report creates the log directory if it does not exist.]] - rationale - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_220
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 56]]
- 5 edges to [[_COMMUNITY_Community 124]]
- 4 edges to [[_COMMUNITY_Community 47]]
- 2 edges to [[_COMMUNITY_Community 82]]
- 1 edge to [[_COMMUNITY_Community 148]]
- 1 edge to [[_COMMUNITY_Community 60]]
- 1 edge to [[_COMMUNITY_Community 459]]

## Top bridge nodes
- [[generate_summary]] - degree 16, connects to 7 communities
- [[parse_trivy_output]] - degree 23, connects to 3 communities
- [[save_report]] - degree 11, connects to 3 communities
- [[TestTrivyParser]] - degree 11, connects to 1 community
- [[TestTrivySummary]] - degree 6, connects to 1 community