---
type: community
members: 1
---

# Large-write-then-network-activity staging/exfiltration pattern detection

**Members:** 1 nodes

## Members
- [[Large-write-then-network-activity stagingexfiltration pattern detection]] - concept - gateway/tests/test_file_sandbox.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Large-write-then-network-activity_staging/exfiltration_pattern_detection
SORT file.name ASC
```
