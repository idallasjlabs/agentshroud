---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "Tool Result Pii"
location: "L207"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Tool_Result_Pii
---

# RedactionResult

## Connections
- [[.test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[.test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[.test_process_tool_result_success()]] - `calls` [EXTRACTED]
- [[.test_sanitize_dict_with_pii()]] - `calls` [EXTRACTED]
- [[.test_sanitize_string_with_pii()]] - `calls` [EXTRACTED]
- [[.test_tool_specific_configuration()]] - `calls` [EXTRACTED]
- [[Any_63]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_1]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RedactionResult_1]] - `uses` [INFERRED]
- [[RedactionResult_3]] - `uses` [INFERRED]
- [[Result of PII sanitization]] - `rationale_for` [EXTRACTED]
- [[TestConfidenceFloor]] - `uses` [INFERRED]
- [[TestConfigurationLoading]] - `uses` [INFERRED]
- [[TestMiddlewareIntegration]] - `uses` [INFERRED]
- [[TestRealWorldScenarios]] - `uses` [INFERRED]
- [[TestToolResultPIIConfig]] - `uses` [INFERRED]
- [[TestToolResultSanitizer]] - `uses` [INFERRED]
- [[ToolResultPIIConfig]] - `uses` [INFERRED]
- [[ToolResultSanitizer]] - `uses` [INFERRED]
- [[models.py]] - `contains` [EXTRACTED]
- [[sanitizer.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Tool_Result_Pii