---
type: community
members: 3
---

# Test Kill Switch Monitor

**Members:** 3 nodes

## Members
- [[Obsidian code-architecture vault (.obsidian-vaultscode-architecture)]] - concept - scripts/gen-code-graph.sh
- [[gen-code-graph.sh]] - code - scripts/gen-code-graph.sh
- [[gen-code-graph.sh script]] - code - scripts/gen-code-graph.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Test_Kill_Switch_Monitor
SORT file.name ASC
```
