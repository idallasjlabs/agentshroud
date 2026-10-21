---
type: community
members: 81
---

# TelegramAPIProxy (2)

**Members:** 81 nodes

## Members
- [[dot-__init__()_154]] - code - gateway/security/session_security.py
- [[dot-_fingerprint()]] - code - gateway/security/session_security.py
- [[dot-cleanup_expired()_2]] - code - gateway/security/session_security.py
- [[dot-create_session()]] - code - gateway/security/session_security.py
- [[dot-destroy_session()]] - code - gateway/security/session_security.py
- [[dot-generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[dot-manager()_1]] - code - gateway/tests/test_session_security.py
- [[dot-register_event_source()]] - code - gateway/security/session_security.py
- [[dot-rotate_session()]] - code - gateway/security/session_security.py
- [[dot-test_agent_registry_module()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[dot-test_consent_framework_loads()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_create_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[dot-test_expired_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_expired_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_first_use_passes()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_generation_unique()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_replay_blocked()]] - code - gateway/tests/test_session_security.py
- [[dot-test_oauth_confused_deputy()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_oauth_pkce_violation()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_rate_limit_exceeded()_1]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[dot-test_reject_empty_token()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_garbage_token()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_malformed_jwt()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_none_algorithm()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_rotate_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotated_session_valid()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_binding()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_session_bound_to_identity()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_cannot_impersonate()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_session_different_fingerprints()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_session_id_is_cryptographically_random()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_rate_limit()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_unknown_event_source_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unknown_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unregistered_session_event_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_valid_event_source_accepted()]] - code - gateway/tests/test_session_security.py
- [[dot-test_valid_session_accepted()]] - code - gateway/tests/test_session_security.py
- [[dot-test_wrong_ip_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_wrong_user_agent_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-token_validator()]] - code - gateway/tests/test_security_audit.py
- [[dot-validate_event()]] - code - gateway/security/session_security.py
- [[dot-validate_nonce()]] - code - gateway/security/session_security.py
- [[dot-validate_session()]] - code - gateway/security/session_security.py
- [[A freshly generated nonce validates on first use.]] - rationale - gateway/tests/test_session_security.py
- [[A nonce with a timestamp outside the 5-min window is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[Agent registry should be importable.]] - rationale - gateway/tests/test_security_audit.py
- [[Any_58]] - code - gateway/security/session_security.py
- [[Chen et al. 2026 (arXiv2602.14364) — Session Hijacking]] - paper - docs/vault/02 - Modules/Security Modules/session_security.py.md
- [[Different fingerprints should create different sessions.]] - rationale - gateway/tests/test_security_audit.py
- [[Different sessions should have different identities.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Each call generates a distinct nonce.]] - rationale - gateway/tests/test_session_security.py
- [[EventInjectionError]] - code - gateway/security/session_security.py
- [[Generate a single-use, time-bound nonce for an instruction.          Format ``]] - rationale - gateway/security/session_security.py
- [[RateLimitExceeded]] - code - gateway/security/session_security.py
- [[Reject JWTs with alg=none (classic attack).]] - rationale - gateway/tests/test_security_audit.py
- [[Replaying the same nonce is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window).]] - rationale - gateway/security/session_security.py
- [[Session]] - code - gateway/security/session_security.py
- [[Session must bind to user identity.]] - rationale - gateway/tests/test_security_audit.py
- [[SessionBindingError]] - code - gateway/security/session_security.py
- [[SessionError]] - code - gateway/security/session_security.py
- [[SessionExpired]] - code - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[Test authentication and authorization enforcement.]] - rationale - gateway/tests/test_security_audit.py
- [[TestAuth]] - code - gateway/tests/test_security_audit.py
- [[TestEventInjection]] - code - gateway/tests/test_session_security.py
- [[TestInstructionNonce]] - code - gateway/tests/test_session_security.py
- [[TestRateLimiting_3]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[TestSessionCreation]] - code - gateway/tests/test_session_security.py
- [[TestSessionRotation]] - code - gateway/tests/test_session_security.py
- [[TestSessionValidation]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 (arXiv2602.08412) — Confused Deputy  Event Injection Attacks]] - paper - docs/vault/02 - Modules/Security Modules/oauth_security.py.md
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - paper - gateway/security/session_security.py
- [[manager()_4]] - code - gateway/tests/test_session_security.py
- [[session_security.py]] - code - gateway/security/session_security.py
- [[test_session_security.py]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy_2
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY__wrap_response()]]
- 13 edges to [[_COMMUNITY_MiddlewareManager]]
- 9 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 4 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 3 edges to [[_COMMUNITY_asyncio]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_SecureBrowser (3)]]
- 3 edges to [[_COMMUNITY_AgentShroud™ README]]
- 3 edges to [[_COMMUNITY__wrap_response() (4)]]
- 3 edges to [[_COMMUNITY__wrap_response() (3)_1]]
- 3 edges to [[_COMMUNITY_PortManager]]
- 2 edges to [[_COMMUNITY_test_playback_state.c]]
- 2 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY__wrap_response() (5)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]

## Top bridge nodes
- [[TestAuth]] - degree 48, connects to 21 communities
- [[Session]] - degree 30, connects to 10 communities
- [[session_security.py]] - degree 14, connects to 4 communities
- [[SessionManager]] - degree 40, connects to 2 communities
- [[SessionError]] - degree 16, connects to 1 community
