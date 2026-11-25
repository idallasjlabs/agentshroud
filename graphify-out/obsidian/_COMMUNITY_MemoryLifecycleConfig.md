---
type: community
members: 8
---

# MemoryLifecycleConfig

**Members:** 8 nodes

## Members
- [[dot-setup_method()_8]] - code - gateway/tests/test_memory_lifecycle.py
- [[Configuration for memory lifecycle management.]] - rationale - gateway/security/memory_config.py
- [[ContentThreatType]] - code - gateway/security/memory_lifecycle.py
- [[Enum_11]] - code
- [[MemoryLifecycleConfig]] - code - gateway/security/memory_config.py
- [[Set up test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Types of content threats detected in memory files.]] - rationale - gateway/security/memory_lifecycle.py
- [[memory_lifecycle.py]] - code - gateway/security/memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MemoryLifecycleConfig
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_memory_lifecycle.py]]
- 5 edges to [[_COMMUNITY_MemoryLifecycleManager]]
- 3 edges to [[_COMMUNITY_TestMemoryLifecycleManager]]
- 1 edge to [[_COMMUNITY_ContentThreat]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[MemoryLifecycleConfig]] - degree 10, connects to 5 communities
- [[memory_lifecycle.py]] - degree 10, connects to 5 communities
- [[ContentThreatType]] - degree 5, connects to 2 communities
- [[dot-setup_method()_8]] - degree 4, connects to 2 communities
