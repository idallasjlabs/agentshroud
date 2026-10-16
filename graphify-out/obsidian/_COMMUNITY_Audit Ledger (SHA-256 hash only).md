---
type: community
cohesion: 0.08
members: 28
---

# Audit Ledger (SHA-256 hash only)

**Cohesion:** 0.08 - loosely connected
**Members:** 28 nodes

## Members
- [[1Password (op-proxy)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Anthropic API]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Approval Queue (human gate)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Cron Scheduler (8 scheduled jobs)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[EnhancedApprovalQueue (`enhanced_queue.py`)]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Environment Variables Used]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Execute Action (tool call  reply)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[GitHub API]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[HTTP CONNECT Proxy (domain allowlist)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Key Class `EnhancedApprovalQueue`]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[LLM Inference (OpenAI  Anthropic)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[MCP Inspector]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[OpenAI API]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[PII Sanitizer (Presidio  regex)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Persistence]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Purpose_74]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Receive message  cron trigger]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Related Notes_34]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Responsibilities_1]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Telegram API_1]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Telegram Input (@agentshroud_bot)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Timeout Behavior]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Tool Risk Tiers]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[Web UI Input (localhost18790)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[WebSocket Notifications]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[agentshroud-config volume (openclaw.json)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[approval_queue.py]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[iMessage Input (imsg-ssh bridge)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit_Ledger_SHA-256_hash_only
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_1]]
- 1 edge to [[_COMMUNITY_Layer-by-Layer Breakdown]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_Layer-by-Layer Breakdown_1]]
- 1 edge to [[_COMMUNITY_Slack Channel Setup]]
- 1 edge to [[_COMMUNITY_hermesSOUL]]

## Top bridge nodes
- [[approval_queue.py]] - degree 7, connects to 5 communities
- [[MCP Inspector]] - degree 3, connects to 1 community
- [[PII Sanitizer (Presidio  regex)]] - degree 3, connects to 1 community
