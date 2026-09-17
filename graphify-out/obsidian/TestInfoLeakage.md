---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Session Manager & PII/Context Guard"
location: "L383"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Session_Manager__PII/Context_Guard
---

# TestInfoLeakage

## Connections
- [[dot-test_encrypted_store_error_no_key_leak()]] - `method` [EXTRACTED]
- [[dot-test_env_guard_scrubs_output()]] - `method` [EXTRACTED]
- [[dot-test_git_guard_no_path_leak()]] - `method` [EXTRACTED]
- [[dot-test_log_sanitizer_covers_stack_traces()]] - `method` [EXTRACTED]
- [[dot-test_metadata_guard_strips_internal_headers()]] - `method` [EXTRACTED]
- [[dot-test_token_error_no_secret_leak()]] - `method` [EXTRACTED]
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
- [[Test that errors don't leak sensitive information.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Session_Manager__PII/Context_Guard