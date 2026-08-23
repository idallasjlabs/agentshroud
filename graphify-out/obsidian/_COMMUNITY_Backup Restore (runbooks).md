---
type: community
cohesion: 0.20
members: 10
---

# Backup Restore (runbooks)

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[Backup & Restore Runbook — AgentShroud]] - document - docs/runbooks/backup-restore.md
- [[Backup Procedure]] - document - docs/runbooks/backup-restore.md
- [[Backup Retention]] - document - docs/runbooks/backup-restore.md
- [[Daily Automated Backup]] - document - docs/runbooks/backup-restore.md
- [[Disaster Recovery (Full Rebuild)]] - document - docs/runbooks/backup-restore.md
- [[Manual Backup]] - document - docs/runbooks/backup-restore.md
- [[Off-Site Backup]] - document - docs/runbooks/backup-restore.md
- [[Restore Procedure]] - document - docs/runbooks/backup-restore.md
- [[Restore from Backup]] - document - docs/runbooks/backup-restore.md
- [[What to Back Up]] - document - docs/runbooks/backup-restore.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Backup_Restore_runbooks
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Daily Operations (runbooks)]]

## Top bridge nodes
- [[Backup & Restore Runbook — AgentShroud]] - degree 5, connects to 1 community