---
type: community
members: 20
---

# run_trivy_scan

**Members:** 20 nodes

## Members
- [[dot-test_run_binary_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_empty_stdout_is_error_not_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_image_scan_type()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_nonzero_exit_code_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_parse_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_success()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_timeout()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_whitespace_only_stdout_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[A 0-byteempty stdout means the scan failed to produce output -- it must never…]] - rationale - gateway/tests/test_security_toolchain.py
- [[Run a Trivy scan and return parsed results. Args target Scan target…]] - rationale - gateway/security/trivy_report.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[Update ClamAV virus database using freshclam. Args freshclam_bin Path to…]] - rationale - gateway/security/clamav_scanner.py
- [[patch_1]] - code
- [[returncode 0 = clean, 1 = vulns found (both expected); anything else means…]] - rationale - gateway/tests/test_security_toolchain.py
- [[run_trivy_scan()]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run_trivy_scan
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 3 edges to [[_COMMUNITY_parse_clamscan_output]]
- 3 edges to [[_COMMUNITY_parse_trivy_output]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]

## Top bridge nodes
- [[run_trivy_scan()]] - degree 17, connects to 6 communities
- [[update_virus_db()]] - degree 5, connects to 3 communities
- [[TestTrivyRun]] - degree 9, connects to 1 community
- [[TestClamAVRun]] - degree 3, connects to 1 community
- [[dot-test_run_not_found()]] - degree 3, connects to 1 community
