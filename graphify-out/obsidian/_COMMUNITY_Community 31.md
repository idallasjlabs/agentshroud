---
type: community
members: 55
---

# Community 31

**Members:** 55 nodes

## Members
- [[._analyze_request_for_rbac()]] - code - gateway/ingest_api/middleware.py
- [[._check_cross_session_access()]] - code - gateway/ingest_api/middleware.py
- [[._check_rbac_permissions()]] - code - gateway/ingest_api/middleware.py
- [[._critical_guard_failure()]] - code - gateway/ingest_api/middleware.py
- [[._enforce_session_isolation()]] - code - gateway/ingest_api/middleware.py
- [[._extract_file_paths()]] - code - gateway/ingest_api/middleware.py
- [[._extract_user_id()]] - code - gateway/ingest_api/middleware.py
- [[._is_owner()]] - code - gateway/ingest_api/middleware.py
- [[._is_path_allowed_for_user()]] - code - gateway/ingest_api/middleware.py
- [[._is_tool_call_request()]] - code - gateway/ingest_api/middleware.py
- [[.close()_8]] - code - gateway/ingest_api/middleware.py
- [[.filter_outbound_response()]] - code - gateway/ingest_api/middleware.py
- [[.get_alert_dispatcher()]] - code - gateway/ingest_api/middleware.py
- [[.get_dns_filter()]] - code - gateway/ingest_api/middleware.py
- [[.get_drift_detector()]] - code - gateway/ingest_api/middleware.py
- [[.get_enhanced_tool_sanitizer()]] - code - gateway/ingest_api/middleware.py
- [[.get_killswitch_monitor()]] - code - gateway/ingest_api/middleware.py
- [[.get_log_sanitizer()]] - code - gateway/ingest_api/middleware.py
- [[.get_multi_turn_tracker()]] - code - gateway/ingest_api/middleware.py
- [[.get_network_validator()]] - code - gateway/ingest_api/middleware.py
- [[.get_output_canary()]] - code - gateway/ingest_api/middleware.py
- [[.get_rbac_manager()]] - code - gateway/ingest_api/middleware.py
- [[.get_tool_chain_analyzer()]] - code - gateway/ingest_api/middleware.py
- [[.process_request()]] - code - gateway/ingest_api/middleware.py
- [[.process_tool_result()]] - code - gateway/ingest_api/middleware.py
- [[.scan_tool_result()]] - code - gateway/ingest_api/middleware.py
- [[.test_defaults()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_denied_with_reason()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_full_init_success_and_getters()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_init_all_modules_fail_falls_back_to_none()]] - code - gateway/tests/test_middleware_coverage.py
- [[Analyze request to determine RBAC action, resource, and tool tier.]] - rationale - gateway/ingest_api/middleware.py
- [[Any_18]] - code - gateway/ingest_api/middleware.py
- [[Check RBAC permissions for the request.]] - rationale - gateway/ingest_api/middleware.py
- [[Check for unauthorized cross-session access attempts.          Implementation]] - rationale - gateway/ingest_api/middleware.py
- [[Check if a file path is allowed for a user to access.]] - rationale - gateway/ingest_api/middleware.py
- [[Check if user_id is the system owner via RBAC config (single source of truth).]] - rationale - gateway/ingest_api/middleware.py
- [[Enforce per-user, per-bot session isolation rules.          Each (user_id, bot_i]] - rationale - gateway/ingest_api/middleware.py
- [[Extract potential file paths from message content.]] - rationale - gateway/ingest_api/middleware.py
- [[Extract user ID from request data.]] - rationale - gateway/ingest_api/middleware.py
- [[Filter outbound response to remove sensitive XML and path information.]] - rationale - gateway/ingest_api/middleware.py
- [[Get the RBAC manager for external access.]] - rationale - gateway/ingest_api/middleware.py
- [[Get the log sanitizer for integration with logging system.]] - rationale - gateway/ingest_api/middleware.py
- [[Manages the P1 security middleware modules.]] - rationale - gateway/ingest_api/middleware.py
- [[MiddlewareManager]] - code - gateway/ingest_api/middleware.py
- [[MiddlewareResult]] - code - gateway/ingest_api/middleware.py
- [[Process request through all middleware modules.]] - rationale - gateway/ingest_api/middleware.py
- [[Process tool result through PII sanitization before it reaches agent          Ar]] - rationale - gateway/ingest_api/middleware.py
- [[Result from middleware processing.]] - rationale - gateway/ingest_api/middleware.py
- [[Return True only when the request contains actual tool calls or tool results.]] - rationale - gateway/ingest_api/middleware.py
- [[Return the name of a failed critical guard, or None if all healthy.          Use]] - rationale - gateway/ingest_api/middleware.py
- [[Scan tool result for injection attempts and return sanitized content.          A]] - rationale - gateway/ingest_api/middleware.py
- [[Shutdown middleware background tasks cleanly.]] - rationale - gateway/ingest_api/middleware.py
- [[TestInit]] - code - gateway/tests/test_middleware_coverage.py
- [[TestMiddlewareResult]] - code - gateway/tests/test_middleware_coverage.py
- [[middleware.py_1]] - document - docs/vault/02 - Modules/Gateway Core/middleware.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_31
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Community 34]]
- 33 edges to [[_COMMUNITY_Community 0]]
- 25 edges to [[_COMMUNITY_Community 6]]
- 20 edges to [[_COMMUNITY_Community 28]]
- 14 edges to [[_COMMUNITY_Community 1]]
- 14 edges to [[_COMMUNITY_Community 60]]
- 10 edges to [[_COMMUNITY_Community 130]]
- 9 edges to [[_COMMUNITY_Community 68]]
- 9 edges to [[_COMMUNITY_Community 16]]
- 8 edges to [[_COMMUNITY_Community 3]]
- 8 edges to [[_COMMUNITY_Community 254]]
- 6 edges to [[_COMMUNITY_Community 72]]
- 6 edges to [[_COMMUNITY_Community 140]]
- 6 edges to [[_COMMUNITY_Community 26]]
- 6 edges to [[_COMMUNITY_Community 146]]
- 6 edges to [[_COMMUNITY_Community 455]]
- 6 edges to [[_COMMUNITY_Community 1658]]
- 6 edges to [[_COMMUNITY_Community 37]]
- 6 edges to [[_COMMUNITY_Community 114]]
- 5 edges to [[_COMMUNITY_Community 7]]
- 5 edges to [[_COMMUNITY_Community 12]]
- 4 edges to [[_COMMUNITY_Community 151]]
- 4 edges to [[_COMMUNITY_Community 4]]
- 4 edges to [[_COMMUNITY_Community 2050]]
- 4 edges to [[_COMMUNITY_Community 605]]
- 4 edges to [[_COMMUNITY_Community 138]]
- 3 edges to [[_COMMUNITY_Community 52]]
- 3 edges to [[_COMMUNITY_Community 196]]
- 3 edges to [[_COMMUNITY_Community 152]]
- 3 edges to [[_COMMUNITY_Community 198]]
- 3 edges to [[_COMMUNITY_Community 9]]
- 3 edges to [[_COMMUNITY_Community 1281]]
- 3 edges to [[_COMMUNITY_Community 71]]
- 3 edges to [[_COMMUNITY_Community 45]]
- 3 edges to [[_COMMUNITY_Community 233]]
- 3 edges to [[_COMMUNITY_Community 5]]
- 3 edges to [[_COMMUNITY_Community 477]]
- 3 edges to [[_COMMUNITY_Community 8]]
- 3 edges to [[_COMMUNITY_Community 154]]
- 3 edges to [[_COMMUNITY_Community 431]]
- 3 edges to [[_COMMUNITY_Community 53]]
- 3 edges to [[_COMMUNITY_Community 1130]]
- 3 edges to [[_COMMUNITY_Community 94]]
- 2 edges to [[_COMMUNITY_Community 978]]
- 2 edges to [[_COMMUNITY_Community 1127]]
- 2 edges to [[_COMMUNITY_Community 1209]]
- 2 edges to [[_COMMUNITY_Community 1343]]
- 1 edge to [[_COMMUNITY_Community 229]]
- 1 edge to [[_COMMUNITY_Community 13]]
- 1 edge to [[_COMMUNITY_Community 1412]]
- 1 edge to [[_COMMUNITY_Community 1131]]
- 1 edge to [[_COMMUNITY_Community 2006]]
- 1 edge to [[_COMMUNITY_Community 1946]]
- 1 edge to [[_COMMUNITY_Community 235]]
- 1 edge to [[_COMMUNITY_Community 14]]
- 1 edge to [[_COMMUNITY_Community 592]]

## Top bridge nodes
- [[MiddlewareResult]] - degree 127, connects to 46 communities
- [[MiddlewareManager]] - degree 185, connects to 41 communities
- [[Any_18]] - degree 55, connects to 27 communities
- [[TestInit]] - degree 7, connects to 3 communities
- [[TestMiddlewareResult]] - degree 7, connects to 3 communities