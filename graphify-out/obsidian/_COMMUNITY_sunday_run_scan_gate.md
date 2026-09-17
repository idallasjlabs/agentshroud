---
type: community
cohesion: 0.25
members: 16
---

# sunday_run_scan_gate

**Cohesion:** 0.25 - loosely connected
**Members:** 16 nodes

## Members
- [[check]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[die (fallback)]] - code - scripts/lib/sunday-scan.sh
- [[log (fallback)]] - code - scripts/lib/sunday-scan.sh
- [[make_apply_bin]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[make_fake_repo]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[run_apply]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[run_gate]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[sunday-scan.sh]] - code - scripts/lib/sunday-scan.sh
- [[sunday-scan.sh script]] - code - scripts/lib/sunday-scan.sh
- [[sunday_ensure_trivy]] - code - scripts/lib/sunday-scan.sh
- [[sunday_resolve_scan_image]] - code - scripts/lib/sunday-scan.sh
- [[sunday_run_scan_gate]] - code - scripts/lib/sunday-scan.sh
- [[test-sunday-upgrade-scan.sh]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[test-sunday-upgrade-scan.sh script]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh
- [[warn (fallback)]] - code - scripts/lib/sunday-scan.sh
- [[write_fake]] - code - scripts/smoke.d/test-sunday-upgrade-scan.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/sunday_run_scan_gate
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 1 edge to [[_COMMUNITY_check_upstream_cves]]
- 1 edge to [[_COMMUNITY_run_test()]]

## Top bridge nodes
- [[sunday_run_scan_gate]] - degree 10, connects to 1 community
- [[sunday-scan.sh]] - degree 8, connects to 1 community
- [[sunday_resolve_scan_image]] - degree 4, connects to 1 community
- [[check]] - degree 3, connects to 1 community
- [[run_apply]] - degree 3, connects to 1 community