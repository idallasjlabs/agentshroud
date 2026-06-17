---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Module Group 110"
location: "L389"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Module_Group_110
---

# TestInfoLeakage

## Connections
- [[.test_encrypted_store_error_no_key_leak()]] - `method` [EXTRACTED]
- [[.test_env_guard_scrubs_output()]] - `method` [EXTRACTED]
- [[.test_git_guard_no_path_leak()]] - `method` [EXTRACTED]
- [[.test_log_sanitizer_covers_stack_traces()]] - `method` [EXTRACTED]
- [[.test_metadata_guard_strips_internal_headers()]] - `method` [EXTRACTED]
- [[.test_token_error_no_secret_leak()]] - `method` [EXTRACTED]
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
- [[Test that errors don't leak sensitive information.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Module_Group_110