---
source_file: "gateway/security/tool_result_sanitizer.py"
type: "code"
community: "RedactionResult"
location: "L25"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RedactionResult
---

# ToolResultPIIConfig

## Connections
- [[dot-__init__()_109]] - `references` [EXTRACTED]
- [[dot-__init__()_108]] - `method` [EXTRACTED]
- [[dot-get_config_for_tool()]] - `method` [EXTRACTED]
- [[dot-set_config()]] - `calls` [EXTRACTED]
- [[dot-test_default_config()_3]] - `calls` [EXTRACTED]
- [[dot-test_email_content_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_icloud_contact_scanning()]] - `calls` [EXTRACTED]
- [[dot-test_sanitize_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_tool_result_config_default_meets_floor()]] - `calls` [EXTRACTED]
- [[dot-test_tool_specific_config()]] - `calls` [EXTRACTED]
- [[dot-tool_config()]] - `calls` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[PII configuration with per-tool overrides]] - `rationale_for` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[TestConfidenceFloor]] - `uses` [INFERRED]
- [[TestRealWorldScenarios]] - `uses` [INFERRED]
- [[TestToolResultPIIConfig]] - `uses` [INFERRED]
- [[TestToolResultSanitizer]] - `uses` [INFERRED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[test_tool_result_pii.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RedactionResult
