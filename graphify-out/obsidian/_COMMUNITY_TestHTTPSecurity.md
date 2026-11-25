---
type: community
members: 33
---

# TestHTTPSecurity

**Members:** 33 nodes

## Members
- [[dot-test_dashboard_has_csp_meta()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_dashboard_html_exists()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_dashboard_no_inline_secrets()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_hmac_comparison_for_secrets()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_mixed_content()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_pickle_in_security_modules()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_shell_true_in_subprocess()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_yaml_unsafe_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_pii_scan_time_independent_of_content()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_requirements_pinned()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_unicode_normalization_bypass()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_xss_in_dashboard_inputs()]] - code - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should escape user inputs (no raw innerHTML from API).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should have Content-Security-Policy or mention it.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should have an HTML file.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should not contain hardcoded secrets.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should not load HTTP resources.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[No yaml.load() without Loader (arbitrary code execution).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[PII scanning time should be roughly linear, not exponential.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Requirements should have pinned versions.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Security modules should not use pickle (deserialization attack).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Subprocess calls should not pass shell=True. Uses AST analysis to flag only a…]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test HTTP-level security CRLF, header injection, content types.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test dependency and supply chain security.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test for timing side-channels in security-critical comparisons.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test web dashboard and API security headers.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestDependencySecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestHTTPSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestTimingAttacks]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestWebSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[Unicode tricks shouldn't bypass PII detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Verify hmac.compare_digest is available for constant-time comparison.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[test_security_audit_advanced.py]] - code - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestHTTPSecurity
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_PromptGuard]]
- 5 edges to [[_COMMUNITY_PIISanitizer]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_TokenValidator]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_TestPrivilegeEscalation]]
- 1 edge to [[_COMMUNITY_EnvironmentGuard]]
- 1 edge to [[_COMMUNITY_TestConcurrency]]

## Top bridge nodes
- [[test_security_audit_advanced.py]] - degree 10, connects to 5 communities
- [[TestTimingAttacks]] - degree 11, connects to 4 communities
- [[TestHTTPSecurity]] - degree 13, connects to 3 communities
- [[dot-test_unicode_normalization_bypass()]] - degree 4, connects to 2 communities
- [[dot-test_pii_scan_time_independent_of_content()]] - degree 4, connects to 2 communities
