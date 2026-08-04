---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "Tool Result Sanitizer"
location: "L175"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tool_Result_Sanitizer
---

# RedactionDetail

## Connections
- [[._sanitize_regex()]] - `calls` [EXTRACTED]
- [[.test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[.test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[.test_process_tool_result_success()]] - `calls` [EXTRACTED]
- [[.test_sanitize_dict_with_pii()]] - `calls` [EXTRACTED]
- [[.test_sanitize_string_with_pii()]] - `calls` [EXTRACTED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[Individual redaction record]] - `rationale_for` [EXTRACTED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RedactionResult_1]] - `uses` [INFERRED]
- [[TestConfidenceFloor]] - `uses` [INFERRED]
- [[TestConfigurationLoading]] - `uses` [INFERRED]
- [[TestMiddlewareIntegration]] - `uses` [INFERRED]
- [[TestRealWorldScenarios]] - `uses` [INFERRED]
- [[TestToolResultPIIConfig]] - `uses` [INFERRED]
- [[TestToolResultSanitizer]] - `uses` [INFERRED]
- [[models.py]] - `contains` [EXTRACTED]
- [[sanitizer.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Tool_Result_Sanitizer
