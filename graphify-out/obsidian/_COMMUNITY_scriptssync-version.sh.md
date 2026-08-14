---
type: community
members: 4
---

# scripts/sync-version.sh

**Members:** 4 nodes

## Members
- [[Manual Update Process]] - document - docs/setup/setup-guide.md
- [[Rollback If Needed]] - document - docs/setup/setup-guide.md
- [[Update OpenClaw]] - document - docs/setup/setup-guide.md
- [[Updating]] - document - docs/setup/setup-guide.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/sync-versionsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Bot Container Scripts]]
- 1 edge to [[_COMMUNITY_skillsopenclaw]]

## Top bridge nodes
- [[Updating]] - degree 5, connects to 2 communities