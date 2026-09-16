---
source_file: "gateway/security/tool_result_sanitizer.py"
type: "code"
community: "PII Sanitizer & Redaction"
location: "L25"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer__Redaction
---

# ToolResultPIIConfig

## Connections
- [[dot-__init__()_123]] - `references` [EXTRACTED]
- [[dot-__init__()_122]] - `method` [EXTRACTED]
- [[dot-get_config_for_tool()]] - `method` [EXTRACTED]
- [[dot-set_config()]] - `calls` [EXTRACTED]
- [[dot-test_default_config()_2]] - `calls` [EXTRACTED]
- [[dot-test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_sanitize_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_tool_result_config_default_meets_floor()]] - `calls` [EXTRACTED]
- [[dot-test_tool_specific_config()]] - `calls` [EXTRACTED]
- [[dot-tool_config()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PII configuration with per-tool overrides]] - `rationale_for` [EXTRACTED]
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
- [[ToolTier_2]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer__Redaction