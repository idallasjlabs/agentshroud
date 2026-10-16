---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "._filter_outbound"
location: "L725"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_filter_outbound
---

# Activate per-chat cascade window to prevent streaming-fragment leak-through.

## Connections
- [[dot-_set_outbound_block_cascade()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_filter_outbound
