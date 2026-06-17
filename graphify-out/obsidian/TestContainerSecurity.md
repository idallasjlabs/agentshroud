---
source_file: "gateway/tests/test_security_audit.py"
type: "code"
community: "PII Sanitizer & Resource Guard"
location: "L886"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer__Resource_Guard
---

# TestContainerSecurity

## Connections
- [[.test_agent_isolation_module()]] - `method` [EXTRACTED]
- [[.test_clamav_binary_not_found()]] - `method` [EXTRACTED]
- [[.test_clamav_parse_clean()]] - `method` [EXTRACTED]
- [[.test_clamav_parse_infected()]] - `method` [EXTRACTED]
- [[.test_network_validator_init()]] - `method` [EXTRACTED]
- [[.test_security_toolchain_clamav()]] - `method` [EXTRACTED]
- [[.test_security_toolchain_falco()]] - `method` [EXTRACTED]
- [[.test_security_toolchain_trivy()]] - `method` [EXTRACTED]
- [[.test_security_toolchain_wazuh()]] - `method` [EXTRACTED]
- [[.test_trivy_binary_not_found()]] - `method` [EXTRACTED]
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
- [[Test container hardening and runtime security.]] - `rationale_for` [EXTRACTED]
- [[ThreatAssessment]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer__Resource_Guard