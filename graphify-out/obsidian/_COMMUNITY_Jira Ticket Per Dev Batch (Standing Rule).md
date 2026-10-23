---
type: community
cohesion: 1.00
members: 1
---

# Jira Ticket Per Dev Batch (Standing Rule)

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[--watch debounce avoids per-file rebuild storms]] - rationale - docker/config/hermes/skills/graphify/references/add-watch.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Jira_Ticket_Per_Dev_Batch_Standing_Rule
SORT file.name ASC
```
