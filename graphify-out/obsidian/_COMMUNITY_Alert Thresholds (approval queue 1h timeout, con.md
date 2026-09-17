---
type: community
cohesion: 1.00
members: 2
---

# Alert Thresholds (approval queue 1h timeout, con

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Alert Thresholds (approval queue 1h timeout, context 200K hard limit, op-proxy 6 retries)]] - concept - docs/diagrams/images/diagram-20-observability-map.svg
- [[Bot observability (docker logs, GET apihealth, context tokens 200K limit)]] - concept - docs/diagrams/images/diagram-20-observability-map.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Alert_Thresholds_approval_queue_1h_timeout_con
SORT file.name ASC
```
