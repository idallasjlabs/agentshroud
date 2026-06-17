---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "Telegram Proxy Outbound Tests"
location: "L4856"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Outbound_Tests
---

# TestOwnerMirrorCoalescing

## Connections
- [[.test_second_message_after_window_sends_again()]] - `method` [EXTRACTED]
- [[.test_two_messages_within_window_send_only_one_mirror()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[_mirror_to_owner_if_collaborator must coalesce within the window.]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Proxy_Outbound_Tests