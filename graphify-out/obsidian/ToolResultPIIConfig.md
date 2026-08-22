---
source_file: "gateway/security/tool_result_sanitizer.py"
type: "code"
community: "Tool Result Pii"
location: "L25"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Tool_Result_Pii
---

# ToolResultPIIConfig

## Connections
- [[.__init__()_124]] - `method` [EXTRACTED]
- [[.__init__()_125]] - `references` [EXTRACTED]
- [[.get_config_for_tool()]] - `method` [EXTRACTED]
- [[.set_config()]] - `calls` [EXTRACTED]
- [[.test_default_config()_6]] - `calls` [EXTRACTED]
- [[.test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[.test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[.test_sanitize_disabled()]] - `calls` [EXTRACTED]
- [[.test_tool_result_config_default_meets_floor()]] - `calls` [EXTRACTED]
- [[.test_tool_specific_config()]] - `calls` [EXTRACTED]
- [[.tool_config()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PII configuration with per-tool overrides]] - `rationale_for` [EXTRACTED]
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
- [[ToolTier]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Tool_Result_Pii