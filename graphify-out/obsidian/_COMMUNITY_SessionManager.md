---
type: community
cohesion: 0.12
members: 22
---

# SessionManager

**Cohesion:** 0.12 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__init__()_145]] - code - gateway/security/session_security.py
- [[dot-_fingerprint()]] - code - gateway/security/session_security.py
- [[dot-cleanup_expired()_2]] - code - gateway/security/session_security.py
- [[dot-create_session()]] - code - gateway/security/session_security.py
- [[dot-destroy_session()]] - code - gateway/security/session_security.py
- [[dot-generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[dot-manager()_1]] - code - gateway/tests/test_session_security.py
- [[dot-register_event_source()]] - code - gateway/security/session_security.py
- [[dot-rotate_session()]] - code - gateway/security/session_security.py
- [[dot-test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[dot-test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_exceeded()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[dot-validate_nonce()]] - code - gateway/security/session_security.py
- [[dot-validate_session()]] - code - gateway/security/session_security.py
- [[Chen et al. 2026 — Agent configuration vulnerabilities  session hijacking (arXiv2602.14364)]] - paper - gateway/security/consent_framework.py
- [[Generate a single-use, time-bound nonce for an instruction.          Format ``]] - rationale - gateway/security/session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window).]] - rationale - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[TestRateLimiting_1]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - paper - gateway/security/session_security.py
- [[manager()_2]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionManager
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_SessionError]]
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_TestSessionValidation]]
- 2 edges to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[SessionManager]] - degree 40, connects to 4 communities
- [[dot-create_session()]] - degree 5, connects to 2 communities
- [[TestRateLimiting_1]] - degree 10, connects to 1 community
- [[dot-validate_session()]] - degree 6, connects to 1 community
- [[dot-rotate_session()]] - degree 3, connects to 1 community
