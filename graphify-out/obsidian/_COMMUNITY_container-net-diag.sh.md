---
type: community
cohesion: 0.12
members: 19
---

# container-net-diag.sh

**Cohesion:** 0.12 - loosely connected
**Members:** 19 nodes

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
- [[iMessage Input (imsg-ssh bridge)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[ledger.db (90-day retention)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/container-net-diagsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_API Keys Setup Guide]]
- 1 edge to [[_COMMUNITY_test_cron_jobs_prompts.py]]
- 1 edge to [[_COMMUNITY_ADR-007 Zero-Config Security (docker-compose up]]
- 1 edge to [[_COMMUNITY_1.4 Implementation Plan]]
- 1 edge to [[_COMMUNITY_test_claude_via_openai_path.py]]

## Top bridge nodes
- [[Audit Ledger (SHA-256 hash only)]] - degree 7, connects to 4 communities
- [[Approval Queue (human gate)]] - degree 3, connects to 1 community