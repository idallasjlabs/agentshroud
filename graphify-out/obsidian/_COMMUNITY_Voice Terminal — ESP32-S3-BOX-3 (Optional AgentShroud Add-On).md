---
type: community
cohesion: 0.11
members: 33
---

# Voice Terminal — ESP32-S3-BOX-3 (Optional AgentShroud Add-On)

**Cohesion:** 0.11 - loosely connected
**Members:** 33 nodes

## Members
- [[Env-split cron enabledisable pass (dev enables, prod disables)]] - code - docker/scripts/start-agentshroud.sh
- [[OpenClaw Cron Jobs Configuration]] - document - docker/config/openclaw/cron/jobs.json
- [[Pending OpenClaw migration repair (openclaw doctor --fix) before gateway start]] - code - docker/scripts/start-agentshroud.sh
- [[S10 start-agentshroud.sh force-reconciles security-critical live cron jobs]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S11 init-openclaw-config.sh seeds jira_dev_ticket.py into live OpenClaw workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S8 no raw sshagentshroud-bot@real Tailscale FQDN in baked bot config]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S9 init-openclaw-config.sh seeds agentshroud-ssh-exec.sh rules into live AGENTS]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[_container_age_seconds()]] - code - docker/scripts/start-agentshroud.sh
- [[_dns_warmup_probe()]] - code - docker/scripts/start-agentshroud.sh
- [[_enforce_sandbox_cap()]] - code - docker/scripts/start-agentshroud.sh
- [[_model_runtime_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_oc_config_set()]] - code - docker/scripts/init-openclaw-config.sh
- [[_poll_openclaw_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_read_hc_secret()]] - code - docker/scripts/start-agentshroud.sh
- [[_read_secret_file()]] - code - docker/scripts/start-agentshroud.sh
- [[_reap_exited_sandboxes()]] - code - docker/scripts/start-agentshroud.sh
- [[_reap_idle_sandboxes()]] - code - docker/scripts/start-agentshroud.sh
- [[_reconcile_security_critical_cron()]] - code - docker/scripts/start-agentshroud.sh
- [[_rename_to_meaningful()]] - code - docker/scripts/start-agentshroud.sh
- [[_sha256()]] - code - docker/scripts/init-openclaw-config.sh
- [[_slack_channel_id()]] - code - docker/scripts/start-agentshroud.sh
- [[_slack_send()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_bot_token()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_get_me_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send_photo()]] - code - docker/scripts/start-agentshroud.sh
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - code - docker/scripts/init-openclaw-config.sh
- [[init-openclaw-config.sh runs doctor --fix before version seed (schema v23-v24 trap)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[init-openclaw-config.sh script]] - code - docker/scripts/init-openclaw-config.sh
- [[op_proxy_read_with_retry()]] - code - docker/scripts/start-agentshroud.sh
- [[start-agentshroud.sh]] - code - docker/scripts/start-agentshroud.sh
- [[start-agentshroud.sh script]] - code - docker/scripts/start-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Voice_Terminal__ESP32-S3-BOX-3_Optional_AgentShroud_Add-On
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py (4)]]
- 2 edges to [[_COMMUNITY_run-standalone.sh]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_Release Notes - AgentShroud v0.9.0]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py]]
- 1 edge to [[_COMMUNITY_TestFabricatedSecurityNotice (2)]]

## Top bridge nodes
- [[start-agentshroud.sh]] - degree 28, connects to 4 communities
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - degree 9, connects to 1 community
- [[OpenClaw Cron Jobs Configuration]] - degree 2, connects to 1 community
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - degree 2, connects to 1 community
