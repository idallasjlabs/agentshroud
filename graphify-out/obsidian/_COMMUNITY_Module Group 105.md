---
type: community
cohesion: 0.14
members: 41
---

# Module Group 105

**Cohesion:** 0.14 - loosely connected
**Members:** 41 nodes

## Members
- [[76 Active Security Modules Across P0-P3 Tiers]] - rationale - CLAUDE.md
- [[76 Security Module Descriptions Table]] - document - README.md
- [[AgentShroud System Overview]] - document - docs/vault/00 - START HERE/System Overview.md
- [[AgentShroud Tool Risk YAML Example]] - document - examples/agentshroud-with-tool-risk.yaml
- [[AgentShroud User Guide v0.2.0]] - document - docs/user-guide.md
- [[AgentShroud Vault Home]] - document - docs/vault/00 - START HERE/Home.md
- [[Approval Queue (Human-in-the-Loop for Sensitive Actions)]] - concept - CLAUDE.md
- [[Auth Module (Bearer token + token-bucket rate limiter, hmac.compare_digest)]] - concept - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[Crash Recovery Options (5 levels)]] - concept - docs/vault/08 - Runbooks/Crash Recovery.md
- [[Crash Recovery Runbook]] - document - docs/vault/08 - Runbooks/Crash Recovery.md
- [[Data Flow — AgentShroud Gateway]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[DataLedger (SQLite WAL, SHA-256 hash chain, privacy-by-design — hashes only, 90-day retention)]] - concept - docs/vault/02 - Modules/Gateway Core/ledger.py.md
- [[Dependency Graph Diagram]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[EgressFilter (Network-level Outbound Control Module)]] - concept - CLAUDE.md
- [[EventBus (in-process pubsub, 200-event rolling buffer, auth failure escalation)]] - concept - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Full System Flowchart Diagram]] - document - docs/vault/09 - Diagrams/Full System Flowchart.md
- [[GSD (Get Shit Done) Issue Template Lightweight Production Approval Gate]] - document - .github/ISSUE_TEMPLATE/gsd.md
- [[Gateway Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway README]] - document - gateway/README.md
- [[Health Checks Runbook]] - document - docs/vault/08 - Runbooks/Health Checks.md
- [[MCP Proxy (tool call inspection layer)]] - concept - docs/SECURITY_PLAN.md
- [[MCP Proxy Config Example]] - document - examples/mcp-config.yml
- [[Monitor Mode (log-only, no enforcement)]] - concept - docs/vault/09 - Diagrams/Security Pipeline Flow.md
- [[PII Sanitizer (Microsoft Presidio, 0.9 Confidence Minimum)]] - concept - CLAUDE.md
- [[PromptGuard (Prompt Injection and Jailbreak Detection)]] - concept - CLAUDE.md
- [[Proxy Routing (MCP→mcp_proxy, LLM→llm_proxy, Telegram→telegram_proxy, HTTP→http_proxy, Web→web_proxy)]] - concept - docs/vault/01 - Architecture/Data Flow.md
- [[SOC Router (socv1 — 60+ endpoints for security, egress, users, groups, delegation, scanners)]] - concept - docs/vault/02 - Modules/Gateway Core/main.py.md
- [[Security Pipeline Flow Diagram]] - document - docs/vault/09 - Diagrams/Security Pipeline Flow.md
- [[Security Pipeline Layers (Auth → Middleware → Input Norm → PII → PromptGuard → Egress → Pipeline → Proxy → Ledger → Approval)]] - concept - docs/vault/00 - START HERE/System Overview.md
- [[SecurityPipeline (76-Module InboundOutbound Pipeline)]] - concept - CLAUDE.md
- [[Startup Errors]] - document - docs/vault/07 - Errors & Troubleshooting/Startup Errors.md
- [[Tool Risk Tiers (criticalhighmediumlow)]] - concept - examples/agentshroud-with-tool-risk.yaml
- [[Troubleshooting Matrix]] - document - docs/vault/07 - Errors & Troubleshooting/Troubleshooting Matrix.md
- [[TrustManager (Cryptographic Agent Identity Verification)]] - concept - CLAUDE.md
- [[auth.py — Gateway Core Module]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[event_bus.py — Gateway Core Module]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[httpx]] - document - docs/vault/05 - Dependencies/httpx.md
- [[ledger.py — Gateway Core Module]] - document - docs/vault/02 - Modules/Gateway Core/ledger.py.md
- [[llm_proxy.py_1]] - concept - docs/vault/05 - Dependencies/httpx.md
- [[main.py — FastAPI Entrypoint (5-step POST forward pipeline, 22 lifespan steps)]] - concept - docs/vault/02 - Modules/Gateway Core/main.py.md
- [[main.py — Gateway Core Module]] - document - docs/vault/02 - Modules/Gateway Core/main.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_105
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Module Group 138]]
- 11 edges to [[_COMMUNITY_Module Group 203]]
- 8 edges to [[_COMMUNITY_Module Group 369]]
- 7 edges to [[_COMMUNITY_Module Group 313]]
- 5 edges to [[_COMMUNITY_Module Group 174]]
- 3 edges to [[_COMMUNITY_Module Group 192]]
- 3 edges to [[_COMMUNITY_Module Group 188]]
- 2 edges to [[_COMMUNITY_Module Group 191]]
- 2 edges to [[_COMMUNITY_Module Group 172]]
- 2 edges to [[_COMMUNITY_Module Group 297]]
- 1 edge to [[_COMMUNITY_Module Group 450]]
- 1 edge to [[_COMMUNITY_Module Group 568]]
- 1 edge to [[_COMMUNITY_Module Group 158]]

## Top bridge nodes
- [[EgressFilter (Network-level Outbound Control Module)]] - degree 22, connects to 8 communities
- [[PII Sanitizer (Microsoft Presidio, 0.9 Confidence Minimum)]] - degree 26, connects to 6 communities
- [[Approval Queue (Human-in-the-Loop for Sensitive Actions)]] - degree 25, connects to 4 communities
- [[SecurityPipeline (76-Module InboundOutbound Pipeline)]] - degree 12, connects to 3 communities
- [[76 Security Module Descriptions Table]] - degree 8, connects to 3 communities