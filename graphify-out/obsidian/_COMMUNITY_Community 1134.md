---
type: community
cohesion: 0.33
members: 6
---

# Community 1134

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_collaborator_internal_network_probe_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_internal_network_probe_returns_protect_egress_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_obfuscated_command_probe_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Blocked internal-network probes should return deterministic Protect egress wordi]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Internal-network target probes should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Obfuscated decode+execute prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1134
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Telegram Proxy Inbound]]
- 3 edges to [[_COMMUNITY_Community 31]]

## Top bridge nodes
- [[.test_collaborator_internal_network_probe_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[.test_collaborator_internal_network_probe_returns_protect_egress_notice()]] - degree 8, connects to 2 communities
- [[.test_collaborator_obfuscated_command_probe_is_blocked_and_quarantined()]] - degree 7, connects to 2 communities