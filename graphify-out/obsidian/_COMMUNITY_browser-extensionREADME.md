---
type: community
members: 4
---

# browser-extension/README.md

**Members:** 4 nodes

## Members
- [[approved (action executed, ledger entry written)]] - concept - docs/diagrams/images/diagram-16-state-approval-queue.svg
- [[expired (1-hour TTL exceeded, auto-transition on load)]] - concept - docs/diagrams/images/diagram-16-state-approval-queue.svg
- [[pending (bot submits action requiring approval)]] - concept - docs/diagrams/images/diagram-16-state-approval-queue.svg
- [[rejected (action blocked, bot notified)]] - concept - docs/diagrams/images/diagram-16-state-approval-queue.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/browser-extension/READMEmd
SORT file.name ASC
```
