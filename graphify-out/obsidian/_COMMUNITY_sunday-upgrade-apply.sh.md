---
type: community
cohesion: 0.07
members: 67
---

# sunday-upgrade-apply.sh

**Cohesion:** 0.07 - loosely connected
**Members:** 67 nodes

## Members
- [[ColimaDocker VM Storage Exhaustion]] - concept - reports/upgrade-2026-09-06-prod.md
- [[Dev-to-Prod Handoff Contract]] - concept - scripts/sunday-upgrade-apply.sh
- [[PATH_55]] - code - scripts/sunday-upgrade-apply.sh
- [[Preflight git hygiene graphify-out never counts as dirty; pathspec-scoped commits only]] - rationale - prompts/sunday-upgrade.md
- [[Prove the Outcome, Never the Steps]] - rationale - CLAUDE.md
- [[Sunday Upgrade Report 2026-08-30 (0734 first-pass abort)]] - document - reports/upgrade-2026-08-30-20260830-2009.md
- [[Sunday Upgrade Report 2026-08-30 (final)]] - document - reports/upgrade-2026-08-30.md
- [[Sunday Upgrade Report 2026-08-30 (local-llms upgrade requested)]] - document - reports/upgrade-2026-08-30-20260830-2010.md
- [[Sunday Upgrade Report 2026-09-06 (prod read-only, pre-crisis)]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Sunday Upgrade Report 2026-09-06 (prod, disk-exhaustion incident)]] - document - reports/upgrade-2026-09-06-prod.md
- [[Sunday Upgrade Report Hermes-cron Delivery]] - code - scripts/hermes-cron/sunday-upgrade-report.sh
- [[Wazuh-Agent Sidecar Split (SIDECAR-GAP-001 resolution)]] - concept - reports/upgrade-2026-09-06-prod.md
- [[_assert_head_unchanged]] - code - scripts/sunday-upgrade-apply.sh
- [[_assert_head_unchanged()]] - code - scripts/sunday-upgrade-apply.sh
- [[_attempt_rollback]] - code - scripts/sunday-upgrade-apply.sh
- [[_attempt_rollback()]] - code - scripts/sunday-upgrade-apply.sh
- [[_build_context_paths()]] - code - scripts/sunday-upgrade-apply.sh
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
- [[check_noop_gate()]] - code - scripts/sunday-upgrade-apply.sh
- [[die()_1]] - code - scripts/sunday-upgrade-apply.sh
- [[err()]] - code - scripts/sunday-upgrade-apply.sh
- [[log()_8]] - code - scripts/sunday-upgrade-apply.sh
- [[op-to-keychain.sh]] - code - scripts/op-to-keychain.sh
- [[op-to-keychain.sh script]] - code - scripts/op-to-keychain.sh
- [[phase_apply()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_baseline()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_discover()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_preflight()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_scan()]] - code - scripts/sunday-upgrade-apply.sh
- [[phase_verify()]] - code - scripts/sunday-upgrade-apply.sh
- [[sunday-upgrade-apply.sh]] - code - scripts/sunday-upgrade-apply.sh
- [[sunday-upgrade-apply.sh exit-code contract (0102025304050127)]] - rationale - prompts/sunday-upgrade.md
- [[sunday-upgrade-apply.sh main flow]] - code - scripts/sunday-upgrade-apply.sh
- [[sunday-upgrade-apply.sh script]] - code - scripts/sunday-upgrade-apply.sh
- [[sunday-upgrade.sh (remote-control launcher)]] - code - scripts/sunday-upgrade.sh
- [[warn()_4]] - code - scripts/sunday-upgrade-apply.sh
- [[write_handoff()]] - code - scripts/sunday-upgrade-apply.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/sunday-upgrade-applysh
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_colima-health-check.sh]]
- 5 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 3 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)_1]]
- 2 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 2 edges to [[_COMMUNITY_test-sunday-upgrade-scan.sh]]
- 2 edges to [[_COMMUNITY_plan_remediation]]
- 1 edge to [[_COMMUNITY_asb (AgentShroud Bot helper)]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh_1]]
- 1 edge to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_setup-secrets.sh]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]
- 1 edge to [[_COMMUNITY_main]]

## Top bridge nodes
- [[sunday-upgrade-apply.sh]] - degree 63, connects to 10 communities
- [[phase_apply()]] - degree 26, connects to 2 communities
- [[check_noop_gate()]] - degree 13, connects to 2 communities
- [[phase_discover()]] - degree 9, connects to 2 communities
- [[Prove the Outcome, Never the Steps]] - degree 4, connects to 2 communities
