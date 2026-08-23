---
type: community
cohesion: 0.11
members: 19
---

# Daily Operations (runbooks)

**Cohesion:** 0.11 - loosely connected
**Members:** 19 nodes

## Members
- [[1. Dependency Updates]] - document - docs/runbooks/daily-operations.md
- [[1. Service Health]] - document - docs/runbooks/daily-operations.md
- [[2. Backup Verification]] - document - docs/runbooks/daily-operations.md
- [[2. Tailscale Connectivity]] - document - docs/runbooks/daily-operations.md
- [[3. Audit Ledger Review]] - document - docs/runbooks/daily-operations.md
- [[3. Tailscale ACL Review]] - document - docs/runbooks/daily-operations.md
- [[4. Log Review]] - document - docs/runbooks/daily-operations.md
- [[4. Test Suite]] - document - docs/runbooks/daily-operations.md
- [[5. Resource Usage]] - document - docs/runbooks/daily-operations.md
- [[Daily Audit Ledger Review]] - concept - docs/runbooks/daily-operations.md
- [[Daily Operations Runbook — AgentShroud]] - document - docs/runbooks/daily-operations.md
- [[Dashboard Monitoring]] - document - docs/runbooks/daily-operations.md
- [[Disaster Recovery Full Rebuild Procedure]] - concept - docs/runbooks/backup-restore.md
- [[Monthly Checklist (30 minutes)]] - document - docs/runbooks/daily-operations.md
- [[Morning Checklist (5 minutes)]] - document - docs/runbooks/daily-operations.md
- [[Tamper-Evident Audit (SHA-256 Hash Chain)]] - concept - docs/papers/agentshroud-ieee-paper.md
- [[Weekly Checklist (15 minutes)]] - document - docs/runbooks/daily-operations.md
- [[backup-restore]] - document - docs/runbooks/backup-restore.md
- [[daily-operations]] - document - docs/runbooks/daily-operations.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Daily_Operations_runbooks
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Telegram Issues (project)]]
- 1 edge to [[_COMMUNITY_Agentshroud Ieee Paper (papers)]]
- 1 edge to [[_COMMUNITY_Backup Restore (runbooks)]]

## Top bridge nodes
- [[backup-restore]] - degree 3, connects to 1 community
- [[Tamper-Evident Audit (SHA-256 Hash Chain)]] - degree 2, connects to 1 community
- [[Disaster Recovery Full Rebuild Procedure]] - degree 2, connects to 1 community