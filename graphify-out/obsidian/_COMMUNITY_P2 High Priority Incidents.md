---
type: community
cohesion: 0.25
members: 8
---

# P2 High Priority Incidents

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[Kill Switch Triggered]] - document - docs/operations/incident-response.md
- [[Layer 1 Pattern Matching]] - document - docs/security/security-architecture.md
- [[Layer 2 Unicode Normalization]] - document - docs/security/security-architecture.md
- [[Layer 3 Multi-Layer Decoding]] - document - docs/security/security-architecture.md
- [[Multi-Layer Detection Strategy]] - document - docs/security/security-architecture.md
- [[P2 High Priority Incidents]] - document - docs/operations/incident-response.md
- [[PII Leak Incident]] - document - docs/operations/incident-response.md
- [[Prompt Injection Detected]] - document - docs/operations/incident-response.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/P2_High_Priority_Incidents
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud Incident Response Plan]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Architecture]]

## Top bridge nodes
- [[P2 High Priority Incidents]] - degree 4, connects to 1 community
- [[Prompt Injection Detected]] - degree 3, connects to 1 community