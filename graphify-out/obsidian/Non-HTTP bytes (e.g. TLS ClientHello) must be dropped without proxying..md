---
source_file: "gateway/tests/test_telegram_executor.py"
type: "rationale"
community: "test_telegram_executor.py"
location: "L46"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_telegram_executorpy
---

# Non-HTTP bytes (e.g. TLS ClientHello) must be dropped without proxying.

## Connections
- [[test_hermes_forwarder_drops_non_http()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_telegram_executorpy