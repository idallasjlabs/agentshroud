---
type: community
cohesion: 0.50
members: 4
---

# Community 1366

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_collaborator_encoded_exfil_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_plugin_discovery_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Encoded exfiltration prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Plugintool auto-discovery inventory prompts should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1366
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Telegram Proxy Inbound]]
- 2 edges to [[_COMMUNITY_Community 31]]

## Top bridge nodes
- [[.test_collaborator_plugin_discovery_request_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[.test_collaborator_encoded_exfil_request_is_blocked_and_quarantined()]] - degree 7, connects to 2 communities