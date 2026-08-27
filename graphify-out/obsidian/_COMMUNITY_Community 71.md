---
type: community
members: 68
---

# Community 71

**Members:** 68 nodes

## Members
- [[.by_name()]] - code - gateway/skills/manifest.py
- [[.client()_7]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_build_excludes_manifest_json_itself()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_build_includes_all_files()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_build_is_sorted_deterministically()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_by_name_lookup()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_deploy_copies_files_to_dest()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_deploy_is_idempotent()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_deploy_overwrites_changed_content()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_deploy_to_multiple_destinations()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_deploy_writes_manifest_json()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_drift_detected_on_hash_mismatch()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_drift_detected_on_missing_file()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_dry_run_does_not_mutate_existing_dest()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_dry_run_writes_nothing_to_empty_dest()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_from_empty_source_raises()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_hash_changes_when_content_changes()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_hash_is_sha256_of_content()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_manifest_json_in_source_is_excluded()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_missing_source_raises()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_no_drift_returns_empty_list()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_classifies_create_when_dest_absent()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_classifies_skip_when_hash_matches()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_classifies_update_when_content_differs()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_is_deterministic()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_is_pure_writes_nothing()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_maps_canonical_to_each_bot_destination()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_planned_action_is_immutable()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_real_deploy_returns_actions_too()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_reload_requires_auth()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_reload_returns_200_with_skills_list()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_reload_returns_500_on_source_missing()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_returns_all_drifted_items()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_serialise_contains_version_and_timestamp()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_serialise_roundtrip()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.to_dict()_15]] - code - gateway/skills/manifest.py
- [[.to_dict()_16]] - code - gateway/skills/manifest.py
- [[.to_json()]] - code - gateway/skills/manifest.py
- [[A single item in the skills manifest.]] - rationale - gateway/skills/manifest.py
- [[An empty source directory must raise ValueError.]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[Compute the deploy plan without mutating the filesystem.      Pure with respect]] - rationale - gateway/skills/manifest.py
- [[Copy all files in manifest from source to each per-bot destination.      Beh]] - rationale - gateway/skills/manifest.py
- [[In-memory representation of the skillsagentsMCP manifest.]] - rationale - gateway/skills/manifest.py
- [[ManifestEntry]] - code - gateway/skills/manifest.py
- [[One unit of work in a deploy plan (canonical entry - per-bot path).      ``acti]] - rationale - gateway/skills/manifest.py
- [[Path_39]] - code - gateway/tests/test_skills_manifest_sync.py
- [[PlannedAction]] - code - gateway/skills/manifest.py
- [[Return names of entries that are missing or hash-mismatched in dest.      Retu]] - rationale - gateway/skills/manifest.py
- [[SkillsManifest]] - code - gateway/skills/manifest.py
- [[TestClient_1]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestDeployDryRun]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestDeployManifest]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestManifestEntry]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestPlanDeploy]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestSkillsManifest]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestSkillsReloadEndpoint]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestValidateManifest]] - code - gateway/tests/test_skills_manifest_sync.py
- [[The plan is a pure function it maps canonical source entries to each     per-bo]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[Write {relative_path content} under root.]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[_sha256()_1]] - code - gateway/tests/test_skills_manifest_sync.py
- [[_write_tree()_1]] - code - gateway/tests/test_skills_manifest_sync.py
- [[deploy_manifest()]] - code - gateway/skills/manifest.py
- [[gatewayskillsmanifest.py (SkillsManifest)]] - code - gateway/skills/manifest.py
- [[manifest.json must never appear as an entry even when present in source.]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[manifest.py]] - code - gateway/skills/manifest.py
- [[plan_deploy()]] - code - gateway/skills/manifest.py
- [[test_skills_manifest_sync.py]] - code - gateway/tests/test_skills_manifest_sync.py
- [[validate_manifest()]] - code - gateway/skills/manifest.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_71
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 557]]
- 4 edges to [[_COMMUNITY_Community 110]]
- 2 edges to [[_COMMUNITY_Community 45]]
- 2 edges to [[_COMMUNITY_Community 1349]]
- 1 edge to [[_COMMUNITY_Community 113]]
- 1 edge to [[_COMMUNITY_Community 31]]

## Top bridge nodes
- [[SkillsManifest]] - degree 25, connects to 4 communities
- [[deploy_manifest()]] - degree 25, connects to 3 communities
- [[test_skills_manifest_sync.py]] - degree 18, connects to 2 communities
- [[ManifestEntry]] - degree 15, connects to 1 community
- [[plan_deploy()]] - degree 13, connects to 1 community