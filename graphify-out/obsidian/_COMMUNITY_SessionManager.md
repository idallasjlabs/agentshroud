---
type: community
members: 60
---

# SessionManager

**Members:** 60 nodes

## Members
- [[dot-__init__()_205]] - code - gateway/security/session_security.py
- [[dot-_fingerprint()]] - code - gateway/security/session_security.py
- [[dot-cleanup_expired()_3]] - code - gateway/security/session_security.py
- [[dot-create_session()]] - code - gateway/security/session_security.py
- [[dot-destroy_session()]] - code - gateway/security/session_security.py
- [[dot-generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[dot-manager()_2]] - code - gateway/tests/test_session_security.py
- [[dot-register_event_source()]] - code - gateway/security/session_security.py
- [[dot-rotate_session()]] - code - gateway/security/session_security.py
- [[dot-test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[dot-test_create_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[dot-test_expired_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_expired_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_first_use_passes()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_generation_unique()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_replay_blocked()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_exceeded()_1]] - code - gateway/tests/test_session_security.py
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
- [[A freshly generated nonce validates on first use.]] - rationale - gateway/tests/test_session_security.py
- [[A nonce with a timestamp outside the 5-min window is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[Any_83]] - code - gateway/security/session_security.py
- [[Chen et al. 2026 (arXiv2602.14364) — Session Hijacking]] - paper - docs/vault/02 - Modules/Security Modules/session_security.py.md
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
- [[TestRateLimiting_4]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[TestSessionCreation]] - code - gateway/tests/test_session_security.py
- [[TestSessionRotation]] - code - gateway/tests/test_session_security.py
- [[TestSessionValidation]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 (arXiv2602.08412) — Confused Deputy  Event Injection Attacks]] - paper - docs/vault/02 - Modules/Security Modules/oauth_security.py.md
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - paper - gateway/security/session_security.py
- [[manager()_4]] - code - gateway/tests/test_session_security.py
- [[session_security.py_2]] - code - gateway/security/session_security.py
- [[test_session_security.py]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionManager
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_ConsentFramework]]
- 2 edges to [[_COMMUNITY_ConsentFramework (2)]]
- 1 edge to [[_COMMUNITY_TrustConfig (2)]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py]]

## Top bridge nodes
- [[session_security.py_2]] - degree 14, connects to 4 communities
- [[SessionManager]] - degree 40, connects to 2 communities
- [[SessionError]] - degree 16, connects to 1 community
- [[test_session_security.py]] - degree 10, connects to 1 community
- [[dot-create_session()]] - degree 5, connects to 1 community
