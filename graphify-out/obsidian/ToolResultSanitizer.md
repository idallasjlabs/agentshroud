---
source_file: "gateway/security/tool_result_sanitizer.py"
type: "code"
community: "Telegram Proxy Test Suite"
location: "L55"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Telegram_Proxy_Test_Suite
---

# ToolResultSanitizer

## Connections
- [[.__init__()_121]] - `method` [EXTRACTED]
- [[._extract_dict_content()]] - `method` [EXTRACTED]
- [[._extract_scannable_content()]] - `method` [EXTRACTED]
- [[._get_sanitizer_for_tool()]] - `method` [EXTRACTED]
- [[._log_redaction_audit()]] - `method` [EXTRACTED]
- [[._reconstruct_result()]] - `method` [EXTRACTED]
- [[.get_supported_tools()]] - `method` [EXTRACTED]
- [[.get_tool_config()]] - `method` [EXTRACTED]
- [[.sanitize_tool_result()]] - `method` [EXTRACTED]
- [[.sanitizer()_3]] - `calls` [EXTRACTED]
- [[.test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[.test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[.test_initialization()_5]] - `calls` [EXTRACTED]
- [[.test_sanitize_disabled()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[RedactionResult]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestConfidenceFloor]] - `uses` [INFERRED]
- [[TestConfigurationLoading]] - `uses` [INFERRED]
- [[TestMiddlewareIntegration]] - `uses` [INFERRED]
- [[TestRealWorldScenarios]] - `uses` [INFERRED]
- [[TestToolResultPIIConfig]] - `uses` [INFERRED]
- [[TestToolResultSanitizer]] - `uses` [INFERRED]
- [[Tool result PII sanitizer with per-tool configuration]] - `rationale_for` [EXTRACTED]
- [[ToolTier]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Telegram_Proxy_Test_Suite