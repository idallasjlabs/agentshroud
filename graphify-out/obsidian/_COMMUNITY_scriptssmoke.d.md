---
type: community
members: 10
---

# scripts/smoke.d

**Members:** 10 nodes

## Members
- [[.test_blocked_entry_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_chain_entries_linked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_hash_chain_changes_on_append()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_hash_chain_genesis()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_hash_chain_valid()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_log_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_log_tool_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_redacted_flag()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tampered_chain_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestAuditTrail]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/smoked
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_PromptGuard Encoding Detection]]
- 3 edges to [[_COMMUNITY_Collaborator Prompt Safety]]
- 3 edges to [[_COMMUNITY_SOC Dashboard]]
- 1 edge to [[_COMMUNITY_Setup Docs]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]

## Top bridge nodes
- [[TestAuditTrail]] - degree 23, connects to 5 communities