---
type: community
members: 17
---

# TestAuditTrail

**Members:** 17 nodes

## Members
- [[dot-test_blocked_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_blocked_entry_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_chain_entries_linked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_failed_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_agent()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_server()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_tool()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_generate_report()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_hash_chain_changes_on_append()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_hash_chain_genesis()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_hash_chain_valid()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_log_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_log_tool_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_redacted_flag()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tampered_chain_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestAuditQueries]] - code - gateway/tests/test_mcp_proxy.py
- [[TestAuditTrail_1]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAuditTrail
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_mcp_proxy.py]]

## Top bridge nodes
- [[TestAuditTrail_1]] - degree 10, connects to 1 community
- [[TestAuditQueries]] - degree 7, connects to 1 community
