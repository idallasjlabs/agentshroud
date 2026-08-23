---
type: community
cohesion: 0.33
members: 6
---

# Tool Result Sanitizer (security)

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[ToolResultSanitizer._extract_dict_content]] - code - gateway/security/tool_result_sanitizer.py
- [[ToolResultSanitizer._extract_scannable_content]] - code - gateway/security/tool_result_sanitizer.py
- [[ToolResultSanitizer._get_sanitizer_for_tool]] - code - gateway/security/tool_result_sanitizer.py
- [[ToolResultSanitizer._log_redaction_audit]] - code - gateway/security/tool_result_sanitizer.py
- [[ToolResultSanitizer._reconstruct_result]] - code - gateway/security/tool_result_sanitizer.py
- [[ToolResultSanitizer.sanitize_tool_result]] - code - gateway/security/tool_result_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Tool_Result_Sanitizer_security
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]

## Top bridge nodes
- [[ToolResultSanitizer.sanitize_tool_result]] - degree 5, connects to 1 community
- [[ToolResultSanitizer._get_sanitizer_for_tool]] - degree 2, connects to 1 community