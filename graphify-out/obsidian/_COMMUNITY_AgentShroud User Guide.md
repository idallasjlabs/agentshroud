---
type: community
cohesion: 0.11
members: 28
---

# AgentShroud User Guide

**Cohesion:** 0.11 - loosely connected
**Members:** 28 nodes

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
- [[Custom report_prefix is used verbatim.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Default report_prefix produces a 'trivy-' filename.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Parse raw Trivy JSON output into a structured summary.      Args         raw R]] - rationale - gateway/security/trivy_report.py
- [[Saved file is valid JSON containing the report keys.]] - rationale - gateway/tests/test_security_toolchain.py
- [[TestTrivyParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySaveReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[parse_trivy_output()]] - code - gateway/security/trivy_report.py
- [[save_report creates the log directory if it does not exist.]] - rationale - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_User_Guide
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 4 edges to [[_COMMUNITY_LLMProxy]]
- 3 edges to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[parse_trivy_output()]] - degree 23, connects to 2 communities
- [[TestTrivyParser]] - degree 12, connects to 2 communities
- [[TestTrivySummary_1]] - degree 7, connects to 2 communities
- [[TestTrivySaveReport]] - degree 6, connects to 2 communities
- [[.test_custom_prefix()]] - degree 4, connects to 1 community