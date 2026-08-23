---
type: community
cohesion: 1.00
members: 3
---

# Memory Integrity (security)

**Cohesion:** 1.00 - tightly connected
**Members:** 3 nodes

## Members
- [[MemoryIntegrityMonitor Tamper Detection]] - code - gateway/security/memory_integrity.py
- [[MemoryLifecycleManager PII Scan and Retention]] - code - gateway/security/memory_lifecycle.py
- [[Test Memory Lifecycle and Integrity]] - code - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Memory_Integrity_security
SORT file.name ASC
```
