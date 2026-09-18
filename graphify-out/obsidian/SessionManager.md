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
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_160]] - `method` [EXTRACTED]
- [[._fingerprint()]] - `method` [EXTRACTED]
- [[.cleanup_expired()_1]] - `method` [EXTRACTED]
- [[.create_session()]] - `method` [EXTRACTED]
- [[.destroy_session()]] - `method` [EXTRACTED]
- [[.generate_instruction_nonce()]] - `method` [EXTRACTED]
- [[.manager()_2]] - `calls` [EXTRACTED]
- [[.register_event_source()]] - `method` [EXTRACTED]
- [[.rotate_session()]] - `method` [EXTRACTED]
- [[.test_cleanup_expired()]] - `calls` [EXTRACTED]
- [[.test_different_ips_not_rate_limited()]] - `calls` [EXTRACTED]
- [[.test_expired_session_rejected()]] - `calls` [EXTRACTED]
- [[.test_rate_limit_exceeded()_1]] - `calls` [EXTRACTED]
- [[.test_rate_limit_resets_after_window()]] - `calls` [EXTRACTED]
- [[.validate_event()]] - `method` [EXTRACTED]
- [[.validate_nonce()]] - `method` [EXTRACTED]
- [[.validate_session()]] - `method` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Chen et al. 2026 — Agent configuration vulnerabilities  session hijacking (arXiv2602.14364)]] - `cites` [EXTRACTED]
- [[ConsentFramework]] - `semantically_similar_to` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestEventInjection]] - `uses` [INFERRED]
- [[TestInstructionNonce]] - `uses` [INFERRED]
- [[TestRateLimiting_2]] - `uses` [INFERRED]
- [[TestSessionCleanup]] - `uses` [INFERRED]
- [[TestSessionCreation]] - `uses` [INFERRED]
- [[TestSessionRotation]] - `uses` [INFERRED]
- [[TestSessionValidation]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - `cites` [EXTRACTED]
- [[manager()_4]] - `calls` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[session_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SessionManager