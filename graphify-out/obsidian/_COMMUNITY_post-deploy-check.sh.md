---
type: community
cohesion: 0.31
members: 9
---

# post-deploy-check.sh

**Cohesion:** 0.31 - loosely connected
**Members:** 9 nodes

## Members
- [[_rollback()]] - code - scripts/update-agentshroud.sh
- [[check()_4]] - code - scripts/post-deploy-check.sh
- [[post-deploy-check.sh]] - code - scripts/post-deploy-check.sh
- [[post-deploy-check.sh script]] - code - scripts/post-deploy-check.sh
- [[restore-backup.sh]] - code - scripts/restore-backup.sh
- [[restore-backup.sh script]] - code - scripts/restore-backup.sh
- [[restore_tar_to_volume()]] - code - scripts/restore-backup.sh
- [[update-agentshroud.sh]] - code - scripts/update-agentshroud.sh
- [[update-agentshroud.sh script]] - code - scripts/update-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/post-deploy-checksh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_run_test()]]
- 1 edge to [[_COMMUNITY_check-vendor-compat.sh]]

## Top bridge nodes
- [[post-deploy-check.sh]] - degree 4, connects to 1 community
- [[update-agentshroud.sh]] - degree 4, connects to 1 community