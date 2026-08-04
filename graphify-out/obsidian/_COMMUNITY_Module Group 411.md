---
type: community
cohesion: 0.22
members: 9
---

# Module Group 411

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[.test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[.test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[.test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[Test enhanced status endpoint with observatory mode and egress info.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test status response in monitor mode.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that StatusResponse model accepts new fields.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that new fields are optional (backward compat).]] - rationale - gateway/tests/test_enhanced_status.py
- [[TestEnhancedStatus]] - code - gateway/tests/test_enhanced_status.py
- [[test_enhanced_status.py]] - code - gateway/tests/test_enhanced_status.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_411
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]

## Top bridge nodes
- [[TestEnhancedStatus]] - degree 6, connects to 1 community
- [[.test_status_response_model()]] - degree 3, connects to 1 community
- [[.test_status_response_monitor_mode()]] - degree 3, connects to 1 community
- [[.test_status_response_optional_fields()]] - degree 3, connects to 1 community
- [[test_enhanced_status.py]] - degree 2, connects to 1 community
