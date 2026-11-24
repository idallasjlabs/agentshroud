---
type: community
members: 57
---

# .from_source

**Members:** 57 nodes

## Members
- [[dot-from_source()]] - code - gateway/skills/manifest.py
- [[dot-test_build_excludes_manifest_json_itself()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_build_includes_all_files()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_build_is_sorted_deterministically()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_by_name_lookup()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_deploy_copies_files_to_dest()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_deploy_is_idempotent()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_deploy_overwrites_changed_content()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_deploy_to_multiple_destinations()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_deploy_writes_manifest_json()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_drift_detected_on_hash_mismatch()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_drift_detected_on_missing_file()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_dry_run_does_not_mutate_existing_dest()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_dry_run_writes_nothing_to_empty_dest()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_from_empty_source_raises()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_manifest_json_in_source_is_excluded()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_missing_source_raises()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_no_drift_returns_empty_list()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_plan_classifies_create_when_dest_absent()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_plan_classifies_skip_when_hash_matches()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_plan_classifies_update_when_content_differs()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_plan_is_deterministic()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_plan_is_pure_writes_nothing()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_plan_maps_canonical_to_each_bot_destination()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_planned_action_is_immutable()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_real_deploy_returns_actions_too()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_returns_all_drifted_items()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_serialise_contains_version_and_timestamp()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-to_dict()_14]] - code - gateway/skills/manifest.py
- [[dot-to_json()]] - code - gateway/skills/manifest.py
- [[An empty source directory must raise ValueError.]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[Build a manifest by walking source (``~.llm_settings``). Raises…]] - rationale - gateway/skills/manifest.py
- [[Compute the deploy plan without mutating the filesystem. Pure with respect to…]] - rationale - gateway/skills/manifest.py
- [[Copy all files in manifest from source to each per-bot destination.…]] - rationale - gateway/skills/manifest.py
- [[In-memory representation of the skillsagentsMCP manifest.]] - rationale - gateway/skills/manifest.py
- [[One unit of work in a deploy plan (canonical entry - per-bot path). ``action``…]] - rationale - gateway/skills/manifest.py
- [[Path_71]] - code
- [[Path_72]] - code
- [[PlannedAction]] - code - gateway/skills/manifest.py
- [[Return names of entries that are missing or hash-mismatched in dest. Returns…]] - rationale - gateway/skills/manifest.py
- [[Skills manifest — build, deploy, and validate the canonical skillsagentsMCP…]] - rationale - gateway/skills/manifest.py
- [[SkillsManifest]] - code - gateway/skills/manifest.py
- [[TestDeployDryRun]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestDeployManifest]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestPlanDeploy]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestSkillsManifest]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestValidateManifest]] - code - gateway/tests/test_skills_manifest_sync.py
- [[Tests for skills manifest sync (Workstream D). TDD these tests were written…]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[The plan is a pure function it maps canonical source entries to each per-bot…]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[Write {relative_path content} under root.]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[_write_tree()_1]] - code - gateway/tests/test_skills_manifest_sync.py
- [[deploy_manifest()]] - code - gateway/skills/manifest.py
- [[manifest.json must never appear as an entry even when present in source.]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[manifest.py]] - code - gateway/skills/manifest.py
- [[plan_deploy()]] - code - gateway/skills/manifest.py
- [[test_skills_manifest_sync.py]] - code - gateway/tests/test_skills_manifest_sync.py
- [[validate_manifest()]] - code - gateway/skills/manifest.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/from_source
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_ManifestEntry]]
- 7 edges to [[_COMMUNITY_TestSkillsReloadEndpoint]]
- 3 edges to [[_COMMUNITY_ScanResult_1]]
- 3 edges to [[_COMMUNITY_api.py]]
- 3 edges to [[_COMMUNITY__skills_reload_impl]]
- 1 edge to [[_COMMUNITY_require_auth]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[SkillsManifest]] - degree 20, connects to 5 communities
- [[test_skills_manifest_sync.py]] - degree 20, connects to 5 communities
- [[dot-from_source()]] - degree 33, connects to 4 communities
- [[deploy_manifest()]] - degree 24, connects to 3 communities
- [[Path_72]] - degree 33, connects to 2 communities
