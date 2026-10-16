---
type: community
cohesion: 0.07
members: 53
---

# colima-health-check.sh

**Cohesion:** 0.07 - loosely connected
**Members:** 53 nodes

## Members
- [[ASH-OCLAW-113 auth_bypass partially_mitigated (running 2026.9.8, fixed_in None)]] - concept - docs/security/cve-triage-gaps.md
- [[ASH-OCLAW-230 dos under_review (running 2026.9.8, fixed_in None)]] - concept - docs/security/cve-triage-gaps.md
- [[CVE Triage — Gaps & Development Plan (OpenClaw), 891 triaged]] - document - docs/security/cve-triage-gaps.md
- [[CVE gap report built from invocation delta, not registry state]] - concept - reports/upgrade-2026-09-24.md
- [[CVE triage running-version gap (98 advisories, 9 registries untriageable)]] - concept - reports/upgrade-2026-09-22.md
- [[CVE-2026-102268 PyJWT HMAC forgery (Hermes image)]] - concept - reports/upgrade-2026-10-04.md
- [[Colima data disk mntlima-colima 100% full (ENOSPC crash loops)]] - concept - reports/upgrade-2026-09-23-20260923-1400.md
- [[Colima docker-socket forward death under load]] - concept - reports/upgrade-2026-09-20-dev.md
- [[Dev Colima VM loses all HTTPS egress]] - concept - reports/upgrade-2026-10-11.md
- [[Dev-prod handoff contract via UsersSharedagentshroud-sundaydev-result-YYYY-MM-DD.json]] - rationale - prompts/sunday-upgrade.md
- [[Devprod account split (agentshroud-bot vs ijefferson.admin)]] - concept - reports/upgrade-2026-09-20-dev.md
- [[Exclusive mkdir run lock + HEAD-pinned build guard (PR 475)]] - rationale - reports/upgrade-2026-09-24.md
- [[Exit 50 build failed and rollback failed (stack may be degraded)]] - concept - reports/upgrade-2026-09-22.md
- [[Host memory pressure on marvin (near-OOM, 90%+ swap)]] - concept - reports/upgrade-2026-09-21.md
- [[Host network filter blocking Homebrew PythonNode outbound]] - concept - reports/upgrade-2026-09-20-dev.md
- [[Human tap-approval gates PR merge (dev) and prod cutover, each independent]] - rationale - prompts/sunday-upgrade.md
- [[Jira MCP writes blocked in unattended sessions (don't-ask mode  allowedTools)]] - concept - reports/upgrade-2026-09-22.md
- [[Jira tracking per Sunday run (project SCRUM, phase comments, Done only on ALL GREEN)]] - rationale - prompts/sunday-upgrade.md
- [[Lima ssh.config lacks keepalive directives]] - concept - reports/upgrade-2026-09-23-20260923-1400.md
- [[Local Trivy scan failures (DB mirror timeouts, local-image 401 fallback)]] - concept - reports/upgrade-2026-09-22.md
- [[PATH_61]] - code - docker/scripts/colima-health-check.sh
- [[Prod promotion blocked dev tested an unmerged branch]] - concept - reports/upgrade-2026-10-11.md
- [[Refuse to build with uncommitted changes in build context]] - rationale - reports/upgrade-2026-09-22.md
- [[Running dev images predate committed Dockerfile bumps]] - concept - reports/upgrade-2026-09-23.md
- [[SCRUM-185 (9-registry triage gap ticket)]] - concept - reports/upgrade-2026-10-04.md
- [[Shared working-tree collision between concurrent sessions]] - rationale - reports/upgrade-2026-09-21.md
- [[Two-arm CVE remediation vendor fix AND AgentShroud gateway control]] - rationale - prompts/sunday-upgrade.md
- [[Upgrade Report 2026-09-20 (dev, ABORTED)]] - document - reports/upgrade-2026-09-20-dev.md
- [[Upgrade Report 2026-09-21 (dev, PARTIAL)]] - document - reports/upgrade-2026-09-21.md
- [[Upgrade Report 2026-09-22 (dev, PARTIAL, 3 sessions)]] - document - reports/upgrade-2026-09-22.md
- [[Upgrade Report 2026-09-23 0300 (dev, ABORTED)]] - document - reports/upgrade-2026-09-23.md
- [[Upgrade Report 2026-09-23 1400 (dev, PARTIAL, disk full)]] - document - reports/upgrade-2026-09-23-20260923-1400.md
- [[Upgrade Report 2026-09-24 (dev, PARTIAL, Hermes compat blocked)]] - document - reports/upgrade-2026-09-24.md
- [[Upgrade Report 2026-10-04 (dev, ALL GREEN after re-scan)]] - document - reports/upgrade-2026-10-04.md
- [[Upgrade Report 2026-10-11 (dev, PARTIAL, prod blocked)]] - document - reports/upgrade-2026-10-11.md
- [[Vendor supply-chain freshness gate (npm min-release-age  uv exclude-newer)]] - rationale - reports/upgrade-2026-09-21.md
- [[Verify the executable line, not the commit message]] - rationale - reports/upgrade-2026-09-21.md
- [[_read_running_version_str]] - code - scripts/triage-cve-mitigations.py
- [[_upgrade_in_progress()]] - code - docker/scripts/colima-health-check.sh
- [[check-version-pins-parity.sh]] - code - scripts/check-version-pins-parity.sh
- [[check-version-pins-parity.sh script]] - code - scripts/check-version-pins-parity.sh
- [[colima-firewall.sh]] - code - docker/scripts/colima-firewall.sh
- [[colima-firewall.sh script]] - code - docker/scripts/colima-firewall.sh
- [[colima-health-check.sh]] - code - docker/scripts/colima-health-check.sh
- [[colima-health-check.sh script]] - code - docker/scripts/colima-health-check.sh
- [[dev-result-date.json dev-prod handoff contract]] - concept - reports/upgrade-2026-09-21.md
- [[dockerd self-DoS on unpruned dangling image backlog (782-1240 images)]] - concept - reports/upgrade-2026-09-23-20260923-1400.md
- [[log()_9]] - code - docker/scripts/colima-health-check.sh
- [[notify()_1]] - code - docker/scripts/colima-health-check.sh
- [[read_state()]] - code - docker/scripts/colima-health-check.sh
- [[resolve_docker_host()]] - code - docker/scripts/colima-health-check.sh
- [[versions.env]] - document - docker/versions.env
- [[write_state()]] - code - docker/scripts/colima-health-check.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/colima-health-checksh
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 16 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 6 edges to [[_COMMUNITY_triage-cve-mitigations.py]]
- 5 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 2 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 2 edges to [[_COMMUNITY_asb (AgentShroud Bot helper)]]
- 2 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_plan_remediation]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_container-net-diag.sh]]
- 1 edge to [[_COMMUNITY_Commit list 2026-10-10 through 2026-10-16 on main]]

## Top bridge nodes
- [[colima-health-check.sh]] - degree 18, connects to 4 communities
- [[Upgrade Report 2026-09-21 (dev, PARTIAL)]] - degree 16, connects to 4 communities
- [[versions.env]] - degree 6, connects to 4 communities
- [[Upgrade Report 2026-09-24 (dev, PARTIAL, Hermes compat blocked)]] - degree 8, connects to 3 communities
- [[Upgrade Report 2026-09-22 (dev, PARTIAL, 3 sessions)]] - degree 13, connects to 2 communities
