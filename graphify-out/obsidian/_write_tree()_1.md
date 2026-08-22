---
source_file: "gateway/tests/test_skills_manifest_sync.py"
type: "code"
community: "Skills Manifest Sync"
location: "L51"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Skills_Manifest_Sync
---

# _write_tree()

## Connections
- [[.test_build_excludes_manifest_json_itself()]] - `calls` [EXTRACTED]
- [[.test_build_includes_all_files()]] - `calls` [EXTRACTED]
- [[.test_build_is_sorted_deterministically()]] - `calls` [EXTRACTED]
- [[.test_by_name_lookup()]] - `calls` [EXTRACTED]
- [[.test_deploy_copies_files_to_dest()]] - `calls` [EXTRACTED]
- [[.test_deploy_is_idempotent()]] - `calls` [EXTRACTED]
- [[.test_deploy_overwrites_changed_content()]] - `calls` [EXTRACTED]
- [[.test_deploy_to_multiple_destinations()]] - `calls` [EXTRACTED]
- [[.test_deploy_writes_manifest_json()]] - `calls` [EXTRACTED]
- [[.test_drift_detected_on_hash_mismatch()]] - `calls` [EXTRACTED]
- [[.test_drift_detected_on_missing_file()]] - `calls` [EXTRACTED]
- [[.test_dry_run_does_not_mutate_existing_dest()]] - `calls` [EXTRACTED]
- [[.test_dry_run_writes_nothing_to_empty_dest()]] - `calls` [EXTRACTED]
- [[.test_manifest_json_in_source_is_excluded()]] - `calls` [EXTRACTED]
- [[.test_no_drift_returns_empty_list()]] - `calls` [EXTRACTED]
- [[.test_plan_classifies_create_when_dest_absent()]] - `calls` [EXTRACTED]
- [[.test_plan_classifies_skip_when_hash_matches()]] - `calls` [EXTRACTED]
- [[.test_plan_classifies_update_when_content_differs()]] - `calls` [EXTRACTED]
- [[.test_plan_is_deterministic()]] - `calls` [EXTRACTED]
- [[.test_plan_is_pure_writes_nothing()]] - `calls` [EXTRACTED]
- [[.test_plan_maps_canonical_to_each_bot_destination()]] - `calls` [EXTRACTED]
- [[.test_real_deploy_returns_actions_too()]] - `calls` [EXTRACTED]
- [[.test_reload_returns_200_with_skills_list()]] - `calls` [EXTRACTED]
- [[.test_returns_all_drifted_items()]] - `calls` [EXTRACTED]
- [[.test_serialise_contains_version_and_timestamp()]] - `calls` [EXTRACTED]
- [[Path_39]] - `references` [EXTRACTED]
- [[Write {relative_path content} under root.]] - `rationale_for` [EXTRACTED]
- [[test_skills_manifest_sync.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Skills_Manifest_Sync