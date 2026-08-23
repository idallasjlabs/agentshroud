---
type: community
cohesion: 0.04
members: 89
---

# Tool Result Pii

**Cohesion:** 0.04 - loosely connected
**Members:** 89 nodes

## Members
- [[.__init__()_125]] - code - gateway/security/tool_result_sanitizer.py
- [[._close_middleware_after()]] - code - gateway/tests/test_tool_result_pii.py
- [[._log_redaction_audit()]] - code - gateway/security/tool_result_sanitizer.py
- [[._sanitize_presidio()]] - code - gateway/ingest_api/sanitizer.py
- [[._sanitize_regex()]] - code - gateway/ingest_api/sanitizer.py
- [[.default_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[.get_supported_tools()]] - code - gateway/security/tool_result_sanitizer.py
- [[.mock_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[.sanitize()]] - code - gateway/ingest_api/sanitizer.py
- [[.sanitizer()_3]] - code - gateway/tests/test_tool_result_pii.py
- [[.set_config()]] - code - gateway/ingest_api/middleware.py
- [[.test_all_production_tool_overrides_meet_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_config_with_tool_result_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_default_config()_6]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_default_pii_config_meets_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_email_content_scanning()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_empty_content_handling()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_extract_scannable_content_dict()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_extract_scannable_content_list()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_extract_scannable_content_string()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_icloud_contact_scanning()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_initialization()_5]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_middleware_set_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_middleware_set_config_disabled()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_middleware_set_config_missing()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_process_tool_result_no_sanitizer()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_process_tool_result_sanitizer_error()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_process_tool_result_success()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_sanitize_dict_with_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_sanitize_disabled()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_sanitize_string_with_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_tool_result_config_default_meets_floor()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_tool_specific_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_tool_specific_configuration()]] - code - gateway/tests/test_tool_result_pii.py
- [[.tool_config()]] - code - gateway/tests/test_tool_result_pii.py
- [[0.9 PII Confidence Floor (CLAUDE.md §7.8)]] - rationale - gateway/tests/test_tool_result_pii.py
- [[CLAUDE.md §7.8 mandates a 0.9 minimum PII confidence — guard the floor.      The]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Default PII configuration for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Detect and redact PII from content          Args             content Text to s]] - rationale - gateway/ingest_api/sanitizer.py
- [[Get list of tools with specific PII configurations]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Individual redaction record]] - rationale - gateway/ingest_api/models.py
- [[Log PII redaction for audit trail without logging actual PII]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Mock configuration for middleware tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[PII configuration with per-tool overrides]] - rationale - gateway/security/tool_result_sanitizer.py
- [[RedactionDetail]] - code - gateway/ingest_api/models.py
- [[RedactionResult_1]] - code - gateway/ingest_api/sanitizer.py
- [[RedactionResult]] - code - gateway/ingest_api/models.py
- [[Result of PII sanitization]] - rationale - gateway/ingest_api/models.py
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
- [[TestToolResultSanitizer]] - code - gateway/tests/test_tool_result_pii.py
- [[Tool result PII configuration for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Tool result PII sanitizer with per-tool configuration]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Tool result sanitizer instance for tests]] - rationale - gateway/tests/test_tool_result_pii.py
- [[ToolResultPIIConfig]] - code - gateway/security/tool_result_sanitizer.py
- [[ToolResultSanitizer]] - code - gateway/security/tool_result_sanitizer.py
- [[Track every MiddlewareManager instantiated in this class and         close its s]] - rationale - gateway/tests/test_tool_result_pii.py
- [[test_tool_result_pii.py]] - code - gateway/tests/test_tool_result_pii.py
- [[tool_result_sanitizer.py]] - code - gateway/security/tool_result_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Tool_Result_Pii
SORT file.name ASC
```

## Connections to other communities
- 45 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 35 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 9 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 5 edges to [[_COMMUNITY_Slack Proxy Coverage]]
- 2 edges to [[_COMMUNITY_Router (soc)]]
- 2 edges to [[_COMMUNITY_Aiosqlite (05 - Dependencies)]]
- 2 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Differential Pii Detector]]
- 1 edge to [[_COMMUNITY_Us Ssn Regex Tightened]]

## Top bridge nodes
- [[ToolResultSanitizer]] - degree 40, connects to 4 communities
- [[RedactionResult]] - degree 27, connects to 3 communities
- [[TestToolResultSanitizer]] - degree 21, connects to 3 communities
- [[RedactionDetail]] - degree 20, connects to 3 communities
- [[TestMiddlewareIntegration]] - degree 17, connects to 3 communities