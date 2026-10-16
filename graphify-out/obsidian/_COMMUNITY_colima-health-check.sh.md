---
type: community
cohesion: 0.06
members: 66
---

# colima-health-check.sh

**Cohesion:** 0.06 - loosely connected
**Members:** 66 nodes

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
- [[PATH_56]] - code - docker/scripts/colima-health-check.sh
- [[PATH_57]] - code - scripts/sunday-upgrade.sh
- [[Prod promotion blocked dev tested an unmerged branch]] - concept - reports/upgrade-2026-10-11.md
- [[Refuse to build with uncommitted changes in build context]] - rationale - reports/upgrade-2026-09-22.md
- [[Running dev images predate committed Dockerfile bumps]] - concept - reports/upgrade-2026-09-23.md
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
- [[Wazuh manager + agent sidecar (+ embedded agent in OpenClaw image)]] - concept - docker/docker-compose.yml
- [[Wrapper 180-min timeout vs session cannot self-terminate]] - concept - reports/upgrade-2026-09-26.md
- [[_read_running_version_str]] - code - scripts/triage-cve-mitigations.py
- [[_upgrade_in_progress()]] - code - docker/scripts/colima-health-check.sh
- [[check-soak-status.sh]] - code - scripts/check-soak-status.sh
- [[check-soak-status.sh script]] - code - scripts/check-soak-status.sh
- [[check-version-pins-parity.sh]] - code - scripts/check-version-pins-parity.sh
- [[check-version-pins-parity.sh script]] - code - scripts/check-version-pins-parity.sh
- [[colima-firewall.sh]] - code - docker/scripts/colima-firewall.sh
- [[colima-firewall.sh script]] - code - docker/scripts/colima-firewall.sh
- [[colima-health-check.sh]] - code - docker/scripts/colima-health-check.sh
- [[colima-health-check.sh script]] - code - docker/scripts/colima-health-check.sh
- [[dev-result-date.json dev-prod handoff contract]] - concept - reports/upgrade-2026-09-21.md
- [[dockerd self-DoS on unpruned dangling image backlog (782-1240 images)]] - concept - reports/upgrade-2026-09-23-20260923-1400.md
- [[falcoctl 0.14.2 requires Go = 1.27 (GOTOOLCHAIN=local)]] - concept - reports/upgrade-2026-09-22.md
- [[log()_7]] - code - docker/scripts/colima-health-check.sh
- [[notify()_1]] - code - docker/scripts/colima-health-check.sh
- [[read_state()]] - code - docker/scripts/colima-health-check.sh
- [[resolve_docker_host()]] - code - docker/scripts/colima-health-check.sh
- [[sunday-upgrade.sh]] - code - scripts/sunday-upgrade.sh
- [[sunday-upgrade.sh script]] - code - scripts/sunday-upgrade.sh
- [[sync-cve-registry NVD append writes to wrong registry constant]] - concept - reports/upgrade-2026-09-26.md
- [[versions.env]] - document - docker/versions.env
- [[write_state()]] - code - docker/scripts/colima-health-check.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/colima-health-checksh
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 6 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 5 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 5 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)_1]]
- 4 edges to [[_COMMUNITY_triage-cve-mitigations.py]]
- 4 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 4 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 3 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 2 edges to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]
- 2 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_TestClassify]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_container-net-diag.sh]]
- 1 edge to [[_COMMUNITY_plan_remediation]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]

## Top bridge nodes
- [[colima-health-check.sh]] - degree 18, connects to 4 communities
- [[Upgrade Report 2026-09-21 (dev, PARTIAL)]] - degree 16, connects to 4 communities
- [[versions.env]] - degree 6, connects to 4 communities
- [[sunday-upgrade.sh]] - degree 13, connects to 3 communities
- [[Upgrade Report 2026-09-25 (dev, PASS gate  PARTIAL)]] - degree 12, connects to 3 communities
