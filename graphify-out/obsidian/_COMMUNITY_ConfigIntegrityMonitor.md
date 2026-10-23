---
type: community
cohesion: 0.11
members: 34
---

# ConfigIntegrityMonitor

**Cohesion:** 0.11 - loosely connected
**Members:** 34 nodes

## Members
- [[dot-__init__()_104]] - code - gateway/security/skill_guard.py
- [[dot-_line_at()]] - code - gateway/security/skill_guard.py
- [[dot-_scan_opaque_blobs()]] - code - gateway/security/skill_guard.py
- [[dot-blocked()]] - code - gateway/security/skill_guard.py
- [[dot-extend()]] - code - gateway/security/skill_guard.py
- [[dot-recommendation()]] - code - gateway/security/skill_guard.py
- [[dot-scan_file()_1]] - code - gateway/security/skill_guard.py
- [[dot-scan_skill_tree()]] - code - gateway/security/skill_guard.py
- [[dot-severity()]] - code - gateway/security/skill_guard.py
- [[A single supply-chain finding within a scanned skill artefact.]] - rationale - gateway/security/skill_guard.py
- [[ALLOW below MEDIUM, FLAG at MEDIUMHIGH, BLOCK at CRITICAL.]] - rationale - gateway/security/skill_guard.py
- [[Aggregated result of scanning a skill file or an entire skill tree.]] - rationale - gateway/security/skill_guard.py
- [[CompletedProcess_3]] - code - gateway/tests/test_skill_guard.py
- [[Finding]] - code - gateway/security/skill_guard.py
- [[Flag long opaque base64hex runs as probable obfuscated payloads.]] - rationale - gateway/security/skill_guard.py
- [[Highest severity across all findings (``NONE`` when clean).]] - rationale - gateway/security/skill_guard.py
- [[Path_27]] - code - gateway/skills/scan.py
- [[Read every manifest entry under source, failing CLOSED on unreadable files.]] - rationale - gateway/skills/scan.py
- [[Recommendation]] - code - gateway/security/skill_guard.py
- [[Scan every file in a skillMCPagent tree and aggregate findings.          ``fil]] - rationale - gateway/security/skill_guard.py
- [[Scan one skill artefact (``name`` = relative path, ``content`` = text).]] - rationale - gateway/security/skill_guard.py
- [[Scan skill  MCP  agent-definition payloads for supply-chain risk.      Usage]] - rationale - gateway/security/skill_guard.py
- [[ScanResult_2]] - code - gateway/skills/scan.py
- [[ScanResult_3]] - code - gateway/tests/test_skill_guard.py
- [[ScanResult_4]] - code - gateway/security/skill_guard.py
- [[SkillGuard_1]] - code - gateway/security/skill_guard.py
- [[What the caller should do with the scanned skill.]] - rationale - gateway/security/skill_guard.py
- [[_Rule]] - code - gateway/security/skill_guard.py
- [[_build_tree()]] - code - gateway/skills/scan.py
- [[_c()]] - code - gateway/security/skill_guard.py
- [[_print_findings()]] - code - gateway/skills/scan.py
- [[main()_11]] - code - gateway/skills/scan.py
- [[scan.py]] - code - gateway/skills/scan.py
- [[skill_guard.py]] - code - gateway/security/skill_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConfigIntegrityMonitor
SORT file.name ASC
```

## Connections to other communities
- 43 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 23 edges to [[_COMMUNITY_AuditStore]]
- 4 edges to [[_COMMUNITY_SecurityPipeline (3)]]
- 2 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[SkillGuard_1]] - degree 34, connects to 4 communities
- [[skill_guard.py]] - degree 9, connects to 3 communities
- [[ScanResult_4]] - degree 32, connects to 2 communities
- [[Recommendation]] - degree 27, connects to 2 communities
- [[scan.py]] - degree 8, connects to 2 communities
