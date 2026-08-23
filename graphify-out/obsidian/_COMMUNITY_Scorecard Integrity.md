---
type: community
cohesion: 1.00
members: 2
---

# Scorecard Integrity

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Scorecard Data Integrity Tests (no stub inflation)]] - code - gateway/tests/test_scorecard_integrity.py
- [[Scorecard Domain Scorer 0-5 Scale Tests]] - code - gateway/tests/test_scorecard_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Scorecard_Integrity
SORT file.name ASC
```
