---
type: community
cohesion: 1.00
members: 2
---

# openclaw/skills/i-chaos-engineering/SKILL.md

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_proxy_request_suppresses_duplicate_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notices should be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/openclaw/skills/i-chaos-engineering/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_proxy_request_suppresses_duplicate_starting_notice()]] - degree 4, connects to 3 communities