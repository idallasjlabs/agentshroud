---
type: community
cohesion: 1.00
members: 2
---

# _req

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[dot-test_form_outbound_pipeline_block_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked form payloads to non-owners must be replaced with a safe notice]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_req
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_GroupApprovalRouter]]

## Top bridge nodes
- [[dot-test_form_outbound_pipeline_block_non_owner()]] - degree 5, connects to 2 communities
