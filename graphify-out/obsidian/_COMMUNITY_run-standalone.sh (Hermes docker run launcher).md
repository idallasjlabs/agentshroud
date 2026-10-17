---
type: community
members: 24
---

# run-standalone.sh (Hermes docker run launcher)

**Members:** 24 nodes

## Members
- [[AGENTSHROUD_ENV auto-detected from invoking account]] - rationale - docker/bots/hermes/run-standalone.sh
- [[AGENTSHROUD_HERMES_DISABLE_TELEGRAM opt-in]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)]] - rationale - docker/bots/hermes/init-config.sh
- [[Hermes cron jobs paused by empty AGENTSHROUD_PROD_CRON_KEEP on container recreate]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Hermes deliberately absent from the dev compose override]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Hermes launched via docker run, not compose]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Hermes resource caps by environment]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Missing-secret visibility banner (expected secrets loop)]] - rationale - docker/bots/hermes/start.sh
- [[S13 Hermes start.sh expected-secrets banner accepts env vars in place of mounted files]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S17 Hermes run-standalone.sh resource caps prod 3g1.5, dev 2g1.0, env override honoured]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[_dashboard_auth_env_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_dashboard_host_default()]] - code - docker/bots/hermes/run-standalone.sh
- [[_feedbin_env_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_hermes_cron_ids_names]] - code - docker/bots/hermes/init-config.sh
- [[_secret_mount_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_wait_for_gateway_healthy()]] - code - docker/bots/hermes/run-standalone.sh
- [[aiohttp ClientSession closed-session crash-loop fix (partial)]] - rationale - docker/bots/hermes/patch_slack_session_recreate.py
- [[cmd_down()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_logs()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_status()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_up()]] - code - docker/bots/hermes/run-standalone.sh
- [[patch_slack_session_recreate.py]] - code - docker/bots/hermes/patch_slack_session_recreate.py
- [[run-standalone.sh]] - code - docker/bots/hermes/run-standalone.sh
- [[run-standalone.sh script]] - code - docker/bots/hermes/run-standalone.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run-standalonesh_Hermes_docker_run_launcher
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_setup-secrets.sh]]
- 2 edges to [[_COMMUNITY_AgentTarget (5)]]
- 2 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 2 edges to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]

## Top bridge nodes
- [[cmd_up()]] - degree 11, connects to 2 communities
- [[run-standalone.sh]] - degree 13, connects to 1 community
- [[Missing-secret visibility banner (expected secrets loop)]] - degree 4, connects to 1 community
- [[_wait_for_gateway_healthy()]] - degree 3, connects to 1 community
- [[Hermes deliberately absent from the dev compose override]] - degree 3, connects to 1 community
