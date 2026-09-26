---
type: community
cohesion: 1.00
members: 2
---

# Incident Classification System

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[SOC Auth WS Token IssuanceRedemption Tests]] - code - gateway/tests/test_soc_auth.py
- [[SOCWebSocketHandler Subscription Filter Tests]] - code - gateway/tests/test_soc_websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Incident_Classification_System
SORT file.name ASC
```
