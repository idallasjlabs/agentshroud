---
type: community
members: 3
---

# openclaw-identity.md (OpenClaw bot identity)

**Members:** 3 nodes

## Members
- [[competitive-analysis.md (bot workspace competitive-intel source of truth)]] - document - docker/config/openclaw/workspace/competitive-analysis.md
- [[hermes-soul.md (Hermes system identity)]] - document - docker/config/openclaw/agents/hermes-soul.md
- [[openclaw-identity.md (OpenClaw bot identity)]] - document - docker/config/openclaw/agents/openclaw-identity.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/openclaw-identitymd_OpenClaw_bot_identity
SORT file.name ASC
```
