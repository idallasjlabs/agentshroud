---
type: community
members: 7
---

# Phase 1 — Raw Collection (4)

**Members:** 7 nodes

## Members
- [[A. `mac_app_catalog.json` — Machine-readable manifest_1]] - document - docker/config/hermes/skills/i-mac/SKILL.md
- [[B. `mac_app_catalog.md` — Human-readable catalog_1]] - document - docker/config/hermes/skills/i-mac/SKILL.md
- [[Discovery Strategy_1]] - document - docker/config/hermes/skills/i-mac/SKILL.md
- [[Phase 2 — Deduplication & Normalization_1]] - document - docker/config/hermes/skills/i-mac/SKILL.md
- [[Phase 3 — Categorization_1]] - document - docker/config/hermes/skills/i-mac/SKILL.md
- [[Phase 4 — Enrichment_1]] - document - docker/config/hermes/skills/i-mac/SKILL.md
- [[Phase 5 — Output Generation_1]] - document - docker/config/hermes/skills/i-mac/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Phase_1__Raw_Collection_4
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Phase 1 — Raw Collection]]
- 1 edge to [[_COMMUNITY_Mac App Discovery Skill]]

## Top bridge nodes
- [[Discovery Strategy_1]] - degree 6, connects to 2 communities
