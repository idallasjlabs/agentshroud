---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L2573"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Detect patterns that must redact for ALL non-owner chats, including full_access.

## Connections
- [[._contains_critical_collaborator_leakage()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy