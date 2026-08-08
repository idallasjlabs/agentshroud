---
type: community
cohesion: 0.40
members: 5
---

# scripts/deploy.sh

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[PATH_2]] - code - scripts/deploy.sh
- [[deploy.sh]] - code - scripts/deploy.sh
- [[deploy.sh script]] - code - scripts/deploy.sh
- [[setup-secrets.sh (Credential Extraction)]] - code - docker/setup-secrets.sh
- [[setup_ephemeral_secrets()]] - code - scripts/asb

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/deploysh
SORT file.name ASC
```
