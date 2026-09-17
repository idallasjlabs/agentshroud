---
type: community
cohesion: 0.50
members: 4
---

# Community 1411

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-test_owner_deny_ambiguous_multiple_pending_shows_usage()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_owner_deny_without_target_auto_selects_single_pending()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner deny with one pending request should deny that request.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner deny without target, with 2+ pending collaborator         requests, is ge]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1411
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Telegram Proxy Inbound Tests]]
- 2 edges to [[_COMMUNITY_Telegram Lockdown & Collaborator UX Tests]]

## Top bridge nodes
- [[dot-test_owner_deny_without_target_auto_selects_single_pending()]] - degree 8, connects to 2 communities
- [[dot-test_owner_deny_ambiguous_multiple_pending_shows_usage()]] - degree 7, connects to 2 communities