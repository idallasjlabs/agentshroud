---
type: community
cohesion: 0.11
members: 24
---

# Community 363

**Cohesion:** 0.11 - loosely connected
**Members:** 24 nodes

## Members
- [[.__init__()_37]] - code - gateway/proxy/telegram_egress_notify.py
- [[._api_url()]] - code - gateway/proxy/telegram_egress_notify.py
- [[._async_send()]] - code - gateway/proxy/telegram_egress_notify.py
- [[._send_request()]] - code - gateway/proxy/telegram_egress_notify.py
- [[._token_for()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.answer_callback()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.cleanup_expired()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.edit_decision_message()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.get_pending_count()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.handle_callback()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.notify_pending()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.send_text()]] - code - gateway/proxy/telegram_egress_notify.py
- [[Async wrapper around sync Telegram API call.]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[EgressTelegramNotifier]] - code - gateway/proxy/telegram_egress_notify.py
- [[Process inline button callback. Returns action result.          Actions allow_1]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Remove pending requests older than max_age_seconds. Returns count removed.]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Replace the inline keyboard approval message with a decision record.          Re]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Return the Telegram bot token to use for a given agent_id.          If the agent]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send Telegram message with time-limited approvedeny buttons.          Buttons]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send a plain text message — public transport for other gateway         component]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send a request to Telegram Bot API (sync, run in executor).]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send answerCallbackQuery to dismiss the button loading state.          Pass ``to]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Sends Telegram inline keyboard notifications for egress approval.      Supports]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Telegram callback_query TTL expiry logged at DEBUG not ERROR]] - rationale - gateway/tests/test_egress_callback_stale.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_363
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 916]]
- 3 edges to [[_COMMUNITY_Community 1095]]
- 3 edges to [[_COMMUNITY_Community 209]]
- 2 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]

## Top bridge nodes
- [[EgressTelegramNotifier]] - degree 25, connects to 4 communities
- [[.answer_callback()]] - degree 4, connects to 1 community
- [[.edit_decision_message()]] - degree 4, connects to 1 community