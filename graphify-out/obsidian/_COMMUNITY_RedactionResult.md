---
type: community
members: 106
---

# RedactionResult

**Members:** 106 nodes

## Members
- [[dot-__init__()_108]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-__init__()_109]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_apply_enforcement()]] - code - gateway/ingest_api/sanitizer.py
- [[dot-_close_middleware_after()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-_extract_dict_content()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_extract_scannable_content()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_get_sanitizer_for_tool()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_log_redaction_audit()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_reconstruct_result()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_resolve_threshold()]] - code - gateway/ingest_api/sanitizer.py
- [[dot-_sanitize_presidio()]] - code - gateway/ingest_api/sanitizer.py
- [[dot-_sanitize_regex()]] - code - gateway/ingest_api/sanitizer.py
- [[dot-default_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-get_config_for_tool()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-mock_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-sanitize()_2]] - code - gateway/ingest_api/sanitizer.py
- [[dot-sanitize_tool_result()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-sanitizer()_3]] - code - gateway/tests/test_tool_result_pii.py
- [[dot-set_config()]] - code - gateway/ingest_api/middleware.py
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
- [[dot-test_initialization()_2]] - code - gateway/tests/test_tool_result_pii.py
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
- [[Any_39]] - code
- [[Apply monitorenforce + redactblock semantics to a redaction result.]] - rationale - gateway/ingest_api/sanitizer.py
- [[CLAUDE.md §7.8 mandates a 0.9 minimum PII confidence — guard the floor. The…]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Default PII configuration for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Detect PII in content and apply the enforcement action Args content Text to…]] - rationale - gateway/ingest_api/sanitizer.py
- [[Extract text content from various tool result formats for PII scanning]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get PII config for a specific tool, applying overrides if configured]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get or create a PIISanitizer instance for the specified tool]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Individual redaction record]] - rationale - gateway/ingest_api/models.py
- [[Log PII redaction for audit trail without logging actual PII]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Mock configuration for middleware tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[PII configuration with per-tool overrides]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Reconstruct the tool result with sanitized content]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Recursively extract string content from dictionary]] - rationale - gateway/security/tool_result_sanitizer.py
- [[RedactionDetail]] - code - gateway/ingest_api/models.py
- [[RedactionResult_1]] - code - gateway/ingest_api/models.py
- [[Result of PII sanitization]] - rationale - gateway/ingest_api/models.py
- [[Return the effective confidence threshold for one call (raise-only). The…]] - rationale - gateway/ingest_api/sanitizer.py
- [[Sanitize a tool result for PII before it reaches the agent Args tool_name…]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Sanitize using Microsoft Presidio Wraps synchronous Presidio calls in…]] - rationale - gateway/ingest_api/sanitizer.py
- [[Sanitize using regex patterns (fallback mode) Detects - US_SSN XXX-XX-XXXX -…]] - rationale - gateway/ingest_api/sanitizer.py
- [[Set configuration and initialize tool result sanitizer]] - rationale - gateway/ingest_api/middleware.py
- [[Test configuration loading and validation]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test content extraction from dictionary results]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test content extraction from list results]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test content extraction from string results]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test default configuration]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test handling of empty or whitespace-only content]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test integration with MiddlewareManager]] - rationale - gateway/tests/test_tool_result_pii.py
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
- [[TestToolResultSanitizer]] - code - gateway/tests/test_tool_result_pii.py
- [[Tests for Tool Result PII Sanitization Comprehensive tests for the tool result…]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Tool result PII configuration for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Tool result PII sanitizer with per-tool configuration]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Tool result sanitizer instance for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[ToolResultPIIConfig]] - code - gateway/security/tool_result_sanitizer.py
- [[ToolResultSanitizer_1]] - code - gateway/security/tool_result_sanitizer.py
- [[Track every MiddlewareManager instantiated in this class and close its sqlite-…]] - rationale - gateway/tests/test_tool_result_pii.py
- [[_analyze_and_anonymize()]] - code - gateway/ingest_api/sanitizer.py
- [[asyncio_45]] - code
- [[fixture_77]] - code
- [[test_tool_result_pii.py]] - code - gateway/tests/test_tool_result_pii.py
- [[tracker()]] - code - gateway/tests/test_tool_result_pii.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RedactionResult
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_lifespan.py]]
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 10 edges to [[_COMMUNITY_GatewayConfig]]
- 5 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[test_tool_result_pii.py]] - degree 18, connects to 4 communities
- [[ToolResultPIIConfig]] - degree 21, connects to 3 communities
- [[ToolResultSanitizer_1]] - degree 21, connects to 3 communities
- [[RedactionResult_1]] - degree 22, connects to 2 communities
- [[RedactionDetail]] - degree 16, connects to 2 communities
