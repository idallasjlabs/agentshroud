---
type: community
cohesion: 0.67
members: 3
---

# health-check.sh

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[competitive-analysis.md (bot workspace competitive-intel source of truth)]] - document - docker/config/openclaw/workspace/competitive-analysis.md
- [[hermes-soul.md (Hermes system identity)]] - document - docker/config/openclaw/agents/hermes-soul.md
- [[openclaw-identity.md (OpenClaw bot identity)]] - document - docker/config/openclaw/agents/openclaw-identity.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/health-checksh
SORT file.name ASC
```
