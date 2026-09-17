---
type: community
cohesion: 0.33
members: 6
---

# AgentShroud Data Assets (root)

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[AgentShroud Data Assets (root)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[External Credentials (1Password vault)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[OpenClaw Volume (openclaw.json, cronjobs.json, sessions)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[SQLite DBs (Backed by SQLite)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[approval_items table (pending, approved, rejected, expired; 1h TTL)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg
- [[ledger table (indexed on timestamp, source, forwarded_to)]] - concept - docs/diagrams/images/diagram-10-data-dictionary.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Data_Assets_root
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Approval Queue (human-in-the-loop)]]

## Top bridge nodes
- [[AgentShroud Data Assets (root)]] - degree 4, connects to 1 community