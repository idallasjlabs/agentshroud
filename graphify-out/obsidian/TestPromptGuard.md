---
source_file: "gateway/tests/test_security_audit.py"
type: "code"
community: "PII Sanitizer & Resource Guard"
location: "L219"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer__Resource_Guard
---

# TestPromptGuard

## Connections
- [[.guard()_5]] - `method` [EXTRACTED]
- [[.test_base64_injection()]] - `method` [EXTRACTED]
- [[.test_clean_message_not_blocked()]] - `method` [EXTRACTED]
- [[.test_clean_technical_message()]] - `method` [EXTRACTED]
- [[.test_dan_jailbreak()]] - `method` [EXTRACTED]
- [[.test_empty_input()_2]] - `method` [EXTRACTED]
- [[.test_ignore_previous_instructions()]] - `method` [EXTRACTED]
- [[.test_indirect_injection_url()]] - `method` [EXTRACTED]
- [[.test_instruction_override()]] - `method` [EXTRACTED]
- [[.test_multilingual_injection()]] - `method` [EXTRACTED]
- [[.test_prompt_leaking_via_markdown()]] - `method` [EXTRACTED]
- [[.test_repeated_injection()]] - `method` [EXTRACTED]
- [[.test_role_reassignment()]] - `method` [EXTRACTED]
- [[.test_system_prompt_extraction()]] - `method` [EXTRACTED]
- [[.test_token_smuggling()]] - `method` [EXTRACTED]
- [[.test_xml_injection()]] - `method` [EXTRACTED]
- [[AlertDispatcher]] - `uses` [INFERRED]
- [[CanaryResult]] - `uses` [INFERRED]
- [[ConfusedDeputyError]] - `uses` [INFERRED]
- [[ConsentDecision]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DNSFilterConfig]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressEvent]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[EntropyCalculator]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[IsolationStatus]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MetadataGuard]] - `uses` [INFERRED]
- [[NetworkValidator]] - `uses` [INFERRED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PKCEViolation]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[RedirectMismatch]] - `uses` [INFERRED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[ResourceLimits]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEvent]] - `uses` [INFERRED]
- [[SubagentMonitor]] - `uses` [INFERRED]
- [[Test prompt injection detection with adversarial payloads.]] - `rationale_for` [EXTRACTED]
- [[ThreatAssessment]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer__Resource_Guard
