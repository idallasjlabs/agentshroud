---
type: community
members: 32
---

# Skill: Project Management (PM) (3)

**Members:** 32 nodes

## Members
- [[dot-test_custom_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_default_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_log_dir_created_if_missing()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_report_content_persisted()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_binary_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_empty_stdout_is_error_not_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_image_scan_type()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_nonzero_exit_code_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_parse_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_success()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_timeout()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_whitespace_only_stdout_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_trivy_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[A 0-byteempty stdout means the scan failed to produce output --         it must]] - rationale - gateway/tests/test_security_toolchain.py
- [[Any_34]] - code - gateway/security/trivy_report.py
- [[Custom report_prefix is used verbatim.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Default report_prefix produces a 'trivy-' filename.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Generate a summary dict suitable for the health report.      Args         alert_1]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/trivy_report.py
- [[Path_23]] - code - gateway/security/trivy_report.py
- [[Run a Trivy scan and return parsed results.      Args         target Scan targ]] - rationale - gateway/security/trivy_report.py
- [[Save a Trivy report to the log directory.      Args         report Parsed repo]] - rationale - gateway/security/trivy_report.py
- [[Saved file is valid JSON containing the report keys.]] - rationale - gateway/tests/test_security_toolchain.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySaveReport]] - code - gateway/tests/test_security_toolchain.py
- [[generate_summary()_2]] - code - gateway/security/trivy_report.py
- [[returncode 0 = clean, 1 = vulns found (both expected); anything         else mea]] - rationale - gateway/tests/test_security_toolchain.py
- [[run_trivy_scan()_1]] - code - gateway/security/trivy_report.py
- [[save_report creates the log directory if it does not exist.]] - rationale - gateway/tests/test_security_toolchain.py
- [[save_report()_1]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py
- [[trivy_report.py]] - code - gateway/security/trivy_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Skill_Project_Management_PM_3
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_TestClassify]]
- 6 edges to [[_COMMUNITY_TestVersionRoutes]]
- 3 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_format_cve_report() (2)]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]

## Top bridge nodes
- [[run_trivy_scan()_1]] - degree 18, connects to 4 communities
- [[generate_summary()_2]] - degree 8, connects to 3 communities
- [[save_report()_1]] - degree 10, connects to 2 communities
- [[TestTrivyRun]] - degree 10, connects to 2 communities
- [[TestTrivySaveReport]] - degree 6, connects to 2 communities
