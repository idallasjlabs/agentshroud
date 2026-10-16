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
- [[dot-__init__()_162]] - `calls` [EXTRACTED]
- [[dot-__init__()_201]] - `method` [EXTRACTED]
- [[dot-_fingerprint()]] - `method` [EXTRACTED]
- [[dot-cleanup_expired()_3]] - `method` [EXTRACTED]
- [[dot-create_session()]] - `method` [EXTRACTED]
- [[dot-destroy_session()]] - `method` [EXTRACTED]
- [[dot-generate_instruction_nonce()]] - `method` [EXTRACTED]
- [[dot-manager()_2]] - `calls` [EXTRACTED]
- [[dot-register_event_source()]] - `method` [EXTRACTED]
- [[dot-rotate_session()]] - `method` [EXTRACTED]
- [[dot-test_cleanup_expired()]] - `calls` [EXTRACTED]
- [[dot-test_different_ips_not_rate_limited()]] - `calls` [EXTRACTED]
- [[dot-test_expired_session_rejected()]] - `calls` [EXTRACTED]
- [[dot-test_rate_limit_exceeded()_1]] - `calls` [EXTRACTED]
- [[dot-test_rate_limit_resets_after_window()]] - `calls` [EXTRACTED]
- [[dot-validate_event()]] - `method` [EXTRACTED]
- [[dot-validate_nonce()]] - `method` [EXTRACTED]
- [[dot-validate_session()]] - `method` [EXTRACTED]
- [[Action_3]] - `uses` [INFERRED]
- [[Any_63]] - `uses` [INFERRED]
- [[Chen et al. 2026 — Agent configuration vulnerabilities  session hijacking (arXiv2602.14364)]] - `cites` [EXTRACTED]
- [[ConsentFramework]] - `semantically_similar_to` [INFERRED]
- [[Exception_3]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_2]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestEventInjection]] - `uses` [INFERRED]
- [[TestInstructionNonce]] - `uses` [INFERRED]
- [[TestRateLimiting_4]] - `uses` [INFERRED]
- [[TestSessionCleanup]] - `uses` [INFERRED]
- [[TestSessionCreation]] - `uses` [INFERRED]
- [[TestSessionRotation]] - `uses` [INFERRED]
- [[TestSessionValidation]] - `uses` [INFERRED]
- [[ToolTier_1]] - `uses` [INFERRED]
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - `cites` [EXTRACTED]
- [[manager()_4]] - `calls` [EXTRACTED]
- [[middleware.py_1]] - `imports` [EXTRACTED]
- [[session_security.py_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SessionManager
