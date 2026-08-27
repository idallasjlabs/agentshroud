---
source_file: "gateway/security/differential_pii_detector.py"
type: "code"
community: "Community 47"
location: "L299"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_47
---

# DifferentialPIIDetector

## Connections
- [[.__init__()_71]] - `method` [EXTRACTED]
- [[._deduplicate()]] - `method` [EXTRACTED]
- [[._detect_pii()]] - `method` [EXTRACTED]
- [[._detect_presidio()]] - `method` [EXTRACTED]
- [[._detect_regex()]] - `method` [EXTRACTED]
- [[._init_presidio()_1]] - `method` [EXTRACTED]
- [[._redact()]] - `method` [EXTRACTED]
- [[._scan()]] - `method` [EXTRACTED]
- [[.scan_prompt()]] - `method` [EXTRACTED]
- [[.scan_tool_result()_1]] - `method` [EXTRACTED]
- [[A2APolicyEngine_3]] - `uses` [INFERRED]
- [[A2AProxy_1]] - `uses` [INFERRED]
- [[Asymmetric PII detector lower floor for tool results, 0.9 for prompts.      Thi]] - `rationale_for` [EXTRACTED]
- [[DifferentialPIIConfig_1]] - `uses` [INFERRED]
- [[DifferentialPIIDetector_1]] - `uses` [INFERRED]
- [[PII Sanitizer Mitigation (Presidio + custom regex)]] - `semantically_similar_to` [INFERRED]
- [[RovoBlast Attack (Atlassian Rovo AI)]] - `implements` [EXTRACTED]
- [[TestAdversarialFormattingCaught]] - `uses` [INFERRED]
- [[TestAsymmetricFloor]] - `uses` [INFERRED]
- [[TestDeterministicPresidioInit]] - `uses` [INFERRED]
- [[TestDifferentialPIIDetectorConstruction]] - `uses` [INFERRED]
- [[TestPerToolConfiguration]] - `uses` [INFERRED]
- [[TestPresidioPathContract]] - `uses` [INFERRED]
- [[TestRedaction]] - `uses` [INFERRED]
- [[TestStandardPIIAlwaysCaught]] - `uses` [INFERRED]
- [[TestToolResultPIIReport]] - `uses` [INFERRED]
- [[ToolResultSanitizer]] - `semantically_similar_to` [INFERRED]
- [[_Event]] - `uses` [INFERRED]
- [[_FakeRecognizerResult]] - `uses` [INFERRED]
- [[_StubAuditStore]] - `uses` [INFERRED]
- [[_StubForwarder]] - `uses` [INFERRED]
- [[differential_pii_detector.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_differential_pii_detector.py]] - `imports` [EXTRACTED]
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_47