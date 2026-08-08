---
source_file: "gateway/skills/manifest.py"
type: "code"
community: "Gateway Test Suite"
location: "L204"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# deploy_manifest()

## Connections
- [[.test_deploy_copies_files_to_dest()]] - `calls` [EXTRACTED]
- [[.test_deploy_is_idempotent()]] - `calls` [EXTRACTED]
- [[.test_deploy_overwrites_changed_content()]] - `calls` [EXTRACTED]
- [[.test_deploy_to_multiple_destinations()]] - `calls` [EXTRACTED]
- [[.test_deploy_writes_manifest_json()]] - `calls` [EXTRACTED]
- [[.test_drift_detected_on_hash_mismatch()]] - `calls` [EXTRACTED]
- [[.test_drift_detected_on_missing_file()]] - `calls` [EXTRACTED]
- [[.test_dry_run_does_not_mutate_existing_dest()]] - `calls` [EXTRACTED]
- [[.test_dry_run_writes_nothing_to_empty_dest()]] - `calls` [EXTRACTED]
- [[.test_no_drift_returns_empty_list()]] - `calls` [EXTRACTED]
- [[.test_plan_classifies_skip_when_hash_matches()]] - `calls` [EXTRACTED]
- [[.test_plan_classifies_update_when_content_differs()]] - `calls` [EXTRACTED]
- [[.test_real_deploy_returns_actions_too()]] - `calls` [EXTRACTED]
- [[.test_reload_returns_200_with_skills_list()]] - `calls` [EXTRACTED]
- [[.test_returns_all_drifted_items()]] - `calls` [EXTRACTED]
- [[.to_json()]] - `calls` [EXTRACTED]
- [[Copy all files in manifest from source to each per-bot destination.      Beh]] - `rationale_for` [EXTRACTED]
- [[Path_20]] - `references` [EXTRACTED]
- [[PlannedAction]] - `references` [EXTRACTED]
- [[SkillsManifest]] - `references` [EXTRACTED]
- [[_skills_reload_impl()]] - `calls` [EXTRACTED]
- [[api.py]] - `imports` [EXTRACTED]
- [[manifest.py]] - `contains` [EXTRACTED]
- [[plan_deploy()]] - `calls` [EXTRACTED]
- [[test_skills_manifest_sync.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite