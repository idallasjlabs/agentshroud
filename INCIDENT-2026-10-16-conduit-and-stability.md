# Incident Log — Conduit connectivity + prod stability, 2026-10-15/16

Owner-facing summary of everything changed tonight, why, and what's still open.
Written at the owner's explicit request before he leaves for the office at ~05:50 EDT.
**No commits were made tonight.** Everything below is either a live/runtime change
(reverts on container restart unless noted) or a working-tree diff not yet committed.

## Context

- Daily Brief podcast silently stopped after 2026-10-12 (root cause: `AGENTSHROUD_PROD_CRON_KEEP`
  empty on a container recreation, paused all 35 Hermes cron jobs — see below).
- Owner wants Conduit (iOS app) working today, then a freeze on all further changes
  until Sunday's unattended upgrade.
- Owner explicitly declined further manual file edits as of 05:50 EDT. If the system
  is not stable by the time he reaches the office, he will revert `main` to the
  2026-10-10 commit and rebuild dev + prod from there.

## Fixes applied (live/runtime, working as of 05:50 EDT)

1. **Hermes cron jobs resumed** — 6 of 35 jobs (`Daily Brief`, `Podcast Discovery`,
   `Feed Curator`, `Breaking AI News`, `Sunday Upgrade Report`, `Feed Refresh`) were
   manually resumed via `hermes cron resume <id>` on `agentshroud-hermes-v2`. The other
   29 remain paused (20 stale since August — pre-existing, unrelated; 9 never had a
   run history — left alone pending an explicit decision). **Not yet committed as a
   code fix** — see "Known gaps" below.

2. **Rapid-MLX `host.docker.internal` trusted-hosts fix** — `/Users/ijefferson.admin/Development/local-llms/scripts/services.sh:1293`
   was missing `host.docker.internal` in its `--trusted-hosts` list, causing every
   gateway-forwarded local-model request (Hermes + OpenClaw chat) to be rejected with
   `Invalid host header`. Added it, restarted rapid-mlx. **This is a committed-looking
   edit in a separate repo (`local-llms`), not `agentshroud`** — confirm with dev
   whether that repo needs a PR too.

3. **Hermes dashboard relay for Conduit** — Tailscale's `:9119` serve mapping was
   repointed from the gateway's own `/hermes-dashboard/` reverse proxy (which has an
   unresolved 502 issue — see "Known gaps") to a new `hermes-dashboard-relay` container
   that forwards directly to Hermes's dashboard bridge port 9120, with a
   `--restart unless-stopped` policy. **This bypasses the gateway's audit/security
   middleware for dashboard traffic** — explicitly flagged as a temporary stopgap, not
   a permanent architecture decision. Confirmed working via Conduit login tonight.

4. **OpenClaw sandbox mode disabled** — `openclaw config set agents.defaults.sandbox.mode off`,
   run live inside `agentshroud-openclaw`. Root cause: `/home/node/.openclaw` is a named
   Docker volume, but OpenClaw's sandbox feature requires a host bind-mount for sibling
   sandbox containers (confirmed via OpenClaw's own docs, `docker-backend.md`: "Named
   volumes... are unsupported sources for sibling sandbox mounts"). Sandboxing was
   SILENTLY OFF in prod before this was ever turned on (see `docker/docker-compose.yml:563-571`),
   so this restores the prior known-stable state. **This does NOT survive a container
   restart** — `docker/scripts/init-openclaw-config.sh:440` hardcodes
   `agents.defaults.sandbox.mode all` on every boot. Owner declined a file edit to fix
   this durably, so **any future restart of `agentshroud-openclaw` will silently
   re-break this** until that line is changed or the volume is migrated to a bind mount.

5. **Hermes Telegram connection recovered** — Hermes's Telegram polling died silently
   around 05:15 EDT (no self-recovery despite its own retry logic) and was stuck for
   ~18 minutes. Fixed by `docker restart agentshroud-hermes-v2`. Confirmed via a live
   Telegram send test (HTTP 200, message delivered).

6. **OpenClaw stuck session cleared** — a single agent run got stuck waiting on an
   unapproved "elevated command" (`systemctl status openclaw-gateway` — an odd
   self-check with no obvious cause, not investigated further), and every subsequent
   "hello" was being merged into that same stuck run instead of starting fresh. Fixed
   by `docker restart agentshroud-openclaw`. This restart is also what re-triggered
   item 4's sandbox-mode revert.

7. **Today's Daily Brief (2026-10-16) published automatically** — the host-side `pke`
   publish job (`~/Development/pke`, launchd `com.pke.daily-brief-publish`, scheduled
   04:35 EDT) ran on its own and successfully published episode_37. No action needed.

## Daily Brief backfill — in progress, not complete

- **2026-10-13**: no content was ever generated (cron was paused all day). Nothing to
  recover — would need fresh generation, and the underlying `daily-brief` script only
  gathers "current window" news (no historical-date parameterization), so a true
  "as it would have been" reconstruction for that specific day is not fully possible.
- **2026-10-14, 2026-10-15**: real content WAS generated and staged
  (`/opt/data/podcasts/outbox/daily/2026-10-14/` and `.../2026-10-15/` inside
  `agentshroud-hermes-v2`, both with `READY` markers never consumed) — the host-side
  publish job only ever processes *today's* dated folder, never catches up on backlog.
  Was in the middle of running `python3 scripts/publish_daily_brief.py --date 2026-10-14`
  (in `~/Development/pke`) when this got interrupted — **status unconfirmed, check
  `~/Library/Logs/daily-brief-publish.log` / `.err` and whether `--date 2026-10-15`
  still needs to be run.**

## Unresolved — flagged, not fixed tonight

- **Suspected prompt-injection / phishing incident on Hermes or OpenClaw.** The owner's
  Telegram history shows a bot-generated message (AgentShroud-branded) offering fake
  "Tailscale Configuration" instructions with a non-existent domain
  (`https://tailscale.tm:443`) and prompts to enter real Tailscale username/password or
  generate an auth key via fabricated CLI syntax. A later session-restore message
  ("we had just covered the Tailscale URL, username/password, and auth key options")
  confirms the bot's own session treated this as real prior conversation — **this was
  not something the owner typed, the bot actually generated and sent it.** Root cause
  NOT investigated tonight (time did not allow). This needs dedicated, careful
  investigation: how a message impersonating AgentShroud's own branding with
  credential-phishing content got into a live conversation. Do not dismiss as a user
  paste — the session-restore message is independent corroborating evidence.
- **Gateway's `/hermes-dashboard/` reverse proxy 502 from host/Tailscale** (works fine
  from inside the Colima VM). `HERMES_DASHBOARD_UPSTREAM` is confirmed correctly set
  (`http://agentshroud-hermes-v2:9120`) in the live gateway container, ruling out the
  obvious stale-config theory. Root cause never found despite a full Colima VM rebuild
  and extensive investigation. Item 3 above is the live workaround.
