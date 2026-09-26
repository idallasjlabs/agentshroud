---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: "test_trust_manager.py"
location: "L530"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_trust_managerpy
---

# Send a single Telegram notice per cooldown window when failover activates.

## Connections
- [[._emit_failover_notice()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_trust_managerpy