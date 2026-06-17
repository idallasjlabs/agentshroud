---
type: community
cohesion: 0.14
members: 16
---

# Module Group 279

**Cohesion:** 0.14 - loosely connected
**Members:** 16 nodes

## Members
- [[.__init__()_29]] - code - gateway/proxy/telegram_egress_notify.py
- [[._api_url()]] - code - gateway/proxy/telegram_egress_notify.py
- [[._send_request()]] - code - gateway/proxy/telegram_egress_notify.py
- [[._token_for()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.cleanup_expired()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.get_pending_count()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.handle_callback()]] - code - gateway/proxy/telegram_egress_notify.py
- [[.notifier()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[.notify_pending()]] - code - gateway/proxy/telegram_egress_notify.py
- [[EgressTelegramNotifier]] - code - gateway/proxy/telegram_egress_notify.py
- [[Process inline button callback. Returns action result.          Actions allow_1]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Remove pending requests older than max_age_seconds. Returns count removed.]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Return the Telegram bot token to use for a given agent_id.          If the agent]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send Telegram message with time-limited approvedeny buttons.          Buttons]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Send a request to Telegram Bot API (sync, run in executor).]] - rationale - gateway/proxy/telegram_egress_notify.py
- [[Sends Telegram inline keyboard notifications for egress approval.      Supports]] - rationale - gateway/proxy/telegram_egress_notify.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_279
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Module Group 328]]
- 5 edges to [[_COMMUNITY_Module Group 410]]
- 3 edges to [[_COMMUNITY_Module Group 145]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]

## Top bridge nodes
- [[EgressTelegramNotifier]] - degree 23, connects to 4 communities
- [[.notify_pending()]] - degree 4, connects to 1 community
- [[.notifier()]] - degree 2, connects to 1 community