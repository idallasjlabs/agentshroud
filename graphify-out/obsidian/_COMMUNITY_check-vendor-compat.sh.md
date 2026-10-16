---
type: community
cohesion: 0.14
members: 24
---

# check-vendor-compat.sh

**Cohesion:** 0.14 - loosely connected
**Members:** 24 nodes

## Members
- [[Hermes 0.21.5 candidate fails A2A JSON-RPC compat check]] - concept - reports/upgrade-2026-09-24.md
- [[No-Op Upgrade Gate (7-week silent no-op)]] - concept - scripts/sunday-upgrade-apply.sh
- [[OpenClaw 2026.10.2 agents.list - agents.entries migration]] - concept - reports/upgrade-2026-10-12.md
- [[Sunday Upgrade Report 2026-09-06 (dev-only scoped run)]] - document - reports/upgrade-2026-09-06-dev.md
- [[Sunday Upgrade Report 2026-09-06 (dev-only, duplicate)]] - document - reports/upgrade-2026-09-06.md
- [[Sunday Upgrade Report 2026-09-14 (dev account)]] - document - reports/upgrade-2026-09-14.md
- [[Upgrade Report 2026-09-24 (dev, PARTIAL, Hermes compat blocked)]] - document - reports/upgrade-2026-09-24.md
- [[_rollback()]] - code - scripts/update-agentshroud.sh
- [[_run_cleanup()]] - code - scripts/check-vendor-compat.sh
- [[check()_6]] - code - scripts/post-deploy-check.sh
- [[check-vendor-compat.sh]] - code - scripts/check-vendor-compat.sh
- [[check-vendor-compat.sh script]] - code - scripts/check-vendor-compat.sh
- [[check_hermes()]] - code - scripts/check-vendor-compat.sh
- [[check_openclaw()]] - code - scripts/check-vendor-compat.sh
- [[fail()_3]] - code - scripts/check-vendor-compat.sh
- [[pass()_2]] - code - scripts/check-vendor-compat.sh
- [[post-deploy-check.sh]] - code - scripts/post-deploy-check.sh
- [[post-deploy-check.sh script]] - code - scripts/post-deploy-check.sh
- [[restore-backup.sh]] - code - scripts/restore-backup.sh
- [[restore-backup.sh script]] - code - scripts/restore-backup.sh
- [[restore_tar_to_volume()]] - code - scripts/restore-backup.sh
- [[update-agentshroud.sh]] - code - scripts/update-agentshroud.sh
- [[update-agentshroud.sh script]] - code - scripts/update-agentshroud.sh
- [[warn()_2]] - code - scripts/check-vendor-compat.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check-vendor-compatsh
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 4 edges to [[_COMMUNITY_colima-health-check.sh]]
- 2 edges to [[_COMMUNITY_triage-cve-mitigations.py]]
- 2 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 1 edge to [[_COMMUNITY_upgrade]]
- 1 edge to [[_COMMUNITY_plan_remediation]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 1 edge to [[_COMMUNITY_validate_network_security]]
- 1 edge to [[_COMMUNITY_test_openclaw_photo.sh]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]

## Top bridge nodes
- [[check-vendor-compat.sh]] - degree 15, connects to 4 communities
- [[post-deploy-check.sh]] - degree 7, connects to 4 communities
- [[Upgrade Report 2026-09-24 (dev, PARTIAL, Hermes compat blocked)]] - degree 8, connects to 2 communities
- [[No-Op Upgrade Gate (7-week silent no-op)]] - degree 3, connects to 2 communities
- [[check_openclaw()]] - degree 8, connects to 1 community
