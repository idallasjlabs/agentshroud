---
type: community
cohesion: 0.07
members: 38
---

# docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)

**Cohesion:** 0.07 - loosely connected
**Members:** 38 nodes

## Members
- [[CI DAST scan (Nuclei, workflow_dispatch, self-hosted)]] - code - .github/workflows/ci.yml
- [[Compose secrets block (file fallbacks; asb extracts from credential backend at runtime)]] - code - docker/docker-compose.yml
- [[Dev Hermes polled prod's Hermes Telegram bot token all night]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Gateway hermes-dashboard reverse proxy 502 from hostTailscale]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - concept - docker/docker-compose.yml
- [[Image signing & provenance job (cosign keyless + syft SBOM attest)]] - code - .github/workflows/security-scan.yml
- [[Inventory EVERYTHING MEANS EVERYTHING — a component missing from the table is a failed run]] - rationale - prompts/sunday-upgrade.md
- [[Local model defaults nemotron-3.5-lightning-rapid anchor, qwen3-coder coding, deepseek-r1 reasoning]] - concept - docker/docker-compose.yml
- [[Multi-Agent Orchestration (specialized agents, per-agent isolation)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Rapid-MLX host.docker.internal trusted-hosts fix (local-llms repo)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Root cause Nemotron in-band reasoning + Qwen-only no_think suffix]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Semgrep --baseline-commit gate (fail only on NEW findings)]] - rationale - .github/workflows/security-scan.yml
- [[Semgrep SAST job (IEC 62443 4-1 SDL)]] - code - .github/workflows/security-scan.yml
- [[Soak, not just boot check-soak-status.sh must report SOAKED on dev OpenClaw]] - rationale - prompts/sunday-upgrade.md
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[The run is judged on state change, not steps completed]] - rationale - prompts/sunday-upgrade.md
- [[Three-tier network segmentation (internal edge  isolated DMZ  dmz) — IEC 62443 FR5]] - rationale - docker/docker-compose.yml
- [[Trivy filesystem scan job (SHA-pinned action)]] - code - .github/workflows/security-scan.yml
- [[VT_AGENTS table (directhermesopenclaw)]] - code - firmware/voice-terminal/main/app_main.c
- [[Voice Interface (STTTTS, wake word)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[agentshroud-secrets.sh script]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[dockerbotshermesagentshroud-secrets.sh (s6 cont-init secret injection)]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - code - docker/docker-compose.yml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - code - docker/docker-compose.yml
- [[hermes-dashboard-relay container (9119 Tailscale bypass of gateway)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[inject()]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - code - docker/docker-compose.yml
- [[pre-commit as single owner of .githookspre-commit]] - rationale - .pre-commit-config.yaml
- [[pre-commit detect-secrets hook (v1.5.0, .secrets.baseline)]] - code - .pre-commit-config.yaml
- [[pre-commit git-secrets local hook (AWS credential patterns)]] - code - .pre-commit-config.yaml
- [[pre-commit semgrep local hook (new findings only, system semgrep)]] - code - .pre-commit-config.yaml
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
- 3 edges to [[_COMMUNITY_colima-health-check.sh]]
- 2 edges to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 2 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh_1]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 1 edge to [[_COMMUNITY_SecureBrowser Skill_1]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_dashboard_bridge.py]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)_1]]
- 1 edge to [[_COMMUNITY_Commit list 2026-10-10 through 2026-10-16 on main]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_Report Delivery Format Instructions_1]]

## Top bridge nodes
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - degree 9, connects to 3 communities
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - degree 6, connects to 3 communities
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - degree 13, connects to 2 communities
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - degree 8, connects to 2 communities
- [[The run is judged on state change, not steps completed]] - degree 6, connects to 2 communities
