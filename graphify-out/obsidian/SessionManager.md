---
source_file: "gateway/security/session_security.py"
type: "code"
community: "SessionManager"
location: "L54"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SessionManager
---

# SessionManager

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_197]] - `method` [EXTRACTED]
- [[dot-_fingerprint()]] - `method` [EXTRACTED]
- [[dot-cleanup_expired()_3]] - `method` [EXTRACTED]
- [[dot-create_session()]] - `method` [EXTRACTED]
- [[dot-destroy_session()]] - `method` [EXTRACTED]
- [[dot-generate_instruction_nonce()]] - `method` [EXTRACTED]
- [[dot-manager()_1]] - `calls` [INFERRED]
- [[dot-register_event_source()]] - `method` [EXTRACTED]
- [[dot-rotate_session()]] - `method` [EXTRACTED]
- [[dot-test_cleanup_expired()]] - `calls` [INFERRED]
- [[dot-test_different_ips_not_rate_limited()]] - `calls` [INFERRED]
- [[dot-test_expired_session_rejected()]] - `calls` [INFERRED]
- [[dot-test_rate_limit_exceeded()]] - `calls` [INFERRED]
- [[dot-test_rate_limit_resets_after_window()]] - `calls` [INFERRED]
- [[dot-validate_event()]] - `method` [EXTRACTED]
- [[dot-validate_nonce()]] - `method` [EXTRACTED]
- [[dot-validate_session()]] - `method` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestInstructionNonce]] - `uses` [INFERRED]
- [[TestRateLimiting_3]] - `uses` [INFERRED]
- [[TestSessionCleanup]] - `uses` [INFERRED]
- [[TestSessionValidation]] - `uses` [INFERRED]
- [[manager()_3]] - `uses` [INFERRED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[session_security.py_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SessionManager
