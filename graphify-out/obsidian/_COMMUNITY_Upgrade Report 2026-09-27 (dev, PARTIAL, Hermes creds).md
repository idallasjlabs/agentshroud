---
type: community
cohesion: 0.07
members: 52
---

# Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)

**Cohesion:** 0.07 - loosely connected
**Members:** 52 nodes

## Members
- [[CI security-scan job (pip-audit dry-run)]] - code - .github/workflows/ci.yml
- [[Compose network version-label mismatch forces network recreate]] - concept - reports/upgrade-2026-10-12.md
- [[GitHub Actions version inventory (first time in scope)]] - concept - reports/upgrade-2026-10-12.md
- [[Hermes anthropic-provider cron jobs fail No Anthropic credentials found]] - concept - reports/upgrade-2026-09-27.md
- [[OpenClawHermesMCP sandbox container reaper]] - code - docker/scripts/start-agentshroud.sh
- [[Outcome taxonomy UPGRADED  HELD BACK  BLOCKED  FAILED  PENDING APPROVAL]] - rationale - prompts/sunday-upgrade.md
- [[PATH_3]] - code - scripts/sunday-upgrade.sh
- [[Python dependency audit job (pip-audit, fails on any vuln)]] - code - .github/workflows/security-scan.yml
- [[Report reportsupgrade-YYYY-MM-DD.md 8 sections written to disk as each completes, unconditional]] - rationale - prompts/sunday-upgrade.md
- [[SCRUM-187 (Hermes credential gap ticket)]] - concept - reports/upgrade-2026-09-27.md
- [[Same-day reinvocation verify-only, no rebuild]] - rationale - reports/upgrade-2026-09-27-20260927-0800.md
- [[Sandbox Container Reaper]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Scan gate crashed on 0-CRITICAL images (grep -o under pipefail)]] - concept - reports/upgrade-2026-09-25.md
- [[Soak status boot-proof is not work-proof]] - rationale - reports/upgrade-2026-09-25.md
- [[Streaming direct voice path (_call_llm_stream)]] - concept - CHANGELOG.md
- [[Sunday upgrade mission every component in dev and prod to latest stable, resolve every finding, dev first]] - document - prompts/sunday-upgrade.md
- [[Tap-approval pipeline (PR 502)]] - concept - reports/upgrade-2026-10-12.md
- [[Transitive-dependency security floors (cryptography, setuptools, multidict, urllib3, anyio, idna, starlette)]] - rationale - gateway/requirements.txt
- [[Trivy action immutable SHA pin (CI supply chain)]] - rationale - CHANGELOG.md
- [[Two-pass pip-audit (bump, re-audit, bump again)]] - rationale - reports/upgrade-2026-10-12.md
- [[Upgrade Report 2026-09-25 (dev, PASS gate  PARTIAL)]] - document - reports/upgrade-2026-09-25.md
- [[Upgrade Report 2026-09-26 (dev, ALL GREEN)]] - document - reports/upgrade-2026-09-26.md
- [[Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]] - document - reports/upgrade-2026-09-27.md
- [[Upgrade Report 2026-09-27 0800 (verify-only)]] - document - reports/upgrade-2026-09-27-20260927-0800.md
- [[Upgrade Report 2026-09-27 1400 (verify-only)]] - document - reports/upgrade-2026-09-27-20260927-1400.md
- [[Upgrade Report 2026-10-12 (dev, on-demand, PARTIAL)]] - document - reports/upgrade-2026-10-12.md
- [[Upstream-advisory watch cron jobs (8 toolchain components)]] - concept - CHANGELOG.md
- [[Wazuh manager + agent sidecar (+ embedded agent in OpenClaw image)]] - concept - docker/docker-compose.yml
- [[Wrapper 180-min timeout vs session cannot self-terminate]] - concept - reports/upgrade-2026-09-26.md
- [[_sunday_warn_expiring_acceptances()]] - code - scripts/lib/sunday-scan.sh
- [[check-soak-status.sh]] - code - scripts/check-soak-status.sh
- [[check-soak-status.sh script]] - code - scripts/check-soak-status.sh
- [[die()_1]] - code - scripts/lib/sunday-scan.sh
- [[docker-socket-proxy service (digest-pinned tecnativa, narrow allowlist)]] - code - docker/docker-compose.yml
- [[dockerdocker-compose.yml]] - code - docker/docker-compose.yml
- [[falcoctl 0.14.2 requires Go = 1.27 (GOTOOLCHAIN=local)]] - concept - reports/upgrade-2026-09-22.md
- [[log()_1]] - code - scripts/lib/sunday-scan.sh
- [[promptssunday-upgrade.md (Sunday mission procedure)]] - document - prompts/sunday-upgrade.md
- [[sunday-rollback.sh]] - code - scripts/sunday-rollback.sh
- [[sunday-rollback.sh script]] - code - scripts/sunday-rollback.sh
- [[sunday-scan.sh (Trivy scan gate library)]] - code - scripts/lib/sunday-scan.sh
- [[sunday-scan.sh script]] - code - scripts/lib/sunday-scan.sh
- [[sunday-upgrade-approve.sh]] - code - scripts/sunday-upgrade-approve.sh
- [[sunday-upgrade-approve.sh script]] - code - scripts/sunday-upgrade-approve.sh
- [[sunday-upgrade.sh]] - code - scripts/sunday-upgrade.sh
- [[sunday-upgrade.sh script]] - code - scripts/sunday-upgrade.sh
- [[sunday_ensure_trivy()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_resolve_scan_image()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_run_scan_gate()]] - code - scripts/lib/sunday-scan.sh
- [[v1.5.1 — A2A Governance patch release]] - document - CHANGELOG.md
- [[v1.6.0 — voice terminal release]] - document - CHANGELOG.md
- [[warn()_1]] - code - scripts/lib/sunday-scan.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Upgrade_Report_2026-09-27_dev_PARTIAL_Hermes_creds
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_colima-health-check.sh]]
- 8 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 4 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 2 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 2 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_asb (AgentShroud Bot helper)]]
- 1 edge to [[_COMMUNITY_TestClassify]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_plan_remediation]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_The run is judged on state change, not steps completed]]
- 1 edge to [[_COMMUNITY_Commit list 2026-10-10 through 2026-10-16 on main]]

## Top bridge nodes
- [[check-soak-status.sh]] - degree 8, connects to 4 communities
- [[Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]] - degree 13, connects to 3 communities
- [[sunday-upgrade.sh]] - degree 13, connects to 3 communities
- [[Upgrade Report 2026-09-26 (dev, ALL GREEN)]] - degree 9, connects to 3 communities
- [[Sunday upgrade mission every component in dev and prod to latest stable, resolve every finding, dev first]] - degree 7, connects to 3 communities
