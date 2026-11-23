---
type: community
members: 34
---

# Approval Queue (human-in-the-loop)

**Members:** 34 nodes

## Members
- [[Agent Decision Logic Flowchart]] - image - docs/diagrams/images/diagram-14-logic-flow.png
- [[Agent routing (bindings config; e.g. Telegram ID 8096968754 → main agent)]] - image - docs/diagrams/images/diagram-14-logic-flow.png
- [[AgentShroud Data Assets Mind Map (data dictionary; mostly illegible black-on-black render)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[AgentShroud Development Roadmap — 2026 Gantt Chart]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Alert Thresholds (health check 3x10s, 200K token hard limit196K compaction trigger, 1h approval timeout, 90-day ledger retention, op-proxy 6 cascading retries)]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[Approval Queue (human-in-the-loop)_1]] - concept - docs/papers/agentshroud-whitepaper.md
- [[Approval Queue State Diagram (pending → approvedrejectedexpired)]] - image - docs/diagrams/images/diagram-16-state-approval-queue.png
- [[Approval queue data (in-memory, backed by SQLite)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[Bot Session State Diagram (fresh → active → idlecompacting → reset)]] - image - docs/diagrams/images/diagram-17-state-bot-session.png
- [[Data Lineage Diagram (5-Layer Pipeline)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[EphemeralTransient data (never persisted raw)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[Layer 1 — Source (TelegramiMessageCron)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[Layer 4 — Processing (Bot LLM API call, MCP-inspected tool call)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[Layer 5 — Consumption (auto-delete at expires_at, audit query, user response)]] - image - docs/diagrams/images/diagram-09-data-lineage.png
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - concept - docs/diagrams/images/diagram-14-logic-flow.png
- [[MCP inspection result (in-memory only, logged to gateway stdout)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[Observability Gaps (future work) no centralised log aggregation (ELKLoki), no metrics export (Prometheus), no uptime monitor, Zabbix installed but not configured]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[Observability Map Diagram]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[OpenClaw auto-compaction (reserveTokensFloor=4000; triggers at ~196K of 200K tokens; hard overflow 200K after 3 failed retries → session reset)]] - concept - docs/diagrams/images/diagram-17-state-bot-session.png
- [[PII Redaction (Presidio-style pattern matching PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png
- [[PII redaction result (hash only in ledger, never persisted raw)]] - image - docs/diagrams/images/diagram-10-data-dictionary.png
- [[Peer binding Telegram 8096968754 → agentmain]] - image - docs/diagrams/images/diagram-15-sequence-telegram.png
- [[Phase 1 — Foundation Gateway API+Ledger, Bot Container+Telegram, HMAC Auth+PII Sanitizer]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 2 — Security Core HTTP CONNECT Proxy, MCP Proxy Inspector, Approval Queue, SSH Proxy]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 3 — Credential Isolation Op-Proxy, 1Password service account, cascading retry+startup]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 4 — Channels iMessage MCP integration, iCloud Email (replaces Gmail), Telegram startup notification]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 5 — Stability Context limit fix (Patch 4), MCP key crash fix (Patch 3), Documentation & Diagrams]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 6 — Observability (planned) Tailscale config & serve, Prometheus+Grafana, Log aggregation (Loki)]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 7 — Enterprise Hardening (planned) IEC 62443 policy docs, Multi-tenant isolation, External contributor access]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Runbook branch Context resets → check reserveTokensFloor setting]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[SHA-256 content hashing (original_content_hash + sanitized content_hash)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png
- [[Telegram Message Sequence Diagram]] - image - docs/diagrams/images/diagram-15-sequence-telegram.png
- [[What Is Instrumented (bot apihealth, gateway status and ledger, MCP audit log, HTTP CONNECT proxy stats)]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - concept - docs/diagrams/images/diagram-09-data-lineage.png

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Approval_Queue_human-in-the-loop
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]]
- 2 edges to [[_COMMUNITY_AgentShroud v0.7.0 Enforcement Audit Results]]
- 1 edge to [[_COMMUNITY_AgentShroud Data Assets (root)]]

## Top bridge nodes
- [[Approval Queue (human-in-the-loop)_1]] - degree 10, connects to 2 communities
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - degree 8, connects to 1 community
- [[Phase 5 — Stability Context limit fix (Patch 4), MCP key crash fix (Patch 3), Documentation & Diagrams]] - degree 7, connects to 1 community
- [[Telegram Message Sequence Diagram]] - degree 6, connects to 1 community
- [[Phase 2 — Security Core HTTP CONNECT Proxy, MCP Proxy Inspector, Approval Queue, SSH Proxy]] - degree 6, connects to 1 community
