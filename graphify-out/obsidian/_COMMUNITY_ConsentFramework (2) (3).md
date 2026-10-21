---
type: community
members: 4
---

# ConsentFramework (2) (3)

**Members:** 4 nodes

## Members
- [[dot-get_private_redaction_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConsentFramework_2_3
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_CrossBotTrustLedger]]

## Top bridge nodes
- [[dot-get_private_redaction_events()]] - degree 3, connects to 1 community
- [[dot-get_private_redaction_summary()]] - degree 3, connects to 1 community
