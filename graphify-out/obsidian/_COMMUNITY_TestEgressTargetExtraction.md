---
type: community
cohesion: 0.12
members: 21
---

# TestEgressTargetExtraction

**Cohesion:** 0.12 - loosely connected
**Members:** 21 nodes

## Members
- [[98-advisory CVE-triage scope gap (CosignFalcoSyftTrivyWazuh)]] - concept - reports/upgrade-2026-09-20.md
- [[ASH-OCLAW-113 auth_bypass gap (partially_mitigated)]] - concept - docs/security/cve-triage-gaps.md
- [[ASH-OCLAW-230 dos gap (under_review)]] - concept - docs/security/cve-triage-gaps.md
- [[Accepted-Risk Register for Sunday Upgrade CVE Gate]] - document - .trivyignore.yaml
- [[CVE Triage — Gaps & Development Plan (OpenClaw)]] - document - docs/security/cve-triage-gaps.md
- [[CVE-2026-60002 openssh-client no fix (accepted risk)]] - rationale - .trivyignore.yaml
- [[CVE-2026-6653 libxml2 use-after-free (accepted risk)]] - rationale - .trivyignore.yaml
- [[Cross-account dev→prod handoff contract]] - concept - prompts/sunday-upgrade.md
- [[Dev session appears hung (~17h, claude --resume agentshroud-dev)]] - concept - reports/upgrade-2026-09-20.md
- [[Gap detail (development plan)]] - document - docs/security/cve-triage-gaps.md
- [[Gap themes]] - document - docs/security/cve-triage-gaps.md
- [[Jira tracking procedure (SCRUM project)]] - concept - prompts/sunday-upgrade.md
- [[Mission_1]] - document - prompts/sunday-upgrade.md
- [[Resulting status breakdown]] - document - docs/security/cve-triage-gaps.md
- [[Run judged on state change, not steps completed (7-week no-op failure)]] - rationale - prompts/sunday-upgrade.md
- [[Sunday Upgrade Report — 2026-09-20 (PROD run, full)]] - document - reports/upgrade-2026-09-20.md
- [[Sunday Upgrade — 2026-09-20 PROD run header (dev handoff check)]] - document - reports/upgrade-2026-09-20-20260920-0802.md
- [[Trivy scan delta vs 2026-09-17 (1.7.0 images)]] - concept - reports/upgrade-2026-09-20.md
- [[Two remediation arms — vendor fix (Arm 1) vs AgentShroud gateway control (Arm 2)]] - rationale - prompts/sunday-upgrade.md
- [[cve-triage-gaps]] - document - docs/security/cve-triage-gaps.md
- [[scriptssunday-upgrade-apply.sh deterministic script + exit codes]] - concept - prompts/sunday-upgrade.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressTargetExtraction
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_auth.py]]
- 3 edges to [[_COMMUNITY_Skills by Category]]
- 1 edge to [[_COMMUNITY_2. Security Analysis]]

## Top bridge nodes
- [[Sunday Upgrade Report — 2026-09-20 (PROD run, full)]] - degree 11, connects to 2 communities
- [[CVE Triage — Gaps & Development Plan (OpenClaw)]] - degree 8, connects to 1 community
- [[Mission_1]] - degree 6, connects to 1 community
- [[scriptssunday-upgrade-apply.sh deterministic script + exit codes]] - degree 4, connects to 1 community
- [[Cross-account dev→prod handoff contract]] - degree 4, connects to 1 community