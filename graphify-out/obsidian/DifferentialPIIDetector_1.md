---
source_file: "gateway/security/differential_pii_detector.py"
type: "code"
community: "Community 46"
location: "L299"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_46
---

# DifferentialPIIDetector

## Connections
- [[dot-__init__()_149]] - `method` [EXTRACTED]
- [[dot-_deduplicate()]] - `method` [EXTRACTED]
- [[dot-_detect_pii()]] - `method` [EXTRACTED]
- [[dot-_detect_presidio()]] - `method` [EXTRACTED]
- [[dot-_detect_regex()]] - `method` [EXTRACTED]
- [[dot-_init_presidio()_1]] - `method` [EXTRACTED]
- [[dot-_redact()]] - `method` [EXTRACTED]
- [[dot-_scan()]] - `method` [EXTRACTED]
- [[dot-scan_prompt()]] - `method` [EXTRACTED]
- [[dot-scan_tool_result()_3]] - `method` [EXTRACTED]
- [[A2APolicyEngine]] - `uses` [INFERRED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[Asymmetric PII detector lower floor for tool results, 0.9 for prompts.      Thi]] - `rationale_for` [EXTRACTED]
- [[DifferentialPIIConfig]] - `uses` [INFERRED]
- [[DifferentialPIIDetector]] - `uses` [INFERRED]
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
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_differential_pii_detector.py]] - `imports` [EXTRACTED]
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_46