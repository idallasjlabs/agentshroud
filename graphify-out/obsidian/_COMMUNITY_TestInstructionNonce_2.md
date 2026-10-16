---
type: community
cohesion: 1.00
members: 2
---

# TestInstructionNonce

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[dot-test_nonce_expired_rejected()]] - code - gateway/tests/test_session_security.py
- [[A nonce with a timestamp outside the 5-min window is rejected.]] - rationale - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestInstructionNonce
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_SessionError]]

## Top bridge nodes
- [[dot-test_nonce_expired_rejected()]] - degree 2, connects to 1 community
