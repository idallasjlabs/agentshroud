---
type: community
cohesion: 0.07
members: 66
---

# sunday-upgrade-apply.sh

**Cohesion:** 0.07 - loosely connected
**Members:** 66 nodes

## Members
- [[AgentShroud CLAUDE.md operating rules]] - document - CLAUDE.md
- [[Baseline phase logs PASS with 0 images captured]] - concept - reports/upgrade-2026-09-22.md
- [[ColimaDocker VM Storage Exhaustion]] - concept - reports/upgrade-2026-09-06-prod.md
- [[Dev-to-Prod Handoff Contract]] - concept - scripts/sunday-upgrade-apply.sh
- [[No-Op Upgrade Gate (7-week silent no-op)]] - concept - scripts/sunday-upgrade-apply.sh
- [[No-op gate false negative baseline captured after pin commits]] - concept - reports/upgrade-2026-09-25.md
- [[PATH_1]] - code - scripts/sunday-upgrade-apply.sh
- [[Prove the Outcome, Never the Steps]] - rationale - CLAUDE.md
- [[SUNDAY_BUILD_VIA_VM=1 detached in-VM build]] - rationale - reports/upgrade-2026-09-23-20260923-1400.md
- [[Sunday Upgrade Report 2026-09-06 (prod read-only, pre-crisis)]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Sunday Upgrade Report 2026-09-06 (prod, disk-exhaustion incident)]] - document - reports/upgrade-2026-09-06-prod.md
- [[Sunday Upgrade Report Hermes-cron Delivery]] - code - scripts/hermes-cron/sunday-upgrade-report.sh
- [[Weekly Upgrades EVERYTHING Means Everything]] - rationale - CLAUDE.md
- [[_assert_head_unchanged]] - code - scripts/sunday-upgrade-apply.sh
- [[_assert_head_unchanged()]] - code - scripts/sunday-upgrade-apply.sh
- [[_attempt_rollback]] - code - scripts/sunday-upgrade-apply.sh
- [[_attempt_rollback()]] - code - scripts/sunday-upgrade-apply.sh
- [[_build_context_paths()]] - code - scripts/sunday-upgrade-apply.sh
- [[_build_one_service]] - code - scripts/sunday-upgrade-apply.sh
- [[_build_one_service()]] - code - scripts/sunday-upgrade-apply.sh
- [[_buildable_services]] - code - scripts/sunday-upgrade-apply.sh
- [[_buildable_services()]] - code - scripts/sunday-upgrade-apply.sh
- [[_capture_pins]] - code - scripts/sunday-upgrade-apply.sh
- [[_capture_pins()]] - code - scripts/sunday-upgrade-apply.sh
- [[_container_is_up]] - code - scripts/sunday-upgrade-apply.sh
- [[_container_is_up()]] - code - scripts/sunday-upgrade-apply.sh
- [[_dirty_build_files]] - code - scripts/sunday-upgrade-apply.sh
- [[_dirty_build_files()]] - code - scripts/sunday-upgrade-apply.sh
- [[_docker_free_gb()]] - code - scripts/sunday-upgrade-apply.sh
- [[_ensure_build_space]] - code - scripts/sunday-upgrade-apply.sh
- [[_ensure_build_space()]] - code - scripts/sunday-upgrade-apply.sh
- [[_hermes_container]] - code - scripts/sunday-upgrade-apply.sh
- [[_hermes_container()]] - code - scripts/sunday-upgrade-apply.sh
- [[_mutating()]] - code - scripts/sunday-upgrade-apply.sh
- [[_prune_build_cache]] - code - scripts/sunday-upgrade-apply.sh
- [[_prune_build_cache()]] - code - scripts/sunday-upgrade-apply.sh
- [[_record_head]] - code - scripts/sunday-upgrade-apply.sh
- [[_record_head()]] - code - scripts/sunday-upgrade-apply.sh
- [[_release_apply_lock()]] - code - scripts/sunday-upgrade-apply.sh
- [[_rollback_target_predates_config]] - code - scripts/sunday-upgrade-apply.sh
- [[_rollback_target_predates_config()]] - code - scripts/sunday-upgrade-apply.sh
- [[_scan_json_field()]] - code - scripts/sunday-upgrade-apply.sh
- [[_should_run()]] - code - scripts/sunday-upgrade-apply.sh
- [[_start_lock_heartbeat]] - code - scripts/sunday-upgrade-apply.sh
- [[_start_lock_heartbeat()]] - code - scripts/sunday-upgrade-apply.sh
- [[_take_apply_lock]] - code - scripts/sunday-upgrade-apply.sh
- [[_take_apply_lock()]] - code - scripts/sunday-upgrade-apply.sh
- [[_ts()]] - code - scripts/sunday-upgrade-apply.sh
- [[_wait_for_docker]] - code - scripts/sunday-upgrade-apply.sh
- [[_wait_for_docker()]] - code - scripts/sunday-upgrade-apply.sh
- [[asb Bot Helper Script]] - code - scripts/asb
- [[check_noop_gate()]] - code - scripts/sunday-upgrade-apply.sh
- [[die()]] - code - scripts/sunday-upgrade-apply.sh
- [[err()]] - code - scripts/sunday-upgrade-apply.sh
- [[log()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_apply()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_baseline()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_preflight()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_scan()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_verify()]] - code - scripts/sunday-upgrade-apply.sh
- [[sunday-upgrade-apply.sh]] - code - scripts/sunday-upgrade-apply.sh
- [[sunday-upgrade-apply.sh main flow]] - code - scripts/sunday-upgrade-apply.sh
- [[sunday-upgrade-apply.sh script]] - code - scripts/sunday-upgrade-apply.sh
- [[sunday-upgrade.sh (remote-control launcher)]] - code - scripts/sunday-upgrade.sh
- [[warn()]] - code - scripts/sunday-upgrade-apply.sh
- [[write_handoff()]] - code - scripts/sunday-upgrade-apply.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/sunday-upgrade-applysh
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_colima-health-check.sh]]
- 8 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 7 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 6 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 2 edges to [[_COMMUNITY_test-sunday-upgrade-scan.sh]]
- 2 edges to [[_COMMUNITY_asb (AgentShroud Bot helper)]]
- 2 edges to [[_COMMUNITY_plan_remediation]]
- 2 edges to [[_COMMUNITY_The run is judged on state change, not steps completed]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_Commit list 2026-10-10 through 2026-10-16 on main]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]
- 1 edge to [[_COMMUNITY_8. Governance Model]]
- 1 edge to [[_COMMUNITY_main]]

## Top bridge nodes
- [[sunday-upgrade-apply.sh]] - degree 65, connects to 10 communities
- [[check_noop_gate()]] - degree 13, connects to 2 communities
- [[sunday-upgrade-apply.sh main flow]] - degree 9, connects to 2 communities
- [[No-op gate false negative baseline captured after pin commits]] - degree 8, connects to 2 communities
- [[Baseline phase logs PASS with 0 images captured]] - degree 4, connects to 2 communities
