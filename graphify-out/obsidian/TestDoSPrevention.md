---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "PII Config & Test Fixtures"
location: "L295"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Config__Test_Fixtures
---

# TestDoSPrevention

## Connections
- [[.test_binary_data_in_text_fields()]] - `method` [EXTRACTED]
- [[.test_deeply_nested_context_attacks()]] - `method` [EXTRACTED]
- [[.test_empty_inputs_everywhere()]] - `method` [EXTRACTED]
- [[.test_many_pii_entities()]] - `method` [EXTRACTED]
- [[.test_rapid_fire_scans()]] - `method` [EXTRACTED]
- [[.test_regex_redos_email()]] - `method` [EXTRACTED]
- [[.test_regex_redos_ssn()]] - `method` [EXTRACTED]
- [[.test_very_long_message()]] - `method` [EXTRACTED]
- [[AlertDispatcher]] - `uses` [INFERRED]
- [[ConsentDecision]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressChannel]] - `uses` [INFERRED]
- [[EgressEvent]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[EntropyCalculator]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MetadataGuard]] - `uses` [INFERRED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEventType]] - `uses` [INFERRED]
- [[SubagentMonitor]] - `uses` [INFERRED]
- [[Test resilience against denial of service patterns.]] - `rationale_for` [EXTRACTED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Config__Test_Fixtures