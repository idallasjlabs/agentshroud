---
type: community
cohesion: 0.67
members: 3
---

# Community 1403

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[GET ledger audit query API]] - concept - docs/diagrams/images/diagram-20-observability-map.svg
- [[Gateway observability (GET status, GET ledger, MCP audit log, HTTP CONNECT proxy stats)]] - concept - docs/diagrams/images/diagram-20-observability-map.svg
- [[Observability Gaps (Future Work) no log aggregation, no metrics export, no uptime monitor, Zabbix uninstalled]] - concept - docs/diagrams/images/diagram-20-observability-map.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1403
SORT file.name ASC
```
