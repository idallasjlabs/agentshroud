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
- [[dot-__init__()_173]] - `references` [EXTRACTED]
- [[dot-__init__()_172]] - `method` [EXTRACTED]
- [[dot-get_config_for_tool()]] - `method` [EXTRACTED]
- [[dot-set_config()]] - `calls` [EXTRACTED]
- [[dot-test_default_config()_7]] - `calls` [EXTRACTED]
- [[dot-test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_sanitize_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_tool_result_config_default_meets_floor()]] - `calls` [EXTRACTED]
- [[dot-test_tool_specific_config()]] - `calls` [EXTRACTED]
- [[dot-tool_config()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_42]] - `uses` [INFERRED]
- [[Exception_3]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PII configuration with per-tool overrides]] - `rationale_for` [EXTRACTED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_2]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[RedactionResult_3]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestConfidenceFloor]] - `uses` [INFERRED]
- [[TestConfigurationLoading]] - `uses` [INFERRED]
- [[TestMiddlewareIntegration]] - `uses` [INFERRED]
- [[TestRealWorldScenarios]] - `uses` [INFERRED]
- [[TestToolResultPIIConfig]] - `uses` [INFERRED]
- [[TestToolResultSanitizer_1]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ToolResultSanitizer
