---
type: community
cohesion: 0.24
members: 11
---

# Recommendations for Production Deployment

**Cohesion:** 0.24 - loosely connected
**Members:** 11 nodes

## Members
- [[_rollback()]] - code - scripts/update-agentshroud.sh
- [[check()]] - code - scripts/post-deploy-check.sh
- [[check-soak-status.sh]] - code - scripts/check-soak-status.sh
- [[check-soak-status.sh script]] - code - scripts/check-soak-status.sh
- [[post-deploy-check.sh]] - code - scripts/post-deploy-check.sh
- [[post-deploy-check.sh script]] - code - scripts/post-deploy-check.sh
- [[restore-backup.sh]] - code - scripts/restore-backup.sh
- [[restore-backup.sh script]] - code - scripts/restore-backup.sh
- [[restore_tar_to_volume()]] - code - scripts/restore-backup.sh
- [[update-agentshroud.sh]] - code - scripts/update-agentshroud.sh
- [[update-agentshroud.sh script]] - code - scripts/update-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Recommendations_for_Production_Deployment
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud™ Telegram-Reported Issues]]
- 1 edge to [[_COMMUNITY_pytest.ini]]
- 1 edge to [[_COMMUNITY_OutputSchemaEnforcer]]
- 1 edge to [[_COMMUNITY_CICD Pipeline Advisor (README)]]
- 1 edge to [[_COMMUNITY_AgentShroud — Master Feature List (Everything Ev]]

## Top bridge nodes
- [[post-deploy-check.sh]] - degree 7, connects to 3 communities
- [[update-agentshroud.sh]] - degree 4, connects to 1 community
- [[check-soak-status.sh]] - degree 3, connects to 1 community