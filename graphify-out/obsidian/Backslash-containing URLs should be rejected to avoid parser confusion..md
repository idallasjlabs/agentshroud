---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "_make_sanitizer"
location: "L3172"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_sanitizer
---

# Backslash-containing URLs should be rejected to avoid parser confusion.

## Connections
- [[dot-test_raw_web_fetch_json_url_with_backslashes_does_not_queue_approval()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_sanitizer
