---
type: community
cohesion: 0.20
members: 10
---

# NetworkSecurityFinding

**Cohesion:** 0.20 - loosely connected
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
TABLE source_file, type FROM #community/NetworkSecurityFinding
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 3 edges to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_brand-guidelines]]
- 1 edge to [[_COMMUNITY_TestParanoidConfig]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.9.0 — Human Interface Testing Gui]]

## Top bridge nodes
- [[TestAuditTrail]] - degree 23, connects to 7 communities