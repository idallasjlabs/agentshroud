---
type: community
cohesion: 0.50
members: 4
---

# Voice Gateway Service

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[VT_AGENTS table (directhermesopenclaw)]] - code - firmware/voice-terminal/main/app_main.c
- [[Voice Gateway Port 8766 Offset (Lima per-port SSH forwarder race)]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Voice Gateway Service]] - code - docker/docker-compose.yml
- [[Voice Interface (STTTTS, wake word)]] - concept - docs/archive/FUTURE-FEATURES.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Voice_Gateway_Service
SORT file.name ASC
```
