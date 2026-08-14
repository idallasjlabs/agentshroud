---
source_file: "docs/vault/02 - Modules/Gateway Core/main.py.md"
type: "document"
community: "Security Docs"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Security_Docs
---

# main.py — Gateway Core Module

## Connections
- [[AgentShroud Vault Home]] - `indexes` [EXTRACTED]
- [[Auth Module (Bearer token + token-bucket rate limiter, hmac.compare_digest)]] - `wires` [EXTRACTED]
- [[DataLedger (SQLite WAL, SHA-256 hash chain, privacy-by-design — hashes only, 90-day retention)]] - `wires` [EXTRACTED]
- [[EventBus (in-process pubsub, 200-event rolling buffer, auth failure escalation)]] - `wires` [EXTRACTED]
- [[Proxy Routing (MCP→mcp_proxy, LLM→llm_proxy, Telegram→telegram_proxy, HTTP→http_proxy, Web→web_proxy)]] - `implements` [EXTRACTED]
- [[SOC Router (socv1 — 60+ endpoints for security, egress, users, groups, delegation, scanners)]] - `references` [EXTRACTED]
- [[SSH Proxy Module (gatewayssh_proxyproxy.py)]] - `wires` [EXTRACTED]
- [[Security Pipeline Layers (Auth → Middleware → Input Norm → PII → PromptGuard → Egress → Pipeline → Proxy → Ledger → Approval)]] - `implements` [EXTRACTED]
- [[auth.py — Gateway Core Module]] - `used_by` [EXTRACTED]
- [[event_bus.py — Gateway Core Module]] - `used_by` [EXTRACTED]
- [[ledger.py — Gateway Core Module]] - `used_by` [EXTRACTED]
- [[main.py — FastAPI Entrypoint (5-step POST forward pipeline, 22 lifespan steps)]] - `documents` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Security_Docs