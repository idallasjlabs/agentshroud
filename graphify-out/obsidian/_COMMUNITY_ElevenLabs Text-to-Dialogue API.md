---
type: community
cohesion: 1.00
members: 2
---

# ElevenLabs Text-to-Dialogue API

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_outbound_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, owner messages should still go through.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ElevenLabs_Text-to-Dialogue_API
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_outbound_owner_exempt_from_fail_closed()]] - degree 4, connects to 3 communities