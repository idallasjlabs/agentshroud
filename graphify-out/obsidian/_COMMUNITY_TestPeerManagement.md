---
type: community
cohesion: 0.40
members: 5
---

# TestPeerManagement

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_register_peer()]] - code - gateway/tests/test_a2a_governance.py
- [[.test_trust_clamped()]] - code - gateway/tests/test_a2a_governance.py
- [[.test_unregister_peer()]] - code - gateway/tests/test_a2a_governance.py
- [[.test_update_trust()]] - code - gateway/tests/test_a2a_governance.py
- [[TestPeerManagement]] - code - gateway/tests/test_a2a_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPeerManagement
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_A2AGovernanceProxy]]
- 2 edges to [[_COMMUNITY_A2AMessage]]
- 1 edge to [[_COMMUNITY_A2APeer]]

## Top bridge nodes
- [[TestPeerManagement]] - degree 11, connects to 3 communities