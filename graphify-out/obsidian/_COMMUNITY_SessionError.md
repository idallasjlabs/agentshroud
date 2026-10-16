---
type: community
cohesion: 0.13
members: 28
---

# SessionError

**Cohesion:** 0.13 - loosely connected
**Members:** 28 nodes

## Members
- [[dot-register_event_source()]] - code - gateway/security/session_security.py
- [[dot-rotate_session()]] - code - gateway/security/session_security.py
- [[dot-test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[dot-test_create_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotate_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotated_session_valid()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_bound_to_identity()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_id_is_cryptographically_random()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unknown_event_source_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unregistered_session_event_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_valid_event_source_accepted()]] - code - gateway/tests/test_session_security.py
- [[dot-validate_event()]] - code - gateway/security/session_security.py
- [[dot-validate_session()]] - code - gateway/security/session_security.py
- [[Any_83]] - code - gateway/security/session_security.py
- [[Chen et al. 2026 (arXiv2602.14364) — Session Hijacking]] - paper - docs/vault/02 - Modules/Security Modules/session_security.py.md
- [[EventInjectionError]] - code - gateway/security/session_security.py
- [[SessionBindingError]] - code - gateway/security/session_security.py
- [[SessionError]] - code - gateway/security/session_security.py
- [[SessionExpired]] - code - gateway/security/session_security.py
- [[TestEventInjection]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[TestSessionCreation]] - code - gateway/tests/test_session_security.py
- [[TestSessionRotation]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 (arXiv2602.08412) — Confused Deputy  Event Injection Attacks]] - paper - docs/vault/02 - Modules/Security Modules/oauth_security.py.md
- [[manager()_4]] - code - gateway/tests/test_session_security.py
- [[session_security.py_2]] - code - gateway/security/session_security.py
- [[test_session_security.py]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionError
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_SessionManager]]
- 5 edges to [[_COMMUNITY_TestInstructionNonce]]
- 5 edges to [[_COMMUNITY_TestSessionValidation]]
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_ThreatAssessment]]
- 2 edges to [[_COMMUNITY_OAuthSecurityValidator]]
- 1 edge to [[_COMMUNITY_SubagentMonitor]]
- 1 edge to [[_COMMUNITY_TestDocumentTagging]]

## Top bridge nodes
- [[session_security.py_2]] - degree 14, connects to 5 communities
- [[SessionError]] - degree 16, connects to 4 communities
- [[test_session_security.py]] - degree 10, connects to 4 communities
- [[EventInjectionError]] - degree 10, connects to 3 communities
- [[SessionBindingError]] - degree 10, connects to 3 communities
