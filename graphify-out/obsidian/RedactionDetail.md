---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "PII Sanitizer & Redaction"
location: "L197"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer__Redaction
---

# RedactionDetail

## Connections
- [[dot-_sanitize_regex()]] - `calls` [EXTRACTED]
- [[dot-test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_process_tool_result_success()]] - `calls` [EXTRACTED]
- [[dot-test_sanitize_dict_with_pii()]] - `calls` [EXTRACTED]
- [[dot-test_sanitize_string_with_pii()]] - `calls` [EXTRACTED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[Individual redaction record]] - `rationale_for` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RedactionResult]] - `uses` [INFERRED]
- [[TestConfidenceFloor]] - `uses` [INFERRED]
- [[TestConfigurationLoading]] - `uses` [INFERRED]
- [[TestMiddlewareIntegration]] - `uses` [INFERRED]
- [[TestRealWorldScenarios]] - `uses` [INFERRED]
- [[TestToolResultPIIConfig]] - `uses` [INFERRED]
- [[TestToolResultSanitizer]] - `uses` [INFERRED]
- [[ingest_apimodels.py]] - `contains` [EXTRACTED]
- [[sanitizer.py]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer__Redaction