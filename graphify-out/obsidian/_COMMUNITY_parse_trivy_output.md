---
type: community
members: 50
---

# parse_trivy_output

**Members:** 50 nodes

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
- [[dot-test_run_binary_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_empty_stdout_is_error_not_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_image_scan_type()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_nonzero_exit_code_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_parse_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_success()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_timeout()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_whitespace_only_stdout_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_critical()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_cves_ids()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_warning_high_only()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_trivy_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[A 0-byteempty stdout means the scan failed to produce output --         it must]] - rationale - gateway/tests/test_security_toolchain.py
- [[Any_6]] - code - gateway/security/trivy_report.py
- [[Custom report_prefix is used verbatim.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Default report_prefix produces a 'trivy-' filename.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/trivy_report.py
- [[Parse raw Trivy JSON output into a structured summary.      Args         raw R]] - rationale - gateway/security/trivy_report.py
- [[Run a Trivy scan and return parsed results.      Args         target Scan targ]] - rationale - gateway/security/trivy_report.py
- [[Save a Trivy report to the log directory.      Args         report Parsed repo]] - rationale - gateway/security/trivy_report.py
- [[Saved file is valid JSON containing the report keys.]] - rationale - gateway/tests/test_security_toolchain.py
- [[TestTrivyParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySaveReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySummary]] - code - gateway/tests/test_security_toolchain.py
- [[generate_summary()]] - code - gateway/security/trivy_report.py
- [[parse_trivy_output()]] - code - gateway/security/trivy_report.py
- [[returncode 0 = clean, 1 = vulns found (both expected); anything         else mea]] - rationale - gateway/tests/test_security_toolchain.py
- [[run_trivy_scan()_1]] - code - gateway/security/trivy_report.py
- [[save_report creates the log directory if it does not exist.]] - rationale - gateway/tests/test_security_toolchain.py
- [[save_report()]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py
- [[trivy_report.py]] - code - gateway/security/trivy_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/parse_trivy_output
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 8 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 4 edges to [[_COMMUNITY_AlertDispatcher]]
- 3 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py (2)]]
- 1 edge to [[_COMMUNITY__build_image_targets]]
- 1 edge to [[_COMMUNITY_test_collaborator_greeter.py (2)]]

## Top bridge nodes
- [[generate_summary()]] - degree 10, connects to 4 communities
- [[run_trivy_scan()_1]] - degree 19, connects to 3 communities
- [[save_report()]] - degree 11, connects to 3 communities
- [[trivy_report.py]] - degree 8, connects to 3 communities
- [[TestTrivyParser]] - degree 12, connects to 2 communities
