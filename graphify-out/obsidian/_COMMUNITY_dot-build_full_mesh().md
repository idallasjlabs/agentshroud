---
type: community
cohesion: 0.29
members: 7
---

# .build_full_mesh()

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-build_full_mesh()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-register_peer()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-register_trust_manager()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Attach a TrustManager instance to a bot name.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Build a ledger where every bot in bot_ids is a mutual peer of         every ot]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Register bot_b as a peer of bot_a.          Args             bot_a Source bot]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[TrustManager_2]] - code - gateway/security/cross_bot_trust_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/build_full_mesh
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]

## Top bridge nodes
- [[dot-build_full_mesh()]] - degree 6, connects to 3 communities
- [[dot-register_trust_manager()]] - degree 4, connects to 1 community
- [[dot-register_peer()]] - degree 3, connects to 1 community
- [[TrustManager_2]] - degree 2, connects to 1 community
