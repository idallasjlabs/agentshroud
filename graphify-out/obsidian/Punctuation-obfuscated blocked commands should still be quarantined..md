---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ingest_api/main.py"
location: "L1430"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# Punctuation-obfuscated blocked commands should still be quarantined.

## Connections
- [[.test_blocked_command_with_punctuation_is_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ingest_api/mainpy