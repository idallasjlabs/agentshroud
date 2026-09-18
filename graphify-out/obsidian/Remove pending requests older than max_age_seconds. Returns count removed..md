---
source_file: "gateway/proxy/telegram_egress_notify.py"
type: "rationale"
community: "EgressTelegramNotifier"
location: "L333"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressTelegramNotifier
---

# Remove pending requests older than max_age_seconds. Returns count removed.

## Connections
- [[.cleanup_expired()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressTelegramNotifier