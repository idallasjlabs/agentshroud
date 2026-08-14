---
type: community
members: 4
---

# scripts/peer-review.sh

**Members:** 4 nodes

## Members
- [[Approve All Pending Requests]] - document - docs/setup/DEVICE_PAIRING.md
- [[Approving Device Pairing Requests]] - document - docs/setup/DEVICE_PAIRING.md
- [[Quick Approval (Single Device)]] - document - docs/setup/DEVICE_PAIRING.md
- [[Verify Approval]] - document - docs/setup/DEVICE_PAIRING.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/peer-reviewsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Bot Skill Config]]

## Top bridge nodes
- [[Approving Device Pairing Requests]] - degree 4, connects to 1 community