---
type: community
cohesion: 0.11
members: 25
---

# start.sh

**Cohesion:** 0.11 - loosely connected
**Members:** 25 nodes

## Members
- [[Crash backoff escalation — 5 restarts600s pauses 300s (raw curl, helpers not yet defined)]] - rationale - docker/bots/hermes/start.sh
- [[HERMES_HOME]] - code - docker/bots/hermes/start.sh
- [[HOME_1]] - code - docker/bots/hermes/start.sh
- [[Post-migration model lock — resolve_model.py sets model.defaultprovider + cron.model after readiness]] - rationale - docker/bots/hermes/start.sh
- [[Referenced resolve_model.py (usrlocallibagentshroudresolve_model.py)]] - code - docker/bots/hermes/start.sh
- [[Sandboxed terminal config — terminal.docker_ keys set via `hermes config set`, not env vars]] - rationale - docker/bots/hermes/start.sh
- [[XDG_CACHE_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_DATA_HOME]] - code - docker/bots/hermes/start.sh
- [[XDG_STATE_HOME]] - code - docker/bots/hermes/start.sh
- [[_count_recent_restarts()]] - code - docker/bots/hermes/crashwatch.sh
- [[_email_owner()]] - code - docker/bots/hermes/start.sh
- [[_log()_1]] - code - docker/bots/hermes/crashwatch.sh
- [[_read_last_alert_epoch()]] - code - docker/bots/hermes/crashwatch.sh
- [[_release_telegram_lock()]] - code - docker/bots/hermes/start.sh
- [[_telegram_alert()]] - code - docker/bots/hermes/crashwatch.sh
- [[_telegram_bot_token()_1]] - code - docker/bots/hermes/start.sh
- [[_telegram_get_me_ready()_1]] - code - docker/bots/hermes/start.sh
- [[_telegram_send()_1]] - code - docker/bots/hermes/start.sh
- [[_telegram_send_photo()_1]] - code - docker/bots/hermes/start.sh
- [[_write_last_alert_epoch()]] - code - docker/bots/hermes/crashwatch.sh
- [[crashwatch.sh]] - code - docker/bots/hermes/crashwatch.sh
- [[crashwatch.sh script]] - code - docker/bots/hermes/crashwatch.sh
- [[start.sh]] - code - docker/bots/hermes/start.sh
- [[start.sh script]] - code - docker/bots/hermes/start.sh
- [[start.sh — Hermes s6-overlay startup wrapper (main program)]] - code - docker/bots/hermes/start.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/startsh
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY__seed_cron]]
- 1 edge to [[_COMMUNITY_test_hermes_model_resolver.py]]

## Top bridge nodes
- [[start.sh — Hermes s6-overlay startup wrapper (main program)]] - degree 5, connects to 2 communities
- [[Post-migration model lock — resolve_model.py sets model.defaultprovider + cron.model after readiness]] - degree 4, connects to 1 community
