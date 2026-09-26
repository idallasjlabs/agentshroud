---
type: community
cohesion: 0.11
members: 20
---

# gateway.security.agent_cve_registry

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
- [[README_120]] - document - docs/diagrams/README.md
- [[Runbook  Decision Tree — On-Call Logic]] - concept - docs/diagrams/06-operations.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gatewaysecurityagent_cve_registry
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_.test_gives_up_and_marks_sent_after_max_retries(]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_Error Index]]
- 1 edge to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_ADR-004 API Keys Never in Agent Container]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]

## Top bridge nodes
- [[README_120]] - degree 8, connects to 4 communities
- [[04-security]] - degree 5, connects to 1 community
- [[Incident Response Flow — Severity & Escalation]] - degree 3, connects to 1 community
- [[Runbook  Decision Tree — On-Call Logic]] - degree 3, connects to 1 community
- [[Credential Flow Diagram (op-proxy)]] - degree 2, connects to 1 community