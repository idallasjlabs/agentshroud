---
type: community
members: 51
---

# SessionManager

**Members:** 51 nodes

## Members
- [[dot-__init__()_198]] - code - gateway/security/session_security.py
- [[dot-_fingerprint()]] - code - gateway/security/session_security.py
- [[dot-cleanup_expired()_3]] - code - gateway/security/session_security.py
- [[dot-create_session()]] - code - gateway/security/session_security.py
- [[dot-destroy_session()]] - code - gateway/security/session_security.py
- [[dot-generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[dot-manager()_2]] - code - gateway/tests/test_session_security.py
- [[dot-register_event_source()]] - code - gateway/security/session_security.py
- [[dot-test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[dot-test_create_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[dot-test_expired_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_exceeded()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotate_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotated_session_valid()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_bound_to_identity()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_id_is_cryptographically_random()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unknown_event_source_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unknown_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unregistered_session_event_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_valid_event_source_accepted()]] - code - gateway/tests/test_session_security.py
- [[dot-test_valid_session_accepted()]] - code - gateway/tests/test_session_security.py
- [[dot-test_wrong_ip_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_wrong_user_agent_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-validate_event()]] - code - gateway/security/session_security.py
- [[dot-validate_nonce()]] - code - gateway/security/session_security.py
- [[dot-validate_session()]] - code - gateway/security/session_security.py
- [[Any_82]] - code
- [[EventInjectionError]] - code - gateway/security/session_security.py
- [[Exception_18]] - code
- [[Generate a single-use, time-bound nonce for an instruction. Format…]] - rationale - gateway/security/session_security.py
- [[RateLimitExceeded]] - code - gateway/security/session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window). Side-…]] - rationale - gateway/security/session_security.py
- [[Session Security Module - Secure session management for MCP gateway. Provides…]] - rationale - gateway/security/session_security.py
- [[SessionBindingError]] - code - gateway/security/session_security.py
- [[SessionError]] - code - gateway/security/session_security.py
- [[SessionExpired]] - code - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[TestEventInjection]] - code - gateway/tests/test_session_security.py
- [[TestRateLimiting_3]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[TestSessionCreation]] - code - gateway/tests/test_session_security.py
- [[TestSessionRotation]] - code - gateway/tests/test_session_security.py
- [[TestSessionValidation]] - code - gateway/tests/test_session_security.py
- [[Tests for session_security module. TDD Written before implementation.]] - rationale - gateway/tests/test_session_security.py
- [[fixture_127]] - code
- [[manager()_3]] - code - gateway/tests/test_session_security.py
- [[session_security.py_2]] - code - gateway/security/session_security.py
- [[test_session_security.py]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionManager
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TestAuth_1]]
- 3 edges to [[_COMMUNITY_TestInstructionNonce]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue]]

## Top bridge nodes
- [[SessionManager]] - degree 26, connects to 4 communities
- [[session_security.py_2]] - degree 10, connects to 3 communities
- [[test_session_security.py]] - degree 9, connects to 1 community
- [[dot-validate_session()]] - degree 6, connects to 1 community
- [[dot-create_session()]] - degree 5, connects to 1 community
