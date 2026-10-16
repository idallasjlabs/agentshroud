---
type: community
cohesion: 0.50
members: 4
---

# .test_owner_deny_without_target_auto_selects_single_pending

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-test_owner_deny_ambiguous_multiple_pending_shows_usage()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_owner_deny_without_target_auto_selects_single_pending()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner deny with one pending request should deny that request.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner deny without target, with 2+ pending collaborator         requests, is ge]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_owner_deny_without_target_auto_selects_single_pending
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY__wrap_response]]

## Top bridge nodes
- [[dot-test_owner_deny_without_target_auto_selects_single_pending()]] - degree 8, connects to 2 communities
- [[dot-test_owner_deny_ambiguous_multiple_pending_shows_usage()]] - degree 7, connects to 2 communities
