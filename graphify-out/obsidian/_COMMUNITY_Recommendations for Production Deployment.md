---
type: community
members: 11
---

# Recommendations for Production Deployment

**Members:** 11 nodes

## Members
- [[7a. Image scan (Trivy, CRITICAL+HIGH, prod's currently-running tags)_1]] - document - reports/upgrade-2026-09-17.md
- [[7b. `npm audit` — browser-extension_1]] - document - reports/upgrade-2026-09-17.md
- [[7c. Python dependency audit — GAP, not silently skipped]] - document - reports/upgrade-2026-09-17.md
- [[7d. WazuhSOC alerts — partial]] - document - reports/upgrade-2026-09-17.md
- [[7e. Base images (Dockerfiles) — inventoried, not re-verified against registry]] - document - reports/upgrade-2026-09-17.md
- [[Application CVE registry (OpenClaw  Hermes agents, per `docssecuritycve-mitigation-matrix.md`)_1]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Fresh Trivy scans (run today, CRITICAL+HIGH only, `--scanners vuln`)_1]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[GitHub-hosted findings_1]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[Language dependencies_1]] - document - reports/upgrade-2026-09-06-20260906-0808.md
- [[SecurityFinding_1]] - document - docs/data/data-dictionary.md
- [[Wazuh  SOC_1]] - document - reports/upgrade-2026-09-06-20260906-0808.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Recommendations_for_Production_Deployment
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 1 edge to [[_COMMUNITY_AgentShroud Operations Cheat Sheet]]
- 1 edge to [[_COMMUNITY_killswitch.sh]]

## Top bridge nodes
- [[SecurityFinding_1]] - degree 15, connects to 3 communities
