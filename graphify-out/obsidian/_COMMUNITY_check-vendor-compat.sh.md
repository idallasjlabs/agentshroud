---
type: community
cohesion: 0.13
members: 25
---

# check-vendor-compat.sh

**Cohesion:** 0.13 - loosely connected
**Members:** 25 nodes

## Members
- [[ColimaDocker VM Storage Exhaustion]] - concept - reports/upgrade-2026-09-06-prod.md
- [[Dev-to-Prod Handoff Contract]] - concept - scripts/sunday-upgrade-apply.sh
- [[Sunday Upgrade Report 2026-08-30 (0734 first-pass abort)]] - document - reports/upgrade-2026-08-30-20260830-2009.md
- [[Sunday Upgrade Report 2026-08-30 (final)]] - document - reports/upgrade-2026-08-30.md
- [[Sunday Upgrade Report 2026-08-30 (local-llms upgrade requested)]] - document - reports/upgrade-2026-08-30-20260830-2010.md
- [[Sunday Upgrade Report 2026-09-06 (dev-only scoped run)]] - document - reports/upgrade-2026-09-06-dev.md
- [[Sunday Upgrade Report 2026-09-06 (dev-only, duplicate)]] - document - reports/upgrade-2026-09-06.md
- [[Sunday Upgrade Report 2026-09-06 (prod read-only, pre-crisis)]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Sunday Upgrade Report 2026-09-06 (prod, disk-exhaustion incident)]] - document - reports/upgrade-2026-09-06-prod.md
- [[Sunday Upgrade Report 2026-09-14 (dev account)]] - document - reports/upgrade-2026-09-14.md
- [[Sunday Upgrade Report Hermes-cron Delivery]] - code - scripts/hermes-cron/sunday-upgrade-report.sh
- [[Wazuh-Agent Sidecar Split (SIDECAR-GAP-001 resolution)]] - concept - reports/upgrade-2026-09-06-prod.md
- [[_run_cleanup()]] - code - scripts/check-vendor-compat.sh
- [[check-vendor-compat.sh]] - code - scripts/check-vendor-compat.sh
- [[check-vendor-compat.sh script]] - code - scripts/check-vendor-compat.sh
- [[check-vendor-compat.sh script_1]] - code - scripts/check-vendor-compat.sh
- [[check_hermes()]] - code - scripts/check-vendor-compat.sh
- [[check_openclaw()]] - code - scripts/check-vendor-compat.sh
- [[fail()_3]] - code - scripts/check-vendor-compat.sh
- [[op-to-keychain.sh]] - code - scripts/op-to-keychain.sh
- [[op-to-keychain.sh script]] - code - scripts/op-to-keychain.sh
- [[op-to-keychain.sh script_1]] - code - scripts/op-to-keychain.sh
- [[pass()_3]] - code - scripts/check-vendor-compat.sh
- [[sunday-upgrade.sh (remote-control launcher)]] - code - scripts/sunday-upgrade.sh
- [[warn()_2]] - code - scripts/check-vendor-compat.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check-vendor-compatsh
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 2 edges to [[_COMMUNITY_auto_remediate_cves.py]]
- 2 edges to [[_COMMUNITY_sunday-upgrade]]
- 1 edge to [[_COMMUNITY_apply-patches.js (OpenClaw)]]
- 1 edge to [[_COMMUNITY_run_test()]]
- 1 edge to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_post-deploy-check.sh]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]

## Top bridge nodes
- [[check-vendor-compat.sh]] - degree 13, connects to 3 communities
- [[check_openclaw()]] - degree 10, connects to 2 communities
- [[Dev-to-Prod Handoff Contract]] - degree 6, connects to 2 communities
- [[Sunday Upgrade Report 2026-09-14 (dev account)]] - degree 5, connects to 2 communities
- [[check_hermes()]] - degree 9, connects to 1 community