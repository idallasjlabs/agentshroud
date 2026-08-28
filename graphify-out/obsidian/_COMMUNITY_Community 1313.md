---
type: community
cohesion: 0.50
members: 4
---

# Community 1313

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[approved (action executed, ledger entry written)]] - concept - docs/diagrams/images/diagram-16-state-approval-queue.svg
- [[expired (1-hour TTL exceeded, auto-transition on load)]] - concept - docs/diagrams/images/diagram-16-state-approval-queue.svg
- [[pending (bot submits action requiring approval)]] - concept - docs/diagrams/images/diagram-16-state-approval-queue.svg
- [[rejected (action blocked, bot notified)]] - concept - docs/diagrams/images/diagram-16-state-approval-queue.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1313
SORT file.name ASC
```
