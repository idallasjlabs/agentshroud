---
type: community
members: 23
---

# EgressTelegramNotifier

**Members:** 23 nodes

## Members
- [[dot-__init__()_192]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-_api_url()]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-_async_send()]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-_send_request()]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-_token_for()]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-answer_callback()]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-cleanup_expired()_2]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-edit_decision_message()]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-get_pending_count()]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-handle_callback()_1]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-notify_pending()]] - code - gateway/proxy/telegram_egress_notify.py
- [[dot-send_text()]] - code - gateway/proxy/telegram_egress_notify.py
- [[Async wrapper around sync Telegram API call.]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[EgressTelegramNotifier]] - code - gateway/proxy/telegram_egress_notify.py
- [[Process inline button callback. Returns action result. Actions allow_1h,…]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Remove pending requests older than max_age_seconds. Returns count removed.]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Replace the inline keyboard approval message with a decision record. Removes…]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Return the Telegram bot token to use for a given agent_id. If the agent maps to…]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send Telegram message with time-limited approvedeny buttons. Buttons Allow 1h…]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send a plain text message — public transport for other gateway components (e.g.…]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send a request to Telegram Bot API (sync, run in executor).]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send answerCallbackQuery to dismiss the button loading state. Pass ``token``…]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Sends Telegram inline keyboard notifications for egress approval. Supports…]] - rationale - gateway/proxy/telegram_egress_notify.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressTelegramNotifier
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_egress_callback_stale.py]]
- 4 edges to [[_COMMUNITY_telegram_egress_notify.py]]
- 2 edges to [[_COMMUNITY_TestEgressTelegramNotify]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[EgressTelegramNotifier]] - degree 24, connects to 5 communities
- [[dot-answer_callback()]] - degree 4, connects to 1 community
- [[dot-edit_decision_message()]] - degree 4, connects to 1 community
