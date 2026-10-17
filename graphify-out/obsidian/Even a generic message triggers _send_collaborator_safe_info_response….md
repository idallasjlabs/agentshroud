---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Every collaborator message must produce a response — never a silent drop."
location: "L7950"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
---

# Even a generic message triggers _send_collaborator_safe_info_response…

## Connections
- [[dot-test_collaborator_always_gets_response_for_generic_message()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
