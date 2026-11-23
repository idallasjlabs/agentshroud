---
type: community
members: 6
---

# 8. Docker System Pruning

**Members:** 6 nodes

## Members
- [[8. Docker System Pruning]] - document - docs/runbooks/colima-docker-guide.md
- [[Check what would be removed (dry run)]] - document - docs/runbooks/colima-docker-guide.md
- [[Nuclear prune (removes everything including volumes)]] - document - docs/runbooks/colima-docker-guide.md
- [[Prune from inside Colima VM (use when host-side prune hangs)]] - document - docs/runbooks/colima-docker-guide.md
- [[Reclaim space from dangling layers in overlay2]] - document - docs/runbooks/colima-docker-guide.md
- [[Safe prune (removes only stopped containers + unused images + build cache)]] - document - docs/runbooks/colima-docker-guide.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/8_Docker_System_Pruning
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Colima & Docker Operations Guide — AgentShroud]]

## Top bridge nodes
- [[8. Docker System Pruning]] - degree 6, connects to 1 community
