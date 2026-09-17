---
source_file: "gateway/tests/test_differential_pii_detector.py"
type: "code"
community: "DifferentialPIIDetector"
location: "L359"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/DifferentialPIIDetector
---

# TestRedaction

## Connections
- [[.test_email_redacted_in_output()]] - `method` [EXTRACTED]
- [[.test_redact_on_hit_false_preserves_original()]] - `method` [EXTRACTED]
- [[.test_redacted_content_is_original_when_no_pii()]] - `method` [EXTRACTED]
- [[DifferentialPIIConfig_1]] - `uses` [INFERRED]
- [[DifferentialPIIDetector_1]] - `uses` [INFERRED]
- [[PIIHit]] - `uses` [INFERRED]
- [[PIIHitSeverity]] - `uses` [INFERRED]
- [[test_differential_pii_detector.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/DifferentialPIIDetector