---
type: community
members: 24
---

# Community 353

**Members:** 24 nodes

## Members
- [[Agent Decision Logic Flowchart]] - image - docs/diagrams/images/diagram-14-logic-flow.png
- [[Agent routing (bindings config; e.g. Telegram ID 8096968754 → main agent)]] - image - docs/diagrams/images/diagram-14-logic-flow.png
- [[AgentShroud Data Assets Mind Map (data dictionary; mostly illegible black-on-black render)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[Approval Queue (human-in-the-loop)_1]] - concept - docs/papers/agentshroud-whitepaper.md
- [[Approval Queue State Diagram (pending → approvedrejectedexpired)]] - image - docs/diagrams/images/diagram-16-state-approval-queue.png
- [[Approval queue data (in-memory, backed by SQLite)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[Bot Session State Diagram (fresh → active → idlecompacting → reset)]] - image - docs/diagrams/images/diagram-17-state-bot-session.png
- [[Current Status_3]] - document - docs/flows/README.md
- [[Data Lineage Diagram (5-Layer Pipeline)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[EphemeralTransient data (never persisted raw)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[Flows Documentation]] - document - docs/flows/README.md
- [[Layer 1 — Source (TelegramiMessageCron)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[Layer 4 — Processing (Bot LLM API call, MCP-inspected tool call)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[Layer 5 — Consumption (auto-delete at expires_at, audit query, user response)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - concept - docs/diagrams/images/diagram-14-logic-flow.png
- [[MCP inspection result (in-memory only, logged to gateway stdout)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[PII Redaction (Presidio-style pattern matching PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png
- [[PII redaction result (hash only in ledger, never persisted raw)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[Peer binding Telegram 8096968754 → agentmain]] - image - docs/diagrams/images/diagram-15-sequence-telegram.png
- [[Planned Documents_2]] - document - docs/flows/README.md
- [[README_121]] - document - docs/flows/README.md
- [[SHA-256 content hashing (original_content_hash + sanitized content_hash)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png
- [[Telegram Message Sequence Diagram]] - image - docs/diagrams/images/diagram-15-sequence-telegram.png
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_353
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 320]]
- 2 edges to [[_COMMUNITY_Community 199]]
- 1 edge to [[_COMMUNITY_Community 1532]]
- 1 edge to [[_COMMUNITY_Community 280]]

## Top bridge nodes
- [[Approval Queue (human-in-the-loop)_1]] - degree 10, connects to 2 communities
- [[Telegram Message Sequence Diagram]] - degree 7, connects to 2 communities
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - degree 8, connects to 1 community
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - degree 8, connects to 1 community
- [[EphemeralTransient data (never persisted raw)]] - degree 5, connects to 1 community