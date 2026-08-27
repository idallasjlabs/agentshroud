---
type: community
members: 8
---

# Community 1012

**Members:** 8 nodes

## Members
- [[.test_clean_result_passes_through()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_credit_card_detected()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_credit_card_redacted()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_email_detected_but_low_threat()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_in_tool_result_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_ssn_detected_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_ssn_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPIIDetection]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1012
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 36]]
- 3 edges to [[_COMMUNITY_Community 106]]
- 1 edge to [[_COMMUNITY_Community 201]]
- 1 edge to [[_COMMUNITY_Community 179]]
- 1 edge to [[_COMMUNITY_Community 283]]

## Top bridge nodes
- [[TestPIIDetection]] - degree 21, connects to 5 communities