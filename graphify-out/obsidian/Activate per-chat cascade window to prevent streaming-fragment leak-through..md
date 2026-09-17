---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L725"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Activate per-chat cascade window to prevent streaming-fragment leak-through.

## Connections
- [[._set_outbound_block_cascade()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy