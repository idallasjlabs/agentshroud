---
type: community
cohesion: 0.67
members: 3
---

# .enforce_retention()

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[Step 0 - Clone GitHub repo(s) (only if a GitHub URL was given)]] - document - .agents/skills/graphify/references/github-and-merge.md
- [[github-and-merge]] - document - .agents/skills/graphify/references/github-and-merge.md
- [[graphify reference GitHub clone and cross-repo merge]] - document - .agents/skills/graphify/references/github-and-merge.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/enforce_retention
SORT file.name ASC
```
