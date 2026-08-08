---
source_file: "gateway/security/differential_pii_detector.py"
type: "code"
community: "Gateway Test Suite"
location: "L299"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# DifferentialPIIDetector

## Connections
- [[.__init__()_68]] - `method` [EXTRACTED]
- [[._deduplicate()]] - `method` [EXTRACTED]
- [[._detect_pii()]] - `method` [EXTRACTED]
- [[._detect_presidio()]] - `method` [EXTRACTED]
- [[._detect_regex()]] - `method` [EXTRACTED]
- [[._init_presidio()_1]] - `method` [EXTRACTED]
- [[._redact()]] - `method` [EXTRACTED]
- [[._scan()]] - `method` [EXTRACTED]
- [[.scan_prompt()]] - `method` [EXTRACTED]
- [[.scan_tool_result()_1]] - `method` [EXTRACTED]
- [[Asymmetric PII detector lower floor for tool results, 0.9 for prompts.      Thi]] - `rationale_for` [EXTRACTED]
- [[DifferentialPIIConfig_1]] - `uses` [INFERRED]
- [[DifferentialPIIDetector_1]] - `uses` [INFERRED]
- [[PIIScanner]] - `semantically_similar_to` [INFERRED]
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
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_differential_pii_detector.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite