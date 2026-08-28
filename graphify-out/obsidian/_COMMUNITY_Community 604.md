---
type: community
cohesion: 0.21
members: 15
---

# Community 604

**Cohesion:** 0.21 - loosely connected
**Members:** 15 nodes

## Members
- [[AgentShroud Development Roadmap — 2026 Gantt Chart]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Alert Thresholds (health check 3x10s, 200K token hard limit196K compaction trigger, 1h approval timeout, 90-day ledger retention, op-proxy 6 cascading retries)]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[Bot Session State Diagram (fresh → active → idlecompacting → reset)]] - image - docs/diagrams/images/diagram-17-state-bot-session.png
- [[Observability Gaps (future work) no centralised log aggregation (ELKLoki), no metrics export (Prometheus), no uptime monitor, Zabbix installed but not configured]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[Observability Map Diagram]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[OpenClaw auto-compaction (reserveTokensFloor=4000; triggers at ~196K of 200K tokens; hard overflow 200K after 3 failed retries → session reset)]] - concept - docs/diagrams/images/diagram-17-state-bot-session.png
- [[Phase 1 — Foundation Gateway API+Ledger, Bot Container+Telegram, HMAC Auth+PII Sanitizer]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 2 — Security Core HTTP CONNECT Proxy, MCP Proxy Inspector, Approval Queue, SSH Proxy]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 3 — Credential Isolation Op-Proxy, 1Password service account, cascading retry+startup]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 4 — Channels iMessage MCP integration, iCloud Email (replaces Gmail), Telegram startup notification]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 5 — Stability Context limit fix (Patch 4), MCP key crash fix (Patch 3), Documentation & Diagrams]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 6 — Observability (planned) Tailscale config & serve, Prometheus+Grafana, Log aggregation (Loki)]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 7 — Enterprise Hardening (planned) IEC 62443 policy docs, Multi-tenant isolation, External contributor access]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Runbook branch Context resets → check reserveTokensFloor setting]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[What Is Instrumented (bot apihealth, gateway status and ledger, MCP audit log, HTTP CONNECT proxy stats)]] - image - docs/diagrams/images/diagram-20-observability-map.png

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_604
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 376]]
- 5 edges to [[_COMMUNITY_Community 492]]
- 1 edge to [[_COMMUNITY_Community 554]]

## Top bridge nodes
- [[Phase 2 — Security Core HTTP CONNECT Proxy, MCP Proxy Inspector, Approval Queue, SSH Proxy]] - degree 6, connects to 2 communities
- [[Alert Thresholds (health check 3x10s, 200K token hard limit196K compaction trigger, 1h approval timeout, 90-day ledger retention, op-proxy 6 cascading retries)]] - degree 5, connects to 2 communities
- [[Phase 5 — Stability Context limit fix (Patch 4), MCP key crash fix (Patch 3), Documentation & Diagrams]] - degree 7, connects to 1 community
- [[Phase 3 — Credential Isolation Op-Proxy, 1Password service account, cascading retry+startup]] - degree 4, connects to 1 community
- [[Bot Session State Diagram (fresh → active → idlecompacting → reset)]] - degree 2, connects to 1 community