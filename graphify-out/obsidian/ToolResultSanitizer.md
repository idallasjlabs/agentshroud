---
source_file: "gateway/security/tool_result_sanitizer.py"
type: "code"
community: "ToolResultSanitizer"
location: "L55"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ToolResultSanitizer
---

# ToolResultSanitizer

## Connections
- [[.__init__()_123]] - `method` [EXTRACTED]
- [[._extract_dict_content()]] - `method` [EXTRACTED]
- [[._extract_scannable_content()]] - `method` [EXTRACTED]
- [[._get_sanitizer_for_tool()]] - `method` [EXTRACTED]
- [[._log_redaction_audit()]] - `method` [EXTRACTED]
- [[._reconstruct_result()]] - `method` [EXTRACTED]
- [[.get_supported_tools()]] - `method` [EXTRACTED]
- [[.get_tool_config()]] - `method` [EXTRACTED]
- [[.sanitize_tool_result()]] - `method` [EXTRACTED]
- [[.sanitizer()_2]] - `calls` [EXTRACTED]
- [[.test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[.test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[.test_initialization()_4]] - `calls` [EXTRACTED]
- [[.test_sanitize_disabled()]] - `calls` [EXTRACTED]
- [[0.9 PII Confidence Floor (CLAUDE.md §7.8)]] - `conceptually_related_to` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[DifferentialPIIDetector_1]] - `semantically_similar_to` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
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
- [[ToolTier_2]] - `uses` [INFERRED]
- [[US_SSN regex tightened to exclude CVE IDs]] - `conceptually_related_to` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ToolResultSanitizer