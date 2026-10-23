---
type: community
cohesion: 0.67
members: 3
---

# i-hermes README (Podcast Production Orchestrator)

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[GET ledger audit query API]] - concept - docs/diagrams/images/diagram-20-observability-map.svg
- [[Gateway observability (GET status, GET ledger, MCP audit log, HTTP CONNECT proxy stats)]] - concept - docs/diagrams/images/diagram-20-observability-map.svg
- [[Observability Gaps (Future Work) no log aggregation, no metrics export, no uptime monitor, Zabbix uninstalled]] - concept - docs/diagrams/images/diagram-20-observability-map.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/i-hermes_README_Podcast_Production_Orchestrator
SORT file.name ASC
```
