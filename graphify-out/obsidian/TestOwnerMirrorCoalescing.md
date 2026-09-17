---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "test_telegram_proxy_outbound.py"
location: "L4868"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_telegram_proxy_outboundpy
---

# TestOwnerMirrorCoalescing

## Connections
- [[.test_second_message_after_window_sends_again()]] - `method` [EXTRACTED]
- [[.test_two_messages_within_window_send_only_one_mirror()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker_1]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[_mirror_to_owner_if_collaborator must coalesce within the window.]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_telegram_proxy_outboundpy