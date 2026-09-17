---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Session Manager & PII/Context Guard"
location: "L576"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Session_Manager__PII/Context_Guard
---

# TestExfiltrationDetection

## Connections
- [[dot-test_dns_tunneling_detection()]] - `method` [EXTRACTED]
- [[dot-test_egress_monitor_loaded()_1]] - `method` [EXTRACTED]
- [[dot-test_env_guard_detects_data_access()]] - `method` [EXTRACTED]
- [[dot-test_file_sandbox_staging_detection()]] - `method` [EXTRACTED]
- [[dot-test_git_guard_detects_credential_patterns()]] - `method` [EXTRACTED]
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
- [[Test detection of data exfiltration patterns.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Session_Manager__PII/Context_Guard