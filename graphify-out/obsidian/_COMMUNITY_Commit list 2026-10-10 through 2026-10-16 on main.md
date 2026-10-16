---
type: community
cohesion: 0.20
members: 11
---

# Commit list 2026-10-10 through 2026-10-16 on main

**Cohesion:** 0.20 - loosely connected
**Members:** 11 nodes

## Members
- [[CI docs-drift version consistency check]] - code - .github/workflows/ci.yml
- [[CI test job (ubuntumacos x py3.113.13 matrix, cov=84)]] - code - .github/workflows/ci.yml
- [[Core framework pins fastapi, uvicorn, pydantic, pydantic-settings, aiosqlite, httpx, docker SDK]] - concept - gateway/requirements.txt
- [[Leak gate ResourceWarningPytestUnraisableExceptionWarning fatal only on ubuntu+3.11]] - rationale - .github/workflows/ci.yml
- [[Release Docker build & tag job]] - code - .github/workflows/release.yml
- [[Release GitHub Release job (CHANGELOG notes extraction)]] - code - .github/workflows/release.yml
- [[Release test job (py3.13, tagversion sync checks)]] - code - .github/workflows/release.yml
- [[check_or_fix()]] - code - scripts/sync-version.sh
- [[sync-version.sh]] - code - scripts/sync-version.sh
- [[sync-version.sh script]] - code - scripts/sync-version.sh
- [[websockets=17.1,18.0 pin]] - concept - gateway/requirements.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Commit_list_2026-10-10_through_2026-10-16_on_main
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_Claude Code skill catalog (59 skills)]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]

## Top bridge nodes
- [[CI test job (ubuntumacos x py3.113.13 matrix, cov=84)]] - degree 4, connects to 1 community
- [[sync-version.sh]] - degree 4, connects to 1 community
- [[websockets=17.1,18.0 pin]] - degree 2, connects to 1 community
- [[CI docs-drift version consistency check]] - degree 2, connects to 1 community
