---
type: community
members: 19
---

# run-standalone.sh (Hermes docker run launcher)

**Members:** 19 nodes

## Members
- [[AGENTSHROUD_HERMES_DISABLE_TELEGRAM opt-in]] - rationale - docker/bots/hermes/run-standalone.sh
- [[HERMES__UPSTREAM - agentshroud-dev-hermes-v2]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Hermes cron jobs paused by empty AGENTSHROUD_PROD_CRON_KEEP on container recreate]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Hermes launched via docker run, not compose]] - rationale - docker/bots/hermes/run-standalone.sh
- [[S13 Hermes start.sh expected-secrets banner accepts env vars in place of mounted files]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S17 Hermes run-standalone.sh resource caps prod 3g1.5, dev 2g1.0, env override honoured]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[_dashboard_auth_env_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_dashboard_host_default()]] - code - docker/bots/hermes/run-standalone.sh
- [[_feedbin_env_args()]] - code - docker/bots/hermes/run-standalone.sh
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
- 3 edges to [[_COMMUNITY_Sunday Upgrade prompt]]
- 2 edges to [[_COMMUNITY_test_hermes_cron_seed.py (2)]]
- 1 edge to [[_COMMUNITY_setup-secrets.sh (2)]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]

## Top bridge nodes
- [[cmd_up()]] - degree 11, connects to 2 communities
- [[run-standalone.sh]] - degree 15, connects to 1 community
- [[_feedbin_env_args()]] - degree 4, connects to 1 community
- [[_secret_mount_args()]] - degree 4, connects to 1 community
- [[S13 Hermes start.sh expected-secrets banner accepts env vars in place of mounted files]] - degree 2, connects to 1 community
