---
type: community
members: 6
---

# gateway/requirements.txt

**Members:** 6 nodes

## Members
- [[Agent Trust Levels (UNTRUSTED, BASIC, STANDARD, TRUSTED, ADMIN)]] - concept - docs/flows/state-diagrams.md
- [[AgentShroud State Diagrams (doc)]] - document - docs/flows/state-diagrams.md
- [[Approval Queue States (PENDING, APPROVED, DENIED, TIMED_OUT, EXECUTED, ARCHIVED)]] - concept - docs/flows/state-diagrams.md
- [[Diagram 16 State — Approval Queue]] - image - docs/diagrams/images/diagram-16-state-approval-queue.svg
- [[Gateway Operational Modes (MONITOR, ENFORCE, LOCKDOWN, EMERGENCY, RECOVERY)]] - concept - docs/flows/state-diagrams.md
- [[Kill Switch States (ACTIVE, SOFT_KILL, HARD_KILL, PANIC, RECOVERY)]] - concept - docs/flows/state-diagrams.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gateway/requirementstxt
SORT file.name ASC
```
