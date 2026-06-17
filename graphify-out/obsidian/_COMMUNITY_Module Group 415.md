---
type: community
cohesion: 0.25
members: 8
---

# Module Group 415

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[AgentShroud Diagram Library (23 diagrams Architecture, Infrastructure, Data, Security, Behavior, Operations, Team)]] - document - docs/diagrams/README.md
- [[Approval Queue State Machine (pending → approvedrejectedexpired, 1-hour TTL)]] - document - docs/diagrams/05-behavior.md
- [[Bot Session State Machine (fresh → active → compacting → activereset, 196K token threshold)]] - document - docs/diagrams/05-behavior.md
- [[C4 Level 0 Context Diagram (Isaiah, AgentShroud, OpenAI, Anthropic, Telegram, GitHub, 1Password, Tailscale)]] - document - docs/diagrams/01-architecture.md
- [[C4 Level 1 Container Diagram (Gateway, OpenClaw Bot, Hermes Agent, HCI, Ledger DB, Approval DB)]] - document - docs/diagrams/01-architecture.md
- [[ERD (LEDGER table, APPROVAL_ITEMS table, SCHEMA_VERSION table)]] - document - docs/diagrams/03-data.md
- [[On-Call Runbook Decision Tree (crash loop, context limit, gateway unhealthy, security alert, no Telegram response)]] - document - docs/diagrams/06-operations.md
- [[Trust Boundary Diagram (Zone 0 Owner, Zone 1 Gateway, Zone 2 Bot, Zone 3 External Services, Zone 4 SSH-gated nodes)]] - document - docs/diagrams/04-security.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_415
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Module Group 261]]

## Top bridge nodes
- [[Trust Boundary Diagram (Zone 0 Owner, Zone 1 Gateway, Zone 2 Bot, Zone 3 External Services, Zone 4 SSH-gated nodes)]] - degree 2, connects to 1 community