---
type: community
members: 12
---

# ._is_domain_allowed

**Members:** 12 nodes

## Members
- [[dot-_domain_matches_pattern()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_is_domain_allowed()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_is_internal_link()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_url_has_blocked_patterns()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-sanitize_images()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if URL contains any blocked patterns.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if a URL's domain is in the allowlist.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if domain matches pattern (supports wildcards).]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if this is an internal link (relative, anchor, etc.).]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Remove or warn about markdown images pointing to non-allowlisted domains.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[replace_image()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[replace_link()]] - code - gateway/security/tool_result_sanitizer_enhanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_is_domain_allowed
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_ToolResultSanitizer]]

## Top bridge nodes
- [[dot-_is_domain_allowed()]] - degree 5, connects to 1 community
- [[dot-_is_internal_link()]] - degree 4, connects to 1 community
- [[dot-sanitize_images()]] - degree 4, connects to 1 community
- [[replace_link()]] - degree 4, connects to 1 community
- [[dot-_url_has_blocked_patterns()]] - degree 4, connects to 1 community
