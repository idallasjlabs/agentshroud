---
type: community
cohesion: 0.15
members: 19
---

# Community 478

**Cohesion:** 0.15 - loosely connected
**Members:** 19 nodes

## Members
- [[.__init__()_116]] - code - gateway/security/session_security.py
- [[._fingerprint()]] - code - gateway/security/session_security.py
- [[.cleanup_expired()_3]] - code - gateway/security/session_security.py
- [[.create_session()]] - code - gateway/security/session_security.py
- [[.destroy_session()]] - code - gateway/security/session_security.py
- [[.generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[.test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[.test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[.test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[.test_rate_limit_exceeded()_1]] - code - gateway/tests/test_session_security.py
- [[.test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[.validate_nonce()]] - code - gateway/security/session_security.py
- [[Generate a single-use, time-bound nonce for an instruction.          Format ``]] - rationale - gateway/security/session_security.py
- [[RateLimitExceeded]] - code - gateway/security/session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window).]] - rationale - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[TestRateLimiting_3]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - paper - gateway/security/session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_478
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Community 474]]
- 10 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 5 edges to [[_COMMUNITY_Community 1132]]
- 3 edges to [[_COMMUNITY_Community 870]]
- 3 edges to [[_COMMUNITY_Community 1133]]
- 2 edges to [[_COMMUNITY_Community 132]]
- 1 edge to [[_COMMUNITY_Middleware & Lifespan]]
- 1 edge to [[_COMMUNITY_Security Audit & Drift Detection]]

## Top bridge nodes
- [[SessionManager]] - degree 40, connects to 7 communities
- [[RateLimitExceeded]] - degree 10, connects to 4 communities
- [[TestRateLimiting_3]] - degree 10, connects to 2 communities
- [[TestSessionCleanup]] - degree 9, connects to 2 communities
- [[.create_session()]] - degree 5, connects to 1 community