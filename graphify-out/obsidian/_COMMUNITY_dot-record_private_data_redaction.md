---
type: community
members: 4
---

# .record_private_data_redaction

**Members:** 4 nodes

## Members
- [[dot-record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[Record admin-private data redaction event for compliance audit.]] - rationale - gateway/proxy/mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/record_private_data_redaction
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_mcp_proxy.py]]

## Top bridge nodes
- [[PrivateRedactionEvent]] - degree 3, connects to 1 community
- [[dot-record_private_data_redaction()]] - degree 3, connects to 1 community
