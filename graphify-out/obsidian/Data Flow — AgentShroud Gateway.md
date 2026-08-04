---
source_file: "docs/vault/01 - Architecture/Data Flow.md"
type: "document"
community: "Module Group 105"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Module_Group_105
---

# Data Flow — AgentShroud Gateway

## Connections
- [[AgentShroud Vault Home]] - `links_to` [EXTRACTED]
- [[Approval Queue (Human-in-the-Loop for Sensitive Actions)]] - `traces` [EXTRACTED]
- [[Auth Module (Bearer token + token-bucket rate limiter, hmac.compare_digest)]] - `traces` [EXTRACTED]
- [[DataLedger (SQLite WAL, SHA-256 hash chain, privacy-by-design — hashes only, 90-day retention)]] - `traces` [EXTRACTED]
- [[EgressFilter (Network-level Outbound Control Module)]] - `traces` [EXTRACTED]
- [[MCP Proxy Wrapper (mcp-proxy-wrapper.js — stdio to HTTP translation)]] - `traces` [EXTRACTED]
- [[PII Sanitizer (Microsoft Presidio, 0.9 Confidence Minimum)]] - `traces` [EXTRACTED]
- [[Proxy Routing (MCP→mcp_proxy, LLM→llm_proxy, Telegram→telegram_proxy, HTTP→http_proxy, Web→web_proxy)]] - `traces` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Module_Group_105
