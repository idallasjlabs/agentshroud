---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "ToolResultSanitizer"
location: "L207"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ToolResultSanitizer
---

# RedactionResult

## Connections
- [[.test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[.test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[.test_process_tool_result_success()]] - `calls` [EXTRACTED]
- [[.test_sanitize_dict_with_pii()]] - `calls` [EXTRACTED]
- [[.test_sanitize_string_with_pii()]] - `calls` [EXTRACTED]
- [[.test_tool_specific_configuration()]] - `calls` [EXTRACTED]
- [[Any_42]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PIISanitizer_2]] - `uses` [INFERRED]
- [[RedactionResult]] - `uses` [INFERRED]
- [[RedactionResult_1]] - `uses` [INFERRED]
- [[Result of PII sanitization]] - `rationale_for` [EXTRACTED]
- [[TestConfidenceFloor]] - `uses` [INFERRED]
- [[TestConfigurationLoading]] - `uses` [INFERRED]
- [[TestMiddlewareIntegration]] - `uses` [INFERRED]
- [[TestRealWorldScenarios]] - `uses` [INFERRED]
- [[TestToolResultPIIConfig]] - `uses` [INFERRED]
- [[TestToolResultSanitizer]] - `uses` [INFERRED]
- [[ToolResultPIIConfig]] - `uses` [INFERRED]
- [[ToolResultSanitizer]] - `uses` [INFERRED]
- [[ingest_apimodels.py]] - `contains` [EXTRACTED]
- [[sanitizer.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ToolResultSanitizer