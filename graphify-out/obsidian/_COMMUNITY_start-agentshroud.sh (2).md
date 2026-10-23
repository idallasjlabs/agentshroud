---
type: community
cohesion: 0.14
members: 18
---

# start-agentshroud.sh (2)

**Cohesion:** 0.14 - loosely connected
**Members:** 18 nodes

## Members
- [[AgentShroud Data Assets (root)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[AgentShroud Data Assets Mind Map (data dictionary; mostly illegible black-on-black render)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[Approval queue data (in-memory, backed by SQLite)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[Data Lineage Diagram (5-Layer Pipeline)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[EphemeralTransient data (never persisted raw)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[External Credentials (1Password vault)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[Layer 1 — Source (TelegramiMessageCron)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[Layer 4 — Processing (Bot LLM API call, MCP-inspected tool call)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[Layer 5 — Consumption (auto-delete at expires_at, audit query, user response)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[MCP inspection result (in-memory only, logged to gateway stdout)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[OpenClaw Volume (openclaw.json, cronjobs.json, sessions)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[PII Redaction (Presidio-style pattern matching PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png
- [[PII redaction result (hash only in ledger, never persisted raw)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[SHA-256 content hashing (original_content_hash + sanitized content_hash)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png
- [[SQLite DBs (Backed by SQLite)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[approval_items table (pending, approved, rejected, expired; 1h TTL)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[ledger table (indexed on timestamp, source, forwarded_to)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/start-agentshroudsh_2
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]]

## Top bridge nodes
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - degree 8, connects to 1 community
- [[Approval queue data (in-memory, backed by SQLite)]] - degree 2, connects to 1 community
- [[MCP inspection result (in-memory only, logged to gateway stdout)]] - degree 2, connects to 1 community
