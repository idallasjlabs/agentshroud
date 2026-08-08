---
source_file: "gateway/tests/test_differential_pii_detector.py"
type: "code"
community: "Gateway Test Suite"
location: "L60"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# TestDeterministicPresidioInit

## Connections
- [[.test_cannot_set_tool_floor_above_prompt_floor()]] - `method` [EXTRACTED]
- [[.test_cannot_set_tool_floor_below_minimum()]] - `method` [EXTRACTED]
- [[.test_init_does_not_construct_bare_analyzer_engine()]] - `method` [EXTRACTED]
- [[.test_init_wires_explicit_nlp_engine_when_model_present()]] - `method` [EXTRACTED]
- [[.test_regex_fallback_when_model_absent()]] - `method` [EXTRACTED]
- [[DifferentialPIIConfig]] - `uses` [INFERRED]
- [[DifferentialPIIDetector]] - `uses` [INFERRED]
- [[PIIHit]] - `uses` [INFERRED]
- [[PIIHitSeverity]] - `uses` [INFERRED]
- [[Presidio init must be deterministic and must NEVER trigger a runtime     model a]] - `rationale_for` [EXTRACTED]
- [[test_differential_pii_detector.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite