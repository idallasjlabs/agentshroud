---
type: community
members: 9
---

# TestOutboundInfoFilter (3)

**Members:** 9 nodes

## Members
- [[dot-test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
- [[Integration tests with other security components.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that outbound filter works alongside PII sanitizer.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test with realistic agent response patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[TestIntegration_1]] - code - gateway/tests/test_outbound_filter.py
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundInfoFilter_3
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_SecurityPipeline]]
- 2 edges to [[_COMMUNITY_TestOutboundInfoFilter (2)]]
- 2 edges to [[_COMMUNITY_TestOutboundInfoFilter]]

## Top bridge nodes
- [[InfoCategory]] - degree 9, connects to 3 communities
- [[test_outbound_filter.py]] - degree 5, connects to 3 communities
- [[TestIntegration_1]] - degree 6, connects to 1 community
- [[dot-test_real_world_agent_responses()]] - degree 3, connects to 1 community
- [[dot-test_with_pii_sanitizer_compatibility()]] - degree 3, connects to 1 community
