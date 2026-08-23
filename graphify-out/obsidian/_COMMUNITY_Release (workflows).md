---
type: community
cohesion: 1.00
members: 2
---

# Release (workflows)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Release Workflow]] - code - .github/workflows/release.yml
- [[TagVersion Sync Verification]] - rationale - .github/workflows/release.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Release_workflows
SORT file.name ASC
```
