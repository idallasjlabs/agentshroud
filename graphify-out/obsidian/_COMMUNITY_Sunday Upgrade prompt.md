---
type: community
members: 68
---

# Sunday Upgrade prompt

**Members:** 68 nodes

## Members
- [[AGENTSHROUD_GATEWAY_CONTAINER for daily CVE scan]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[ASH-OCLAW-113 auth_bypass partially_mitigated (running 2026.9.8, fixed_in None)]] - concept - docs/security/cve-triage-gaps.md
- [[ASH-OCLAW-230 dos under_review (running 2026.9.8, fixed_in None)]] - concept - docs/security/cve-triage-gaps.md
- [[AgentShroud-side CVE remediation arm]] - rationale - prompts/sunday-upgrade.md
- [[All bot egress via gateway8181 HTTP proxy]] - rationale - docker/docker-compose.yml
- [[Anti-security-theater value]] - rationale - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Automatic prod cutover gate (no human tap, 2026-10-18)]] - rationale - prompts/sunday-upgrade.md
- [[Base docker-compose stack]] - code - docker/docker-compose.yml
- [[CI lint job (pinned blackisortflake8)]] - code - .github/workflows/ci.yml
- [[CVE Triage — Gaps & Development Plan (OpenClaw), 891 triaged]] - document - docs/security/cve-triage-gaps.md
- [[Collaborator workspace SOUL.md (Isaiah persona)]] - document - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Compose network version-label mismatch forces network recreate]] - concept - reports/upgrade-2026-10-12.md
- [[Current Focus (AgentShroud v1.7.x)]] - concept - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Dev handoff JSON (dev-result-YYYY-MM-DD.json)]] - concept - prompts/sunday-upgrade.md
- [[Dev-first, prod-promoted-after-pass flow]] - concept - prompts/sunday-upgrade.md
- [[GitHub Actions version inventory (first time in scope)]] - concept - reports/upgrade-2026-10-12.md
- [[Goal any agent wrappable with gateway protection]] - concept - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Hermes pin silent no-op (0.21.5 while upstream 0.22.2)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Hermes v0.22.2 held back (A2A 9900 unreachable)]] - concept - reports/upgrade-2026-10-18.md
- [[Host trivy cannot reach registries (scans_failed=3 root cause)]] - concept - reports/upgrade-2026-10-18.md
- [[Jira run tracking]] - concept - prompts/sunday-upgrade.md
- [[Marvin dev compose override (agentshroud-bot)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Multi-Agent Orchestration (specialized agents, per-agent isolation)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[NOTHING_UPGRADED status]] - concept - prompts/sunday-upgrade.md
- [[Non-agent components not inventoried]] - concept - reports/upgrade-2026-10-18.md
- [[OpenClaw 2026.10.2 - 2026.10.4 upgrade (dev)]] - concept - reports/upgrade-2026-10-18.md
- [[OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[OpenClawHermesMCP sandbox container reaper]] - code - docker/scripts/start-agentshroud.sh
- [[Prod promotion BLOCKED (0800 window)]] - concept - reports/upgrade-2026-10-18.md
- [[Proxy-layer inversion pattern]] - concept - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Run judged on state change, not steps completed]] - rationale - prompts/sunday-upgrade.md
- [[S5 docker-compose.yml does not bind port 8080 to 0.0.0.0]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Sandbox Container Reaper]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Seven-week PASS-while-upgrading-nothing failure (2026-07-29..09-15)]] - concept - prompts/sunday-upgrade.md
- [[Soak-not-just-boot check]] - rationale - prompts/sunday-upgrade.md
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Sunday Upgrade Report 2026-10-18 (dev)]] - document - reports/upgrade-2026-10-18.md
- [[Sunday Upgrade prompt]] - document - prompts/sunday-upgrade.md
- [[Tap-approval pipeline (PR 502)]] - concept - reports/upgrade-2026-10-12.md
- [[Two-pass pip-audit (bump, re-audit, bump again)]] - rationale - reports/upgrade-2026-10-12.md
- [[Upgrade Report 2026-10-12 (dev, on-demand, PARTIAL)]] - document - reports/upgrade-2026-10-12.md
- [[VT_AGENTS table (directhermesopenclaw)]] - code - firmware/voice-terminal/main/app_main.c
- [[Voice Interface (STTTTS, wake word)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[agentshroud-console network (legacy)]] - code - docker/docker-compose.yml
- [[agentshroud-dmz network (IEC 62443 FR5 SL2, unwired)]] - code - docker/docker-compose.yml
- [[agentshroud-internal network 10.254.110.024]] - code - docker/docker-compose.yml
- [[agentshroud-isolated network (internal, no internet)]] - code - docker/docker-compose.yml
- [[check()_11]] - code - scripts/post-deploy-check.sh
- [[check-soak-status.sh]] - code - scripts/check-soak-status.sh
- [[check-soak-status.sh script]] - code - scripts/check-soak-status.sh
- [[docker-socket-proxy service (tecnativa, digest-pinned)]] - code - docker/docker-compose.yml
- [[dockerversions.env version pins]] - code - docker/docker-compose.yml
- [[falco-alerts  clamav-db volumes (in-gateway sidecars)]] - code - docker/docker-compose.yml
- [[gateway service (agentshroud-gateway)]] - code - docker/docker-compose.yml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[hermes bot service (profile hermesfull)]] - code - docker/docker-compose.yml
- [[openclaw bot service]] - code - docker/docker-compose.yml
- [[post-deploy-check.sh]] - code - scripts/post-deploy-check.sh
- [[post-deploy-check.sh script]] - code - scripts/post-deploy-check.sh
- [[security-entrypoint.sh boot scan flow]] - code - docker/scripts/security-entrypoint.sh
- [[start-agentshroud.sh (OpenClaw entrypoint)]] - code - docker/scripts/start-agentshroud.sh
- [[sunday-rollback.sh]] - code - scripts/sunday-rollback.sh
- [[sunday-rollback.sh script]] - code - scripts/sunday-rollback.sh
- [[sunday-upgrade-approve.sh]] - code - scripts/sunday-upgrade-approve.sh
- [[sunday-upgrade-approve.sh script]] - code - scripts/sunday-upgrade-approve.sh
- [[voice-gateway service]] - code - docker/docker-compose.yml
- [[wazuh-agent sidecar service]] - code - docker/docker-compose.yml
- [[wazuh-manager service (wazuh 4.14.8)]] - code - docker/docker-compose.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Sunday_Upgrade_prompt
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_colima-health-check.sh]]
- 7 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 5 edges to [[_COMMUNITY_Incident ConduitHermes instability 2026-10-16]]
- 3 edges to [[_COMMUNITY_triage-cve-mitigations.py]]
- 3 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 3 edges to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 2 edges to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh (2)]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher) (2)]]
- 1 edge to [[_COMMUNITY_TestClassify]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_test_openclaw_photo.sh]]
- 1 edge to [[_COMMUNITY_NetworkSecurityFinding]]
- 1 edge to [[_COMMUNITY_plan_remediation]]
- 1 edge to [[_COMMUNITY_sunday-scan.sh]]
- 1 edge to [[_COMMUNITY_Report Delivery Format Instructions (2)]]

## Top bridge nodes
- [[Sunday Upgrade prompt]] - degree 25, connects to 6 communities
- [[post-deploy-check.sh]] - degree 7, connects to 3 communities
- [[Base docker-compose stack]] - degree 18, connects to 2 communities
- [[check-soak-status.sh]] - degree 10, connects to 2 communities
- [[gateway service (agentshroud-gateway)]] - degree 10, connects to 2 communities
