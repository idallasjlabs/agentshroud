---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "_wrap_response()"
location: "L5712"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# Malformed callback payloads should not crash inbound processing.

## Connections
- [[dot-test_egress_callback_non_dict_result_is_handled()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response
