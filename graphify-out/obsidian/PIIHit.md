---
source_file: "gateway/security/differential_pii_detector.py"
type: "code"
community: "DifferentialPIIDetector"
location: "L94"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/DifferentialPIIDetector
---

# PIIHit

## Connections
- [[._deduplicate()]] - `references` [EXTRACTED]
- [[._detect_pii()]] - `references` [EXTRACTED]
- [[._detect_presidio()]] - `references` [EXTRACTED]
- [[._detect_regex()]] - `references` [EXTRACTED]
- [[._redact()]] - `references` [EXTRACTED]
- [[A single PII detection result.]] - `rationale_for` [EXTRACTED]
- [[DifferentialPIIConfig]] - `uses` [INFERRED]
- [[DifferentialPIIDetector]] - `uses` [INFERRED]
- [[TestAdversarialFormattingCaught]] - `uses` [INFERRED]
- [[TestAsymmetricFloor]] - `uses` [INFERRED]
- [[TestDeterministicPresidioInit]] - `uses` [INFERRED]
- [[TestDifferentialPIIDetectorConstruction]] - `uses` [INFERRED]
- [[TestPerToolConfiguration]] - `uses` [INFERRED]
- [[TestPresidioPathContract]] - `uses` [INFERRED]
- [[TestRedaction]] - `uses` [INFERRED]
- [[TestStandardPIIAlwaysCaught]] - `uses` [INFERRED]
- [[TestToolResultPIIReport]] - `uses` [INFERRED]
- [[_FakeRecognizerResult]] - `uses` [INFERRED]
- [[differential_pii_detector.py]] - `contains` [EXTRACTED]
- [[test_differential_pii_detector.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/DifferentialPIIDetector