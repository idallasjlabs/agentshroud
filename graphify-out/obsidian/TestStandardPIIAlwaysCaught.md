---
source_file: "gateway/tests/test_differential_pii_detector.py"
type: "code"
community: "DifferentialPIIDetector"
location: "L168"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/DifferentialPIIDetector
---

# TestStandardPIIAlwaysCaught

## Connections
- [[.test_clean_content_no_hits()]] - `method` [EXTRACTED]
- [[.test_plain_email_caught_in_prompt()]] - `method` [EXTRACTED]
- [[.test_plain_email_caught_in_tool_result()]] - `method` [EXTRACTED]
- [[.test_us_ssn_caught_in_tool_result()]] - `method` [EXTRACTED]
- [[DifferentialPIIConfig_1]] - `uses` [INFERRED]
- [[DifferentialPIIDetector_1]] - `uses` [INFERRED]
- [[PIIHit]] - `uses` [INFERRED]
- [[PIIHitSeverity]] - `uses` [INFERRED]
- [[test_differential_pii_detector.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/DifferentialPIIDetector