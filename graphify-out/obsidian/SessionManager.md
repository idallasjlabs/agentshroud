---
source_file: "gateway/security/session_security.py"
type: "code"
community: "Module Group 67"
location: "L54"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_67
---

# SessionManager

## Connections
- [[.__init__()_8]] - `calls` [EXTRACTED]
- [[.__init__()_92]] - `method` [EXTRACTED]
- [[._fingerprint()]] - `method` [EXTRACTED]
- [[.cleanup_expired()_3]] - `method` [EXTRACTED]
- [[.create_session()]] - `method` [EXTRACTED]
- [[.destroy_session()]] - `method` [EXTRACTED]
- [[.generate_instruction_nonce()]] - `method` [EXTRACTED]
- [[.manager()_2]] - `calls` [EXTRACTED]
- [[.register_event_source()]] - `method` [EXTRACTED]
- [[.rotate_session()]] - `method` [EXTRACTED]
- [[.test_cleanup_expired()]] - `calls` [EXTRACTED]
- [[.test_different_ips_not_rate_limited()]] - `calls` [EXTRACTED]
- [[.test_expired_session_rejected()]] - `calls` [EXTRACTED]
- [[.test_rate_limit_exceeded()]] - `calls` [EXTRACTED]
- [[.test_rate_limit_resets_after_window()]] - `calls` [EXTRACTED]
- [[.validate_event()]] - `method` [EXTRACTED]
- [[.validate_nonce()]] - `method` [EXTRACTED]
- [[.validate_session()]] - `method` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_6]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestEventInjection]] - `uses` [INFERRED]
- [[TestInstructionNonce]] - `uses` [INFERRED]
- [[TestRateLimiting_2]] - `uses` [INFERRED]
- [[TestSessionCleanup]] - `uses` [INFERRED]
- [[TestSessionCreation]] - `uses` [INFERRED]
- [[TestSessionRotation]] - `uses` [INFERRED]
- [[TestSessionValidation]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[manager()_1]] - `calls` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[session_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_67
