---
type: community
members: 56
---

# _make_sanitizer()

**Members:** 56 nodes

## Members
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
- [[PATH_2]] - code - scripts/sunday-upgrade.sh
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
- [[Upgrade Report 2026-09-20 (dev, ABORTED)]] - document - reports/upgrade-2026-09-20-dev.md
- [[Upgrade Report 2026-09-21 (dev, PARTIAL)]] - document - reports/upgrade-2026-09-21.md
- [[Upgrade Report 2026-09-22 (dev, PARTIAL, 3 sessions)]] - document - reports/upgrade-2026-09-22.md
- [[Upgrade Report 2026-09-23 0300 (dev, ABORTED)]] - document - reports/upgrade-2026-09-23.md
- [[Upgrade Report 2026-09-23 1400 (dev, PARTIAL, disk full)]] - document - reports/upgrade-2026-09-23-20260923-1400.md
- [[Upgrade Report 2026-09-25 (dev, PASS gate  PARTIAL)]] - document - reports/upgrade-2026-09-25.md
- [[Upgrade Report 2026-09-26 (dev, ALL GREEN)]] - document - reports/upgrade-2026-09-26.md
- [[Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]] - document - reports/upgrade-2026-09-27.md
- [[Upgrade Report 2026-09-27 0800 (verify-only)]] - document - reports/upgrade-2026-09-27-20260927-0800.md
- [[Upgrade Report 2026-09-27 1400 (verify-only)]] - document - reports/upgrade-2026-09-27-20260927-1400.md
- [[Upgrade Report 2026-10-04 (dev, ALL GREEN after re-scan)]] - document - reports/upgrade-2026-10-04.md
- [[Upgrade Report 2026-10-11 (dev, PARTIAL, prod blocked)]] - document - reports/upgrade-2026-10-11.md
- [[Vendor supply-chain freshness gate (npm min-release-age  uv exclude-newer)]] - rationale - reports/upgrade-2026-09-21.md
- [[Verify the executable line, not the commit message]] - rationale - reports/upgrade-2026-09-21.md
- [[Wrapper 180-min timeout vs session cannot self-terminate]] - concept - reports/upgrade-2026-09-26.md
- [[_notify_on_exit()]] - code - scripts/sunday-upgrade.sh
- [[_read_running_version_str]] - code - scripts/triage-cve-mitigations.py
- [[_return_to_main()]] - code - scripts/sunday-upgrade.sh
- [[_session_guard()]] - code - scripts/sunday-upgrade.sh
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
- [[versions.env]] - document - docker/versions.env

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_sanitizer
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_PIIConfig]]
- 7 edges to [[_COMMUNITY__wrap_response() (2)]]
- 5 edges to [[_COMMUNITY_Sunday Upgrade prompt]]
- 5 edges to [[_COMMUNITY__w]]
- 5 edges to [[_COMMUNITY_run_multi_host]]
- 4 edges to [[_COMMUNITY_browserscriptsbrowse.py]]
- 4 edges to [[_COMMUNITY_One Shroud Over Every Wire (founding mantra)]]
- 2 edges to [[_COMMUNITY_Path (2)]]
- 2 edges to [[_COMMUNITY_A2APolicyEngine]]
- 1 edge to [[_COMMUNITY_DataExfilVolumeGuard]]
- 1 edge to [[_COMMUNITY__FakeUpstreamWS]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_dot-_run_and_read]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_make_event]]

## Top bridge nodes
- [[Upgrade Report 2026-09-21 (dev, PARTIAL)]] - degree 16, connects to 4 communities
- [[Upgrade Report 2026-09-22 (dev, PARTIAL, 3 sessions)]] - degree 13, connects to 3 communities
- [[Upgrade Report 2026-09-25 (dev, PASS gate  PARTIAL)]] - degree 11, connects to 3 communities
- [[check-soak-status.sh]] - degree 9, connects to 3 communities
- [[Upgrade Report 2026-09-20 (dev, ABORTED)]] - degree 8, connects to 3 communities
