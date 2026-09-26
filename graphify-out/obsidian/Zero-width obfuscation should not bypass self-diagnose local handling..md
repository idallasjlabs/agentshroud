---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ingest_api/main.py"
location: "L5193"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# Zero-width obfuscation should not bypass self-diagnose local handling.

## Connections
- [[.test_self_diagnose_with_zero_width_char_is_handled_locally()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ingest_api/mainpy