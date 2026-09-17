---
source_file: "gateway/security/tool_result_sanitizer.py"
type: "code"
community: "ToolResultSanitizer"
location: "L25"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ToolResultSanitizer
---

# ToolResultPIIConfig

## Connections
- [[.__init__()_122]] - `method` [EXTRACTED]
- [[.__init__()_123]] - `references` [EXTRACTED]
- [[.get_config_for_tool()]] - `method` [EXTRACTED]
- [[.set_config()]] - `calls` [EXTRACTED]
- [[.test_default_config()_2]] - `calls` [EXTRACTED]
- [[.test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[.test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[.test_sanitize_disabled()]] - `calls` [EXTRACTED]
- [[.test_tool_result_config_default_meets_floor()]] - `calls` [EXTRACTED]
- [[.test_tool_specific_config()]] - `calls` [EXTRACTED]
- [[.tool_config()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/ToolResultSanitizer