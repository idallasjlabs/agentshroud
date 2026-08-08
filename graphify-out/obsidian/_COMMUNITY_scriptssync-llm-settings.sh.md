---
type: community
cohesion: 0.13
members: 19
---

# scripts/sync-llm-settings.sh

**Cohesion:** 0.13 - loosely connected
**Members:** 19 nodes

## Members
- [[BOT_CONTAINER]] - code - scripts/update-bot-agents.sh
- [[BOT_DEFAULTS_DIR]] - code - scripts/update-bot-agents.sh
- [[BOT_LIVE_SKILLS_DIR]] - code - scripts/update-bot-agents.sh
- [[PYTHONPATH]] - code - scripts/smoke.d/test-skills-sync.sh
- [[SKILLGUARD_TEST_DEST_ROOT]] - code - scripts/smoke.d/test-skills-sync.sh
- [[_python()]] - code - scripts/sync-llm-settings.sh
- [[_sha256()_2]] - code - scripts/sync-llm-settings.sh
- [[_sha256()_3]] - code - scripts/validate-skills-manifest.sh
- [[_write_manifest()]] - code - scripts/sync-llm-settings.sh
- [[check()_3]] - code - scripts/smoke.d/test-skills-sync.sh
- [[gatewayskillsscan.py (scan CLI)]] - code - gateway/skills/scan.py
- [[sync-llm-settings.sh]] - code - scripts/sync-llm-settings.sh
- [[sync-llm-settings.sh script]] - code - scripts/sync-llm-settings.sh
- [[test-skills-sync.sh]] - code - scripts/smoke.d/test-skills-sync.sh
- [[test-skills-sync.sh script]] - code - scripts/smoke.d/test-skills-sync.sh
- [[update-bot-agents.sh]] - code - scripts/update-bot-agents.sh
- [[update-bot-agents.sh script]] - code - scripts/update-bot-agents.sh
- [[validate-skills-manifest.sh]] - code - scripts/validate-skills-manifest.sh
- [[validate-skills-manifest.sh script]] - code - scripts/validate-skills-manifest.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/sync-llm-settingssh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_scriptssmoke.d]]

## Top bridge nodes
- [[test-skills-sync.sh]] - degree 7, connects to 1 community
- [[gatewayskillsscan.py (scan CLI)]] - degree 2, connects to 1 community