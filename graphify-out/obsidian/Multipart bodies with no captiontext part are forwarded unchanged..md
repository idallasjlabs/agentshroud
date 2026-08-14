---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "SECURITY.md"
location: "L5151"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SECURITYmd
---

# Multipart bodies with no caption/text part are forwarded unchanged.

## Connections
- [[.test_multipart_without_text_part_passes_through()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SECURITYmd