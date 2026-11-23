---
type: community
members: 4
---

# S8 no raw ssh/agentshroud-bot@/real Tailscale FQDN in baked bot config

**Members:** 4 nodes

## Members
- [[OpenClaw Cron Jobs Configuration]] - document - docker/config/openclaw/cron/jobs.json
- [[S10 start-agentshroud.sh force-reconciles security-critical live cron jobs]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S8 no raw sshagentshroud-bot@real Tailscale FQDN in baked bot config]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S9 init-openclaw-config.sh seeds agentshroud-ssh-exec.sh rules into live AGENTS]] - concept - tests/startup_smoke/test_bot_boot_static.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/S8_no_raw_ssh/agentshroud-bot/real_Tailscale_FQDN_in_baked_bot_config
SORT file.name ASC
```
