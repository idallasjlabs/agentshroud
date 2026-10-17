---
type: community
members: 20
---

# Audit Ledger (SHA-256 hash only)

**Members:** 20 nodes

## Members
- [[1Password (op-proxy)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Anthropic API]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Approval Queue (human gate)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Audit Ledger (SHA-256 hash only)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Cron Scheduler (8 scheduled jobs)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Execute Action (tool call  reply)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[GitHub API]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[HTTP CONNECT Proxy (domain allowlist)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[LLM Inference (OpenAI  Anthropic)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[MCP Inspector]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[OpenAI API]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[PII Sanitizer (Presidio  regex)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Receive message  cron trigger]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Telegram API_1]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Telegram Input (@agentshroud_bot)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Web UI Input (localhost18790)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[agentshroud-config volume (openclaw.json)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[approval_queue.py]] - document - docs/vault/02 - Modules/Other/approval_queue.py.md
- [[iMessage Input (imsg-ssh bridge)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[ledger.db (90-day retention)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit_Ledger_SHA-256_hash_only
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Layer-by-Layer Breakdown]]
- 1 edge to [[_COMMUNITY_hermesSOUL]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only) (2)]]
- 1 edge to [[_COMMUNITY_Layer-by-Layer Breakdown (3)]]
- 1 edge to [[_COMMUNITY_Slack Channel Setup (2)]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context) (3)]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity (2)]]

## Top bridge nodes
- [[approval_queue.py]] - degree 7, connects to 6 communities
- [[Audit Ledger (SHA-256 hash only)]] - degree 7, connects to 4 communities
