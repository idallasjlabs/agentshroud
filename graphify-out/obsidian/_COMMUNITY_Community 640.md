---
type: community
cohesion: 0.21
members: 15
---

# Community 640

**Cohesion:** 0.21 - loosely connected
**Members:** 15 nodes

## Members
- [[.test_run_binary_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_empty_stdout_is_error_not_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_image_scan_type()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_nonzero_exit_code_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_parse_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_success()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_timeout()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_whitespace_only_stdout_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_trivy_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[A 0-byteempty stdout means the scan failed to produce output --         it must]] - rationale - gateway/tests/test_security_toolchain.py
- [[Run a Trivy scan and return parsed results.      Args         target Scan targ]] - rationale - gateway/security/trivy_report.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[returncode 0 = clean, 1 = vulns found (both expected); anything         else mea]] - rationale - gateway/tests/test_security_toolchain.py
- [[run_trivy_scan()_1]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_640
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 215]]
- 3 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 2 edges to [[_COMMUNITY_Community 112]]
- 1 edge to [[_COMMUNITY_Community 100]]
- 1 edge to [[_COMMUNITY_Community 122]]
- 1 edge to [[_COMMUNITY_Community 410]]

## Top bridge nodes
- [[run_trivy_scan()_1]] - degree 17, connects to 6 communities
- [[TestTrivyRun]] - degree 10, connects to 2 communities
- [[.test_run_empty_stdout_is_error_not_clean()]] - degree 4, connects to 1 community
- [[.test_run_nonzero_exit_code_is_error()]] - degree 4, connects to 1 community
- [[.test_trivy_binary_not_found()]] - degree 2, connects to 1 community