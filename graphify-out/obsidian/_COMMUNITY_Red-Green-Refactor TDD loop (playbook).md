---
type: community
cohesion: 1.00
members: 2
---

# Red-Green-Refactor TDD loop (playbook)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound markdown exfil links should be stripped before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Red-Green-Refactor_TDD_loop_playbook
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_markdown_exfil_link_scrubbed()]] - degree 4, connects to 3 communities