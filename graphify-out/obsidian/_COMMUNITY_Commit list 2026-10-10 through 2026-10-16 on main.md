---
type: community
cohesion: 0.14
members: 15
---

# Commit list 2026-10-10 through 2026-10-16 on main

**Cohesion:** 0.14 - loosely connected
**Members:** 15 nodes

## Members
- [[CI docs-drift version consistency check]] - code - .github/workflows/ci.yml
- [[CI test job (ubuntumacos x py3.113.13 matrix, cov=84)]] - code - .github/workflows/ci.yml
- [[Commit list 2026-10-10 through 2026-10-16 on main]] - document - INCIDENT_2026-10-16_conduit-outage.md
- [[Core framework pins fastapi, uvicorn, pydantic, pydantic-settings, aiosqlite, httpx, docker SDK]] - concept - gateway/requirements.txt
- [[Leak gate ResourceWarningPytestUnraisableExceptionWarning fatal only on ubuntu+3.11]] - rationale - .github/workflows/ci.yml
- [[Preflight git hygiene graphify-out never counts as dirty; pathspec-scoped commits only]] - rationale - prompts/sunday-upgrade.md
- [[Release Docker build & tag job]] - code - .github/workflows/release.yml
- [[Release GitHub Release job (CHANGELOG notes extraction)]] - code - .github/workflows/release.yml
- [[Release test job (py3.13, tagversion sync checks)]] - code - .github/workflows/release.yml
- [[Why a blanket revert to the 2026-10-10 commit was not done]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[check_or_fix()]] - code - scripts/sync-version.sh
- [[sunday-upgrade-apply.sh exit-code contract (0102025304050127)]] - rationale - prompts/sunday-upgrade.md
- [[sync-version.sh]] - code - scripts/sync-version.sh
- [[sync-version.sh script]] - code - scripts/sync-version.sh
- [[websockets=17.1,18.0 pin]] - concept - gateway/requirements.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Commit_list_2026-10-10_through_2026-10-16_on_main
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_Claude Code skill catalog (59 skills)]]
- 1 edge to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 1 edge to [[_COMMUNITY_tailscale-serve.sh]]
- 1 edge to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]

## Top bridge nodes
- [[Commit list 2026-10-10 through 2026-10-16 on main]] - degree 8, connects to 5 communities
- [[CI test job (ubuntumacos x py3.113.13 matrix, cov=84)]] - degree 5, connects to 1 community
- [[sync-version.sh]] - degree 4, connects to 1 community
- [[websockets=17.1,18.0 pin]] - degree 2, connects to 1 community
- [[CI docs-drift version consistency check]] - degree 2, connects to 1 community
