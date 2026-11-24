---
type: community
members: 67
---

# MiddlewareManager

**Members:** 67 nodes

## Members
- [[dot-__init__()]] - code - gateway/ingest_api/middleware.py
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
- [[dot-test_all_module_attrs_exist_after_init()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_defaults()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_denied_with_reason()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_endpoint_reports_no_key_collisions_and_high_total()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_full_init_success_and_getters()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_init_all_modules_fail_falls_back_to_none()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_manage_modules_endpoint_uses_the_same_registry()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_middleware_set_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[Any]] - code
- [[Check RBAC permissions for the request.]] - rationale - gateway/ingest_api/middleware.py
- [[Check for unauthorized cross-session access attempts. Implementation note…]] - rationale - gateway/ingest_api/middleware.py
- [[Check if a file path is allowed for a user to access.]] - rationale - gateway/ingest_api/middleware.py
- [[Check if user_id is the system owner via RBAC config (single source of truth).]] - rationale - gateway/ingest_api/middleware.py
- [[Enforce per-user, per-bot session isolation rules. Each (user_id, bot_id) pair…]] - rationale - gateway/ingest_api/middleware.py
- [[Exception]] - code
- [[Execute the real endpoint against a fully-populated app_state and verify it…]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Extract potential file paths from message content.]] - rationale - gateway/ingest_api/middleware.py
- [[Extract user ID from request data.]] - rationale - gateway/ingest_api/middleware.py
- [[Filter outbound response to remove sensitive XML and path information. Args…]] - rationale - gateway/ingest_api/middleware.py
- [[Get the RBAC manager for external access.]] - rationale - gateway/ingest_api/middleware.py
- [[Initialize all security modules.]] - rationale - gateway/ingest_api/middleware.py
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
- [[Test middleware configuration setup]] - rationale - gateway/tests/test_tool_result_pii.py
- [[TestInit]] - code - gateway/tests/test_middleware_coverage.py
- [[TestManageModulesEndpointAccuracy]] - code - gateway/tests/test_docs_accuracy.py
- [[TestMiddlewareResult]] - code - gateway/tests/test_middleware_coverage.py
- [[The endpoint's P1 section must be generated from ALL_MODULE_ATTRS, not a…]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Verify managemodules enumerates every module MiddlewareManager wires.…]] - rationale - gateway/tests/test_docs_accuracy.py
- [[asyncio]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_socrouter.py]]
- 11 edges to [[_COMMUNITY_RedactionResult]]
- 8 edges to [[_COMMUNITY_middleware.py]]
- 6 edges to [[_COMMUNITY_FileSandbox]]
- 5 edges to [[_COMMUNITY_test_middleware_coverage.py]]
- 4 edges to [[_COMMUNITY_run]]
- 4 edges to [[_COMMUNITY_UserSessionManager]]
- 4 edges to [[_COMMUNITY_test_file_sandbox_message_gate.py]]
- 4 edges to [[_COMMUNITY_SubagentMonitor]]
- 4 edges to [[_COMMUNITY_TestApprovalHardening]]
- 4 edges to [[_COMMUNITY_DNSFilterConfig]]
- 4 edges to [[_COMMUNITY_web_proxy.py]]
- 4 edges to [[_COMMUNITY_PathIsolationManager]]
- 4 edges to [[_COMMUNITY_asyncio_1]]
- 3 edges to [[_COMMUNITY__FakeRBAC]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_test_docs_accuracy.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_LogSanitizer]]
- 2 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_MetadataGuard]]
- 2 edges to [[_COMMUNITY_EnvironmentGuard]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_SessionManager]]
- 2 edges to [[_COMMUNITY_TokenValidator]]
- 2 edges to [[_COMMUNITY_ServerConfig]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_ToolResultInjectionScanner]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_BrowserSecurityGuard]]
- 2 edges to [[_COMMUNITY_CredentialInjector]]
- 2 edges to [[_COMMUNITY_ContainerSnapshot]]
- 2 edges to [[_COMMUNITY_KeyRotationManager]]
- 2 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 2 edges to [[_COMMUNITY_MultiTurnTracker]]
- 2 edges to [[_COMMUNITY_NetworkValidator]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_OutputCanary]]
- 2 edges to [[_COMMUNITY_ToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_TestRBACIntegration]]
- 2 edges to [[_COMMUNITY_app]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizerConfig]]
- 1 edge to [[_COMMUNITY_TestMiddlewareSessionEnforcement]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_normalize_input]]

## Top bridge nodes
- [[MiddlewareManager]] - degree 115, connects to 44 communities
- [[dot-__init__()]] - degree 42, connects to 31 communities
- [[MiddlewareResult]] - degree 20, connects to 7 communities
- [[dot-process_request()]] - degree 15, connects to 2 communities
- [[TestManageModulesEndpointAccuracy]] - degree 8, connects to 2 communities
