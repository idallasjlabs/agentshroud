---
type: community
members: 11
---

# MiddlewareManager (11)

**Members:** 11 nodes

## Members
- [[dot-__post_init__()_9]] - code - gateway/security/memory_lifecycle.py
- [[dot-sanitize_content()]] - code - gateway/security/memory_lifecycle.py
- [[dot-scan_content_for_threats()]] - code - gateway/security/memory_lifecycle.py
- [[dot-test_threat_cleanup()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-validate_memory_write()]] - code - gateway/security/memory_lifecycle.py
- [[ContentThreat]] - code - gateway/security/memory_lifecycle.py
- [[Detected threat in memory file content.]] - rationale - gateway/security/memory_lifecycle.py
- [[Sanitize content by removingredacting threats.]] - rationale - gateway/security/memory_lifecycle.py
- [[Scan memory file content for security threats.]] - rationale - gateway/security/memory_lifecycle.py
- [[Test cleanup of old threat records.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Validate content before writing to memory file.]] - rationale - gateway/security/memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager_11
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_MiddlewareManager (6)]]
- 4 edges to [[_COMMUNITY_MiddlewareManager (8)]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (9)]]

## Top bridge nodes
- [[ContentThreat]] - degree 15, connects to 4 communities
- [[dot-validate_memory_write()]] - degree 5, connects to 2 communities
- [[dot-scan_content_for_threats()]] - degree 5, connects to 1 community
- [[dot-sanitize_content()]] - degree 4, connects to 1 community
- [[dot-test_threat_cleanup()]] - degree 3, connects to 1 community
