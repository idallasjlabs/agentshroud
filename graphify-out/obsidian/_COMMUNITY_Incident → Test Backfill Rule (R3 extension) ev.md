---
type: community
cohesion: 0.13
members: 28
---

# Incident → Test Backfill Rule (R3 extension): ev

**Cohesion:** 0.13 - loosely connected
**Members:** 28 nodes

## Members
- [[.by_name()]] - code - gateway/skills/manifest.py
- [[.client()_7]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_hash_changes_when_content_changes()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_hash_is_sha256_of_content()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_planned_action_is_immutable()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_reload_requires_auth()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_reload_returns_200_with_skills_list()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_reload_returns_500_on_source_missing()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_serialise_roundtrip()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.to_dict()_15]] - code - gateway/skills/manifest.py
- [[.to_dict()_16]] - code - gateway/skills/manifest.py
- [[.to_json()]] - code - gateway/skills/manifest.py
- [[A single item in the skills manifest.]] - rationale - gateway/skills/manifest.py
- [[In-memory representation of the skillsagentsMCP manifest.]] - rationale - gateway/skills/manifest.py
- [[ManifestEntry]] - code - gateway/skills/manifest.py
- [[One unit of work in a deploy plan (canonical entry - per-bot path).      ``acti]] - rationale - gateway/skills/manifest.py
- [[PlannedAction]] - code - gateway/skills/manifest.py
- [[Return names of entries that are missing or hash-mismatched in dest.      Retu]] - rationale - gateway/skills/manifest.py
- [[SkillsManifest]] - code - gateway/skills/manifest.py
- [[TestClient_1]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestDeployDryRun]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestManifestEntry]] - code - gateway/tests/test_skills_manifest_sync.py
- [[TestSkillsReloadEndpoint]] - code - gateway/tests/test_skills_manifest_sync.py
- [[_sha256()_1]] - code - gateway/tests/test_skills_manifest_sync.py
- [[gatewayskillsmanifest.py (SkillsManifest)]] - code - gateway/skills/manifest.py
- [[manifest.py]] - code - gateway/skills/manifest.py
- [[test_skills_manifest_sync.py]] - code - gateway/tests/test_skills_manifest_sync.py
- [[validate_manifest()]] - code - gateway/skills/manifest.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Incident__Test_Backfill_Rule_R3_extension_ev
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_AWS Cloud Management & FinOps Agent]]
- 8 edges to [[_COMMUNITY_Skill Branding Specialist (BS)]]
- 3 edges to [[_COMMUNITY_TestAlertDispatcher]]
- 3 edges to [[_COMMUNITY_Daedalus — Concept Illustrator]]
- 2 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.7.0 — Red Team Remediation Plan]]

## Top bridge nodes
- [[SkillsManifest]] - degree 25, connects to 6 communities
- [[test_skills_manifest_sync.py]] - degree 18, connects to 3 communities
- [[ManifestEntry]] - degree 15, connects to 3 communities
- [[PlannedAction]] - degree 15, connects to 2 communities
- [[validate_manifest()]] - degree 9, connects to 2 communities