---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "test_ptt_state.c"
location: "L5161"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_ptt_statec
---

# A multipart 'text' field (sendMessage via multipart) is scanned too.

## Connections
- [[.test_multipart_text_field_scanned_when_no_caption()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_ptt_statec