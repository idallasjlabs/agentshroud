---
source_file: "gateway/tests/test_session_isolation.py"
type: "rationale"
community: "Webhook Receiver"
location: "L468"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Webhook_Receiver
---

# Input normalization should strip zero-width obfuscation before guards run.

## Connections
- [[.test_middleware_normalizes_invisible_unicode()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Webhook_Receiver