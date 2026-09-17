---
source_file: "gateway/tests/test_differential_pii_detector.py"
type: "code"
community: "DifferentialPIIDetector"
location: "L303"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/DifferentialPIIDetector
---

# TestAdversarialFormattingCaught

## Connections
- [[.test_dotted_email_caught_in_tool_result()]] - `method` [EXTRACTED]
- [[.test_spaced_email_caught_in_tool_result()]] - `method` [EXTRACTED]
- [[.test_zero_width_space_injection_caught()]] - `method` [EXTRACTED]
- [[DifferentialPIIConfig_1]] - `uses` [INFERRED]
- [[DifferentialPIIDetector_1]] - `uses` [INFERRED]
- [[PIIHit]] - `uses` [INFERRED]
- [[PIIHitSeverity]] - `uses` [INFERRED]
- [[test_differential_pii_detector.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/DifferentialPIIDetector