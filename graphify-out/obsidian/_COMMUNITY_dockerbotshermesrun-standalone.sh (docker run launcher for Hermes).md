---
type: community
cohesion: 0.04
members: 67
---

# docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)

**Cohesion:** 0.04 - loosely connected
**Members:** 67 nodes

## Members
- [[dot-test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[AGENTSHROUD_HERMES_DISABLE_TELEGRAM=1 opt-in for dev Hermes]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[CI DAST scan (Nuclei, workflow_dispatch, self-hosted)]] - code - .github/workflows/ci.yml
- [[Compose secrets block (file fallbacks; asb extracts from credential backend at runtime)]] - code - docker/docker-compose.yml
- [[Compose-version label mismatch forces network recreation + stale endpoint records]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Dev Hermes polled prod's Hermes Telegram bot token all night]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Dev gateway HERMES_DASHBOARD_UPSTREAM pointed at prod hostname (always 502)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Dev override secrets telegram_bot_token_marvin  hermes_telegram_bot_token_marvin]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Dev override gateway (agentshroud-dev-gateway, 9080, dev Hermes upstreams)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Dev override openclaw (agentshroud-dev-openclaw, 18790, agentshroud_bot_marvin)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Dev override voice-gateway on 127.0.0.18766]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Devprod coexistence on one host offset ports (908018790) and subnets (172.20-2224)]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Edge TTS Microsoft 403 anti-abuse rejection; Gemini fallback blocked]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Gateway hermes-dashboard reverse proxy 502 from hostTailscale]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Hermes cron jobs paused by empty AGENTSHROUD_PROD_CRON_KEEP on container recreate]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - concept - docker/docker-compose.yml
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor hermes-…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Local model defaults nemotron-3.5-lightning-rapid anchor, qwen3-coder coding, deepseek-r1 reasoning]] - concept - docker/docker-compose.yml
- [[Multi-Agent Orchestration (specialized agents, per-agent isolation)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[OpenClaw sandbox provisioning named volume vs required bind-mount]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Rapid-MLX host.docker.internal trusted-hosts fix (local-llms repo)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Root cause Nemotron in-band reasoning + Qwen-only no_think suffix]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Soak, not just boot check-soak-status.sh must report SOAKED on dev OpenClaw]] - rationale - prompts/sunday-upgrade.md
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Three-tier network segmentation (internal edge  isolated DMZ  dmz) — IEC 62443 FR5]] - rationale - docker/docker-compose.yml
- [[VT_AGENTS table (directhermesopenclaw)]] - code - firmware/voice-terminal/main/app_main.c
- [[Voice Interface (STTTTS, wake word)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[_dashboard_auth_env_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_dashboard_host_default()]] - code - docker/bots/hermes/run-standalone.sh
- [[_feedbin_env_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_oc_config_set()]] - code - docker/scripts/init-openclaw-config.sh
- [[_secret_mount_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_sha256()_1]] - code - docker/scripts/init-openclaw-config.sh
- [[_wait_for_gateway_healthy()]] - code - docker/bots/hermes/run-standalone.sh
- [[agentshroud-secrets.sh script]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[aiohttp ClientSession closed-session crash-loop fix (partial)]] - rationale - docker/bots/hermes/patch_slack_session_recreate.py
- [[cmd_down()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_logs()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_status()_1]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_up()]] - code - docker/bots/hermes/run-standalone.sh
- [[discover_upstream_versions.py hardening bounded retry, 90s deadline thread, IPv4 fallback]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[dockerbotshermesagentshroud-secrets.sh (s6 cont-init secret injection)]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]] - code - docker/bots/hermes/run-standalone.sh
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - code - docker/scripts/init-openclaw-config.sh
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - code - docker/docker-compose.yml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - code - docker/docker-compose.yml
- [[hermes-dashboard-relay container (9119 Tailscale bypass of gateway)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[init-openclaw-config.sh runs doctor --fix before version seed (schema v23-v24 trap)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[init-openclaw-config.sh script]] - code - docker/scripts/init-openclaw-config.sh
- [[inject()]] - code - docker/bots/hermes/agentshroud-secrets.sh
- [[lazydocker docker.sock connection leak through Colima ssh forward]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[llm_proxy._suppress_qwen3_thinking (no_think for qwen only, reasoning_effort none otherwise)]] - code - gateway/proxy/llm_proxy.py
- [[missing-secret startup visibility check]] - code - docker/bots/hermes/start.sh
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - code - docker/docker-compose.yml
- [[patch_slack_session_recreate.py]] - code - docker/bots/hermes/patch_slack_session_recreate.py
- [[pre-commit check-yaml hook (--unsafe)]] - code - .pre-commit-config.yaml
- [[run-standalone.sh is the actual deploy path for Hermes (docker run, not compose…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[run-standalone.sh script]] - code - docker/bots/hermes/run-standalone.sh
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
- 4 edges to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_asb (AgentShroud Bot helper)]]
- 2 edges to [[_COMMUNITY_Commit list 2026-10-10 through 2026-10-16 on main]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_The run is judged on state change, not steps completed]]
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY__seed_cron]]
- 1 edge to [[_COMMUNITY_AgentShroud Falco Rules]]
- 1 edge to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]]
- 1 edge to [[_COMMUNITY_tailscale-serve.sh]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_dashboard_bridge.py]]
- 1 edge to [[_COMMUNITY_Report Delivery Format Instructions]]

## Top bridge nodes
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - degree 14, connects to 3 communities
- [[dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]] - degree 19, connects to 2 communities
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - degree 9, connects to 2 communities
- [[Dev override gateway (agentshroud-dev-gateway, 9080, dev Hermes upstreams)]] - degree 8, connects to 2 communities
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - degree 7, connects to 2 communities
