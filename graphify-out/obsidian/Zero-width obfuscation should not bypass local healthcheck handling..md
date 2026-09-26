---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ingest_api/main.py"
location: "L4801"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# Zero-width obfuscation should not bypass local healthcheck handling.

## Connections
- [[.test_healthcheck_with_zero_width_char_is_handled_locally()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ingest_api/mainpy