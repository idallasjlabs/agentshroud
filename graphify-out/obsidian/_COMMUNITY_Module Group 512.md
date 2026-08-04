---
type: community
cohesion: 0.40
members: 5
---

# Module Group 512

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[Immutable files list (SOUL.md, system_prompt, .env, docker-compose)]] - concept - docs/redteam/04-separation-of-privilege.md
- [[IntegrityChecker — SHA-256 baseline for critical files]] - concept - docs/redteam/04-separation-of-privilege.md
- [[Read-only Docker volume mounts for gateway source]] - concept - docs/redteam/04-separation-of-privilege.md
- [[SSH Proxy host deny list — block SSH to gateway host]] - concept - docs/redteam/04-separation-of-privilege.md
- [[Separation of Privilege (Remediation) — gateway read-only to agent]] - document - docs/redteam/04-separation-of-privilege.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_512
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 432]]
- 1 edge to [[_COMMUNITY_Module Group 400]]

## Top bridge nodes
- [[Separation of Privilege (Remediation) — gateway read-only to agent]] - degree 7, connects to 2 communities
