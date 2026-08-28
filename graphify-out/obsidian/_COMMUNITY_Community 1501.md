---
type: community
cohesion: 1.00
members: 2
---

# Community 1501

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Alert Thresholds (approval queue 1h timeout, context 200K hard limit, op-proxy 6 retries)]] - concept - docs/diagrams/images/diagram-20-observability-map.svg
- [[Bot observability (docker logs, GET apihealth, context tokens 200K limit)]] - concept - docs/diagrams/images/diagram-20-observability-map.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1501
SORT file.name ASC
```
