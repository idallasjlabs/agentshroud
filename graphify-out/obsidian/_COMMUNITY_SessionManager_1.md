---
type: community
cohesion: 0.15
members: 19
---

# SessionManager

**Cohesion:** 0.15 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-__init__()_63]] - code - gateway/security/session_security.py
- [[dot-_fingerprint()]] - code - gateway/security/session_security.py
- [[dot-cleanup_expired()]] - code - gateway/security/session_security.py
- [[dot-create_session()]] - code - gateway/security/session_security.py
- [[dot-destroy_session()]] - code - gateway/security/session_security.py
- [[dot-generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[dot-test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[dot-test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[dot-test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_exceeded()]] - code - gateway/tests/test_session_security.py
- [[dot-test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[dot-validate_nonce()]] - code - gateway/security/session_security.py
- [[Generate a single-use, time-bound nonce for an instruction.          Format ``]] - rationale - gateway/security/session_security.py
- [[RateLimitExceeded]] - code - gateway/security/session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window).]] - rationale - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[TestRateLimiting_1]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - paper - gateway/security/session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionManager
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_SessionManager]]
- 10 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_AgentShroud v0.7.0 Blue Team Security Audit Report_2]]
- 3 edges to [[_COMMUNITY_AgentShroud v0.7.0 Blue Team Security Audit Report_3]]
- 3 edges to [[_COMMUNITY_TestInstructionNonce]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[SessionManager]] - degree 40, connects to 7 communities
- [[RateLimitExceeded]] - degree 10, connects to 4 communities
- [[TestRateLimiting_1]] - degree 10, connects to 2 communities
- [[TestSessionCleanup]] - degree 9, connects to 2 communities
- [[dot-create_session()]] - degree 5, connects to 1 community
