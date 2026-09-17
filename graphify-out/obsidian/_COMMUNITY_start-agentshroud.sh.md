---
type: community
cohesion: 0.16
members: 20
---

# start-agentshroud.sh

**Cohesion:** 0.16 - loosely connected
**Members:** 20 nodes

## Members
- [[_container_age_seconds()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_dns_warmup_probe()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_enforce_sandbox_cap()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_model_runtime_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_poll_openclaw_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_read_hc_secret()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_read_secret_file()]] - code - docker/scripts/start-agentshroud.sh
- [[_reap_exited_sandboxes()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_reap_idle_sandboxes()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_reconcile_security_critical_cron()]] - code - docker/scripts/start-agentshroud.sh
- [[_rename_to_meaningful()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_slack_channel_id()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_slack_send()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_bot_token()_2]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_get_me_ready()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send_photo()_1]] - code - docker/scripts/start-agentshroud.sh
- [[op_proxy_read_with_retry()]] - code - docker/scripts/start-agentshroud.sh
- [[start-agentshroud.sh_1]] - code - docker/scripts/start-agentshroud.sh
- [[start-agentshroud.sh script_1]] - code - docker/scripts/start-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/start-agentshroudsh
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_init-openclaw-config.sh]]
- 1 edge to [[_COMMUNITY_AgentShroud Falco Detection Rules]]
- 1 edge to [[_COMMUNITY_security-entrypoint.sh]]

## Top bridge nodes
- [[start-agentshroud.sh_1]] - degree 24, connects to 3 communities