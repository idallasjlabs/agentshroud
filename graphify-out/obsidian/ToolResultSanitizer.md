---
source_file: "gateway/security/tool_result_sanitizer.py"
type: "code"
community: "MiddlewareManager"
location: "L55"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MiddlewareManager
---

# ToolResultSanitizer

## Connections
- [[dot-__init__()_79]] - `method` [EXTRACTED]
- [[dot-_extract_dict_content()]] - `method` [EXTRACTED]
- [[dot-_extract_scannable_content()]] - `method` [EXTRACTED]
- [[dot-_get_sanitizer_for_tool()]] - `method` [EXTRACTED]
- [[dot-_log_redaction_audit()]] - `method` [EXTRACTED]
- [[dot-_reconstruct_result()]] - `method` [EXTRACTED]
- [[dot-get_supported_tools()]] - `method` [EXTRACTED]
- [[dot-get_tool_config()]] - `method` [EXTRACTED]
- [[dot-sanitize_tool_result()]] - `method` [EXTRACTED]
- [[dot-sanitizer()_3]] - `calls` [EXTRACTED]
- [[dot-test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_initialization()_3]] - `calls` [EXTRACTED]
- [[dot-test_sanitize_disabled()]] - `calls` [EXTRACTED]
- [[0.9 PII Confidence Floor (CLAUDE.md §7.8)]] - `conceptually_related_to` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_21]] - `uses` [INFERRED]
- [[DifferentialPIIDetector_1]] - `semantically_similar_to` [INFERRED]
- [[Exception_3]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_1]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[RedactionResult_2]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestConfidenceFloor]] - `uses` [INFERRED]
- [[TestConfigurationLoading]] - `uses` [INFERRED]
- [[TestMiddlewareIntegration]] - `uses` [INFERRED]
- [[TestRealWorldScenarios]] - `uses` [INFERRED]
- [[TestToolResultPIIConfig]] - `uses` [INFERRED]
- [[TestToolResultSanitizer]] - `uses` [INFERRED]
- [[Tool result PII sanitizer with per-tool configuration]] - `rationale_for` [EXTRACTED]
- [[ToolResultSanitizer_1]] - `semantically_similar_to` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[US_SSN regex tightened to exclude CVE IDs]] - `conceptually_related_to` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MiddlewareManager
