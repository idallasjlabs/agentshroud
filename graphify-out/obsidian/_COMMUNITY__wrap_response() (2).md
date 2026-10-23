---
type: community
cohesion: 0.05
members: 48
---

# _wrap_response() (2)

**Cohesion:** 0.05 - loosely connected
**Members:** 48 nodes

## Members
- [[ASH-OCLAW-113 auth_bypass partially_mitigated (running 2026.9.8, fixed_in None)]] - concept - docs/security/cve-triage-gaps.md
- [[ASH-OCLAW-230 dos under_review (running 2026.9.8, fixed_in None)]] - concept - docs/security/cve-triage-gaps.md
- [[Anti-security-theater value]] - rationale - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Base docker-compose stack]] - code - docker/docker-compose.yml
- [[CVE Triage — Gaps & Development Plan (OpenClaw), 891 triaged]] - document - docs/security/cve-triage-gaps.md
- [[CVE gap report built from invocation delta, not registry state]] - concept - reports/upgrade-2026-09-24.md
- [[ClamAV upstream vs Debian lag finding]] - concept - prompts/sunday-upgrade.md
- [[Collaborator workspace SOUL.md (Isaiah persona)]] - document - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Compose network version-label mismatch forces network recreate]] - concept - reports/upgrade-2026-10-12.md
- [[Current Focus (AgentShroud v1.7.x)]] - concept - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Dev-to-prod handoff contract (dev-result JSON + dev-merge-commit)]] - concept - prompts/sunday-upgrade.md
- [[EVERYTHING MEANS EVERYTHING inventory scope]] - rationale - prompts/sunday-upgrade.md
- [[Exit 25 NOTHING_UPGRADED]] - concept - prompts/sunday-upgrade.md
- [[Exit code contract (01015202125304050127)]] - concept - prompts/sunday-upgrade.md
- [[Features Prompt Injection Defense, PII Sanitization, Egress Filtering, Human-in-the-Loop, IEC 62443]] - concept - docs/index.html
- [[GitHub Actions version inventory (first time in scope)]] - concept - reports/upgrade-2026-10-12.md
- [[Goal any agent wrappable with gateway protection]] - concept - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Hard 0800 ET availability window]] - rationale - prompts/sunday-upgrade.md
- [[Host trivy cannot reach registries (scans_failed=3 root cause)]] - concept - reports/upgrade-2026-10-18.md
- [[Jira SCRUM run-ticket tracking]] - concept - prompts/sunday-upgrade.md
- [[Non-agent components not inventoried]] - concept - reports/upgrade-2026-10-18.md
- [[Partial progress ships (not all-or-nothing)]] - rationale - prompts/sunday-upgrade.md
- [[Presidio PII detection deps (analyzeranonymizerspacy)]] - code - gateway/requirements.txt
- [[Prod promotion BLOCKED (0800 window)]] - concept - reports/upgrade-2026-10-18.md
- [[Proxy-layer inversion pattern]] - concept - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Run judged on state change, not steps completed]] - rationale - prompts/sunday-upgrade.md
- [[S5 docker-compose.yml does not bind port 8080 to 0.0.0.0]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Seven-week no-op upgrade failure (2026-07-29 to 2026-09-15)]] - concept - prompts/sunday-upgrade.md
- [[Sunday Upgrade Report 2026-10-18 (dev)]] - document - reports/upgrade-2026-10-18.md
- [[Sunday Upgrade prompt (weekly maintenance run)]] - document - prompts/sunday-upgrade.md
- [[Tap-approval pipeline (PR 502)]] - concept - reports/upgrade-2026-10-12.md
- [[Transitive-dependency security floors (pip-audit gate)]] - rationale - gateway/requirements.txt
- [[Two-arm CVE remediation (vendor fix + AgentShroud gateway control)]] - rationale - prompts/sunday-upgrade.md
- [[Two-pass pip-audit (bump, re-audit, bump again)]] - rationale - reports/upgrade-2026-10-12.md
- [[Unattended PR auto-merge gates]] - concept - prompts/sunday-upgrade.md
- [[Upgrade Report 2026-10-12 (dev, on-demand, PARTIAL)]] - document - reports/upgrade-2026-10-12.md
- [[Upgrade report reportsupgrade-YYYY-MM-DD.md (8 sections, incremental writes)]] - document - prompts/sunday-upgrade.md
- [[gatewayrequirements.txt]] - code - gateway/requirements.txt
- [[python-jose removal (CVE-2024-3366333664)]] - rationale - gateway/requirements.txt
- [[scriptscheck-soak-status.sh (SOAKED gate)]] - code - prompts/sunday-upgrade.md
- [[scriptssunday-rollback.sh  rollback.sh]] - code - prompts/sunday-upgrade.md
- [[scriptssunday-upgrade-apply.sh (deterministic gates)]] - code - prompts/sunday-upgrade.md
- [[scriptstriage-cve-mitigations.py (Coverage FULLPARTIALNONE)]] - code - prompts/sunday-upgrade.md
- [[sunday-rollback.sh]] - code - scripts/sunday-rollback.sh
- [[sunday-rollback.sh script]] - code - scripts/sunday-rollback.sh
- [[sunday-upgrade-approve.sh]] - code - scripts/sunday-upgrade-approve.sh
- [[sunday-upgrade-approve.sh script]] - code - scripts/sunday-upgrade-approve.sh
- [[websockets 16.1.1 - 17.1 Sunday upgrade bump]] - rationale - gateway/requirements.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_wrap_response_2
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY__make_sanitizer()]]
- 5 edges to [[_COMMUNITY_run-standalone.sh]]
- 3 edges to [[_COMMUNITY_One Shroud Over Every Wire (founding mantra)]]
- 2 edges to [[_COMMUNITY_dot-_run_and_read]]
- 2 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_Sunday Upgrade prompt]]
- 1 edge to [[_COMMUNITY_AgentShroud Sunday Upgrade — 2026-09-06 (dev-only, read-only inventory → scoped fixes)]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_run_multi_host]]

## Top bridge nodes
- [[Sunday Upgrade prompt (weekly maintenance run)]] - degree 18, connects to 4 communities
- [[Sunday Upgrade Report 2026-10-18 (dev)]] - degree 11, connects to 3 communities
- [[Base docker-compose stack]] - degree 8, connects to 3 communities
- [[CVE gap report built from invocation delta, not registry state]] - degree 4, connects to 3 communities
- [[CVE Triage — Gaps & Development Plan (OpenClaw), 891 triaged]] - degree 6, connects to 2 communities
