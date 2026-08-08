---
source_file: "docs/vault/04 - Environment Variables/TELEGRAM_API_BASE_URL.md"
type: "document"
community: "docs/vault"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/docs/vault
---

# TELEGRAM_API_BASE_URL (env var — routes bot Telegram calls through gateway for PII scanning)

## Connections
- [[agentshroud-bot service (docker-compose port 18789, 4GB memory, isolated network)]] - `sets` [EXTRACTED]
- [[gateway service (docker-compose port 8080, read-only rootfs, 1280MB memory)]] - `routes_traffic_to` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/docs/vault