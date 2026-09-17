---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: ".proxy_messages()"
location: "L530"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/proxy_messages
---

# Send a single Telegram notice per cooldown window when failover activates.

## Connections
- [[._emit_failover_notice()]] - `rationale_for` [EXTRACTED]
- [[._emit_failover_notice()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/proxy_messages