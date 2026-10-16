---
type: community
cohesion: 0.18
members: 19
---

# SessionManager

**Cohesion:** 0.18 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-register_event_source()]] - code - gateway/security/session_security.py
- [[dot-rotate_session()]] - code - gateway/security/session_security.py
- [[dot-test_create_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotate_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rotated_session_valid()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_bound_to_identity()]] - code - gateway/tests/test_session_security.py
- [[dot-test_session_id_is_cryptographically_random()]] - code - gateway/tests/test_session_security.py
- [[dot-validate_event()]] - code - gateway/security/session_security.py
- [[dot-validate_session()]] - code - gateway/security/session_security.py
- [[Any_4]] - code - gateway/security/session_security.py
- [[Chen et al. 2026 (arXiv2602.14364) — Session Hijacking]] - paper - docs/vault/02 - Modules/Security Modules/session_security.py.md
- [[EventInjectionError]] - code - gateway/security/session_security.py
- [[SessionBindingError]] - code - gateway/security/session_security.py
- [[SessionError]] - code - gateway/security/session_security.py
- [[SessionExpired]] - code - gateway/security/session_security.py
- [[TestSessionCreation]] - code - gateway/tests/test_session_security.py
- [[TestSessionRotation]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 (arXiv2602.08412) — Confused Deputy  Event Injection Attacks]] - paper - docs/vault/02 - Modules/Security Modules/oauth_security.py.md
- [[session_security.py]] - code - gateway/security/session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionManager
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_SessionManager_1]]
- 7 edges to [[_COMMUNITY_AgentShroud v0.7.0 Blue Team Security Audit Report_2]]
- 4 edges to [[_COMMUNITY_TestInstructionNonce]]
- 4 edges to [[_COMMUNITY_AgentShroud v0.7.0 Blue Team Security Audit Report_3]]
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_ConsentFramework_1]]
- 2 edges to [[_COMMUNITY_AlertDispatcher_1]]
- 1 edge to [[_COMMUNITY_TrustConfig_1]]

## Top bridge nodes
- [[session_security.py]] - degree 14, connects to 6 communities
- [[SessionError]] - degree 16, connects to 5 communities
- [[EventInjectionError]] - degree 10, connects to 4 communities
- [[SessionBindingError]] - degree 10, connects to 4 communities
- [[SessionExpired]] - degree 10, connects to 4 communities
