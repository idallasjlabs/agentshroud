---
type: community
cohesion: 0.06
members: 54
---

# run-standalone.sh (Hermes docker run launcher)

**Cohesion:** 0.06 - loosely connected
**Members:** 54 nodes

## Members
- [[2026-10-12 silent Daily Brief outage (AGENTSHROUD_PROD_CRON_KEEP empty)]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[AGENTSHROUD_VERSION fallback to dockerversions.env]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Compose version mismatch forces network recreate + stale endpoints]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[Edge TTS Microsoft 403 (external anti-abuse rotation)]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)]] - rationale - docker/bots/hermes/init-config.sh
- [[Hermes 'latest' image-tag outage (~5 min)]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[Hermes Conduit (iOS app)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Hermes cron jobs paused by empty AGENTSHROUD_PROD_CRON_KEEP on container recreate]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Incident 2026-10-16 ConduitHermes instability record]] - document - INCIDENT_2026-10-16_conduit-outage.md
- [[Missing-secret visibility banner (expected secrets loop)]] - rationale - docker/bots/hermes/start.sh
- [[Nemotron + Qwen-only no_think suffix broke chat since Sunday]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[OpenClaw sandbox mode set to off (named-volume vs bind-mount mismatch)]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[Post-migration model lock + sandboxed terminal + cron fleet default]] - rationale - docker/bots/hermes/start.sh
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S13 start.sh env-provided feedbin secrets not reported missing]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S14 run-standalone.sh image tag falls back to dockerversions.env]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[Sunday-upgrade no-op gate hardening (CLAUDE.md section 0.0)]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[Suspected prompt-injection  phishing (fake Tailscale credential request)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[_asb_banner]] - code - scripts/asb
- [[_dashboard_auth_env_args]] - code - docker/bots/hermes/run-standalone.sh
- [[_dashboard_host_default]] - code - docker/bots/hermes/run-standalone.sh
- [[_ensure_sandbox_image]] - code - scripts/asb
- [[_feedbin_env_args]] - code - docker/bots/hermes/run-standalone.sh
- [[_fstrim_colima_datadisk]] - code - scripts/asb
- [[_hermes_cron_ids_names]] - code - docker/bots/hermes/init-config.sh
- [[_hermes_down]] - code - scripts/asb
- [[_hermes_up]] - code - scripts/asb
- [[_prune_docker]] - code - scripts/asb
- [[_prune_superseded_images]] - code - scripts/asb
- [[_reset_device_store]] - code - scripts/asb
- [[_secret_mount_args]] - code - docker/bots/hermes/run-standalone.sh
- [[_wait_for_gateway_healthy]] - code - docker/bots/hermes/run-standalone.sh
- [[aiohttp ClientSession closed-session crash-loop fix (partial)]] - rationale - docker/bots/hermes/patch_slack_session_recreate.py
- [[asb (AgentShroud Bot helper)]] - code - scripts/asb
- [[check]] - code - tests/startup_smoke/test_bot_boot_static.sh
- [[cmd_down]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_logs]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_persist]] - code - scripts/tailscale-serve.sh
- [[cmd_start]] - code - scripts/tailscale-serve.sh
- [[cmd_status]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_status_1]] - code - scripts/tailscale-serve.sh
- [[cmd_stop]] - code - scripts/tailscale-serve.sh
- [[cmd_up]] - code - docker/bots/hermes/run-standalone.sh
- [[hermes-dashboard-relay container bypassing the gateway reverse proxy]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[lazydocker docker.sock connection leak through Colima ssh forward]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[patch_slack_session_recreate.py]] - code - docker/bots/hermes/patch_slack_session_recreate.py
- [[patch_telegram_edit_message_date.py (KeyError 'date' on editMessageText)]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[run-standalone.sh (Hermes docker run launcher)]] - code - docker/bots/hermes/run-standalone.sh
- [[run-standalone.sh script]] - code - docker/bots/hermes/run-standalone.sh
- [[setup_ephemeral_secrets]] - code - scripts/asb
- [[tailscale-serve.sh]] - code - scripts/tailscale-serve.sh
- [[tailscale-serve.sh script]] - code - scripts/tailscale-serve.sh
- [[test_bot_boot_static.sh (static bot boot assertions S1-S14)]] - code - tests/startup_smoke/test_bot_boot_static.sh
- [[test_bot_boot_static.sh script]] - code - tests/startup_smoke/test_bot_boot_static.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run-standalonesh_Hermes_docker_run_launcher
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 5 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 5 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 4 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 3 edges to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 1 edge to [[_COMMUNITY_setup-secrets.sh]]
- 1 edge to [[_COMMUNITY_asb (AgentShroud Bot helper)]]
- 1 edge to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY__is_op_reference_allowed]]
- 1 edge to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy()]]

## Top bridge nodes
- [[asb (AgentShroud Bot helper)]] - degree 11, connects to 4 communities
- [[Incident 2026-10-16 ConduitHermes instability record]] - degree 18, connects to 3 communities
- [[cmd_up]] - degree 10, connects to 2 communities
- [[cmd_start]] - degree 6, connects to 2 communities
- [[setup_ephemeral_secrets]] - degree 3, connects to 2 communities
