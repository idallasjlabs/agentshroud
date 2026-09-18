---
type: community
cohesion: 0.09
members: 39
---

# SkillGuard

**Cohesion:** 0.09 - loosely connected
**Members:** 39 nodes

## Members
- [[.__init__()_189]] - code - gateway/security/skill_guard.py
- [[._line_at()]] - code - gateway/security/skill_guard.py
- [[._scan_opaque_blobs()]] - code - gateway/security/skill_guard.py
- [[.blocked()]] - code - gateway/security/skill_guard.py
- [[.extend()]] - code - gateway/security/skill_guard.py
- [[.recommendation()]] - code - gateway/security/skill_guard.py
- [[.scan_file()_1]] - code - gateway/security/skill_guard.py
- [[.scan_skill_tree()]] - code - gateway/security/skill_guard.py
- [[.severity()]] - code - gateway/security/skill_guard.py
- [[.test_clean_skill_allows()]] - code - gateway/tests/test_skill_guard.py
- [[.test_clean_skill_tree_allows()]] - code - gateway/tests/test_skill_guard.py
- [[.test_empty_content_allows()]] - code - gateway/tests/test_skill_guard.py
- [[A single supply-chain finding within a scanned skill artefact.]] - rationale - gateway/security/skill_guard.py
- [[ALLOW below MEDIUM, FLAG at MEDIUMHIGH, BLOCK at CRITICAL.]] - rationale - gateway/security/skill_guard.py
- [[Aggregated result of scanning a skill file or an entire skill tree.]] - rationale - gateway/security/skill_guard.py
- [[Finding]] - code - gateway/security/skill_guard.py
- [[Flag long opaque base64hex runs as probable obfuscated payloads.]] - rationale - gateway/security/skill_guard.py
- [[Highest severity across all findings (``NONE`` when clean).]] - rationale - gateway/security/skill_guard.py
- [[IntEnum]] - code
- [[Path_21]] - code - gateway/skills/scan.py
- [[Read every manifest entry under source, failing CLOSED on unreadable files.]] - rationale - gateway/skills/scan.py
- [[Recommendation]] - code - gateway/security/skill_guard.py
- [[Scan every file in a skillMCPagent tree and aggregate findings.          ``fil]] - rationale - gateway/security/skill_guard.py
- [[Scan one skill artefact (``name`` = relative path, ``content`` = text).]] - rationale - gateway/security/skill_guard.py
- [[Scan skill  MCP  agent-definition payloads for supply-chain risk.      Usage]] - rationale - gateway/security/skill_guard.py
- [[ScanResult_2]] - code - gateway/skills/scan.py
- [[ScanResult_3]] - code - gateway/security/skill_guard.py
- [[SkillGuard_1]] - code - gateway/security/skill_guard.py
- [[SkillGuard.scan_skill_tree()]] - code - gateway/security/skill_guard.py
- [[SkillsManifest.from_source()]] - code - gateway/skills/manifest.py
- [[TestCleanSkill]] - code - gateway/tests/test_skill_guard.py
- [[What the caller should do with the scanned skill.]] - rationale - gateway/security/skill_guard.py
- [[_Rule]] - code - gateway/security/skill_guard.py
- [[_build_tree()]] - code - gateway/skills/scan.py
- [[_c()]] - code - gateway/security/skill_guard.py
- [[_print_findings()]] - code - gateway/skills/scan.py
- [[main()_16]] - code - gateway/skills/scan.py
- [[scan.py]] - code - gateway/skills/scan.py
- [[skill_guard.py]] - code - gateway/security/skill_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SkillGuard
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_SkillGuard]]
- 33 edges to [[_COMMUNITY_test_skill_guard.py]]
- 4 edges to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_TrustLevel]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_DifferentialPIIDetector]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY__skills_reload_impl()]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[IntEnum]] - degree 7, connects to 6 communities
- [[SkillGuard_1]] - degree 34, connects to 5 communities
- [[ScanResult_3]] - degree 32, connects to 2 communities
- [[Recommendation]] - degree 27, connects to 2 communities
- [[skill_guard.py]] - degree 9, connects to 2 communities