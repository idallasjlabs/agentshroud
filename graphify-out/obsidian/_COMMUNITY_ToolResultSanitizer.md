---
type: community
cohesion: 0.03
members: 106
---

# ToolResultSanitizer

**Cohesion:** 0.03 - loosely connected
**Members:** 106 nodes

## Members
- [[dot-__init__()_102]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_close_middleware_after()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-_extract_dict_content()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_extract_scannable_content()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_get_sanitizer_for_tool()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_log_redaction_audit()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_reconstruct_result()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_sanitize_presidio()]] - code - gateway/ingest_api/sanitizer.py
- [[dot-_sanitize_regex()]] - code - gateway/ingest_api/sanitizer.py
- [[dot-default_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-get_config_for_tool()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-get_tool_config()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-mock_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-sanitize()_2]] - code - gateway/ingest_api/sanitizer.py
- [[dot-sanitize_tool_result()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-sanitizer()_3]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_all_production_tool_overrides_meet_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_config_with_tool_result_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_default_config()_3]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_default_pii_config_meets_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_email_content_scanning()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_empty_content_handling()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_extract_scannable_content_dict()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_extract_scannable_content_list()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_extract_scannable_content_string()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_icloud_contact_scanning()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_initialization()_3]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_middleware_set_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_middleware_set_config_disabled()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_middleware_set_config_missing()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_process_tool_result_no_sanitizer()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_process_tool_result_sanitizer_error()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_process_tool_result_success()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_sanitize_dict_with_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_sanitize_string_with_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_tool_result_config_default_meets_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_tool_specific_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_tool_specific_configuration()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-tool_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[0.9 PII Confidence Floor (CLAUDE.md §7.8)]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Any_32]] - code - gateway/security/tool_result_sanitizer.py
- [[CLAUDE.md §7.8 mandates a 0.9 minimum PII confidence — guard the floor.      The]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Default PII configuration for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Detect and redact PII from content          Args             content Text to s]] - rationale - gateway/ingest_api/sanitizer.py
- [[Extract text content from various tool result formats for PII scanning]] - rationale - gateway/security/tool_result_sanitizer.py
- [[GatewayConfig_3]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[Get PII config for a specific tool, applying overrides if configured]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get or create a PIISanitizer instance for the specified tool]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get the PII configuration for a specific tool]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Individual redaction record]] - rationale - gateway/ingest_api/models.py
- [[Log PII redaction for audit trail without logging actual PII]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Mock configuration for middleware tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[PII detection and redaction configuration]] - rationale - gateway/ingest_api/config.py
- [[PIIConfig_1]] - code - gateway/security/tool_result_sanitizer.py
- [[PIIConfig_2]] - code - gateway/ingest_api/config.py
- [[PIISanitizer_3]] - code - gateway/security/tool_result_sanitizer.py
- [[Reconstruct the tool result with sanitized content]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Recursively extract string content from dictionary]] - rationale - gateway/security/tool_result_sanitizer.py
- [[RedactionDetail]] - code - gateway/ingest_api/models.py
- [[RedactionResult]] - code - gateway/ingest_api/sanitizer.py
- [[RedactionResult_1]] - code - gateway/security/tool_result_sanitizer.py
- [[RedactionResult_2]] - code - gateway/ingest_api/models.py
- [[Result of PII sanitization]] - rationale - gateway/ingest_api/models.py
- [[Sanitize a tool result for PII before it reaches the agent          Args]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Sanitize using Microsoft Presidio          Wraps synchronous Presidio calls in a]] - rationale - gateway/ingest_api/sanitizer.py
- [[Sanitize using regex patterns (fallback mode)          Detects         - US_SSN]] - rationale - gateway/ingest_api/sanitizer.py
- [[Test configuration loading and validation]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test content extraction from dictionary results]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test content extraction from string results]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test default configuration]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test handling of empty or whitespace-only content]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test integration with MiddlewareManager]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test middleware configuration setup]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test middleware configuration with disabled tool result PII]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test middleware configuration with missing tool_result_pii config]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test realistic tool result scenarios]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test sanitizer initialization]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test sanitizing dictionary content with PII]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test sanitizing string content with PII]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test scanning email content for sensitive data]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test scanning iCloud contact data for PII]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test successful tool result processing]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test that configuration includes tool result PII settings]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test that different tools get different PII configurations]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test the ToolResultPIIConfig configuration class]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test the ToolResultSanitizer class]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test tool result processing when sanitizer not configured]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test tool result processing when sanitizer raises an exception]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test tool-specific configuration overrides]] - rationale - gateway/tests/test_tool_result_pii.py
- [[TestConfidenceFloor]] - code - gateway/tests/test_tool_result_pii.py
- [[TestConfigurationLoading]] - code - gateway/tests/test_tool_result_pii.py
- [[TestMiddlewareIntegration]] - code - gateway/tests/test_tool_result_pii.py
- [[TestRealWorldScenarios]] - code - gateway/tests/test_tool_result_pii.py
- [[TestToolResultPIIConfig]] - code - gateway/tests/test_tool_result_pii.py
- [[TestToolResultSanitizer]] - code - gateway/tests/test_tool_result_pii.py
- [[Tool result PII configuration for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Tool result sanitizer instance for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Track every MiddlewareManager instantiated in this class and         close its s]] - rationale - gateway/tests/test_tool_result_pii.py
- [[canary-cron.sh embedded Python main()]] - code - scripts/canary-cron.sh
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[sanitizer.py]] - code - gateway/ingest_api/sanitizer.py
- [[test_config()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[test_tool_result_pii.py]] - code - gateway/tests/test_tool_result_pii.py
- [[tool_result_sanitizer.py]] - code - gateway/security/tool_result_sanitizer.py
- [[verify.sh]] - code - gateway/verify.sh
- [[verify.sh script]] - code - gateway/verify.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolResultSanitizer
SORT file.name ASC
```

## Connections to other communities
- 67 edges to [[_COMMUNITY_MiddlewareManager]]
- 36 edges to [[_COMMUNITY_PIIConfig]]
- 19 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 17 edges to [[_COMMUNITY_ApprovalQueueConfig_3]]
- 16 edges to [[_COMMUNITY_PipelineAction]]
- 14 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 14 edges to [[_COMMUNITY__req]]
- 7 edges to [[_COMMUNITY_AsyncMock_1]]
- 5 edges to [[_COMMUNITY_MiddlewareManager_2]]
- 5 edges to [[_COMMUNITY_create_auth_dependency]]
- 4 edges to [[_COMMUNITY_MiddlewareManager_3]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig_2]]
- 4 edges to [[_COMMUNITY_UserSessionManager_3]]
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 3 edges to [[_COMMUNITY_InjectionAction]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY__FakeRBAC]]
- 3 edges to [[_COMMUNITY_test_hermes_model_resolver.py_1]]
- 2 edges to [[_COMMUNITY_AWS Cloud Management & FinOps]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 2 edges to [[_COMMUNITY_test_filter_xml_blocks.py]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_5]]
- 2 edges to [[_COMMUNITY_AgentTarget_1]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py_4]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_9]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_7]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 1 edge to [[_COMMUNITY_TestMCPResultEndpoint]]
- 1 edge to [[_COMMUNITY_TestBuildCollaboratorSafeInfoResponse]]
- 1 edge to [[_COMMUNITY_TestInternalBannerMatcher]]
- 1 edge to [[_COMMUNITY_TestLooksLikeSafeCollaboratorInfoQuery]]
- 1 edge to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 1 edge to [[_COMMUNITY_TestOutboundClassifierHelpers]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_TestMultipartOutboundPipeline_1]]
- 1 edge to [[_COMMUNITY_TestWebSearchLog]]
- 1 edge to [[_COMMUNITY_egress_filter.py_3]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_Implementation Status]]
- 1 edge to [[_COMMUNITY_Git History Purge Plan]]
- 1 edge to [[_COMMUNITY_Local-Model Job Quality Matrix]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_3]]
- 1 edge to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[PIIConfig_2]] - degree 175, connects to 34 communities
- [[sanitizer.py]] - degree 13, connects to 7 communities
- [[RedactionResult_2]] - degree 27, connects to 5 communities
- [[tool_result_sanitizer.py]] - degree 9, connects to 5 communities
- [[GatewayConfig_3]] - degree 7, connects to 5 communities
