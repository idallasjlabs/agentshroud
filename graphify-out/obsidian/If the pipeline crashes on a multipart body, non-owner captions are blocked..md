---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "_make_multipart_body"
location: "L5099"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_multipart_body
---

# If the pipeline crashes on a multipart body, non-owner captions are blocked.

## Connections
- [[dot-test_multipart_fails_closed_for_non_owner()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_multipart_body
