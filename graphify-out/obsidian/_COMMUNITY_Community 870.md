---
type: community
cohesion: 0.20
members: 10
---

# Community 870

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.manager()_2]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_expired_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_first_use_passes()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_generation_unique()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_replay_blocked()]] - code - gateway/tests/test_session_security.py
- [[A freshly generated nonce validates on first use.]] - rationale - gateway/tests/test_session_security.py
- [[A nonce with a timestamp outside the 5-min window is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[Each call generates a distinct nonce.]] - rationale - gateway/tests/test_session_security.py
- [[Replaying the same nonce is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[TestInstructionNonce]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_870
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 474]]
- 3 edges to [[_COMMUNITY_Community 478]]
- 1 edge to [[_COMMUNITY_Community 1132]]

## Top bridge nodes
- [[TestInstructionNonce]] - degree 12, connects to 3 communities
- [[.manager()_2]] - degree 2, connects to 1 community