---
type: community
cohesion: 0.05
members: 67
---

# Middleware Coverage Tests

**Cohesion:** 0.05 - loosely connected
**Members:** 67 nodes

## Members
- [[.__init__()_129]] - code - gateway/tests/test_middleware_coverage.py
- [[.check_permission()_1]] - code - gateway/tests/test_middleware_coverage.py
- [[.check_tool_permission()_2]] - code - gateway/tests/test_middleware_coverage.py
- [[.get_user_role()_2]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_blocked_non_owner_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_blocked_owner_exempted()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_browser_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_clean_message_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_command_indicator_allowed_when_check_passes()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_command_indicator_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_critical_attack_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_critical_finding_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_dict_message_handled()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_direct_no_session_manager_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_env_guard_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_existing_session_context_not_reinjected()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_expected_write_registered()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_fallback_without_rbac_manager()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_git_guard_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_guard_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_headers_sanitized()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_high_threat_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_invisible_chars_normalized()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_isolation_error_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_isolation_fail_closed_without_session_manager()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_low_finding_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_low_severity_not_blocking()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_low_threat_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_message_dict_is_stringified_and_normalized()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_metadata_exception_non_blocking()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_no_path_match_no_registration()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_no_user_id_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_non_owner_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_outer_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_bypass()_1]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_bypass()_2]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_plain_message_skips_check()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_rbac_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_rbac_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_rbac_pass_logs_role_and_allows()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_rbac_requires_approval()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_repetition_attack_not_blocking()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_session_context_injected()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_tool_permission_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_tool_permission_requires_approval()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_tracker_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_with_rbac_manager()]] - code - gateway/tests/test_middleware_coverage.py
- [[Deterministic stand-in for RBACManager.]] - rationale - gateway/tests/test_middleware_coverage.py
- [[MiddlewareManager built via __new__ — every module attr explicitly None     so e]] - rationale - gateway/tests/test_middleware_coverage.py
- [[TestBrowserSecurity]] - code - gateway/tests/test_middleware_coverage.py
- [[TestContextGuard]] - code - gateway/tests/test_middleware_coverage.py
- [[TestCrossSessionAccess]] - code - gateway/tests/test_middleware_coverage.py
- [[TestEnvGuard]] - code - gateway/tests/test_middleware_coverage.py
- [[TestGitGuard_1]] - code - gateway/tests/test_middleware_coverage.py
- [[TestIsOwner]] - code - gateway/tests/test_middleware_coverage.py
- [[TestMemoryIntegrityRegistration]] - code - gateway/tests/test_middleware_coverage.py
- [[TestMetadataGuard_1]] - code - gateway/tests/test_middleware_coverage.py
- [[TestMultiTurnTracker]] - code - gateway/tests/test_middleware_coverage.py
- [[TestProcessRequestIdentity]] - code - gateway/tests/test_middleware_coverage.py
- [[TestProcessRequestRBAC]] - code - gateway/tests/test_middleware_coverage.py
- [[_FakeRBAC]] - code - gateway/tests/test_middleware_coverage.py
- [[_req()]] - code - gateway/tests/test_middleware_coverage.py
- [[mm()]] - code - gateway/tests/test_middleware_coverage.py
- [[temp_workspace()_1]] - code - gateway/tests/test_middleware_coverage.py
- [[test_middleware_coverage.py]] - code - gateway/tests/test_middleware_coverage.py
- [[usm()]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Middleware_Coverage_Tests
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 16 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 13 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 6 edges to [[_COMMUNITY_Module Group 292]]
- 3 edges to [[_COMMUNITY_Module Group 214]]
- 2 edges to [[_COMMUNITY_Module Group 469]]
- 2 edges to [[_COMMUNITY_Module Group 443]]
- 2 edges to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[test_middleware_coverage.py]] - degree 37, connects to 8 communities
- [[_FakeRBAC]] - degree 20, connects to 4 communities
- [[TestProcessRequestIdentity]] - degree 13, connects to 3 communities
- [[TestProcessRequestRBAC]] - degree 11, connects to 3 communities
- [[TestContextGuard]] - degree 10, connects to 3 communities
