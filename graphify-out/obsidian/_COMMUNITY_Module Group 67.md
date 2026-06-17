---
type: community
cohesion: 0.08
members: 57
---

# Module Group 67

**Cohesion:** 0.08 - loosely connected
**Members:** 57 nodes

## Members
- [[.__init__()_92]] - code - gateway/security/session_security.py
- [[._fingerprint()]] - code - gateway/security/session_security.py
- [[.cleanup_expired()_3]] - code - gateway/security/session_security.py
- [[.create_session()]] - code - gateway/security/session_security.py
- [[.destroy_session()]] - code - gateway/security/session_security.py
- [[.generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[.manager()_2]] - code - gateway/tests/test_session_security.py
- [[.register_event_source()]] - code - gateway/security/session_security.py
- [[.rotate_session()]] - code - gateway/security/session_security.py
- [[.test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[.test_create_session()]] - code - gateway/tests/test_session_security.py
- [[.test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[.test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[.test_expired_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_expired_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_first_use_passes()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_generation_unique()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_replay_blocked()]] - code - gateway/tests/test_session_security.py
- [[.test_rate_limit_exceeded()]] - code - gateway/tests/test_session_security.py
- [[.test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[.test_rotate_session()]] - code - gateway/tests/test_session_security.py
- [[.test_rotated_session_valid()]] - code - gateway/tests/test_session_security.py
- [[.test_session_bound_to_identity()]] - code - gateway/tests/test_session_security.py
- [[.test_session_id_is_cryptographically_random()]] - code - gateway/tests/test_session_security.py
- [[.test_unknown_event_source_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_unknown_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_unregistered_session_event_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_valid_event_source_accepted()]] - code - gateway/tests/test_session_security.py
- [[.test_valid_session_accepted()]] - code - gateway/tests/test_session_security.py
- [[.test_wrong_ip_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_wrong_user_agent_rejected()]] - code - gateway/tests/test_session_security.py
- [[.validate_event()]] - code - gateway/security/session_security.py
- [[.validate_nonce()]] - code - gateway/security/session_security.py
- [[.validate_session()]] - code - gateway/security/session_security.py
- [[A freshly generated nonce validates on first use.]] - rationale - gateway/tests/test_session_security.py
- [[A nonce with a timestamp outside the 5-min window is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[Any_53]] - code - gateway/security/session_security.py
- [[Each call generates a distinct nonce.]] - rationale - gateway/tests/test_session_security.py
- [[EventInjectionError]] - code - gateway/security/session_security.py
- [[Generate a single-use, time-bound nonce for an instruction.          Format ``]] - rationale - gateway/security/session_security.py
- [[RateLimitExceeded]] - code - gateway/security/session_security.py
- [[Replaying the same nonce is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window).]] - rationale - gateway/security/session_security.py
- [[SessionBindingError]] - code - gateway/security/session_security.py
- [[SessionError]] - code - gateway/security/session_security.py
- [[SessionExpired]] - code - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[TestEventInjection]] - code - gateway/tests/test_session_security.py
- [[TestInstructionNonce]] - code - gateway/tests/test_session_security.py
- [[TestRateLimiting_2]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[TestSessionCreation]] - code - gateway/tests/test_session_security.py
- [[TestSessionRotation]] - code - gateway/tests/test_session_security.py
- [[TestSessionValidation]] - code - gateway/tests/test_session_security.py
- [[manager()_1]] - code - gateway/tests/test_session_security.py
- [[session_security.py]] - code - gateway/security/session_security.py
- [[test_session_security.py]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_67
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 3 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 1 edge to [[_COMMUNITY_Module Group 113]]

## Top bridge nodes
- [[SessionManager]] - degree 36, connects to 1 community
- [[SessionError]] - degree 16, connects to 1 community
- [[session_security.py]] - degree 8, connects to 1 community
- [[.create_session()]] - degree 5, connects to 1 community
- [[.rotate_session()]] - degree 3, connects to 1 community