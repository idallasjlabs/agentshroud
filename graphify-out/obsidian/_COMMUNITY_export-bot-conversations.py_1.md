---
type: community
cohesion: 0.20
members: 15
---

# export-bot-conversations.py

**Cohesion:** 0.20 - loosely connected
**Members:** 15 nodes

## Members
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
- [[Run a Trivy scan and return parsed results.      Args         target Scan targ]] - rationale - gateway/security/trivy_report.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[returncode 0 = clean, 1 = vulns found (both expected); anything         else mea]] - rationale - gateway/tests/test_security_toolchain.py
- [[run_trivy_scan()_1]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/export-bot-conversationspy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_daily_cve_report.py_1]]
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_parse_trivy_output]]

## Top bridge nodes
- [[run_trivy_scan()_1]] - degree 19, connects to 5 communities
- [[TestTrivyRun]] - degree 10, connects to 2 communities
- [[dot-test_trivy_binary_not_found()]] - degree 2, connects to 1 community
