---
type: community
members: 35
---

# AgentShroud Development Roadmap — 2026 Gantt Chart

**Members:** 35 nodes

## Members
- [[1Password Cloud]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]] - concept - docs/diagrams/images/diagram-12-credential-flow.png
- [[Agent Decision Logic Flowchart]] - image - docs/diagrams/images/diagram-14-logic-flow.png
- [[Agent routing (bindings config; e.g. Telegram ID 8096968754 → main agent)]] - image - docs/diagrams/images/diagram-14-logic-flow.png
- [[AgentShroud Development Roadmap — 2026 Gantt Chart]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Alert Thresholds (health check 3x10s, 200K token hard limit196K compaction trigger, 1h approval timeout, 90-day ledger retention, op-proxy 6 cascading retries)]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[Approval Queue (human-in-the-loop)_1]] - concept - docs/papers/agentshroud-whitepaper.md
- [[Approval Queue State Diagram (pending → approvedrejectedexpired)]] - image - docs/diagrams/images/diagram-16-state-approval-queue.png
- [[Bot Environment (secrets live only in container memory as env vars; never written to disk, never logged)]] - image - docs/diagrams/images/diagram-12-credential-flow.png
- [[Bot Session State Diagram (fresh → active → idlecompacting → reset)]] - image - docs/diagrams/images/diagram-17-state-bot-session.png
- [[Credential Flow Sequence Diagram (1Password op-proxy)]] - image - docs/diagrams/images/diagram-12-credential-flow.png
- [[Current Status_6]] - document - docs/flows/README.md
- [[Flows Documentation]] - document - docs/flows/README.md
- [[Incident Response Severity Flowchart]] - image - docs/diagrams/images/diagram-19-incident-response.png
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - concept - docs/diagrams/images/diagram-14-logic-flow.png
- [[Observability Gaps (future work) no centralised log aggregation (ELKLoki), no metrics export (Prometheus), no uptime monitor, Zabbix installed but not configured]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[Observability Map Diagram]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[OpenClaw auto-compaction (reserveTokensFloor=4000; triggers at ~196K of 200K tokens; hard overflow 200K after 3 failed retries → session reset)]] - concept - docs/diagrams/images/diagram-17-state-bot-session.png
- [[Peer binding Telegram 8096968754 → agentmain]] - image - docs/diagrams/images/diagram-15-sequence-telegram.png
- [[Phase 1 — Foundation Gateway API+Ledger, Bot Container+Telegram, HMAC Auth+PII Sanitizer]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 2 — Security Core HTTP CONNECT Proxy, MCP Proxy Inspector, Approval Queue, SSH Proxy]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 3 — Credential Isolation Op-Proxy, 1Password service account, cascading retry+startup]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 4 — Channels iMessage MCP integration, iCloud Email (replaces Gmail), Telegram startup notification]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 5 — Stability Context limit fix (Patch 4), MCP key crash fix (Patch 3), Documentation & Diagrams]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 6 — Observability (planned) Tailscale config & serve, Prometheus+Grafana, Log aggregation (Loki)]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Phase 7 — Enterprise Hardening (planned) IEC 62443 policy docs, Multi-tenant isolation, External contributor access]] - image - docs/diagrams/images/diagram-23-roadmap-gantt.png
- [[Planned Documents_5]] - document - docs/flows/README.md
- [[Runbook branch Container crash loop → docker logs → config invalid  op-proxy failed  OOM  Node.js error]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[Runbook branch Context resets → check reserveTokensFloor setting]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[Runbook branch Security alert → review blocked_domainHIGH threat entries → legitimate action allowlist vs kill switch]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[Severity matrix P1 Critical  P2 High  P3 Medium  P4 Low, with owners and response windows]] - image - docs/diagrams/images/diagram-19-incident-response.png
- [[Telegram Message Sequence Diagram]] - image - docs/diagrams/images/diagram-15-sequence-telegram.png
- [[Troubleshooting Runbook Decision Tree]] - image - docs/diagrams/images/diagram-18-runbook.png
- [[What Is Instrumented (bot apihealth, gateway status and ledger, MCP audit log, HTTP CONNECT proxy stats)]] - image - docs/diagrams/images/diagram-20-observability-map.png
- [[flowsREADME]] - document - docs/flows/README.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Development_Roadmap__2026_Gantt_Chart
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]]
- 6 edges to [[_COMMUNITY_Approval Queue (human-in-the-loop)]]
- 2 edges to [[_COMMUNITY_AgentShroud v0.7.0 Enforcement Audit Results]]
- 1 edge to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s) (2)]]
- 1 edge to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s) (3)]]

## Top bridge nodes
- [[Approval Queue (human-in-the-loop)_1]] - degree 10, connects to 2 communities
- [[Telegram Message Sequence Diagram]] - degree 7, connects to 2 communities
- [[1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]] - degree 11, connects to 1 community
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - degree 8, connects to 1 community
- [[Phase 2 — Security Core HTTP CONNECT Proxy, MCP Proxy Inspector, Approval Queue, SSH Proxy]] - degree 6, connects to 1 community
