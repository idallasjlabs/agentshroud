---
source_file: "docs/vault/01 - Architecture/Data Flow.md"
type: "document"
community: "docs/vault"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/docs/vault
---

# Data Flow — AgentShroud Gateway

## Connections
- [[AgentShroud Vault Home]] - `links_to` [EXTRACTED]
- [[Auth Module (Bearer token + token-bucket rate limiter, hmac.compare_digest)]] - `traces` [EXTRACTED]
- [[DataLedger (SQLite WAL, SHA-256 hash chain, privacy-by-design — hashes only, 90-day retention)]] - `traces` [EXTRACTED]
- [[MCP Proxy Wrapper (mcp-proxy-wrapper.js — stdio to HTTP translation)]] - `traces` [EXTRACTED]
- [[Proxy Routing (MCP→mcp_proxy, LLM→llm_proxy, Telegram→telegram_proxy, HTTP→http_proxy, Web→web_proxy)]] - `traces` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/docs/vault