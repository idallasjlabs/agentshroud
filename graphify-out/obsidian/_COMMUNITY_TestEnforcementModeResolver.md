---
type: community
cohesion: 0.50
members: 4
---

# TestEnforcementModeResolver

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_owner_revoke_command_persists_pause_to_disk()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_owner_revoke_command_requires_target_user_id()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[revoke must persist through pause_collaborator() so the pause survives]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner revoke without target should return usage guidance.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEnforcementModeResolver
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]

## Top bridge nodes
- [[.test_owner_revoke_command_requires_target_user_id()]] - degree 8, connects to 2 communities
- [[.test_owner_revoke_command_persists_pause_to_disk()]] - degree 7, connects to 2 communities