---
type: community
members: 2
---

# Gateway Test Suite

**Members:** 2 nodes

## Members
- [[OpenClaw SOUL]] - document - docker/config/openclaw/workspace/SOUL.md
- [[SOUL.md Freshness Check Job]] - code - .github/workflows/ci.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gateway_Test_Suite
SORT file.name ASC
```
