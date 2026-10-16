---
type: community
cohesion: 0.09
members: 38
---

# MiddlewareManager

**Cohesion:** 0.09 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-__post_init__()_1]] - code - gateway/security/memory_lifecycle.py
- [[dot-setup_method()_13]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-setup_method()_14]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-teardown_method()_6]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_content_sanitization()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_daily_notes_retention()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_lifecycle_maintenance()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_memory_md_size_limit()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_pii_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_prompt_injection_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_status_reporting()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_threat_cleanup()]] - code - gateway/tests/test_memory_lifecycle.py
- [[Clean up integration test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Configuration for memory lifecycle management.]] - rationale - gateway/security/memory_config.py
- [[ContentThreat]] - code - gateway/security/memory_lifecycle.py
- [[ContentThreatType]] - code - gateway/security/memory_lifecycle.py
- [[Detected threat in memory file content.]] - rationale - gateway/security/memory_lifecycle.py
- [[Manages memory file lifecycle and content security.]] - rationale - gateway/security/memory_lifecycle.py
- [[MemoryLifecycleConfig]] - code - gateway/security/memory_config.py
- [[MemoryLifecycleManager]] - code - gateway/security/memory_lifecycle.py
- [[Set up integration test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test MEMORY.md size limit enforcement.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test PII detection in memory content.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test cleanup of old threat records.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test complete lifecycle maintenance run.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test content sanitization removes threats.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test integration of memory security components.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory integrity configuration.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory lifecycle management.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test prompt injection detection.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test retention policy for daily notes.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test status reporting from both components.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryIntegrityConfig]] - code - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryLifecycleManager]] - code - gateway/tests/test_memory_lifecycle.py
- [[TestMemorySecurityIntegration]] - code - gateway/tests/test_memory_lifecycle.py
- [[Types of content threats detected in memory files.]] - rationale - gateway/security/memory_lifecycle.py
- [[memory_lifecycle.py]] - code - gateway/security/memory_lifecycle.py
- [[test_memory_lifecycle.py]] - code - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_MiddlewareManager_4]]
- 17 edges to [[_COMMUNITY_MiddlewareManager]]
- 14 edges to [[_COMMUNITY_MiddlewareManager_5]]
- 9 edges to [[_COMMUNITY_MiddlewareManager_7]]
- 4 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_9]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_10]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_11]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_12]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_13]]

## Top bridge nodes
- [[MemoryLifecycleManager]] - degree 39, connects to 5 communities
- [[TestMemoryLifecycleManager]] - degree 20, connects to 4 communities
- [[MemoryLifecycleConfig]] - degree 18, connects to 4 communities
- [[TestMemoryIntegrityConfig]] - degree 12, connects to 4 communities
- [[ContentThreat]] - degree 15, connects to 3 communities
