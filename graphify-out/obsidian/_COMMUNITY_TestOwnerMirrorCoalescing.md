---
type: community
members: 6
---

# TestOwnerMirrorCoalescing

**Members:** 6 nodes

## Members
- [[dot-test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerMirrorCoalescing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake_admin_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake_admin_notice()_1]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_mirror_to_owner_if_collaborator must coalesce within the window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOwnerMirrorCoalescing
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY__make_sanitizer]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[TestOwnerMirrorCoalescing]] - degree 5, connects to 2 communities
- [[dot-test_second_message_after_window_sends_again()]] - degree 5, connects to 1 community
- [[dot-test_two_messages_within_window_send_only_one_mirror()]] - degree 4, connects to 1 community
