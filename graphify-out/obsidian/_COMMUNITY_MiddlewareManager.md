---
type: community
members: 91
---

# MiddlewareManager

**Members:** 91 nodes

## Members
- [[dot-_analyze_request_for_rbac()]] - code - gateway/ingest_api/middleware.py
- [[dot-_check_cross_session_access()]] - code - gateway/ingest_api/middleware.py
- [[dot-_check_rbac_permissions()]] - code - gateway/ingest_api/middleware.py
- [[dot-_critical_guard_failure()]] - code - gateway/ingest_api/middleware.py
- [[dot-_enforce_session_isolation()]] - code - gateway/ingest_api/middleware.py
- [[dot-_extract_file_paths()]] - code - gateway/ingest_api/middleware.py
- [[dot-_extract_user_id()]] - code - gateway/ingest_api/middleware.py
- [[dot-_is_owner()]] - code - gateway/ingest_api/middleware.py
- [[dot-_is_path_allowed_for_user()]] - code - gateway/ingest_api/middleware.py
- [[dot-_is_tool_call_request()]] - code - gateway/ingest_api/middleware.py
- [[dot-_record_guard_init_failure()]] - code - gateway/ingest_api/middleware.py
- [[dot-close()]] - code - gateway/ingest_api/middleware.py
- [[dot-filter_outbound_response()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_alert_dispatcher()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_dns_filter()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_drift_detector()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_enhanced_tool_sanitizer()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_killswitch_monitor()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_multi_turn_tracker()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_network_validator()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_output_canary()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_rbac_manager()]] - code - gateway/ingest_api/middleware.py
- [[dot-get_tool_chain_analyzer()]] - code - gateway/ingest_api/middleware.py
- [[dot-process_request()]] - code - gateway/ingest_api/middleware.py
- [[dot-process_tool_result()]] - code - gateway/ingest_api/middleware.py
- [[dot-scan_tool_result()]] - code - gateway/ingest_api/middleware.py
- [[dot-setup_method()]] - code - gateway/tests/test_rbac.py
- [[dot-teardown_method()]] - code - gateway/tests/test_rbac.py
- [[dot-test_actual_test_count_meets_minimum()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_all_module_attrs_exist_after_init()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_defaults()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_denied_with_reason()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_endpoint_reports_no_key_collisions_and_high_total()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_forward_middleware_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_forward_middleware_blocking()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_manage_modules_endpoint_uses_the_same_registry()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_module_has_implementation()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_rbac_allows_authorized_access()]] - code - gateway/tests/test_rbac.py
- [[dot-test_rbac_blocks_unauthorized_access()]] - code - gateway/tests/test_rbac.py
- [[dot-test_rbac_handles_missing_user_id()]] - code - gateway/tests/test_rbac.py
- [[dot-test_rbac_initialization_in_middleware()]] - code - gateway/tests/test_rbac.py
- [[Analyze request to determine RBAC action, resource, and tool tier.]] - rationale - gateway/ingest_api/middleware.py
- [[Any]] - code
- [[Check RBAC permissions for the request.]] - rationale - gateway/ingest_api/middleware.py
- [[Check for unauthorized cross-session access attempts. Implementation note…]] - rationale - gateway/ingest_api/middleware.py
- [[Check if a file path is allowed for a user to access.]] - rationale - gateway/ingest_api/middleware.py
- [[Check if user_id is the system owner via RBAC config (single source of truth).]] - rationale - gateway/ingest_api/middleware.py
- [[Close sqlite-holding sub-modules so Python 3.13's GC does not finalize them…]] - rationale - gateway/tests/test_rbac.py
- [[Documentation Verification Tests — ensure docs match reality.]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Enforce per-user, per-bot session isolation rules. Each (user_id, bot_id) pair…]] - rationale - gateway/ingest_api/middleware.py
- [[Exception]] - code
- [[Execute the real endpoint against a fully-populated app_state and verify it…]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Extract potential file paths from message content.]] - rationale - gateway/ingest_api/middleware.py
- [[Extract user ID from request data.]] - rationale - gateway/ingest_api/middleware.py
- [[Filter outbound response to remove sensitive XML and path information. Args…]] - rationale - gateway/ingest_api/middleware.py
- [[Get the RBAC manager for external access.]] - rationale - gateway/ingest_api/middleware.py
- [[Manages the P1 security middleware modules.]] - rationale - gateway/ingest_api/middleware.py
- [[MiddlewareManager]] - code - gateway/ingest_api/middleware.py
- [[MiddlewareResult]] - code - gateway/ingest_api/middleware.py
- [[Process request through all middleware modules.]] - rationale - gateway/ingest_api/middleware.py
- [[Process tool result through PII sanitization before it reaches agent Args…]] - rationale - gateway/ingest_api/middleware.py
- [[Record a guard __init__ exception so the request path can fail closed. For…]] - rationale - gateway/ingest_api/middleware.py
- [[Result from middleware processing.]] - rationale - gateway/ingest_api/middleware.py
- [[Return True only when the request contains actual tool calls or tool results.…]] - rationale - gateway/ingest_api/middleware.py
- [[Return the name of a failed critical guard, or None if all healthy. Uses…]] - rationale - gateway/ingest_api/middleware.py
- [[Scan tool result for injection attempts and return sanitized content. Args…]] - rationale - gateway/ingest_api/middleware.py
- [[Set up test environment.]] - rationale - gateway/tests/test_rbac.py
- [[Shutdown middleware background tasks cleanly.]] - rationale - gateway/ingest_api/middleware.py
- [[Test forward endpoint with middleware integration.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test RBAC handling when user ID is missing.]] - rationale - gateway/tests/test_rbac.py
- [[Test RBAC integration with middleware.]] - rationale - gateway/tests/test_rbac.py
- [[Test that RBAC allows authorized access.]] - rationale - gateway/tests/test_rbac.py
- [[Test that RBAC blocks unauthorized access attempts.]] - rationale - gateway/tests/test_rbac.py
- [[Test that RBAC is properly initialized in middleware.]] - rationale - gateway/tests/test_rbac.py
- [[Test that middleware allows requests when they pass checks.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware can block requests with HTTP 403.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestForwardEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestManageModulesEndpointAccuracy]] - code - gateway/tests/test_docs_accuracy.py
- [[TestMiddlewareResult]] - code - gateway/tests/test_middleware_coverage.py
- [[TestRBACIntegration]] - code - gateway/tests/test_rbac.py
- [[TestReadmeModulesMatchCode]] - code - gateway/tests/test_docs_accuracy.py
- [[TestTestCountAccuracy]] - code - gateway/tests/test_docs_accuracy.py
- [[The endpoint's P1 section must be generated from ALL_MODULE_ATTRS, not a…]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Verify managemodules enumerates every module MiddlewareManager wires.…]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Verify each module listed in README has actual implementation.]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Verify test count claims in READMEdocs are reasonable.]] - rationale - gateway/tests/test_docs_accuracy.py
- [[We should have at least 350 tests (README says 351+).]] - rationale - gateway/tests/test_docs_accuracy.py
- [[asyncio]] - code
- [[asyncio_1]] - code
- [[parametrize]] - code
- [[test_docs_accuracy.py]] - code - gateway/tests/test_docs_accuracy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_middleware.py]]
- 11 edges to [[_COMMUNITY_RedactionResult]]
- 10 edges to [[_COMMUNITY_socrouter.py]]
- 7 edges to [[_COMMUNITY_test_middleware_coverage.py]]
- 5 edges to [[_COMMUNITY_TestContributingMdAccuracy]]
- 4 edges to [[_COMMUNITY_UserSessionManager]]
- 4 edges to [[_COMMUNITY_test_file_sandbox_message_gate.py]]
- 3 edges to [[_COMMUNITY_TestCriticalGuardInitFailClosed]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_dot-test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative]]
- 3 edges to [[_COMMUNITY_SecurityPipeline]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_SubagentMonitor]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_EgressEvent]]
- 2 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 2 edges to [[_COMMUNITY_fastapi]]
- 2 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 2 edges to [[_COMMUNITY_app]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_MetadataGuard]]
- 1 edge to [[_COMMUNITY_EnvironmentGuard]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_TokenValidator]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_test_memory_lifecycle.py]]
- 1 edge to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_MemoryLifecycleManager]]
- 1 edge to [[_COMMUNITY_ToolResultInjectionScanner]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_BrowserSecurityGuard]]
- 1 edge to [[_COMMUNITY_CredentialInjector]]
- 1 edge to [[_COMMUNITY_ContainerSnapshot]]
- 1 edge to [[_COMMUNITY_KeyRotationManager]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_NetworkValidator]]
- 1 edge to [[_COMMUNITY_OAuthSecurityValidator]]
- 1 edge to [[_COMMUNITY_OutputCanary]]
- 1 edge to [[_COMMUNITY_PathIsolationManager]]
- 1 edge to [[_COMMUNITY_ToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizerConfig]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[MiddlewareManager]] - degree 115, connects to 42 communities
- [[MiddlewareResult]] - degree 20, connects to 6 communities
- [[test_docs_accuracy.py]] - degree 12, connects to 3 communities
- [[dot-process_request()]] - degree 15, connects to 2 communities
- [[TestManageModulesEndpointAccuracy]] - degree 8, connects to 2 communities
