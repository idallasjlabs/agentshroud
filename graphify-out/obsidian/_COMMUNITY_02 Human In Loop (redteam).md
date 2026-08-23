---
type: community
cohesion: 0.50
members: 4
---

# 02 Human In Loop (redteam)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[MCP Tool Risk Tier Classification (criticalhighmediumlow) with Approval Policy]] - concept - docs/planning/redteam/02-human-in-the-loop.md
- [[Red Team Finding 02 No Human Approval for High-Risk Tool Calls]] - document - docs/planning/redteam/02-human-in-the-loop.md
- [[Red Team Finding 03 All Users Share Agent Context and File System]] - document - docs/planning/redteam/03-session-isolation.md
- [[SessionManager — Telegram User ID as Partition Key for Workspaces and Memory]] - concept - docs/planning/redteam/03-session-isolation.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/02_Human_In_Loop_redteam
SORT file.name ASC
```
