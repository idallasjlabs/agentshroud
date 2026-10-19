---
type: community
members: 18
---

# ToolResultSanitizer (2)

**Members:** 18 nodes

## Members
- [[dot-__init__()_167]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_extract_dict_content()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_extract_scannable_content()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_get_sanitizer_for_tool()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_log_redaction_audit()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-_reconstruct_result()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-get_config_for_tool()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-get_tool_config()]] - code - gateway/security/tool_result_sanitizer.py
- [[dot-sanitize_tool_result()]] - code - gateway/security/tool_result_sanitizer.py
- [[Any_61]] - code - gateway/security/tool_result_sanitizer.py
- [[Extract text content from various tool result formats for PII scanning]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get PII config for a specific tool, applying overrides if configured]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get or create a PIISanitizer instance for the specified tool]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Get the PII configuration for a specific tool]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Log PII redaction for audit trail without logging actual PII]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Reconstruct the tool result with sanitized content]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Recursively extract string content from dictionary]] - rationale - gateway/security/tool_result_sanitizer.py
- [[Sanitize a tool result for PII before it reaches the agent          Args]] - rationale - gateway/security/tool_result_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolResultSanitizer_2
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 7 edges to [[_COMMUNITY_ApprovalQueueConfig]]

## Top bridge nodes
- [[Any_61]] - degree 8, connects to 2 communities
- [[dot-sanitize_tool_result()]] - degree 8, connects to 2 communities
- [[dot-get_config_for_tool()]] - degree 5, connects to 2 communities
- [[dot-_get_sanitizer_for_tool()]] - degree 5, connects to 2 communities
- [[dot-get_tool_config()]] - degree 4, connects to 2 communities
