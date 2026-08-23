---
type: community
cohesion: 0.67
members: 3
---

# Gen Code Graph (scripts)

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[Obsidian code-architecture vault (.obsidian-vaultscode-architecture)]] - concept - scripts/gen-code-graph.sh
- [[gen-code-graph.sh]] - code - scripts/gen-code-graph.sh
- [[gen-code-graph.sh script]] - code - scripts/gen-code-graph.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gen_Code_Graph_scripts
SORT file.name ASC
```
