---
type: community
members: 4
---

# scripts/preflight-check.sh

**Members:** 4 nodes

## Members
- [[Finding Pending Pairing Requests]] - document - docs/setup/DEVICE_PAIRING.md
- [[Method 1 Via CLI (Recommended)]] - document - docs/setup/DEVICE_PAIRING.md
- [[Method 2 View Raw Pending File]] - document - docs/setup/DEVICE_PAIRING.md
- [[Method 3 Check Container Logs]] - document - docs/setup/DEVICE_PAIRING.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/preflight-checksh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Bot Skill Config]]

## Top bridge nodes
- [[Finding Pending Pairing Requests]] - degree 4, connects to 1 community