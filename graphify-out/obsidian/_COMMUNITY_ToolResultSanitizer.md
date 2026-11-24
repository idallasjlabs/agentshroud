---
type: community
members: 14
---

# ToolResultSanitizer

**Members:** 14 nodes

## Members
- [[dot-__init__()_21]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_extract_code_blocks()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_restore_code_blocks()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-sanitize()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-sanitize_links()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-test_warn_mode()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Enhanced markdown sanitizer with configurable domain allowlist.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Extract code blocks to preserve them during sanitization.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Remove or warn about markdown links pointing to non-allowlisted domains.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Restore code blocks after sanitization.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Sanitize tool result content by filtering markdown links and images. Args…]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Test warn mode that marks but preserves external content.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[ToolResultSanitizer]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[replace_code_block()]] - code - gateway/security/tool_result_sanitizer_enhanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolResultSanitizer
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_ToolResultSanitizerConfig]]
- 7 edges to [[_COMMUNITY_dot-_is_domain_allowed]]
- 2 edges to [[_COMMUNITY_TestToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_dot-setup_method]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[ToolResultSanitizer]] - degree 22, connects to 6 communities
- [[dot-test_warn_mode()]] - degree 4, connects to 2 communities
- [[dot-sanitize()]] - degree 6, connects to 1 community
- [[dot-sanitize_links()]] - degree 4, connects to 1 community
- [[dot-__init__()_21]] - degree 2, connects to 1 community
