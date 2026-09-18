---
type: community
cohesion: 0.11
members: 20
---

# diagrams/README.md

**Cohesion:** 0.11 - loosely connected
**Members:** 20 nodes

## Members
- [[04-security]] - document - docs/diagrams/04-security.md
- [[06-operations]] - document - docs/diagrams/06-operations.md
- [[11. Trust Boundary Diagram]] - document - docs/diagrams/04-security.md
- [[12. Credential Flow Diagram]] - document - docs/diagrams/04-security.md
- [[13. Network Security Diagram — Egress Controls]] - document - docs/diagrams/04-security.md
- [[18. Runbook  Decision Tree — On-Call Logic]] - document - docs/diagrams/06-operations.md
- [[19. Incident Response Flow — Severity & Escalation]] - document - docs/diagrams/06-operations.md
- [[20. Monitoring & Observability Map]] - document - docs/diagrams/06-operations.md
- [[AgentShroud — Diagram Library]] - document - docs/diagrams/README.md
- [[AgentShroud — Operations & Reliability Diagrams]] - document - docs/diagrams/06-operations.md
- [[AgentShroud — Security & Access Diagrams]] - document - docs/diagrams/04-security.md
- [[Credential Flow Diagram (op-proxy)]] - concept - docs/diagrams/04-security.md
- [[Diagrams Not Yet Implemented]] - document - docs/diagrams/README.md
- [[Incident Response Flow — Severity & Escalation]] - concept - docs/diagrams/06-operations.md
- [[Index]] - document - docs/diagrams/README.md
- [[Monitoring & Observability Map]] - concept - docs/diagrams/06-operations.md
- [[Network Security Diagram — Egress Controls]] - concept - docs/diagrams/04-security.md
- [[Priority Reading Order]] - document - docs/diagrams/README.md
- [[Runbook  Decision Tree — On-Call Logic]] - concept - docs/diagrams/06-operations.md
- [[diagramsREADME]] - document - docs/diagrams/README.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/diagrams/READMEmd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_02-infrastructure]]
- 2 edges to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_AgentShroud Gateway (Trust Zone 1) holds 1Passw]]
- 1 edge to [[_COMMUNITY_01-architecture]]
- 1 edge to [[_COMMUNITY_03-data]]
- 1 edge to [[_COMMUNITY_05-behavior]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]

## Top bridge nodes
- [[diagramsREADME]] - degree 8, connects to 4 communities
- [[04-security]] - degree 5, connects to 1 community
- [[Incident Response Flow — Severity & Escalation]] - degree 3, connects to 1 community
- [[Runbook  Decision Tree — On-Call Logic]] - degree 3, connects to 1 community
- [[Credential Flow Diagram (op-proxy)]] - degree 2, connects to 1 community