---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Every collaborator message must produce a response — never a silent drop."
location: "L7971"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
---

# A blocked slash command must always produce a protected notice.

## Connections
- [[dot-test_collaborator_blocked_command_always_gets_notice()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
