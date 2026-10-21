---
source_file: "scripts/sunday-upgrade-apply.sh"
type: "code"
community: "PIIConfig"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PIIConfig
---

# sunday-upgrade-apply.sh

## Connections
- [[Base docker-compose stack]] - `references` [EXTRACTED]
- [[Drift PR (result gate, prod gate, wrapper, launchd install.sh)]] - `references` [EXTRACTED]
- [[Exclusive mkdir run lock + HEAD-pinned build guard (PR 475)]] - `rationale_for` [EXTRACTED]
- [[Exit 50 build failed and rollback failed (stack may be degraded)]] - `references` [EXTRACTED]
- [[Hermes pin silent no-op (0.21.5 while upstream 0.22.2)]] - `references` [EXTRACTED]
- [[PATH_7]] - `defines` [EXTRACTED]
- [[Refuse to build with uncommitted changes in build context]] - `rationale_for` [EXTRACTED]
- [[Sunday Upgrade Report 2026-09-06 (prod, disk-exhaustion incident)]] - `references` [EXTRACTED]
- [[Sunday Upgrade Report 2026-09-14 (dev account)]] - `references` [EXTRACTED]
- [[Sunday Upgrade Report 2026-10-18 (dev)]] - `references` [EXTRACTED]
- [[TestKnownServices]] - `shares_data_with` [INFERRED]
- [[Upgrade Report 2026-09-20 (dev, ABORTED)]] - `references` [EXTRACTED]
- [[_assert_head_unchanged()]] - `defines` [EXTRACTED]
- [[_attempt_rollback()]] - `defines` [EXTRACTED]
- [[_build_context_paths()]] - `defines` [EXTRACTED]
- [[_build_one_service()]] - `defines` [EXTRACTED]
- [[_buildable_services()]] - `defines` [EXTRACTED]
- [[_capture_pins()]] - `defines` [EXTRACTED]
- [[_container_is_up()]] - `defines` [EXTRACTED]
- [[_dirty_build_files()]] - `defines` [EXTRACTED]
- [[_docker_free_gb()]] - `defines` [EXTRACTED]
- [[_ensure_build_space()]] - `defines` [EXTRACTED]
- [[_hermes_container()]] - `defines` [EXTRACTED]
- [[_mutating()]] - `defines` [EXTRACTED]
- [[_prune_build_cache()]] - `defines` [EXTRACTED]
- [[_record_head()]] - `defines` [EXTRACTED]
- [[_release_apply_lock()]] - `defines` [EXTRACTED]
- [[_rollback_target_predates_config()]] - `defines` [EXTRACTED]
- [[_scan_json_field()]] - `defines` [EXTRACTED]
- [[_should_run()]] - `defines` [EXTRACTED]
- [[_start_lock_heartbeat()]] - `defines` [EXTRACTED]
- [[_take_apply_lock()]] - `defines` [EXTRACTED]
- [[_ts()]] - `defines` [EXTRACTED]
- [[_wait_for_docker()]] - `defines` [EXTRACTED]
- [[apply_remediation()]] - `references` [EXTRACTED]
- [[auto_remediate_cves.py]] - `conceptually_related_to` [EXTRACTED]
- [[check_noop_gate()]] - `defines` [EXTRACTED]
- [[check_openclaw()]] - `conceptually_related_to` [INFERRED]
- [[colima-health-check.sh]] - `shares_data_with` [EXTRACTED]
- [[dev-result-date.json dev-prod handoff contract]] - `shares_data_with` [EXTRACTED]
- [[die()_1]] - `defines` [EXTRACTED]
- [[err()]] - `defines` [EXTRACTED]
- [[log()_1]] - `defines` [EXTRACTED]
- [[phase_apply()]] - `defines` [EXTRACTED]
- [[phase_baseline()]] - `defines` [EXTRACTED]
- [[phase_discover()]] - `defines` [EXTRACTED]
- [[phase_preflight()]] - `defines` [EXTRACTED]
- [[phase_scan()]] - `defines` [EXTRACTED]
- [[phase_verify()]] - `defines` [EXTRACTED]
- [[sunday-scan.sh]] - `imports_from` [INFERRED]
- [[sunday-upgrade-apply.sh script]] - `contains` [EXTRACTED]
- [[sunday-upgrade.sh]] - `references` [EXTRACTED]
- [[sunday-upgrade.sh (remote-control launcher)]] - `conceptually_related_to` [INFERRED]
- [[sunday_run_scan_gate()]] - `calls` [EXTRACTED]
- [[test-sunday-upgrade-scan.sh]] - `calls` [EXTRACTED]
- [[versions.env]] - `imports_from` [INFERRED]
- [[warn()_2]] - `defines` [EXTRACTED]
- [[write_handoff()]] - `defines` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PIIConfig
