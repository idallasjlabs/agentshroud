---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "LogSanitizer"
location: "L383"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LogSanitizer
---

# TestInfoLeakage

## Connections
- [[dot-test_encrypted_store_error_no_key_leak()]] - `method` [EXTRACTED]
- [[dot-test_env_guard_scrubs_output()]] - `method` [EXTRACTED]
- [[dot-test_git_guard_no_path_leak()]] - `method` [EXTRACTED]
- [[dot-test_log_sanitizer_covers_stack_traces()]] - `method` [EXTRACTED]
- [[dot-test_metadata_guard_strips_internal_headers()]] - `method` [EXTRACTED]
- [[dot-test_token_error_no_secret_leak()]] - `method` [EXTRACTED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MetadataGuard]] - `uses` [INFERRED]
- [[Test that errors don't leak sensitive information.]] - `rationale_for` [EXTRACTED]
- [[TokenValidator]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LogSanitizer
