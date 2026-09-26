---
type: community
cohesion: 1.00
members: 2
---

# openclaw/skills/i-value-stream-mapping/SKILL.md

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_embedded_tool_call_json_is_removed_from_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[If tool-call JSON is embedded in prose, strip JSON block before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/openclaw/skills/i-value-stream-mapping/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_embedded_tool_call_json_is_removed_from_text()]] - degree 4, connects to 3 communities