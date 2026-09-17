---
type: community
cohesion: 0.13
members: 15
---

# Backup & Restore Runbook — AgentShroud

**Cohesion:** 0.13 - loosely connected
**Members:** 15 nodes

## Members
- [[Backup & Restore Runbook — AgentShroud]] - document - docs/runbooks/backup-restore.md
- [[Backup Procedure]] - document - docs/runbooks/backup-restore.md
- [[Backup Retention]] - document - docs/runbooks/backup-restore.md
- [[Daily Audit Ledger Review]] - concept - docs/runbooks/daily-operations.md
- [[Daily Automated Backup]] - document - docs/runbooks/backup-restore.md
- [[Disaster Recovery (Full Rebuild)]] - document - docs/runbooks/backup-restore.md
- [[Disaster Recovery Full Rebuild Procedure]] - concept - docs/runbooks/backup-restore.md
- [[Manual Backup]] - document - docs/runbooks/backup-restore.md
- [[Off-Site Backup]] - document - docs/runbooks/backup-restore.md
- [[Restore Procedure]] - document - docs/runbooks/backup-restore.md
- [[Restore from Backup]] - document - docs/runbooks/backup-restore.md
- [[Tamper-Evident Audit (SHA-256 Hash Chain)]] - concept - docs/papers/agentshroud-ieee-paper.md
- [[What to Back Up]] - document - docs/runbooks/backup-restore.md
- [[backup-restore]] - document - docs/runbooks/backup-restore.md
- [[daily-operations]] - document - docs/runbooks/daily-operations.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Backup__Restore_Runbook__AgentShroud
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_agentshroud-ieee-paper]]
- 1 edge to [[_COMMUNITY_Morning Checklist (5 minutes)]]
- 1 edge to [[_COMMUNITY_TELEGRAM_ISSUES]]

## Top bridge nodes
- [[daily-operations]] - degree 3, connects to 1 community
- [[Tamper-Evident Audit (SHA-256 Hash Chain)]] - degree 2, connects to 1 community
- [[Disaster Recovery Full Rebuild Procedure]] - degree 2, connects to 1 community