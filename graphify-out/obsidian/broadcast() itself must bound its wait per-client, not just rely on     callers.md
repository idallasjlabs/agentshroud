---
source_file: "gateway/tests/test_enhanced_approval.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L545"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# broadcast() itself must bound its wait per-client, not just rely on     callers

## Connections
- [[test_broadcast_does_not_hang_forever_on_dead_client()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy