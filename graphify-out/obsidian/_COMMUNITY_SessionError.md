---
type: community
cohesion: 0.16
members: 27
---

# SessionError

**Cohesion:** 0.16 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-test_create_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_nonce_generation_unique()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotate_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotated_session_valid()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_bound_to_identity()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_id_is_cryptographically_random()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unknown_event_source_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unregistered_session_event_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_valid_event_source_accepted()]] - code - gateway/tests/test_session_security.py
- [[dot-validate_event()]] - code - gateway/security/session_security.py
- [[Any_45]] - code - gateway/security/session_security.py
- [[Chen et al. 2026 (arXiv2602.14364) — Session Hijacking]] - paper - docs/vault/02 - Modules/Security Modules/session_security.py.md
- [[Each call generates a distinct nonce.]] - rationale - gateway/tests/test_session_security.py
- [[EventInjectionError]] - code - gateway/security/session_security.py
- [[RateLimitExceeded]] - code - gateway/security/session_security.py
- [[SessionBindingError]] - code - gateway/security/session_security.py
- [[SessionError]] - code - gateway/security/session_security.py
- [[SessionExpired]] - code - gateway/security/session_security.py
- [[TestEventInjection]] - code - gateway/tests/test_session_security.py
- [[TestInstructionNonce]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[TestSessionCreation]] - code - gateway/tests/test_session_security.py
- [[TestSessionRotation]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 (arXiv2602.08412) — Confused Deputy  Event Injection Attacks]] - paper - docs/vault/02 - Modules/Security Modules/oauth_security.py.md
- [[session_security.py]] - code - gateway/security/session_security.py
- [[test_session_security.py]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionError
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_SessionManager]]
- 6 edges to [[_COMMUNITY_TestSessionValidation]]
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_SubagentMonitor]]
- 1 edge to [[_COMMUNITY_TestInstructionNonce]]
- 1 edge to [[_COMMUNITY_TestInstructionNonce_1]]
- 1 edge to [[_COMMUNITY_TestInstructionNonce_2]]
- 1 edge to [[_COMMUNITY_KeyVault]]
- 1 edge to [[_COMMUNITY_TestDocumentTagging]]

## Top bridge nodes
- [[session_security.py]] - degree 14, connects to 5 communities
- [[TestInstructionNonce]] - degree 12, connects to 4 communities
- [[SessionError]] - degree 16, connects to 3 communities
- [[test_session_security.py]] - degree 10, connects to 3 communities
- [[EventInjectionError]] - degree 10, connects to 2 communities
