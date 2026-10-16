---
type: community
cohesion: 0.50
members: 4
---

# ToolResultSanitizer

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-_domain_matches_pattern()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_is_domain_allowed()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if a URL's domain is in the allowlist.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if domain matches pattern (supports wildcards).]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolResultSanitizer
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ToolResultSanitizer_3]]

## Top bridge nodes
- [[dot-_domain_matches_pattern()]] - degree 3, connects to 1 community
- [[dot-_is_domain_allowed()]] - degree 3, connects to 1 community
