---
type: community
cohesion: 1.00
members: 2
---

# sunday-upgrade-report.sh

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_block_cascade_blocks_followup_fragment()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[A blocked fragment should cascade-block immediate follow-up chunks.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/sunday-upgrade-reportsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_block_cascade_blocks_followup_fragment()]] - degree 4, connects to 3 communities