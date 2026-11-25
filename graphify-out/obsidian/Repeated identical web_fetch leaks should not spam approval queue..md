---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "_make_sanitizer"
location: "L2657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_sanitizer
---

# Repeated identical web_fetch leaks should not spam approval queue.

## Connections
- [[dot-test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_sanitizer
