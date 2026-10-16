---
type: community
cohesion: 0.16
members: 21
---

# start-agentshroud.sh

**Cohesion:** 0.16 - loosely connected
**Members:** 21 nodes

## Members
- [[Pending OpenClaw migration repair (openclaw doctor --fix) before gateway start]] - code - docker/scripts/start-agentshroud.sh
- [[_container_age_seconds()]] - code - docker/scripts/start-agentshroud.sh
- [[_dns_warmup_probe()]] - code - docker/scripts/start-agentshroud.sh
- [[_enforce_sandbox_cap()]] - code - docker/scripts/start-agentshroud.sh
- [[_model_runtime_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_poll_openclaw_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_read_hc_secret()]] - code - docker/scripts/start-agentshroud.sh
- [[_read_secret_file()]] - code - docker/scripts/start-agentshroud.sh
- [[_reap_exited_sandboxes()]] - code - docker/scripts/start-agentshroud.sh
- [[_reap_idle_sandboxes()]] - code - docker/scripts/start-agentshroud.sh
- [[_reconcile_security_critical_cron()]] - code - docker/scripts/start-agentshroud.sh
- [[_rename_to_meaningful()]] - code - docker/scripts/start-agentshroud.sh
- [[_slack_channel_id()]] - code - docker/scripts/start-agentshroud.sh
- [[_slack_send()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_bot_token()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_get_me_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send_photo()]] - code - docker/scripts/start-agentshroud.sh
- [[op_proxy_read_with_retry()]] - code - docker/scripts/start-agentshroud.sh
- [[start-agentshroud.sh]] - code - docker/scripts/start-agentshroud.sh
- [[start-agentshroud.sh script]] - code - docker/scripts/start-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/start-agentshroudsh
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_AgentShroud Falco Rules]]
- 1 edge to [[_COMMUNITY_security-entrypoint.sh]]
- 1 edge to [[_COMMUNITY__seed_cron]]
- 1 edge to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 1 edge to [[_COMMUNITY__is_op_reference_allowed]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]

## Top bridge nodes
- [[start-agentshroud.sh]] - degree 29, connects to 8 communities
