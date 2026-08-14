---
type: community
members: 19
---

# gateway/README.md

**Members:** 19 nodes

## Members
- [[.teardown_method()_1]] - code - gateway/tests/test_memory_lifecycle.py
- [[.teardown_method()_2]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_content_sanitization()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_daily_notes_retention()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_lifecycle_maintenance()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_memory_md_size_limit()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_memory_write_validation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_pii_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_prompt_injection_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[Clean up test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test MEMORY.md size limit enforcement.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test PII detection in memory content.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test complete lifecycle maintenance run.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test content sanitization removes threats.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory lifecycle management.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test prompt injection detection.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test retention policy for daily notes.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test validation before writing to memory files.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryLifecycleManager]] - code - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gateway/READMEmd
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Progressive Trust Config]]
- 2 edges to [[_COMMUNITY_docsvault]]
- 2 edges to [[_COMMUNITY_docsoperations]]
- 1 edge to [[_COMMUNITY_docsvault]]

## Top bridge nodes
- [[TestMemoryLifecycleManager]] - degree 21, connects to 4 communities
- [[.teardown_method()_1]] - degree 2, connects to 1 community