---
type: community
members: 105
---

# openclaw/skills/i-cr/SKILL.md

**Members:** 105 nodes

## Members
- [[dot-__init__()_120]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-__init__()_121]] - code - gateway/security/tool_result_sanitizer.py
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
- [[dot-get_supported_tools()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-get_tool_config()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-mock_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-sanitize()_4]] - code - gateway/ingest_api/sanitizer.py
- [[dot-sanitize_tool_result()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-sanitizer()_2]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-set_config()]] - code - gateway/ingest_api/middleware.py
- [[dot-test_all_production_tool_overrides_meet_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_config_with_tool_result_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_default_config()_5]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_default_pii_config_meets_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_email_content_scanning()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_empty_content_handling()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_extract_scannable_content_dict()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_extract_scannable_content_list()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_extract_scannable_content_string()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_icloud_contact_scanning()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_initialization()_2]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_middleware_set_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_middleware_set_config_disabled()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_middleware_set_config_missing()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_process_tool_result_no_sanitizer()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_process_tool_result_sanitizer_error()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_process_tool_result_success()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_sanitize_dict_with_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_sanitize_disabled()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_sanitize_string_with_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_tool_result_config_default_meets_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_tool_specific_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-test_tool_specific_configuration()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-tool_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[0.9 PII Confidence Floor (CLAUDE.md §7.8)]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Any_40]] - code - gateway/security/tool_result_sanitizer.py
- [[CLAUDE.md §7.8 mandates a 0.9 minimum PII confidence — guard the floor.      The]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Default PII configuration for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Detect and redact PII from content          Args             content Text to s]] - rationale - gateway/ingest_api/sanitizer.py
- [[Extract text content from various tool result formats for PII scanning]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get PII config for a specific tool, applying overrides if configured]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get list of tools with specific PII configurations]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get or create a PIISanitizer instance for the specified tool]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get the PII configuration for a specific tool]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Individual redaction record]] - rationale - gateway/ingest_api/models.py
- [[Log PII redaction for audit trail without logging actual PII]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Mock configuration for middleware tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[PII configuration with per-tool overrides]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Reconstruct the tool result with sanitized content]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Recursively extract string content from dictionary]] - rationale - gateway/security/tool_result_sanitizer.py
- [[RedactionDetail]] - code - gateway/ingest_api/models.py
- [[RedactionResult_1]] - code - gateway/ingest_api/sanitizer.py
- [[RedactionResult_2]] - code - gateway/ingest_api/models.py
- [[Result of PII sanitization]] - rationale - gateway/ingest_api/models.py
- [[Sanitize a tool result for PII before it reaches the agent          Args]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Sanitize using Microsoft Presidio          Wraps synchronous Presidio calls in a]] - rationale - gateway/ingest_api/sanitizer.py
- [[Sanitize using regex patterns (fallback mode)          Detects         - US_SSN]] - rationale - gateway/ingest_api/sanitizer.py
- [[Set configuration and initialize tool result sanitizer]] - rationale - gateway/ingest_api/middleware.py
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
- [[Test sanitizer when disabled]] - rationale - gateway/tests/test_tool_result_pii.py
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
- [[TestToolResultSanitizer_1]] - code - gateway/tests/test_tool_result_pii.py
- [[Tool result PII configuration for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Tool result PII sanitizer with per-tool configuration]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Tool result sanitizer instance for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[ToolResultPIIConfig]] - code - gateway/security/tool_result_sanitizer.py
- [[ToolResultSanitizer_1]] - code - gateway/security/tool_result_sanitizer.py
- [[Track every MiddlewareManager instantiated in this class and         close its s]] - rationale - gateway/tests/test_tool_result_pii.py
- [[test_tool_result_pii.py]] - code - gateway/tests/test_tool_result_pii.py
- [[tool_result_sanitizer.py]] - code - gateway/security/tool_result_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/openclaw/skills/i-cr/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_EgressFilterConfig]]
- 35 edges to [[_COMMUNITY_MiddlewareManager]]
- 9 edges to [[_COMMUNITY_MCPPermissionManager]]
- 5 edges to [[_COMMUNITY_api.py (2)]]
- 4 edges to [[_COMMUNITY__make_proxy()]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 2 edges to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_web_config.py]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]

## Top bridge nodes
- [[ToolResultSanitizer_1]] - degree 40, connects to 4 communities
- [[RedactionResult_2]] - degree 27, connects to 4 communities
- [[RedactionDetail]] - degree 20, connects to 4 communities
- [[tool_result_sanitizer.py]] - degree 8, connects to 4 communities
- [[TestToolResultSanitizer_1]] - degree 21, connects to 3 communities
