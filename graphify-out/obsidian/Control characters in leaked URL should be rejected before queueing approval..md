---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "_make_sanitizer"
location: "L3139"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_sanitizer
---

# Control characters in leaked URL should be rejected before queueing approval.

## Connections
- [[dot-test_raw_web_fetch_json_url_with_control_character_does_not_queue_approval()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_sanitizer