- **Hermes Telegram message-edit `KeyError('date')`** (`plugins/platforms/telegram/adapter.py:3987`) —
  dev (separate session, `agentshroud-dev`) wrote and dry-run verified a patch
  (`docker/bots/hermes/patch_telegram_edit_message_date.py`), wired into
  `docker/bots/hermes/Dockerfile`, and was applying it live to prod's running container
  without a rebuild when this session's work was interrupted. **Confirm with dev
  whether this actually landed on prod.**
- **OpenClaw `execute_code` tool error**: "Python 3 is not available in the docker
  terminal environment" — traced to `tools/code_execution_tool.py:634`'s remote-backend
  python3 check; the configured `docker_image` (`nikolaik/python-nodejs:python3.11-nodejs20`)
  does ship Python 3.11, so the check failing is unexplained. Not root-caused.
- **Telegram SSL `UNEXPECTED_EOF_WHILE_READING` reconnect warnings** — recurring every
  few minutes in Hermes, always self-healing via retry, not investigated further
  (assumed transient network/Telegram-API-side).
- **OpenClaw Slack Socket Mode reconnect loop** (`socket-mode:socket-mode WebSocket
  error! SMWebsocketError`, repeating ~every 20s) — noticed late, not investigated.
- **Trivy "2 CRITICAL vulnerabilities" alert** received via Telegram at 05:31 EDT —
  could not find a matching scan result anywhere (gateway's own entrypoint scan history
  shows 0 critical consistently, including the most recent run). Likely stale/delayed
  alert delivery, not confirmed either way.
- **Container sprawl**: 16+ `openclaw-mcp-github-*` sidecars and similar accumulating
  over the session (partially self-cleaned by OpenClaw's own `sandbox-reaper` on
  restart). The `~/Development/.colima-backup-temp` directory (~4.7GB, pre-Colima-rebuild
  backup, likely safe to delete now) and general `docker system prune` cleanup the
  owner requested earlier tonight were never executed.

## What requires a code change (deferred, needs review — NOT done tonight)

- `docker/scripts/init-openclaw-config.sh:440` — change `agents.defaults.sandbox.mode all`
  to `off` (or migrate `/home/node/.openclaw` to a host bind-mount instead, the "proper"
  fix) so the sandbox stopgap survives restarts.
- `docker/bots/hermes/run-standalone.sh` — self-source `docker/.env` (working-tree diff
  already written, sitting on branch `fix/hermes-cron-pause-alert-20261012`, uncommitted).
- `docker/bots/hermes/init-config.sh` — add a loud Telegram alert when prod cron
  reconciliation keeps 0 jobs (not started; was assigned to dev).
- Gateway-routed replacement for the `:9119` dashboard relay bypass (item 3) and the
  pre-existing `:8642`/`:8765` direct-to-Hermes/Voice-Gateway Tailscale bypasses
  (`scripts/tailscale-serve.sh:85-89`) — proper fix scoped for after Sunday.

## For dev / prod sync

Message sent to `agentshroud-dev` asking them to write the equivalent doc for any
changes made on their side tonight (the Hermes Telegram patch, their own duplicate
Telegram-poller fix, anything else). Cross-reference both docs before Sunday's upgrade.
