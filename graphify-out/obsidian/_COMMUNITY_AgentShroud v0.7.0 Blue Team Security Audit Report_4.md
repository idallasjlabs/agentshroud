---
type: community
cohesion: 0.33
members: 6
---

# AgentShroud v0.7.0 Blue Team Security Audit Report

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_custom_config()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_default_config()_1]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test ToolResultSanitizerConfig.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test custom configuration.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test default configuration values.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[TestToolResultSanitizerConfig]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_v070_Blue_Team_Security_Audit_Report
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TestSSRFDetection_2]]
- 1 edge to [[_COMMUNITY_ForwardRequest_1]]
- 1 edge to [[_COMMUNITY_egress_filter.py_1]]

## Top bridge nodes
- [[TestToolResultSanitizerConfig]] - degree 6, connects to 2 communities
- [[dot-test_custom_config()]] - degree 3, connects to 1 community
- [[dot-test_default_config()_1]] - degree 3, connects to 1 community
- [[Test ToolResultSanitizerConfig.]] - degree 2, connects to 1 community
