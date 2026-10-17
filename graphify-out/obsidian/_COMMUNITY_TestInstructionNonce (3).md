---
type: community
members: 2
---

# TestInstructionNonce (3)

**Members:** 2 nodes

## Members
- [[dot-test_nonce_expired_rejected()]] - code - gateway/tests/test_session_security.py
- [[A nonce with a timestamp outside the 5-min window is rejected.]] - rationale - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestInstructionNonce_3
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_SessionManager]]

## Top bridge nodes
- [[dot-test_nonce_expired_rejected()]] - degree 2, connects to 1 community
