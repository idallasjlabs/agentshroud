---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Session Manager & PII/Context Guard"
location: "L41"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Session_Manager__PII/Context_Guard
---

# TestTimingAttacks

## Connections
- [[dot-test_encrypted_store_constant_time()]] - `method` [EXTRACTED]
- [[dot-test_hmac_comparison_for_secrets()]] - `method` [EXTRACTED]
- [[dot-test_pii_scan_time_independent_of_content()]] - `method` [EXTRACTED]
- [[dot-test_prompt_guard_no_early_exit_leak()]] - `method` [EXTRACTED]
- [[dot-test_token_validation_rejects_fast()]] - `method` [EXTRACTED]
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
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEventType]] - `uses` [INFERRED]
- [[Test for timing side-channels in security-critical comparisons.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Session_Manager__PII/Context_Guard