---
type: community
members: 58
---

# docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)

**Members:** 58 nodes

## Members
- [[dot-test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[CI DAST scan (Nuclei, workflow_dispatch, self-hosted)]] - code - .github/workflows/ci.yml
- [[Compose secrets block (file fallbacks; asb extracts from credential backend at runtime)]] - code - docker/docker-compose.yml
- [[Dev Hermes polled prod's Hermes Telegram bot token all night]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Gateway hermes-dashboard reverse proxy 502 from hostTailscale]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - concept - docker/docker-compose.yml
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor hermes-…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Image signing & provenance job (cosign keyless + syft SBOM attest)]] - code - .github/workflows/security-scan.yml
- [[Inventory EVERYTHING MEANS EVERYTHING — a component missing from the table is a failed run]] - rationale - prompts/sunday-upgrade.md
- [[Local model defaults nemotron-3.5-lightning-rapid anchor, qwen3-coder coding, deepseek-r1 reasoning]] - concept - docker/docker-compose.yml
- [[Multi-Agent Orchestration (specialized agents, per-agent isolation)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[OpenClaw Cron Jobs Configuration]] - document - docker/config/openclaw/cron/jobs.json
- [[OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[OpenClawHermesMCP sandbox container reaper]] - code - docker/scripts/start-agentshroud.sh
- [[Outcome taxonomy UPGRADED  HELD BACK  BLOCKED  FAILED  PENDING APPROVAL]] - rationale - prompts/sunday-upgrade.md
- [[Report reportsupgrade-YYYY-MM-DD.md 8 sections written to disk as each completes, unconditional]] - rationale - prompts/sunday-upgrade.md
- [[S10 start-agentshroud.sh force-reconciles security-critical live cron jobs]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S11 init-openclaw-config.sh seeds jira_dev_ticket.py into live OpenClaw workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S8 no raw sshagentshroud-bot@real Tailscale FQDN in baked bot config]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S9 init-openclaw-config.sh seeds agentshroud-ssh-exec.sh rules into live AGENTS]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Sandbox Container Reaper]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Semgrep --baseline-commit gate (fail only on NEW findings)]] - rationale - .github/workflows/security-scan.yml
- [[Semgrep SAST job (IEC 62443 4-1 SDL)]] - code - .github/workflows/security-scan.yml
- [[Soak, not just boot check-soak-status.sh must report SOAKED on dev OpenClaw]] - rationale - prompts/sunday-upgrade.md
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Sunday upgrade mission every component in dev and prod to latest stable, resolve every finding, dev first]] - document - prompts/sunday-upgrade.md
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[The run is judged on state change, not steps completed]] - rationale - prompts/sunday-upgrade.md
- [[Three-tier network segmentation (internal edge  isolated DMZ  dmz) — IEC 62443 FR5]] - rationale - docker/docker-compose.yml
- [[Trivy filesystem scan job (SHA-pinned action)]] - code - .github/workflows/security-scan.yml
- [[VT_AGENTS table (directhermesopenclaw)]] - code - firmware/voice-terminal/main/app_main.c
- [[Voice Interface (STTTTS, wake word)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[_oc_config_set()]] - code - docker/scripts/init-openclaw-config.sh
- [[_sha256()_3]] - code - docker/scripts/init-openclaw-config.sh
- [[agentshroud-secrets.sh script]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[docker-socket-proxy service (digest-pinned tecnativa, narrow allowlist)]] - code - docker/docker-compose.yml
- [[dockerbotshermesagentshroud-secrets.sh (s6 cont-init secret injection)]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - code - docker/scripts/init-openclaw-config.sh
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - code - docker/docker-compose.yml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - code - docker/docker-compose.yml
- [[hermes-dashboard-relay container (9119 Tailscale bypass of gateway)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[init-openclaw-config.sh runs doctor --fix before version seed (schema v23-v24 trap)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[init-openclaw-config.sh script]] - code - docker/scripts/init-openclaw-config.sh
- [[inject()]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - code - docker/docker-compose.yml
- [[pre-commit as single owner of .githookspre-commit]] - rationale - .pre-commit-config.yaml
- [[pre-commit detect-secrets hook (v1.5.0, .secrets.baseline)]] - code - .pre-commit-config.yaml
- [[pre-commit git-secrets local hook (AWS credential patterns)]] - code - .pre-commit-config.yaml
- [[pre-commit semgrep local hook (new findings only, system semgrep)]] - code - .pre-commit-config.yaml
- [[run-standalone.sh is the actual deploy path for Hermes (docker run, not compose…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[security-entrypoint.sh boot scan flow]] - code - docker/scripts/security-entrypoint.sh
- [[start-agentshroud.sh (OpenClaw entrypoint)]] - code - docker/scripts/start-agentshroud.sh
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge, cpu_shares 4096, cpuset 0-3)]] - code - docker/docker-compose.yml
- [[wazuh-agent sidecar (root moment for privilege drop, then uid 1000)]] - code - docker/docker-compose.yml
- [[wazuh-manager service (4.14.8, isolated-network only, open enrollment)]] - code - docker/docker-compose.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_colima-health-check.sh]]
- 2 edges to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh (2)]]
- 1 edge to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY_apply-patches.js]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_SecureBrowser Skill (2)]]
- 1 edge to [[_COMMUNITY_dashboard_bridge.py]]
- 1 edge to [[_COMMUNITY_Commit list 2026-10-10 through 2026-10-16 on main]]
- 1 edge to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 1 edge to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_Report Delivery Format Instructions (2)]]
- 1 edge to [[_COMMUNITY_triage-cve-mitigations.py]]

## Top bridge nodes
- [[Sunday upgrade mission every component in dev and prod to latest stable, resolve every finding, dev first]] - degree 7, connects to 3 communities
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - degree 13, connects to 2 communities
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - degree 6, connects to 2 communities
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - degree 10, connects to 1 community
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - degree 9, connects to 1 community
