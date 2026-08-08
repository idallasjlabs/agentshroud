---
type: community
cohesion: 0.67
members: 3
---

# docs/runbooks

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[Backup and Restore Runbook]] - document - docs/runbooks/backup-restore.md
- [[Critical Data Audit Ledger + Docker Secrets (1Password-managed)]] - concept - docs/runbooks/backup-restore.md
- [[Disaster Recovery Procedure (clone, conda env, restore secrets from 1Password)]] - concept - docs/runbooks/backup-restore.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docs/runbooks
SORT file.name ASC
```
