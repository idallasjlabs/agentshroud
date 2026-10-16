---
type: community
cohesion: 1.00
members: 2
---

# AGENTSHROUD_VERSION fallback to docker/versions.env

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[AGENTSHROUD_VERSION fallback to dockerversions.env]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Hermes 'latest'-tag outage on prod]] - rationale - INCIDENT_2026-10-16_conduit-outage.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AGENTSHROUD_VERSION_fallback_to_docker/versionsenv
SORT file.name ASC
```
