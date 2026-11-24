---
type: community
members: 60
---

# upgrade-2026-09-21.md

**Members:** 60 nodes

## Members
- [[Baseline phase logs PASS with 0 images captured]] - concept - reports/upgrade-2026-09-22.md
- [[CVE triage running-version gap (98 advisories, 9 registries untriageable)]] - concept - reports/upgrade-2026-09-22.md
- [[CVE-2026-102268 PyJWT HMAC forgery (Hermes image)]] - concept - reports/upgrade-2026-10-04.md
- [[Colima data disk mntlima-colima 100% full (ENOSPC crash loops)]] - concept - reports/upgrade-2026-09-23-20260923-1400.md
- [[Colima docker-socket forward death under load]] - concept - reports/upgrade-2026-09-20-dev.md
- [[Dev Colima VM loses all HTTPS egress]] - concept - reports/upgrade-2026-10-11.md
- [[Devprod account split (agentshroud-bot vs ijefferson.admin)]] - concept - reports/upgrade-2026-09-20-dev.md
- [[Exclusive mkdir run lock + HEAD-pinned build guard (PR 475)]] - rationale - reports/upgrade-2026-09-24.md
- [[Exit 50 build failed and rollback failed (stack may be degraded)]] - concept - reports/upgrade-2026-09-22.md
- [[Hermes anthropic-provider cron jobs fail No Anthropic credentials found]] - concept - reports/upgrade-2026-09-27.md
- [[Host memory pressure on marvin (near-OOM, 90%+ swap)]] - concept - reports/upgrade-2026-09-21.md
- [[Host network filter blocking Homebrew PythonNode outbound]] - concept - reports/upgrade-2026-09-20-dev.md
- [[Jira MCP writes blocked in unattended sessions (don't-ask mode  allowedTools)]] - concept - reports/upgrade-2026-09-22.md
- [[Lima ssh.config lacks keepalive directives]] - concept - reports/upgrade-2026-09-23-20260923-1400.md
- [[Local Trivy scan failures (DB mirror timeouts, local-image 401 fallback)]] - concept - reports/upgrade-2026-09-22.md
- [[No-op gate false negative baseline captured after pin commits]] - concept - reports/upgrade-2026-09-25.md
- [[PATH_6]] - code - scripts/sunday-upgrade.sh
- [[Prod promotion blocked dev tested an unmerged branch]] - concept - reports/upgrade-2026-10-11.md
- [[Refuse to build with uncommitted changes in build context]] - rationale - reports/upgrade-2026-09-22.md
- [[Running dev images predate committed Dockerfile bumps]] - concept - reports/upgrade-2026-09-23.md
- [[S14 Hermes run-standalone.sh image tag falls back to dockerversions.env, not 'latest']] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[SCRUM-185 (9-registry triage gap ticket)]] - concept - reports/upgrade-2026-10-04.md
- [[SCRUM-187 (Hermes credential gap ticket)]] - concept - reports/upgrade-2026-09-27.md
- [[SUNDAY_BUILD_VIA_VM=1 detached in-VM build]] - rationale - reports/upgrade-2026-09-23-20260923-1400.md
- [[Same-day reinvocation verify-only, no rebuild]] - rationale - reports/upgrade-2026-09-27-20260927-0800.md
- [[Scan gate crashed on 0-CRITICAL images (grep -o under pipefail)]] - concept - reports/upgrade-2026-09-25.md
- [[Shared working-tree collision between concurrent sessions]] - rationale - reports/upgrade-2026-09-21.md
- [[Soak status boot-proof is not work-proof]] - rationale - reports/upgrade-2026-09-25.md
- [[Vendor supply-chain freshness gate (npm min-release-age  uv exclude-newer)]] - rationale - reports/upgrade-2026-09-21.md
- [[Verify the executable line, not the commit message]] - rationale - reports/upgrade-2026-09-21.md
- [[Wrapper 180-min timeout vs session cannot self-terminate]] - concept - reports/upgrade-2026-09-26.md
- [[_notify_on_exit()]] - code - scripts/sunday-upgrade.sh
- [[_other_run_live()]] - code - scripts/sunday-upgrade.sh
- [[_read_running_version_str]] - code - scripts/triage-cve-mitigations.py
- [[_return_to_main()]] - code - scripts/sunday-upgrade.sh
- [[_session_guard()]] - code - scripts/sunday-upgrade.sh
- [[_switch_to_main()]] - code - scripts/sunday-upgrade.sh
- [[check-soak-status.sh]] - code - scripts/check-soak-status.sh
- [[check-soak-status.sh script]] - code - scripts/check-soak-status.sh
- [[check-version-pins-parity.sh]] - code - scripts/check-version-pins-parity.sh
- [[check-version-pins-parity.sh script]] - code - scripts/check-version-pins-parity.sh
- [[dev-result-date.json dev-prod handoff contract]] - concept - reports/upgrade-2026-09-21.md
- [[dockerd self-DoS on unpruned dangling image backlog (782-1240 images)]] - concept - reports/upgrade-2026-09-23-20260923-1400.md
- [[falcoctl 0.14.2 requires Go = 1.27 (GOTOOLCHAIN=local)]] - concept - reports/upgrade-2026-09-22.md
- [[sunday-upgrade.sh]] - code - scripts/sunday-upgrade.sh
- [[sunday-upgrade.sh script]] - code - scripts/sunday-upgrade.sh
- [[sync-cve-registry NVD append writes to wrong registry constant]] - concept - reports/upgrade-2026-09-26.md
- [[upgrade-2026-09-20-dev]] - document - reports/upgrade-2026-09-20-dev.md
- [[upgrade-2026-09-21]] - document - reports/upgrade-2026-09-21.md
- [[upgrade-2026-09-22]] - document - reports/upgrade-2026-09-22.md
- [[upgrade-2026-09-23-20260923-1400]] - document - reports/upgrade-2026-09-23-20260923-1400.md
- [[upgrade-2026-09-23]] - document - reports/upgrade-2026-09-23.md
- [[upgrade-2026-09-25]] - document - reports/upgrade-2026-09-25.md
- [[upgrade-2026-09-26]] - document - reports/upgrade-2026-09-26.md
- [[upgrade-2026-09-27-20260927-0800]] - document - reports/upgrade-2026-09-27-20260927-0800.md
- [[upgrade-2026-09-27-20260927-1400]] - document - reports/upgrade-2026-09-27-20260927-1400.md
- [[upgrade-2026-09-27]] - document - reports/upgrade-2026-09-27.md
- [[upgrade-2026-10-04]] - document - reports/upgrade-2026-10-04.md
- [[upgrade-2026-10-11]] - document - reports/upgrade-2026-10-11.md
- [[versions.env]] - document - docker/versions.env

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/upgrade-2026-09-21md
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 5 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 4 edges to [[_COMMUNITY_triage-cve-mitigations.py]]
- 4 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 3 edges to [[_COMMUNITY_upgrade-2026-10-12]]
- 3 edges to [[_COMMUNITY_AgentShroud Sunday Upgrade — 2026-09-27, 0800 ET verification pass (DEV run, session 2)]]
- 3 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY_classify_1]]
- 1 edge to [[_COMMUNITY_deployment-mode.sh]]
- 1 edge to [[_COMMUNITY_AgentShroud Weekly Upgrade — 2026-09-20 (DEV run, account agentshroud-bot)]]
- 1 edge to [[_COMMUNITY_AgentShroud Weekly Upgrade — 2026-09-21 (DEV run, account agentshroud-bot)]]
- 1 edge to [[_COMMUNITY_AgentShroud Weekly Upgrade — 2026-09-22 (DEV run, account agentshroud-bot)]]
- 1 edge to [[_COMMUNITY_AgentShroud Sunday Upgrade — 2026-09-23 (DEV run)]]
- 1 edge to [[_COMMUNITY_AgentShroud Sunday Upgrade — 2026-09-23 1400 ET (DEV run, afternoon continuation)]]
- 1 edge to [[_COMMUNITY_AgentShroud Sunday Upgrade — 2026-09-25 (DEV run)]]
- 1 edge to [[_COMMUNITY_Final report]]
- 1 edge to [[_COMMUNITY_AgentShroud Sunday Upgrade — 2026-09-26 (DEV run)]]
- 1 edge to [[_COMMUNITY_AgentShroud Sunday Upgrade — 2026-09-27 (DEV run)]]
- 1 edge to [[_COMMUNITY_cve-mitigation-matrix]]
- 1 edge to [[_COMMUNITY_Sunday Upgrade 2026-10-11 — DEV run (agentshroud-bot, 0300 ET)]]
- 1 edge to [[_COMMUNITY_plan_remediation]]

## Top bridge nodes
- [[upgrade-2026-09-21]] - degree 16, connects to 4 communities
- [[upgrade-2026-09-25]] - degree 11, connects to 3 communities
- [[upgrade-2026-09-26]] - degree 9, connects to 3 communities
- [[check-soak-status.sh]] - degree 8, connects to 3 communities
- [[upgrade-2026-09-20-dev]] - degree 8, connects to 3 communities
