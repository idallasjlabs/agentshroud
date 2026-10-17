---
type: community
members: 28
---

# Audit Ledger (SHA-256 hash only)

**Members:** 28 nodes

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
- [[MCP Proxy]] - concept - docs/architecture/system-architecture.md
- [[MCP Server Integration Guide]] - document - docs/api/integration-guide.md
- [[Op-Proxy (Credential Gateway)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[OpenAI API]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[PII Sanitizer (Presidio  regex)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Proxy Layer_1]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[Receive message  cron trigger]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[SSH Proxy]] - concept - docs/architecture/system-architecture.md
- [[Telegram Input (@agentshroud_bot)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[Web Proxy]] - concept - docs/architecture/system-architecture.md
- [[Web UI Input (localhost18790)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[agentshroud-config volume (openclaw.json)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[http_proxy.py (HTTP CONNECT 8181, domain allowlist)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[iMessage Input (imsg-ssh bridge)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[ledger.db (90-day retention)]] - concept - docs/diagrams/images/diagram-07-data-flow.svg
- [[mcp-config.yml]] - code - docs/data/schema-documentation.md
- [[mcp_proxy.py (MCP tool call gate)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[ssh_proxy (approved hosts only)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[web_proxy.py (domain allowlist engine)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit_Ledger_SHA-256_hash_only
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity]]
- 2 edges to [[_COMMUNITY_Layer-by-Layer Breakdown]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context)]]

## Top bridge nodes
- [[Audit Ledger (SHA-256 hash only)]] - degree 7, connects to 3 communities
- [[HTTP CONNECT Proxy (domain allowlist)]] - degree 7, connects to 1 community
- [[MCP Proxy]] - degree 4, connects to 1 community
- [[PII Sanitizer (Presidio  regex)]] - degree 3, connects to 1 community
- [[Op-Proxy (Credential Gateway)]] - degree 2, connects to 1 community
