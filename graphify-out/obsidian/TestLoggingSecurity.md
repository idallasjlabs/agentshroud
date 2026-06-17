---
source_file: "gateway/tests/test_security_audit.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L955"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Environment_Guard__Leak_Detection
---

# TestLoggingSecurity

## Connections
- [[._make_record()]] - `method` [EXTRACTED]
- [[.sanitizer()_2]] - `method` [EXTRACTED]
- [[.test_aws_key_redaction()]] - `method` [EXTRACTED]
- [[.test_aws_key_redaction_via_pattern()]] - `method` [EXTRACTED]
- [[.test_credit_card_in_logs()]] - `method` [EXTRACTED]
- [[.test_env_guard_command_check()]] - `method` [EXTRACTED]
- [[.test_env_guard_monitoring()]] - `method` [EXTRACTED]
- [[.test_env_guard_scrub_output()]] - `method` [EXTRACTED]
- [[.test_git_guard_scan_repo()]] - `method` [EXTRACTED]
- [[.test_github_token_redaction()]] - `method` [EXTRACTED]
- [[.test_jwt_redaction()]] - `method` [EXTRACTED]
- [[.test_ssn_redaction_in_logs()]] - `method` [EXTRACTED]
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
- [[Test log sanitization and information leakage prevention.]] - `rationale_for` [EXTRACTED]
- [[ThreatAssessment]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Environment_Guard__Leak_Detection