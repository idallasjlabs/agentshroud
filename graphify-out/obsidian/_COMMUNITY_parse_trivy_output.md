---
type: community
cohesion: 0.18
members: 19
---

# parse_trivy_output

**Cohesion:** 0.18 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-test_parse_affected_packages()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_counts_by_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_output()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_has_timestamp()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_no_results_key()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_scanner_name()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_top_cves_limited()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_top_cves_ordered_by_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_total_vulnerabilities()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_unknown_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_critical()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_error()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_cves_ids()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_warning_high_only()]] - code - gateway/tests/test_security_toolchain.py
- [[Parse raw Trivy JSON output into a structured summary.      Args         raw R]] - rationale - gateway/security/trivy_report.py
- [[TestTrivyParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[parse_trivy_output()]] - code - gateway/security/trivy_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/parse_trivy_output
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_daily_cve_report.py_1]]
- 3 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py_1]]

## Top bridge nodes
- [[parse_trivy_output()]] - degree 23, connects to 3 communities
- [[TestTrivyParser]] - degree 12, connects to 2 communities
- [[TestTrivySummary_1]] - degree 7, connects to 2 communities
