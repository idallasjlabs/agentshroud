---
type: community
cohesion: 0.33
members: 6
---

# Diagram 19 Incident Response (images)

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[Assess severity]] - concept - docs/diagrams/images/diagram-19-incident-response.svg
- [[Incident detected]] - concept - docs/diagrams/images/diagram-19-incident-response.svg
- [[P1 — Critical (respond immediately; owner Isaiah Jefferson; kill switch  revoke  rotate)]] - concept - docs/diagrams/images/diagram-19-incident-response.svg
- [[P2 — High (respond within 1 hour; restart containers, rebuild image)]] - concept - docs/diagrams/images/diagram-19-incident-response.svg
- [[P3 — Medium (respond within 4 hours; review logs, apply config fix)]] - concept - docs/diagrams/images/diagram-19-incident-response.svg
- [[P4 — Low (resolve in next session; fix branch + PR)]] - concept - docs/diagrams/images/diagram-19-incident-response.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Diagram_19_Incident_Response_images
SORT file.name ASC
```
