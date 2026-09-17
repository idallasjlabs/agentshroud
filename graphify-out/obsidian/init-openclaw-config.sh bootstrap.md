---
source_file: "docker/scripts/init-openclaw-config.sh"
type: "code"
community: "TELEGRAM_API_BASE_URL"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TELEGRAM_API_BASE_URL
---

# init-openclaw-config.sh bootstrap

## Connections
- [[_reconcile_security_critical_cron]] - `references` [EXTRACTED]
- [[patch-anthropic-sdk.sh]] - `calls` [EXTRACTED]
- [[patch-telegram-sdk.sh]] - `calls` [EXTRACTED]
- [[start-agentshroud.sh (OpenClaw entrypoint)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TELEGRAM_API_BASE_URL