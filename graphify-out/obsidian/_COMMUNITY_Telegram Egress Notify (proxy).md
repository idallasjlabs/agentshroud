---
type: community
cohesion: 0.60
members: 6
---

# Telegram Egress Notify (proxy)

**Cohesion:** 0.60 - moderately connected
**Members:** 6 nodes

## Members
- [[BaseException_1]] - code - gateway/proxy/telegram_egress_notify.py
- [[_err_text()]] - code - gateway/proxy/telegram_egress_notify.py
- [[_is_stale_callback_error()]] - code - gateway/proxy/telegram_egress_notify.py
- [[_is_stale_edit_error()]] - code - gateway/proxy/telegram_egress_notify.py
- [[telegram_egress_notify.py]] - code - gateway/proxy/telegram_egress_notify.py
- [[urllib HTTPError carries the response body on .read(); fall back to str.]] - rationale - gateway/proxy/telegram_egress_notify.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Telegram_Egress_Notify_proxy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Egress Callback Stale]]
- 3 edges to [[_COMMUNITY_Telegram Egress Notify (proxy)]]

## Top bridge nodes
- [[_is_stale_callback_error()]] - degree 6, connects to 2 communities
- [[_is_stale_edit_error()]] - degree 6, connects to 2 communities
- [[telegram_egress_notify.py]] - degree 4, connects to 1 community