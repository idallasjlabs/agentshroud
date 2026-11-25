---
source_file: "gateway/tests/test_tool_result_pii.py"
type: "code"
community: "PIIConfig"
location: "L582"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PIIConfig
---

# TestConfidenceFloor

## Connections
- [[dot-test_all_production_tool_overrides_meet_floor()]] - `method` [EXTRACTED]
- [[dot-test_default_pii_config_meets_floor()]] - `method` [EXTRACTED]
- [[dot-test_tool_result_config_default_meets_floor()]] - `method` [EXTRACTED]
- [[CLAUDE.md §7.8 mandates a 0.9 minimum PII confidence — guard the floor. The…]] - `rationale_for` [EXTRACTED]
- [[GatewayConfig]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[ToolResultPIIConfig]] - `uses` [INFERRED]
- [[test_tool_result_pii.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PIIConfig
