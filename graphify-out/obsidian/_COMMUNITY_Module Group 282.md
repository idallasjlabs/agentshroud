---
type: community
cohesion: 0.17
members: 16
---

# Module Group 282

**Cohesion:** 0.17 - loosely connected
**Members:** 16 nodes

## Members
- [[._classify_response_risk()]] - code - gateway/security/outbound_filter.py
- [[._is_allowed_for_trust()]] - code - gateway/security/outbound_filter.py
- [[.filter_response()]] - code - gateway/security/outbound_filter.py
- [[A single match found by the outbound filter.]] - rationale - gateway/security/outbound_filter.py
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[Check if a disclosure category is permitted for the user's trust level.]] - rationale - gateway/security/outbound_filter.py
- [[Classify the risk level of a response based on info disclosure density.]] - rationale - gateway/security/outbound_filter.py
- [[Filter agent response for sensitive information disclosure.          Args]] - rationale - gateway/security/outbound_filter.py
- [[FilterMatch]] - code - gateway/security/outbound_filter.py
- [[FilterResult]] - code - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
- [[Integration tests with other security components.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Result of filtering agent response content.]] - rationale - gateway/security/outbound_filter.py
- [[TestIntegration]] - code - gateway/tests/test_outbound_filter.py
- [[outbound_filter.py]] - code - gateway/security/outbound_filter.py
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_282
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Module Group 198]]
- 3 edges to [[_COMMUNITY_Module Group 181]]
- 3 edges to [[_COMMUNITY_Module Group 81]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]

## Top bridge nodes
- [[InfoCategory]] - degree 9, connects to 4 communities
- [[outbound_filter.py]] - degree 7, connects to 4 communities
- [[test_outbound_filter.py]] - degree 6, connects to 3 communities
- [[FilterMatch]] - degree 8, connects to 2 communities
- [[TestIntegration]] - degree 7, connects to 1 community