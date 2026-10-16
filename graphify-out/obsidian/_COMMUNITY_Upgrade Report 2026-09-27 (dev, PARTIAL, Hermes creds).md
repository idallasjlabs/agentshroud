---
type: community
cohesion: 0.10
members: 26
---

# Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)

**Cohesion:** 0.10 - loosely connected
**Members:** 26 nodes

## Members
- [[CI security-scan job (pip-audit dry-run)]] - code - .github/workflows/ci.yml
- [[Compose network version-label mismatch forces network recreate]] - concept - reports/upgrade-2026-10-12.md
- [[Dev-prod handoff contract via UsersSharedagentshroud-sundaydev-result-YYYY-MM-DD.json]] - rationale - prompts/sunday-upgrade.md
- [[GitHub Actions version inventory (first time in scope)]] - concept - reports/upgrade-2026-10-12.md
- [[Human tap-approval gates PR merge (dev) and prod cutover, each independent]] - rationale - prompts/sunday-upgrade.md
- [[Jira tracking per Sunday run (project SCRUM, phase comments, Done only on ALL GREEN)]] - rationale - prompts/sunday-upgrade.md
- [[Outcome taxonomy UPGRADED  HELD BACK  BLOCKED  FAILED  PENDING APPROVAL]] - rationale - prompts/sunday-upgrade.md
- [[Python dependency audit job (pip-audit, fails on any vuln)]] - code - .github/workflows/security-scan.yml
- [[Report reportsupgrade-YYYY-MM-DD.md 8 sections written to disk as each completes, unconditional]] - rationale - prompts/sunday-upgrade.md
- [[S5 docker-compose.yml does not bind port 8080 to 0.0.0.0]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Streaming direct voice path (_call_llm_stream)]] - concept - CHANGELOG.md
- [[Sunday upgrade mission every component in dev and prod to latest stable, resolve every finding, dev first]] - document - prompts/sunday-upgrade.md
- [[Tap-approval pipeline (PR 502)]] - concept - reports/upgrade-2026-10-12.md
- [[Transitive-dependency security floors (cryptography, setuptools, multidict, urllib3, anyio, idna, starlette)]] - rationale - gateway/requirements.txt
- [[Trivy action immutable SHA pin (CI supply chain)]] - rationale - CHANGELOG.md
- [[Two-pass pip-audit (bump, re-audit, bump again)]] - rationale - reports/upgrade-2026-10-12.md
- [[Upgrade Report 2026-10-12 (dev, on-demand, PARTIAL)]] - document - reports/upgrade-2026-10-12.md
- [[Upstream-advisory watch cron jobs (8 toolchain components)]] - concept - CHANGELOG.md
- [[dockerdocker-compose.yml]] - code - docker/docker-compose.yml
- [[promptssunday-upgrade.md (Sunday mission procedure)]] - document - prompts/sunday-upgrade.md
- [[sunday-rollback.sh]] - code - scripts/sunday-rollback.sh
- [[sunday-rollback.sh script]] - code - scripts/sunday-rollback.sh
- [[sunday-upgrade-approve.sh]] - code - scripts/sunday-upgrade-approve.sh
- [[sunday-upgrade-approve.sh script]] - code - scripts/sunday-upgrade-approve.sh
- [[v1.5.1 — A2A Governance patch release]] - document - CHANGELOG.md
- [[v1.6.0 — voice terminal release]] - document - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Upgrade_Report_2026-09-27_dev_PARTIAL_Hermes_creds
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_colima-health-check.sh]]
- 2 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 2 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 2 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_plan_remediation]]
- 1 edge to [[_COMMUNITY_triage-cve-mitigations.py]]

## Top bridge nodes
- [[dockerdocker-compose.yml]] - degree 7, connects to 2 communities
- [[Sunday upgrade mission every component in dev and prod to latest stable, resolve every finding, dev first]] - degree 7, connects to 2 communities
- [[promptssunday-upgrade.md (Sunday mission procedure)]] - degree 5, connects to 2 communities
- [[Upgrade Report 2026-10-12 (dev, on-demand, PARTIAL)]] - degree 10, connects to 1 community
- [[Dev-prod handoff contract via UsersSharedagentshroud-sundaydev-result-YYYY-MM-DD.json]] - degree 4, connects to 1 community
