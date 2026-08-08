---
source_file: "gateway/tests/test_tool_result_pii.py"
type: "code"
community: "Security Module Middleware"
location: "L582"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Module_Middleware
---

# TestConfidenceFloor

## Connections
- [[.test_all_production_tool_overrides_meet_floor()]] - `method` [EXTRACTED]
- [[.test_default_pii_config_meets_floor()]] - `method` [EXTRACTED]
- [[.test_tool_result_config_default_meets_floor()]] - `method` [EXTRACTED]
- [[CLAUDE.md §7.8 mandates a 0.9 minimum PII confidence — guard the floor.      The]] - `rationale_for` [EXTRACTED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[RedactionDetail]] - `uses` [INFERRED]
- [[RedactionResult]] - `uses` [INFERRED]
- [[ToolResultPIIConfig]] - `uses` [INFERRED]
- [[ToolResultSanitizer]] - `uses` [INFERRED]
- [[test_tool_result_pii.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Module_Middleware