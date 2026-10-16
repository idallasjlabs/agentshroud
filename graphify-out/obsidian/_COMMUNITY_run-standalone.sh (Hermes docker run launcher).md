---
type: community
cohesion: 0.15
members: 22
---

# run-standalone.sh (Hermes docker run launcher)

**Cohesion:** 0.15 - loosely connected
**Members:** 22 nodes

## Members
- [[AGENTSHROUD_VERSION fallback to dockerversions.env]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Hermes cron jobs paused by empty AGENTSHROUD_PROD_CRON_KEEP on container recreate]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Missing-secret visibility banner (expected secrets loop)]] - rationale - docker/bots/hermes/start.sh
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S13 start.sh env-provided feedbin secrets not reported missing]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S14 run-standalone.sh image tag falls back to dockerversions.env]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[_dashboard_auth_env_args]] - code - docker/bots/hermes/run-standalone.sh
- [[_dashboard_host_default]] - code - docker/bots/hermes/run-standalone.sh
- [[_feedbin_env_args]] - code - docker/bots/hermes/run-standalone.sh
- [[_secret_mount_args]] - code - docker/bots/hermes/run-standalone.sh
- [[_wait_for_gateway_healthy]] - code - docker/bots/hermes/run-standalone.sh
- [[aiohttp ClientSession closed-session crash-loop fix (partial)]] - rationale - docker/bots/hermes/patch_slack_session_recreate.py
- [[check]] - code - tests/startup_smoke/test_bot_boot_static.sh
- [[cmd_down]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_logs]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_status_1]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_up]] - code - docker/bots/hermes/run-standalone.sh
- [[patch_slack_session_recreate.py]] - code - docker/bots/hermes/patch_slack_session_recreate.py
- [[run-standalone.sh (Hermes docker run launcher)]] - code - docker/bots/hermes/run-standalone.sh
- [[run-standalone.sh script]] - code - docker/bots/hermes/run-standalone.sh
- [[test_bot_boot_static.sh (static bot boot assertions S1-S14)]] - code - tests/startup_smoke/test_bot_boot_static.sh
- [[test_bot_boot_static.sh script]] - code - tests/startup_smoke/test_bot_boot_static.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run-standalonesh_Hermes_docker_run_launcher
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 3 edges to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 2 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py_1]]

## Top bridge nodes
- [[cmd_up]] - degree 10, connects to 3 communities
- [[Missing-secret visibility banner (expected secrets loop)]] - degree 5, connects to 2 communities
- [[run-standalone.sh (Hermes docker run launcher)]] - degree 16, connects to 1 community
- [[_dashboard_host_default]] - degree 3, connects to 1 community
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py]] - degree 2, connects to 1 community
