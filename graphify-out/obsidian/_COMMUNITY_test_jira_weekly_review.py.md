---
type: community
cohesion: 0.12
members: 19
---

# test_jira_weekly_review.py

**Cohesion:** 0.12 - loosely connected
**Members:** 19 nodes

## Members
- [[1Password (op-proxy)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Anthropic API]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
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
- [[SSH Proxy]] - concept - docs/architecture/system-architecture.md
- [[Telegram Input (@agentshroud_bot)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Web UI Input (localhost18790)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[agentshroud-config volume (openclaw.json)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[iMessage Input (imsg-ssh bridge)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[ledger.db (90-day retention)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[ssh_proxy (approved hosts only)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_jira_weekly_reviewpy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Mode A — Single task (3)]]
- 1 edge to [[_COMMUNITY_dot-cursormcp.json]]
- 1 edge to [[_COMMUNITY_ADR-007 Zero-Config Security (docker-compose up = fully secured)]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]
- 1 edge to [[_COMMUNITY_Proxy Layer]]

## Top bridge nodes
- [[Audit Ledger (SHA-256 hash only)]] - degree 7, connects to 3 communities
- [[HTTP CONNECT Proxy (domain allowlist)]] - degree 7, connects to 1 community
- [[PII Sanitizer (Presidio  regex)]] - degree 3, connects to 1 community
- [[ssh_proxy (approved hosts only)]] - degree 2, connects to 1 community
