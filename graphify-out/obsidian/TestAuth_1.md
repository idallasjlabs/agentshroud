---
source_file: "gateway/tests/test_security_audit.py"
type: "code"
community: "OAuth & Metadata Guard"
location: "L377"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/OAuth__Metadata_Guard
---

# TestAuth

## Connections
- [[.test_agent_registry_module()]] - `method` [EXTRACTED]
- [[.test_consent_framework_loads()]] - `method` [EXTRACTED]
- [[.test_oauth_confused_deputy()]] - `method` [EXTRACTED]
- [[.test_oauth_pkce_violation()]] - `method` [EXTRACTED]
- [[.test_reject_empty_token()]] - `method` [EXTRACTED]
- [[.test_reject_garbage_token()]] - `method` [EXTRACTED]
- [[.test_reject_malformed_jwt()]] - `method` [EXTRACTED]
- [[.test_reject_none_algorithm()]] - `method` [EXTRACTED]
- [[.test_session_binding()]] - `method` [EXTRACTED]
- [[.test_session_different_fingerprints()]] - `method` [EXTRACTED]
- [[.test_trust_level_enforcement()]] - `method` [EXTRACTED]
- [[.test_trust_recovery()]] - `method` [EXTRACTED]
- [[.token_validator()]] - `method` [EXTRACTED]
- [[AlertDispatcher]] - `uses` [INFERRED]
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
- [[Test authentication and authorization enforcement.]] - `rationale_for` [EXTRACTED]
- [[ThreatAssessment]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/OAuth__Metadata_Guard