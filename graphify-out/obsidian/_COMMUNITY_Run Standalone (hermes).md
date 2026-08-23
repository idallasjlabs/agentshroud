---
type: community
cohesion: 0.19
members: 17
---

# Run Standalone (hermes)

**Cohesion:** 0.19 - loosely connected
**Members:** 17 nodes

## Members
- [[_rollback()]] - code - scripts/update-agentshroud.sh
- [[_secret_mount_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_wait_for_gateway_healthy()]] - code - docker/bots/hermes/run-standalone.sh
- [[check()]] - code - scripts/post-deploy-check.sh
- [[cmd_down()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_logs()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_status()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_up()]] - code - docker/bots/hermes/run-standalone.sh
- [[post-deploy-check.sh]] - code - scripts/post-deploy-check.sh
- [[post-deploy-check.sh script]] - code - scripts/post-deploy-check.sh
- [[restore-backup.sh]] - code - scripts/restore-backup.sh
- [[restore-backup.sh script]] - code - scripts/restore-backup.sh
- [[restore_tar_to_volume()]] - code - scripts/restore-backup.sh
- [[run-standalone.sh]] - code - docker/bots/hermes/run-standalone.sh
- [[run-standalone.sh script]] - code - docker/bots/hermes/run-standalone.sh
- [[update-agentshroud.sh]] - code - scripts/update-agentshroud.sh
- [[update-agentshroud.sh script]] - code - scripts/update-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Run_Standalone_hermes
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Dashboard Bridge (hermes)]]
- 1 edge to [[_COMMUNITY_Apply Patches (openclaw)]]
- 1 edge to [[_COMMUNITY_Start (hermes)]]
- 1 edge to [[_COMMUNITY_Check Vendor Compat (scripts)]]

## Top bridge nodes
- [[run-standalone.sh]] - degree 12, connects to 3 communities
- [[update-agentshroud.sh]] - degree 5, connects to 1 community