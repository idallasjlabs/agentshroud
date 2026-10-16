---
type: community
cohesion: 0.17
members: 16
---

# SessionManager

**Cohesion:** 0.17 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-__init__()_177]] - code - gateway/security/session_security.py
- [[dot-_fingerprint()]] - code - gateway/security/session_security.py
- [[dot-cleanup_expired()_2]] - code - gateway/security/session_security.py
- [[dot-create_session()]] - code - gateway/security/session_security.py
- [[dot-destroy_session()]] - code - gateway/security/session_security.py
- [[dot-generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[dot-test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_exceeded()_1]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[dot-validate_nonce()]] - code - gateway/security/session_security.py
- [[Generate a single-use, time-bound nonce for an instruction.          Format ``]] - rationale - gateway/security/session_security.py
- [[RateLimitExceeded]] - code - gateway/security/session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window).]] - rationale - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[TestRateLimiting_4]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - paper - gateway/security/session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionManager
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_SessionError]]
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_TestInstructionNonce]]
- 3 edges to [[_COMMUNITY_TestSessionValidation]]
- 2 edges to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[SessionManager]] - degree 40, connects to 5 communities
- [[RateLimitExceeded]] - degree 10, connects to 3 communities
- [[TestRateLimiting_4]] - degree 10, connects to 1 community
- [[dot-create_session()]] - degree 5, connects to 1 community
- [[dot-_fingerprint()]] - degree 3, connects to 1 community
