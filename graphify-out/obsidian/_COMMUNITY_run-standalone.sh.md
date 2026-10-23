---
type: community
cohesion: 0.07
members: 45
---

# run-standalone.sh

**Cohesion:** 0.07 - loosely connected
**Members:** 45 nodes

## Members
- [[AGENTSHROUD_GATEWAY_CONTAINER for daily CVE scan]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[AGENTSHROUD_HERMES_DISABLE_TELEGRAM opt-in]] - rationale - docker/bots/hermes/run-standalone.sh
- [[AgentShroud production compose stack]] - code - docker/docker-compose.yml
- [[HERMES__UPSTREAM - agentshroud-dev-hermes-v2]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Hermes cron jobs paused by empty AGENTSHROUD_PROD_CRON_KEEP on container recreate]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Hermes launched via docker run, not compose]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Hermes v0.22.2 held back (A2A 9900 unreachable)]] - concept - reports/upgrade-2026-10-18.md
- [[Marvin dev compose override (agentshroud-bot)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Multi-Agent Orchestration (specialized agents, per-agent isolation)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[OpenClaw 2026.10.2 - 2026.10.4 upgrade (dev)]] - concept - reports/upgrade-2026-10-18.md
- [[OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[OpenClawHermesMCP sandbox container reaper]] - code - docker/scripts/start-agentshroud.sh
- [[S13 Hermes start.sh expected-secrets banner accepts env vars in place of mounted files]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S14 Hermes run-standalone.sh image tag falls back to dockerversions.env, not 'latest']] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S17 Hermes run-standalone.sh resource caps prod 3g1.5, dev 2g1.0, env override honoured]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Sandbox Container Reaper]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[VT_AGENTS table (directhermesopenclaw)]] - code - firmware/voice-terminal/main/app_main.c
- [[Voice Interface (STTTTS, wake word)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[_dashboard_auth_env_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_dashboard_host_default()]] - code - docker/bots/hermes/run-standalone.sh
- [[_feedbin_env_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_secret_mount_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_wait_for_gateway_healthy()]] - code - docker/bots/hermes/run-standalone.sh
- [[agentshroud-dmz network (IEC 62443 FR5 SL2)]] - code - docker/docker-compose.yml
- [[agentshroud-isolated network (internal)]] - code - docker/docker-compose.yml
- [[aiohttp ClientSession closed-session crash-loop fix (partial)]] - rationale - docker/bots/hermes/patch_slack_session_recreate.py
- [[cmd_down()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_logs()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_status()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_up()]] - code - docker/bots/hermes/run-standalone.sh
- [[docker-socket-proxy (digest pinned)]] - code - docker/docker-compose.yml
- [[falco-alerts  security-reports shared volumes]] - code - docker/docker-compose.yml
- [[gateway service (sole egress, FalcoClamAV in-process)]] - code - docker/docker-compose.yml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[hermes service (agentshroud-hermes-v2)]] - code - docker/docker-compose.yml
- [[openclaw service]] - code - docker/docker-compose.yml
- [[patch_slack_session_recreate.py]] - code - docker/bots/hermes/patch_slack_session_recreate.py
- [[run-standalone.sh]] - code - docker/bots/hermes/run-standalone.sh
- [[run-standalone.sh script]] - code - docker/bots/hermes/run-standalone.sh
- [[security-entrypoint.sh boot scan flow]] - code - docker/scripts/security-entrypoint.sh
- [[start-agentshroud.sh (OpenClaw entrypoint)]] - code - docker/scripts/start-agentshroud.sh
- [[voice-gateway service]] - code - docker/docker-compose.yml
- [[wazuh-agent sidecar]] - code - docker/docker-compose.yml
- [[wazuh-manager service (4.14.8)]] - code - docker/docker-compose.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run-standalonesh
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY__wrap_response() (2)]]
- 3 edges to [[_COMMUNITY__make_sanitizer()]]
- 2 edges to [[_COMMUNITY_AgentShroud Sunday Upgrade — 2026-09-06 (dev-only, read-only inventory → scoped fixes)]]
- 2 edges to [[_COMMUNITY_Voice Terminal — ESP32-S3-BOX-3 (Optional AgentShroud Add-On)]]
- 2 edges to [[_COMMUNITY_TestFabricatedSecurityNotice (2)]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py (4)]]
- 1 edge to [[_COMMUNITY_DataExfilVolumeGuard]]
- 1 edge to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 1 edge to [[_COMMUNITY_Sunday Upgrade prompt]]
- 1 edge to [[_COMMUNITY__make_cve]]
- 1 edge to [[_COMMUNITY_Report Delivery Format Instructions (2)]]

## Top bridge nodes
- [[docker-socket-proxy (digest pinned)]] - degree 10, connects to 2 communities
- [[gateway service (sole egress, FalcoClamAV in-process)]] - degree 10, connects to 2 communities
- [[OpenClaw 2026.10.2 - 2026.10.4 upgrade (dev)]] - degree 3, connects to 2 communities
- [[cmd_up()]] - degree 11, connects to 1 community
- [[Marvin dev compose override (agentshroud-bot)]] - degree 11, connects to 1 community
