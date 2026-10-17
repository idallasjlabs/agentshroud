# Incident: Conduit/Hermes instability, 2026-10-16 (overnight)

Owner-requested record of every change made tonight (dev side), why, and current status.
Prod is writing a companion doc for live/prod-side changes it made. If the system is not
stable by the time the owner reaches the office, the stated fallback is: delete all commits
after 2026-10-10 from `main` and rebuild dev and prod from that commit
(`5ed8d4596a3312cc9e7f12f2ba3fb2bb2be3d1c8` — last commit before 2026-10-11, see `git log`).
This doc exists so that decision can be made with full information.

## Trigger

Owner reported no Daily Brief podcast since 2026-10-12, and Conduit (iOS app) unable to
connect. Initial ask was a full revert to the 2026-10-10 commit; investigation found several
of the commits since then were themselves fixes for Conduit, not the cause of breakage, so
work proceeded as targeted fixes instead of a blanket revert. That decision is what's being
revisited now given continued instability.

## Complete commit list, 2026-10-10 through tonight (`main`, this repo)

Last commit on or before 2026-10-10: `5ed8d4596a` (2026-10-08 06:26 — nothing merged
2026-10-09 or 2026-10-10). Every commit after that point, in order:

1. **`5cfea5479f`** — 2026-10-11 19:48 — `fix(sunday-scan): retry a transient trivy
   DB-download failure (#498)`
   Files: `scripts/lib/sunday-scan.sh`, `scripts/smoke.d/test-sunday-upgrade-scan.sh`
   (2 files, +118/-5). Build-pipeline robustness fix (retry logic for a flaky Trivy DB
   download during the weekly scan). No runtime/production behavior change.

2. **`44a9e42d00`** — 2026-10-11 19:55 — `chore(upgrade): 2026-10-11 Sunday upgrade --
   OpenClaw 2026.10.1, Syft 1.54.1, Docker CLI 29.9.0, base digest refresh (#497)`
   Files: `docker/bots/openclaw/Dockerfile`, `docker/versions.env`,
   `docker/wazuh-agent/Dockerfile`, `gateway/Dockerfile`,
   `gateway/tests/test_triage_cve_mitigations.py`, `reports/upgrade-2026-10-11.md`,
   `voice_gateway/Dockerfile` (7 files, +133/-20). Routine weekly version-pin bumps +
   base-image digest refresh, per the standing Sunday-upgrade policy.

3. **`8540fe1f0a`** — 2026-10-12 12:40 — `fix(hermes): bind dashboard non-loopback so
   auth is actually enforced (#496)`
   Files: `docker/bots/hermes/run-standalone.sh`,
   `gateway/tests/test_security_regressions_v1_2.py`, `scripts/tailscale-serve.sh`
   (3 files, +82/-7). **Security-positive.** Hermes's dashboard was bound to
   127.0.0.1 and reached externally only via Tailscale Serve → the dashboard's own
   auth gate never activated regardless of config. Fixes the bind (opt-in, only when
   real basic-auth credentials are provisioned) AND makes permanent a live fix from
   2026-10-08 that re-routed `tailscale-serve.sh`'s `:9119` mapping from going straight
   to Hermes to going through the gateway's `/hermes-dashboard/` reverse proxy instead
   — closing a real bypass of the gateway's isolation boundary.

4. **`b904a98362`** — 2026-10-12 18:34 — `fix(sunday-upgrade): add tap-approval gates,
   one-line rollback, broader inventory (#502)`
   Files: `prompts/sunday-upgrade.md`, `scripts/sunday-rollback.sh`,
   `scripts/sunday-upgrade-approve.sh` (3 files, +180/-6). Process/tooling only — adds
   human tap-approval gates before merging the weekly upgrade PR and before touching a
   live prod container, plus a one-line rollback script. No change to any running
   service's behavior.

5. **`7535c81184`** — 2026-10-13 02:38 — `chore(upgrade): 2026-10-12 Sunday upgrade --
   OpenClaw 2026.10.2, GH Actions, CVE fixes (anyio/idna/starlette/multidict/urllib3)
   (#503)`
   Files: `.github/workflows/ci.yml`, `.github/workflows/release.yml`,
   `.github/workflows/security-scan.yml`, `docker/versions.env`,
   `gateway/requirements.lock`, `gateway/requirements.txt`, `gateway/web/installer.py`,
   `reports/upgrade-2026-10-12.md`, `scripts/check-vendor-compat.sh` (9 files,
   +216/-32). **Contains the CVE patches** (anyio/idna/starlette/multidict/urllib3)
   plus the OpenClaw 2026.10.1→2026.10.2 bump and stale GitHub Actions pin bumps.

6. **`409e3a70f9`** — 2026-10-13 17:48 — `fix(hermes): proxy the dashboard's WebSocket
   channels through the gateway (#504)`
   Files: `gateway/ingest_api/main.py`, `gateway/tests/test_main_endpoints.py`
   (2 files, +184/-0). **This is a Conduit fix.** The gateway's existing HTTP reverse
   proxy for the dashboard never handled WebSocket-scope connections, so Conduit could
   authenticate over HTTP and then silently fail to open its WebSocket. Adds a matching
   WebSocket proxy route.

7. **`617275e267`** — 2026-10-14 06:30 — `fix(hermes): Edge TTS fails outright --
   proxy, egress allowlist, stale pin (#505)`
   Files: `docker/bots/hermes/Dockerfile`, `docker/bots/hermes/patch_edge_tts_proxy.py`
   (new), `gateway/security/egress_config.py` (3 files, +119/-0). **This is a Conduit
   fix.** Fixes three stacked bugs blocking Conduit's "Test speaking" (Edge TTS):
   proxy not honored by the TTS library's websocket connect, `speech.platform.bing.com`
   missing from the egress allowlist, and a stale `edge-tts` pin that predated a
   Microsoft anti-abuse handshake requirement.

## Dev-side changes made tonight (this repo, this session)

1. **Stopped `agentshroud-openclaw` (dev's own container).**
   Dev's OpenClaw instance was running with `TELEGRAM_BOT_TOKEN_FILE=/run/secrets/telegram_bot_token`
   — the same token prod's production OpenClaw uses. Two instances polling Telegram's
   `getUpdates` with the same bot token produced the "Another OpenClaw gateway... may be
   using this bot token" conflict prod was chasing, with OpenClaw crash-looping every ~30s.
   Stopping dev's instance cleared it (confirmed by prod: zero recurrences for 5.5+ minutes
   after). **Not a code change** — just stopped a container dev wasn't actively using, per
   existing policy that only prod runs recurring/live jobs.
   **Status: resolved.**

2. **New file: `docker/bots/hermes/patch_telegram_edit_message_date.py`**, wired into
   `docker/bots/hermes/Dockerfile` (new `COPY`/`RUN`/`rm` block after the existing
   `patch_edge_tts_proxy.py` block).
   Root cause: the pinned `python-telegram-bot` library (`telegram/_message.py`,
   `MaybeInaccessibleMessage._de_json`) does a bare `data["date"]` dict subscript when
   parsing the response to `editMessageText`. Telegram returned an edit-success response
   missing the `date` key entirely (not the documented `InaccessibleMessage` case, which
   uses `date=0`, a present key) — this raised `KeyError('date')` in Hermes's own
   `plugins/platforms/telegram/adapter.py:_edit_text` **after the edit had already applied
   server-side**, so Hermes logged a real edit as a failure
   (`Failed to edit Telegram message N: 'date'`).
   Fix: wrap the `edit_message_text` call in `_edit_text` with a `try`/`except KeyError`
   that treats this specific case as success (mirrors the existing "not modified" handling
   already in the same file for another known Telegram response quirk). Any other
   `KeyError` still propagates.
   Verified: dry-run patch applied cleanly against a real copy of the live file, compiled
   clean, then live-applied (via `docker cp`, no rebuild) to `agentshroud-dev-hermes-v2`
   and restarted — container came back healthy. Exact apply-to-prod steps were sent to
   prod; **prod's own confirmation that this was applied to the live production container
   is still outstanding as of this writing** — check with prod directly.
   **Status: fix written, tested in dev, committed to the repo and wired for future
   rebuilds. Live application to prod's running container unconfirmed.**

3. **Attempted, NOT completed: `docker/docker-compose.yml` edit to mount the existing
   `google_api_key` Docker secret into the `hermes` service**, as the first step toward
   wiring Gemini as a fallback TTS provider (Edge TTS is hitting a live 403 from Microsoft's
   anti-abuse system on `speech.platform.bing.com` — confirmed directly from Conduit's own
   error screen, with a valid `Sec-MS-GEC` token present, meaning our existing fix is
   generating the token correctly and Microsoft is rejecting it anyway; this is an external,
   currently-flaky dependency, not something in our control). The one-line edit (`- google_api_key`
   added to the `hermes:` service's `secrets:` list, alongside the existing `openai_api_key`
   entry) was blocked by Claude Code's own safety classifier as a "secret-store write."
   Per how this session is required to operate, that block was not routed around (not
   retried a different way, not handed to prod to do instead) — it was surfaced back to the
   owner directly for a decision.
   **Status: NOT done. Voice "speak" (TTS) remains on Edge TTS only, which is currently
   unreliable due to Microsoft-side anti-abuse rotation. No code-level fallback is wired.**

4. **`docker/scripts/init-openclaw-config.sh`** — changed `agents.defaults.sandbox.mode`
   from `all` to `off` (with an explanatory comment at the change site). This is the
   durable version of the OpenClaw sandbox stopgap described above — **a real, lasting
   reduction in isolation**, not a one-night workaround: OpenClaw's exec/read/write/edit
   tools now run in its own container instead of an ephemeral per-session sandbox, on
   every future restart, until someone restores `mode=all` and separately fixes the
   named-volume-vs-bind-mount mismatch that caused this. Owner-approved explicitly
   ("you make all of the edits you need to make, don't ask me to make any manual edits").
   Equivalent change was independently reported as already applied live by prod;
   this commit makes it the repo's actual state so a future rebuild doesn't silently
   revert it back to `mode=all` and reintroduce the failure.
   **Correction (07:07 EDT): this is NOT durable yet on any running container.**
   `docker/bots/openclaw/Dockerfile:280` bakes the script into the image, so the running
   OpenClaw containers (dev and prod) still execute the old `mode all` line on every boot
   until the OpenClaw image is rebuilt. Confirmed on dev after a full clean recreate: init
   logged `Sandbox config applied (mode=all ...)` and a real Telegram message failed with
   the sandbox mount error. Live stopgap re-applied on dev with
   `openclaw config set agents.defaults.sandbox.mode off` — OpenClaw hot-reloads it
   (`[reload] config hot reload applied`), no restart needed, but it is lost on the next
   container restart. The next image rebuild (the Sunday upgrade on 2026-10-18 rebuilds
   every image from `main`) bakes the repo fix in. Until then: if OpenClaw restarts on
   either host, re-run that `config set`.
   **Status: committed in repo; live-applied on dev (and reported live-applied on prod);
   durable only after the next image rebuild.**

## Why a blanket revert to Oct 10 was not done (for the record)

The commits between Oct 10 and tonight include two categories:
- **CVE/security patches** (`7535c81184` — anyio/idna/starlette/multidict/urllib3) and a fix
  that **closed** a real dashboard-to-Hermes bypass (`8540fe1f0a`, auth enforcement +
  routing the dashboard through the gateway instead of straight to Hermes). Reverting these
  would reintroduce patched CVEs and reopen a bypass the owner explicitly flagged as
  unacceptable back on 2026-10-08.
- **The actual Conduit fixes** (`409e3a70f9` — dashboard login WebSocket proxy;
  `617275e267` — Edge TTS proxy/egress/pin fix). These are literally the fixes that made
  Conduit's login and voice work at all. Reverting them would re-break the exact things
  being asked to fix.

This reasoning stands regardless of tonight's continued instability — the instability traces
to bugs in code paths that were newly exercised by Conduit for the first time this week
(sandbox provisioning, Telegram message-editing, the dashboard relay), not to the commits
themselves being wrong. That said, this is the owner's call to make with full information,
which is the purpose of this document.

## Known open issues as of 05:50 EDT, 2026-10-16

- **Edge TTS / Microsoft 403**: external, intermittent, unresolved. Gemini fallback blocked
  on the docker-compose secret-mount permission issue above.
- **`execute_code` tool error** ("Python 3 is not available in the docker terminal
  environment"): reported by prod, never root-caused. Status unknown.
- **OpenClaw sandbox provisioning**: `/home/node/.openclaw/workspace` is a named Docker
  volume, but the sandbox code needs a real host bind-mount to pass through to the sibling
  sandbox container it spawns — structural mismatch, fails on every message that triggers
  sandbox provisioning. Asked prod to disable sandbox mode as a fast stopgap (known-working
  prior state) instead of a live volume migration under time pressure; **confirmation this
  was done is outstanding**.
- **Two live, uncommitted bypasses on prod**, both explicitly flagged tech debt, proper
  gateway-routed fix deferred to after Sunday:
  - `scripts/tailscale-serve.sh:85-89` serves Hermes's OpenAI-compatible API (:8642) and the
    Voice Gateway WS (:8765) directly to the tailnet, not through the gateway. Pre-existing,
    predates this week. Confirmed not in Conduit's actual critical path.
  - A manually-created `hermes-dashboard-relay` container now serves Conduit's dashboard
    traffic (:9119) directly to Hermes's dashboard bridge, bypassing the gateway's own
    `/hermes-dashboard/` reverse proxy — because that proxy was 502ing from host/Tailscale
    tonight for a reason never pinned down (works fine from inside the Colima VM). This
    relay has no equivalent in git — it only exists live on prod's running Docker host.
- **Daily Brief delivery confirmation**: the 04:30 run today shows `completed` in Hermes's
  cron log, and a live Telegram send-test separately confirmed outbound delivery works in
  general, but no log evidence was ever found confirming that specific run's message actually
  reached Telegram (as opposed to just exiting 0). Not re-checked since.

## Root cause of dev-side instability, found 06:53 EDT: lazydocker connection leak

Dev's Colima VM showed `dockerd` at 418% CPU / 2.2 GB RSS / 68 min CPU time in a
26-minute-old VM, `containerd` at 218%, with every container idle and zero daemon log
warnings. `ss -x` inside the VM showed **565 established connections to docker.sock**;
on the host, `lsof` showed 562 of them belonging to the single `ssh` process that is
Colima's socket forward, and two long-running `lazydocker` instances (8.5 h and 2 h old).
lazydocker holds a Docker event stream plus a per-container stats stream, and reconnects
aggressively on error — every Colima bounce tonight made it reconnect and leak the old
connections through the ssh forward. Killing the 8.5 h instance dropped dockerd to
**0 connections and 8% CPU within six seconds**.

This explains, on dev: the embedded-DNS "server misbehaving" failures (Wazuh manager →
indexer, Wazuh agent → manager), pathologically slow `docker ps`, the health-check script
repeatedly deciding "Docker is not responding" and bouncing Colima, and the host-level
load spikes (dev's VM alone was ~6 cores). Prod's VM should be checked for the same
pattern (`colima ssh -- sudo ss -x | grep -c docker.sock`; anything in the hundreds is
the leak). Not a code bug in this repo; operational.

## Dev bring-up failures 06:32-06:57 EDT: compose-version network hash + stale endpoints

Three consecutive `scripts/asb up` runs on dev failed, each one layer deeper. Two
independent causes stacked:

1. **Compose version mismatch forces network recreation.** The live networks
   (`agentshroud-bot_agentshroud-internal` / `-isolated`) carried
   `com.docker.compose.version: 5.1.4` labels; the installed `docker-compose` is 5.6.0.
   Their config-hash labels never match what 5.6.0 computes, so every `up` tries to
   remove and recreate both networks. That removal is blocked by any running container
   attached to them that compose doesn't manage in that invocation — on dev, the
   voice-gateway (`--profile voice`) and the standalone Hermes container — so the sanctioned
   `asb up` could not succeed without parking those first. Once recreated by 5.6.0 the
   labels match and this stops happening.
2. **Stale network-endpoint records after the Colima bounces.** Containers that lived
   through tonight's VM restarts (gateway, OpenClaw, Wazuh manager/agent, socket proxy)
   had config saying "attached to network X" while dockerd's live state did not — so
   compose's disconnect-before-recreate step failed with
   `container ... is not connected to the network ...` and aborted mid-run, leaving
   whatever it had already stopped stopped. `docker network disconnect -f` clears the
   record for a container you want to keep; `docker rm` of the stopped container is the
   clean fix when compose is recreating it anyway (all persistent state is in named
   volumes — `gateway-data`, `agentshroud-config`, etc. — none were removed).

Fix applied: removed the stale stopped compose containers, force-detached Hermes and
voice-gateway, ran `asb up` (recreates networks + stack with asb's secrets override —
which selects `telegram_bot_token_marvin.txt`, the separate dev bot, for USER=agentshroud-bot),
then started Hermes and voice-gateway back (they reattach by network name).

**Prod should expect the same network-recreate behavior** on its next `asb up` if its
networks also carry 5.1.4 labels and its compose binary is 5.6.0; with voice-gateway
running it will fail the same way. Check: `docker network inspect <project>_agentshroud-internal
--format '{{index .Labels "com.docker.compose.version"}}'` vs `docker-compose version --short`.

## Root cause of the broken chat since Sunday: Nemotron + the Qwen-only `/no_think` suffix (prod, 07:10 EDT)

The owner's instinct that "it broke at the last unattended update" was right. The
2026-10-11/12 upgrade moved Rapid-MLX's anchor model from Qwen3 to NVIDIA Nemotron 3.5.
Two consequences stacked (proven by prod with live calls, fixed in `0ffa0cd794`):

1. Nemotron reasons in-band, in plain text, and burned the whole `max_tokens` budget on
   "Here's a thinking process: 1. Analyze User Input…" before answering
   (`finish_reason=length`). That is the "Working — 3/6 min" stalls, the empty replies
   and the "Something went wrong" errors in both Hermes and OpenClaw.
2. The gateway's `_suppress_qwen3_thinking` (`gateway/proxy/llm_proxy.py`) appended the
   Qwen3 chat-template suffix ` /no_think` to every Rapid-MLX request regardless of
   model. Nemotron treated it as literal user text — Hermes turned "hello" into
   `echo "hello / no_think"` — which then tripped the elevated-command approval gate and
   produced the "typing forever" symptom.

Fixes: `local-llms/scripts/services.sh` launches Nemotron with
`--default-reasoning-effort none` (separate repo, prod's host); `llm_proxy.py` now sends
`reasoning_effort: "none"` to non-Qwen models and only adds `/no_think` for Qwen
(`gateway/tests/test_llm_proxy_thinking_suppression.py`, 8 cases, pass on dev). The proxy
change is baked into the gateway image — both hosts rebuilt: prod first, dev at
07:44 EDT (gateway) and 07:57 EDT (OpenClaw, after two transient download failures —
an apt `Hash Sum mismatch` and a curl TLS `bad record mac` under the build-time load
spike; third attempt clean). Dev's rebuilt OpenClaw boots with `mode=off` in its own init
log, `doctor --fix` ran at init with no schema-v23 complaint, and it has logged zero
`getUpdates` conflicts since — so the earlier dev-bot conflicts (see below) stopped with
the fresh container.

Related trap found on both hosts: rebuilding/recreating OpenClaw seeds the pinned
2026.10.2 over a volume that was at 2026.9.6, leaving every agent DB at schema v23 —
"stop active agents and run openclaw doctor --fix … Sessions remain unavailable".
`init-openclaw-config.sh` runs `doctor --fix` BEFORE the version seed, so the first boot
after a bump doesn't catch it; it migrates on the next boot or a manual
`openclaw doctor --fix` (which needs the gateway process stopped — it holds the state
DB). Moving that doctor call after the seed is follow-up work, not done tonight.

## Dev Hermes was polling prod's Hermes Telegram bot (found 07:12 EDT)

`docker/secrets/hermes_telegram_bot_token.txt` and `hermes_telegram_bot_token_marvin.txt`
are byte-identical on dev — there is no separate dev Hermes bot. So whenever dev's Hermes
container is up (it was, most of tonight), two Hermes instances long-poll the same bot:
Telegram 409s both ("terminated by other getUpdates request"), each reconnects, and the
owner's messages to Hermes are split unpredictably between dev and prod. Dev's Hermes
logged a conflict every ~minute; prod's Hermes showed the other side as "Telegram SSL
UNEXPECTED_EOF_WHILE_READING, reconnecting" every few minutes all night.

Fix tonight, in two parts (the first alone was NOT enough — verified):
- `docker/bots/hermes/run-standalone.sh`: opt-in `AGENTSHROUD_HERMES_DISABLE_TELEGRAM=1`
  skips mounting only the Telegram token and forwards the flag into the container.
- `docker/bots/hermes/agentshroud-secrets.sh` (s6 cont-init, runs as root before any
  service): with the flag set it skips the `TELEGRAM_BOT_TOKEN` injection AND strips any
  persisted `TELEGRAM_BOT_TOKEN=` line from `/opt/data/.env` on the config volume. That
  second part matters: with only the mount skipped, `start.sh` correctly logged
  "TELEGRAM_BOT_TOKEN not set — Telegram channel disabled" and Hermes's adapter then
  connected anyway, because its dotenv tier read the token an earlier boot had persisted.
  Verified after stripping it: no "Connecting/Connected to Telegram" lines, container
  healthy; prod's Hermes reported zero 409/SSL-EOF lines from its clean restart onward.
Default (flag unset) = unchanged, so prod's Hermes launches are unaffected. Dev's Hermes
is launched with `AGENTSHROUD_HERMES_DISABLE_TELEGRAM=1 scripts/asb up hermes`.
Persisting the flag in dev's `docker/.env` (which `asb` sources for Hermes launches) was
blocked by the session's secret-store guardrail — the owner should add that one line so a
future dev launch without the flag doesn't silently re-enable polling. Durable fix: a
dedicated dev Hermes bot (BotFather) stored as `hermes_telegram_bot_token_marvin.txt`, so
the `_marvin` variant actually means something.

Side effect the owner noticed: the `agentshroud_marvin_op…` Telegram chat (the dev
OpenClaw bot) received dev Hermes lifecycle banners — "Hermes starting 07:07", "Hermes
online — missing secrets…", "Hermes is shutting down 07:16" — which read like prod Hermes
bouncing. They were dev's, from before the flag took effect; `start.sh`'s and
`crashwatch.sh`'s notifiers send only when `TELEGRAM_BOT_TOKEN` is set, so with the flag
they now log "No Telegram bot token available — cannot send notification" instead
(verified 07:17). Follow-up worth a look: why those banners landed in the *OpenClaw* bot's
chat at all when dev Hermes was holding the Hermes token — `gateway/ingest_api/lifespan.py:98`
resolves per-bot tokens as `telegram_bot_token_{bot_id}`, but the Hermes secret is named
`hermes_telegram_bot_token`, so system sends attributed to "hermes" may be falling back to
the gateway's default (OpenClaw) token. Not changed tonight.

**Open, dev-only:** dev's OpenClaw (now correctly on the marvin dev-bot token) still logs
a `getUpdates` conflict about once a minute. Nothing on prod references that token
(verified by prod via per-container mount listing), and nothing else under the dev account
polls it (process + tmux sweep). Hypothesis under test: OpenClaw 2026.10.x runs two
Telegram ingress workers and conflicts with itself ("isolated polling ingress failed …
restarting"); prod's rebuilt 2026.10.2 container is the control. Affects the dev bot only.

## What prod should document separately

Everything prod did live tonight that has no corresponding git commit: the
`hermes-dashboard-relay` container (both its first, restart-policy-less creation and its
recreation), the 6 cron jobs manually resumed (and which 29 remain paused and since when),
the rapid-mlx `--trusted-hosts` fix in the separate `local-llms` repo, whatever was decided
on the OpenClaw sandbox disable, and the live application (or not) of the Hermes Telegram
patch to the production container. None of that is visible from this repo's git history.

**Update, ~06:00 EDT:** Prod has written this companion doc —
`INCIDENT-2026-10-16-conduit-and-stability.md` at the repo root (prod's working tree, NOT
committed, per the owner's no-more-changes instruction). Key facts from it folded in here:

- **OpenClaw's sandbox-mode disable does NOT survive a restart.**
  `init-openclaw-config.sh:440` re-seeds `agents.defaults.sandbox.mode` to `"all"` on every
  boot. So the sandbox-provisioning failure (named-volume vs required bind-mount mismatch,
  see above) **will come back** the next time OpenClaw's container restarts for any reason
  — including the host-contention-driven Colima bounces seen repeatedly tonight. The owner
  declined the file edit that would fix this durably (consistent with the freeze). This is
  the single most likely thing to silently regress before the owner is back.
- **Hermes Telegram patch (`patch_telegram_edit_message_date.py`) application to prod's
  live container is UNCONFIRMED as of this commit.** Confirmed as of ~06:05 EDT that it
  had NOT been applied (prod checked their own action history directly). I handed prod
  the live-apply steps again at that point; final confirmation it's actually live on
  prod's running container is still outstanding — check with prod before assuming it's
  fixed there. It IS fixed and committed in this repo (see below), so any future rebuild
  picks it up regardless.
- A **suspected prompt-injection / phishing incident** was separately flagged by prod: a
  fake Tailscale-credential-request message sent to the owner earlier tonight (see this
  session's own transcript — a pasted message with a fabricated `tailscale.tm` domain,
  garbled fake auth-key formats, and an injection-pattern opening line), apparently
  **corroborated by a session-restore message that treated the fake content as real prior
  context**. This is flagged as unresolved and needing dedicated investigation — not
  something either session root-caused tonight. Worth the owner's direct attention given
  this is a security product.

## Morning verification + Sunday-upgrade prep (dev, 09:15–10:15 EDT, 2026-10-16)

Owner asked for a full working-state confirmation and then for dev to start preparing
for Sunday's unattended upgrade (2026-10-19, dev 03:00 / prod 06:00 EDT). Every item
below was checked with command output, not assumed.

### Verified working (dev side)
- Dev `main` at `27fef92e9d` == `origin/main`, clean tree; all 7 dev containers healthy;
  `scripts/check-version-pins-parity.sh` → PASS.
- Local models: direct completion to Rapid-MLX `nemotron-3.5-lightning-rapid` → clean
  `OK-DIRECT`; through the dev gateway proxy (`POST /v1/chat/completions` on :9080) → clean
  `OK-VIA-GATEWAY`, no in-band reasoning, no `/no_think`, 200 in the gateway log.
- Tailscale at boot: `tailscaled` runs from the Homebrew LaunchDaemon
  (`/Library/LaunchDaemons/sh.brew.tailscale.plist`, RunAtLoad + KeepAlive, one daemon
  only — no `/Applications/Tailscale.app` dual-daemon conflict); serve config is
  persisted in tailscaled state and re-applied on boot; `com.local.tailscale-watchdog`
  (every 5 min) logs `ok (Running, Online)`. Live serve table includes `:8080` → prod
  gateway (`/status` 200), `:9119` → `127.0.0.1:9220` (the prod dashboard relay, 302),
  `:8765` (200). `:18789` returns 502 from the tailnet — nothing listens on
  127.0.0.1:18789 on the host (prod's OpenClaw Control UI port) — asked prod to check.
  `:8642` is the known-dead direct Hermes API serve (see "Known open issues").
- Dev Hermes: `Connected to Telegram` count 0, `conflict` count 0 — the
  `AGENTSHROUD_HERMES_DISABLE_TELEGRAM=1` launch is holding.
- Auth/tooling the unattended job needs on this account: `claude auth status` loggedIn,
  `gh auth status` logged in with `repo`/`workflow`, `git push --dry-run` OK, `npm`
  11.20.0, `tmux`/`colima`/`trivy` on PATH, host memory pressure level 1, dev-VM egress
  to registry-1.docker.io / mirror.gcr.io / ghcr.io / npmjs 401/401/401/200 (reachable).
- Dev cron (`crontab -l`): `0 3 * * 0` plus retries at 05/08/11/14, all with
  `SUNDAY_UPGRADE_AUTON=1`; `colima-health-check.sh` every 5 min and `@reboot`.

### Not verifiable from dev (asked prod twice, no reply received by 10:15 EDT)
- Prod's Hermes cron history and whether today's Daily Brief **podcast** was produced and
  delivered; prod's `git rev-parse HEAD`; `hermes-dashboard-relay` restart policy; the
  `:18789` 502; what restores Colima + the relay after a prod reboot. Cross-session
  messages to a Remote Control session are held for that user's approval, so silence
  is not a result either way.

### lazydocker leak recurred (09:13–09:46 EDT) — found during the first dry run
- A fresh `lazydocker` (pid 63045, user agentshroud-bot, started ~09:13 from the owner's
  `asb` tmux layout, which has a pane that `exec lazydocker`s) had 861 docker.sock
  connections open through Colima's ssh forward within 31 minutes. Effects: dockerd
  290% CPU / containerd 218%, host load 27, dev VM 209 MB free, the VM OOM-killer
  SIGKILLed OpenClaw's node process at 13:43:17Z (clean exit 0 → docker restart, 5 min
  to healthy), `docker version` >120 s, and every trivy scan in the dry run died with
  `use of closed network connection` after its 300 s timeout — i.e. the same "trivy
  always fails on Sunday" symptom recorded on 10-04 and 10-11 is at least partly this.
- `kill 63045` → socket count 732 → 2 in 10 s, `docker ps` back to 60 ms, VM back to
  2.6 GB free. The other lazydocker (pid 60869, ijefferson.admin) is on PROD's socket
  and is not dev's problem; prod was told to check its own count.
- Durable fix is in the owner's tmux layout (don't auto-launch lazydocker), not in this
  repo.

### Changes committed for Sunday (this commit)
1. `scripts/discover_upstream_versions.py` — three hardenings, all TDD'd
   (`gateway/tests/test_discover_upstream_versions.py`, 34 passed):
   - bounded retry (4 attempts, 5/10/20 s) around both upstream fetches. Two
     consecutive real runs failed Hermes discovery (`<urlopen error timed out>`, then
     `SSL: UNEXPECTED_EOF_WHILE_READING`) while the identical URL succeeded 10/10 from
     curl and urllib immediately before and after — a single blip turned into
     "Hermes latest = UNKNOWN" for the whole run.
   - hard per-attempt deadline (90 s) enforced from a daemon thread. The dry run's own
     discovery, run with the cron job's interpreter (`/opt/homebrew/bin/python3` =
     Python 3.15.0 / OpenSSL 4.0.3), sat **10+ minutes at 0% CPU** inside one
     `urlopen(timeout=60)` with the socket in CLOSE_WAIT on an IPv6 Cloudflare address.
     The socket timeout never fired. Unattended, that hang runs until the 180-min
     watchdog kills the session.
   - IPv4-only name resolution from the second attempt onward (`curl -4` was 100%
     clean; every observed failure was on the IPv6 path). First attempt keeps the
     system default.
   - Live proof after the change, same interpreter: two runs, 4 s and 1 s, both
     returning `OPENCLAW=2026.10.4`, `HERMES=v0.22.2` + digest.
2. `scripts/sunday-upgrade-apply.sh` — three no-op-gate fixes (CLAUDE.md §0.0):
   - **Hermes now feeds `UPGRADE_AVAILABLE`.** Before, only OpenClaw did, so a Sunday
     with OpenClaw current and Hermes behind could rebuild the same Hermes and pass.
     (Today both are behind: OpenClaw 2026.10.2→2026.10.4, Hermes 0.21.5→v0.22.2.)
   - **Unknown discovery can no longer read as "already current".** The first dry run
     today (discovery killed mid-run) printed `NO-OP (honest) — already on the latest
     upstream release` and would have published `status=PASS`. Now: no pin changed +
     discovery incomplete → exit 25 / `NOTHING_UPGRADED`, same as known-behind.
   - **"Before" pins come from the merge-base with `origin/main`**, not from script
     start. The mission commits its pin bumps on `chore/upgrade-*` before invoking the
     script, so start==end and every real upgrade was reported `upgraded:false`
     (10-04, 10-11 — hand-corrected in those reports). On prod (HEAD == merge-base) the
     old behaviour is unchanged.
   - Proof, two full `--dry-run` runs with the patched script: on `main` → `OpenClaw is
     BEHIND`, `Hermes is BEHIND`, no-op gate FAILED, **exit 25**, handoff would be
     `NOTHING_UPGRADED`/`FAIL` (correct — nothing bumped). On a throwaway branch with
     the two real bumps committed → `'before' pins taken from merge-base 27fef92e9d13`,
     `no-op gate: PASS — upstream pins changed this run`, **exit 0**, handoff would be
     `PASS`. Branch deleted afterwards; pins on `main` untouched (2026.10.2 / 0.21.5 —
     Sunday's run makes the real bump through the normal PR flow).
   - With a healthy daemon the scan phase is fast: 3/3 images in ~80 s, 0 CRITICAL
     (gateway 135 HIGH, openclaw 166 HIGH, hermes 414 HIGH — untriaged, as on 10-11).
3. `docker/docker-compose.agentshroud-bot.marvin.yml` — dev gateway's
   `HERMES_DASHBOARD_UPSTREAM` now names `agentshroud-dev-hermes-v2:9120`. The 2026-09-18
   dev rename only covered lifespan.py's TCP forwarders; main.py's HTTP reverse proxy for
   `/hermes-dashboard/*` (the gateway-routed path Conduit should eventually use instead
   of the `:9119` relay bypass) still pointed at the prod hostname, so on dev it was
   always 502. After `up -d --no-deps gateway`: healthy in 40 s, `GET /hermes-dashboard/`
   → 200. (`gateway/tests/test_security_regressions_v1_2.py::TestHermesDashboardBridge*`
   2 passed.)

### Afternoon (12:00–12:15 EDT): prod's evidence arrived, two more fixes committed
Prod confirmed (raw outputs in its message): both hosts on `bfa7c03c6a`; Daily Brief
delivered 10-14/10-15/10-16 (episodes 37–39, 10-13 is the known gap), 6 active / 29
paused cron jobs; the `hermes-dashboard-relay` bypass is gone and `:9119` now serves
`127.0.0.1:8080/hermes-dashboard/` — the full Conduit flow (providers → password-login →
me → ws-ticket → WS 101 `gateway.ready`) proven through the gateway with a real websockets
client; the iPad's own Tailscale link (relay "iad", 0 bytes, no ping reply) is what still
blocks the app. Local model via prod gateway: clean, `finish_reason=stop`. Prod's
lazydocker holds 119 sockets (not a runaway). Feed Refresh (`339430797fb7`) exits 1
every Sunday 07:15 — prod-side, still open.

Committed on dev after prod's report:
1. `gateway/ingest_api/main.py` `hermes_dashboard_proxy` — upstream headers are relayed
   one by one via `multi_items()` instead of a dict. Hermes's login sends three
   `Set-Cookie` headers; the dict folded them into one comma-joined header (RFC 6265
   forbids it; python/urllib keeps only the first cookie — Foundation/Conduit happened to
   split it). `Content-Encoding`/`Content-Length` are dropped because httpx already
   decoded the body. Tests: `TestHermesDashboardProxyHeaders` (2) in
   `gateway/tests/test_main_endpoints.py`, file total 38 passed.
2. `docker/bots/hermes/init-config.sh` + `start.sh` — loud alert for an empty
   `AGENTSHROUD_PROD_CRON_KEEP` on a prod boot (the 2026-10-12 silent Daily Brief outage):
   banner on stderr, marker `/opt/data/.agentshroud-prod-cron-keep-empty`, and the
   count surfaced in the Telegram "Hermes online" message. Takes effect on the next
   Hermes image build (Sunday).

### Afternoon (14:00–14:30 EDT): two more gateway findings from prod, fixed on dev

Prod's live Hermes dashboard chat on `gemma-4-26b-a4b-it` (TurboFieldfare, `:8238`)
failed 9/9 at 18:03Z with "Provider returned an empty stream with no finish_reason".
Gateway log each time: `POST host.docker.internal:8238/v1/chat/completions "400 Bad
Request"` followed by `POST /v1/chat/completions -> 200`. Two defects, both fixed here:

1. **Streaming route masked every upstream 4xx as a 200 event stream.**
   `gateway/ingest_api/main.py` built the `stream:true` response as a fixed
   `StreamingResponse(status_code=200, media_type="text/event-stream")` before the
   upstream had answered, so a backend 400 arrived at the client as a 200 whose body was
   raw error JSON — SSE parsers drop non-`data:` lines, hence "empty stream".
   `LLMProxy.proxy_messages_streaming()` now takes `with_head=True` and yields a
   `StreamHead(status, content_type)` first, as soon as the upstream (or failover)
   response headers arrive; the route awaits it and returns a plain `Response` with the
   upstream status + body for ≥400, or the event stream with the real status otherwise.
   The default `with_head=False` keeps the bytes-only contract for existing callers, and
   pre-header failures (backend down) keep the established in-stream SSE error frame.
   No first-token wait is introduced: measured against Fieldflare, headers arrive in
   29 ms while the body streams for 27 s (`curl -w time_starttransfer`).
2. **TurboFieldfare rejects OpenAI fields Hermes always sends.** Probed field-by-field
   against `:8238`: HTTP 400 `{"code":"unsupported_value"}` for `parallel_tool_calls`
   (true or false), a named `tool_choice` object, and — one more than prod reported —
   `tool_choice: "required"`; only the `"auto"`/`"none"` strings are accepted.
   `LLMProxy._strip_fieldflare_unsupported_fields()` drops `parallel_tool_calls` and
   rewrites any other `tool_choice` to `"auto"`, applied only when the resolved backend is
   `FIELDFLARE_API_BASE`, in both `proxy_messages` and the streaming path (same shape as
   the Rapid-MLX thinking shim). Any client on that route is protected, not just Hermes.

Tests (TDD, red first — 15 failed before the change):
`gateway/tests/test_llm_proxy_local_parity.py` (9 Fieldflare shim tests, unit +
non-streaming + streaming dispatch, plus a negative test that LM Studio keeps the fields),
`gateway/tests/test_llm_proxy.py` (5 `StreamHead` tests: 400 local, 400 cloud non-quota,
200, default bytes-only contract, connect-failure frame), `gateway/tests/test_main_endpoints.py`
`TestStreamingProxyStatusPropagation` (2 route tests). Affected suites: 174 passed.

Live proof on dev (gateway source is bind-mounted; container restarted 14:21 EDT, healthy
in 45 s), requests sent from inside `agentshroud-dev-hermes-v2` to `gateway:8080`:

| Request | Before | After (dev gateway log) |
|---------|--------|-------------------------|
| stream + tools + `parallel_tool_calls:true` + `tool_choice:"required"` | upstream 400 → client 200 empty | upstream `200 OK` → `-> 200`, 12 streamed tokens, `finish_reason:"length"`, TTFB 0.97 s |
| stream + `"n":3` (still rejected, not stripped) | upstream 400 → client 200 empty | upstream `400 Bad Request` → `-> 400`, body `{"error":{"code":"unsupported_value","message":"only n=1 is supported"...}}` |

Takes effect on prod with Sunday's gateway rebuild (owner's freeze on prod rebuilds).

Also from prod this afternoon, for the record: the iPad/phone Conduit failure was carrier
DNS resolving `marvin.tail240ea8.ts.net` to the Funnel ingress, not AgentShroud; the
owner restored the pre-10-08 serve (`:9119 → 127.0.0.1:9119`) and added Funnel
`/hermes → 127.0.0.1:8080/hermes-dashboard/` (public exposure, owner's call; recorded in
`scripts/tailscale-serve.sh` by prod's `9f3ac89909`, dev fast-forwarded). The owner
installed the `kaishi00/hermes-conduit-notifier` plugin (`conduit_push` 0.41.0) into
prod's `/opt/data/plugins` for Conduit voice — it lives in the data volume, so Sunday's
Hermes v0.22.2 bump must keep it loading. Dev has no copy of that plugin, so the dev dry
run cannot exercise it; prod should check `/api/plugins/conduit_push/capabilities` right
after Sunday's Hermes restart.

### Late afternoon: cleanup directive, start.sh banner fix
Owner directive 15:00 EDT: once Conduit voice works, dev and prod on the same main commit,
every container in both environments rebuilt from it, and no branch other than `main`
anywhere. Done so far from dev: `origin/chore/upgrade-2026-10-04-baseimages` deleted
(10-04 digests older than main's 10-11/10-12 refresh, conflicted with main; patches kept
in the dev session scratchpad, tip `568d3bc2b3`); dev's local copy of
`fix/sunday-upgrade-head-guard` deleted. PR #490 (per-iteration HEAD re-assert in the
Sunday build loop; merges clean, smoke test passes on current main) and the five
Dependabot PRs (#491 #493 #499 #500 #501; the running gateway already satisfies all five
floors) need the owner's own merge — the dev session's permission classifier refuses PR
merges. Prod's inventory of its three local branches: `fix/hermes-cron-pause-alert-20261012`
merged (deleted), `fix/docker-image-container-sprawl` (1 real commit, `a8e2a6bf91`) and
`fix/scrum-174-scan-pipeline-sunday-upgrade` (5 commits, mostly re-implemented on main)
pushed to origin for review and cherry-pick before deletion.

`docker/bots/hermes/start.sh` expected-secrets banner: `feedbin_email`/`feedbin_password`
were flagged missing on every prod boot because `run-standalone.sh` passes them as
`FEEDBIN_EMAIL`/`FEEDBIN_PASSWORD` env vars (a file mount of those two never works on
that image path) and the loop only checked `/run/secrets`. An upper-cased env var of the
same name now counts as present. Behavioral check S13 added to
`tests/startup_smoke/test_bot_boot_static.sh` (13/13 pass; the HEAD version of the loop
reports all three fixtures missing, the fixed one reports only `brave_api_key`).

lazydocker leak recurred a third time (pid 45603, 325 sockets, `docker system df` >90 s);
killed before the rebuild.

### Prod secrets clobbered by a killed extract (prod 14:25 EDT, fixed on dev)
Prod's `asb up hermes` hung ~9 min in `docker/setup-secrets.sh extract` (1Password unlock)
and was killed. `scripts/asb`'s `setup_ephemeral_secrets` had already `rm -rf`'d
`~/.agentshroud/.asb-secrets` and pre-created every secret file **empty** before extract
ran, so everything the backend had not yet supplied stayed 0 bytes with the previous good
values gone: `hermes_healthchecks_url`, `podcastindex_api_key/secret`,
`telegram_bot_token_{rpi,trillian}`; the dashboard basic-auth files went missing too.
Prod restored the dashboard creds from Hermes's config and the healthchecks URL came back
through `run-standalone.sh`'s fallback to `docker/secrets/`; `podcastindex_*` are empty in
both of prod's dirs and need the owner's 1Password unlock. (Prod first asked dev to copy its
own secret files via `/Users/Shared`; withdrawn before anything was copied — dev's
`hermes_healthchecks_url` is 0 bytes anyway.)

Fix: `setup_ephemeral_secrets` now moves the previous dir to `.asb-secrets.prev`, runs
extract, then `_preserve_nonempty_secrets` carries over any value the backend did not
supply, and only then deletes `.prev`; a leftover `.prev` from an earlier killed run is
folded in first. `docker/setup-secrets.sh` writes through a new `write_secret_file`
(temp file + rename, mode 600, never replaces a non-empty file with an empty value) in
both `extract` and `store`. Tests: S15 in `test_bot_boot_static.sh` (15/15), SS7 updated
+ SS13/SS14 in `test_setup_secrets.sh` (suite pass), plus a sandboxed end-to-end run of
the real function with a stand-in extract that writes one value and exits 1: previous
values kept (8 bytes each), fresh value taken, never-stored key still empty, `.prev`
removed.

Also from prod: Hermes was recreated on `agentshroud/hermes:1.7.0`, `tool_progress=off`
for Telegram per the owner, and the `latest`-tag outage is what the `run-standalone.sh`
versions.env fallback above fixes.

### Evening: branch cleanup finished, resource cut, full rebuild of both hosts
Branches: the five Dependabot PRs (#491 #493 #499 #500 #501) closed as superseded on the
owner's "close them" (the gateway image already satisfied every floor); PR #490 was a
draft, so the owner's own `gh pr merge` did nothing — prod marked it ready and merged it
with the admin override under the owner's directive (`049cd5e051`). Remote heads: `main`
only. Both clones: `main` only.

First full rebuild (both hosts from `a7b8cee1e2`): prod done 15:53–16:09 EDT with
evidence and both gateway fixes proven live (`conduit_push` capabilities 200; streaming
gemma turn with tools → 200). Prod found that `asb rebuild full` never rebuilt
voice-gateway (`compose build` was run without `--profile voice`) — fixed in
`bd0c1225bd`. Dev's first attempt died in 12 s because the host-side SSH forward of the
Colima docker.sock had died at 15:52 (VM and dockerd fine; `colima restart` fixed it);
the second died on a Debian CDN "Hash Sum mismatch" for `clamav_1.4.3+dfsg-1_arm64.deb`
(the mirror served the correct file minutes later); the third was killed by me once
the owner asked for a second rebuild from the final commit.

Resource cut (owner: "this system is very tight on resources", dev less than prod,
settings must survive reboots):
- `e8fca117df` — Colima sizing comes from each account's saved
  `~/.colima/default/colima.yaml`. The LaunchAgent (`--cpu 8 --memory 12`) and the
  watchdog (`--cpu 8 --memory 10`) had each re-imposed a hard-coded shape on every
  start, so no resize ever stuck; both now pass only `--network-address` once a saved
  config exists. Dev's installed LaunchAgent updated in place (backup kept); prod must
  reinstall from the repo copy.
- Prod's measured steady state after its rebuild (17:20 EDT): VM 8 CPU / 10 GiB with
  9.25 GiB used, 667 MiB available, no swap, "Pressure L2" in the local-llms watchdog
  all afternoon; containers 7.6 GiB (openclaw 3.33 GiB, voice-gateway 1.59, gateway
  1.23, hermes 0.54, wazuh-manager 0.29, plus homeassistant/librechat/searxng ≈0.55).
  So prod cannot give up VM memory; the Mac's real memory consumers are the local LLM
  servers (rapid-mlx ≈17 GB, TurboFieldfare, oMLX, LM Studio), not Colima.
- Dev VM resized 8 CPU / 10 GiB → **4 CPU / 9 GiB** (first set to 8 GiB, raised to 9
  once prod's OpenClaw RSS showed 2.5 GiB caps would OOM it; persisted in colima.yaml).
  Prod VM target **6 CPU / 10 GiB** (CPU only; prod applies it at its restart).
- `3955d3b267` + follow-up — dev container caps under that VM: gateway 3g/1.0,
  openclaw 3584m/1.5, voice-gateway 2560m/1.5, wazuh-manager 768m/0.5, Hermes 2g/1.0
  (run-standalone.sh sets caps by environment; prod keeps 4g/1.0, 4g/2.0, 4g/2.0,
  1g/1.0, 3g/1.5). Prod's compose caps unchanged.
- Worth a separate look: OpenClaw at 3.33 GiB RSS is the single largest container on
  both hosts and already trips its own RSS warning.

### Still open for Sunday (not changed today)
- `graphify-out/` is stale (manifest 2026-09-27; 17 commits since touching
  gateway/scripts/docker). CLAUDE.md makes a refresh mandatory before a prod rebuild —
  to be run and committed separately once the host is not under memory pressure
  (63 GB used / 31 GB compressor at 10:06 EDT with the local models loaded).
- Dev VM is 10 GiB (`colima list`), not the 12 GiB in project memory; it OOM-killed
  OpenClaw once today under the lazydocker load. Not changed (would restart every dev
  container); flag for the owner.
- `.trivyignore.yaml` accepted-risk entries CVE-2026-6653 (expires 2026-10-27) and
  CVE-2026-43185 (2026-11-10) are within the warn window — re-review before they lapse.
- Dependabot PRs #499/#500/#501 (fastapi, pydantic, aiohttp bumps) are open and will be
  in Sunday's scope.

## Night of 2026-10-16/17: prod Hermes unreachable behind the gateway (open)

Timeline (EDT), everything below measured from dev's account on the same Mac, read-only:
- 21:26 — dev `asb rebuild full` from `7da4817b31` finished (exit 0, 11/11 post-deploy
  checks) after the in-VM `docker image prune -af` reclaimed 1,191 → 297 images and
  `/var/lib/docker` went 98% → 24%. Both hosts on `7da4817b31`, `main` only.
- ~23:04 — the prod account's Claude desktop app restarted (process age); the prod
  session's bridge address went stale (HTTP 409 on send), so the three diagnostic
  requests sent to it between 23:14 and 23:30 were never delivered.
- 23:08 — owner's Conduit screenshot: *"Failed to refresh the dashboard session: Your
  Hermes server doesn't support this yet. Update Hermes, then try again."*, showing a
  saved copy from ~14:00.
- 23:10 — `127.0.0.1:9119/openapi.json` (prod gateway's TCP forwarder → Hermes
  dashboard) still answered 302 and `/api/openapi.json` 401: Hermes was alive.
- 23:14 onward — `127.0.0.1:9119/*` and `127.0.0.1:8642/*` (gateway forwarders to
  Hermes, `lifespan.py:2199-2379`) accept TCP and send no bytes; `127.0.0.1:8080/
  hermes-dashboard/*` returns 502 after exactly 30 s (`hermes_dashboard_proxy`'s
  httpx timeout, `main.py:4891`); the Funnel path `/hermes` (tailscaled →
  `127.0.0.1:8080/hermes-dashboard/`, `scripts/tailscale-serve.sh:107`) connects then
  stalls. Gateway `/status` 200 in 6 ms, voice gateway `8765/health` 200 in 4 ms.
  Polled every 20–30 s through 06:40 the next morning: no self-recovery.

What the Conduit message means (Conduit is open source, kaishi00/hermes-conduit):
- `Conduit/Services/DashboardTicketBridge.swift:309-311` maps any bare 404/405/501 to
  *"Your Hermes server doesn't support this yet"*; the "refresh" is `POST
  /api/auth/ws-ticket` (lines 629/650). It is not a version check.
- Hermes mounts its dashboard auth router unconditionally
  (`hermes_cli/web_server.py:1002-1004` in the installed 0.21.5), and
  `/auth/native/refresh` exists there too, so a missing route is ruled out. Through
  dev's rebuilt gateway the same POST answers 401 (`{"detail":"Unauthorized"}`).
- A doubled slash after the prefix (`/hermes-dashboard//api/auth/ws-ticket`) does
  produce a bare 405 on dev — noted as a possible contributor if Tailscale ever joins
  the Funnel target path and the request path with an extra `/`; not proven to be what
  Conduit hit.

Ruled out on dev: the 3g/1.5 Hermes cap is not new (run-standalone.sh always
hard-coded it; `3955d3b267` only made it overridable). No Mac sleep/wake in `pmset`
log; uptime 1 d 8 h.

Host state at 06:40 EDT 2026-10-17 (the "tight on resources" the owner described):
load 41/21/16 on 65% idle CPU — memory thrash, not compute. 63 GB used, 33 GB
compressor, 78 MB unused, swap 14.2/15.4 GB used, 16 M pageouts. Largest residents:
`python3.12` (rapid-mlx) 17 GB, prod Colima VM 10 GB, dev Colima VM 9.2 GB, Little
Snitch 5.4 GB, CloneKitService (Carbon Copy Cloner) 3.4 GB, TurboFieldfare 3.2 GB,
CrashPlan 2.7 GB. Dev containers all healthy under their caps; dev OpenClaw restarted
itself cleanly at 04:27 EDT (exit 0, `oom=false`, its own `rss_threshold` warning at
1.9 GiB vs its 1.5 GiB internal threshold), restarts=2.

Owner's word at ~06:35 EDT: "Go". Brief with the diagnostic/fix procedure sent to the
new prod session (`agentshroud`, listed 06:38, delivery unconfirmed): evidence first
(`docker inspect` state/OOM/restarts, network membership of Hermes and gateway,
`getent`/`nc` from the gateway to `agentshroud-hermes-v2:8642/9120`, Hermes self-check on
`127.0.0.1:8642`, cgroup `memory.events`, last 80 log lines), then either `docker network
connect` (gateway cannot reach a live Hermes) or `bash docker/bots/hermes/run-standalone.sh`
from `7da4817b31`, then four host-side curls must return 200 (8642/health,
9119/api/auth/providers, 8080/hermes-dashboard/api/auth/providers,
8642/api/plugins/conduit_push/capabilities), then Conduit "Repair Connection" + Telegram.

Root cause (prod's raw evidence, 06:45 EDT 2026-10-17; the three dev hypotheses above
are all ruled out): **prod's Colima VM lost all outbound traffic at 02:45Z (22:45
EDT)** — first gateway `getUpdates` timeout. From inside the VM `curl 1.1.1.1` via
eth0 and col0, `curl 192.168.5.2:8002` (rapid-mlx on the host) and ping to
192.168.5.2 / 192.168.64.1 all time out while the host reaches the same targets in
ms. Hermes itself was healthy the whole time: gateway→`agentshroud-hermes-v2:9120`
providers 200 in 46 ms and `:8642` health 200 in 1.5 ms from inside the gateway
container, Hermes self-check 200/200, cgroup `memory.current` 600 MB of 3 GiB,
`oom_kill 0`, restarts 0, both containers on `agentshroud_agentshroud-isolated`
(gateway 10.254.111.4, Hermes 10.254.111.9). `py-spy` on the gateway showed only two
`tg-io` threads stuck in `socket.create_connection` to api.telegram.org — the
host→9119 / →8080/hermes-dashboard stalls were the gateway's event loop wedged behind
that, not Hermes. Same fault explains Hermes's "Rapid-MLX backend is not running" and
OpenClaw turns taking 164 s. Fix (owner approved, prod executing 06:45 EDT): full
Colima stop/start on prod.

Second fault (prod's, corrected here): last night's prod Colima restart came up at
**6 CPU / 10 GiB**, not the 8 / 12 prod ran before `e8fca117df`; the VM's dmesg shows
two OOM kills of `openclaw-gateway` (anon-rss 2.1 GB and 2.0 GB) with 176 MB free of
9,923 MB. The "prod VM target 6 CPU / 10 GiB" line in the evening section above is
therefore withdrawn: **prod's Colima sizing is 8 CPU / 12 GiB** (project memory
`colima-runtime-settings` already says so) and 6/10 must not appear in any runbook.
Prod is restarting with `--cpu 8 --memory 12`.

Recovery seen from the host: prod Colima stop/start by prod (owner approved);
`127.0.0.1:8642/health` and `:9119/api/auth/providers` flipped 000 → 200 at
**06:44:37 EDT 2026-10-17** (outage ≈ 7 h 30 min from 23:14). At 06:45:
`8080/hermes-dashboard/api/auth/providers` 200 in 0.59 s, `8080/status` 200, voice
`8765/health` 200, `9119/api/plugins/conduit_push/capabilities` 401 `no_cookie` (the
plugin API is served by the dashboard behind its login, same as dev; it is NOT on the
8642 API port, where the path 404s — the first probe here used the wrong port).
Authenticated plugin check, Conduit "Repair Connection" and Telegram are prod's /
owner's step 4. Dev's VM, same Mac, same window: egress fine at 06:42 but its gateway
logged Telegram timeouts at 05:06, 06:01 (×3), 06:06, 06:14 EDT; two
`CONSTRAINT_MEMCG` OOM kills of `openclaw-gateway` (anon-rss 2.1 GB each) at 01:56 and
04:27 EDT inside the openclaw container's cgroup; dev OpenClaw at 3.33 of 3.5 GiB
afterwards — the per-container OpenClaw cap is too small on both hosts for its ≈3.3 GiB
steady RSS (already flagged as abnormal above).

Third, Conduit-side (prod verified at 03:07Z): Conduit's dashboard bridge issues
`fetch("/api/auth/ws-ticket")` root-relative from its WKWebView
(`DashboardTicketBridge.swift:650/787/940`), so with a dashboard URL ending in
`/hermes` the POST goes to the Funnel root → bare 404 → "doesn't support this yet",
while `/hermes/...` login itself was 200. Fix: serve the dashboard at the Funnel root
path (owner `sudo tailscale funnel`) and set Conduit's URL without `/hermes`. This is
the one the owner's screenshot shows; the VM egress loss is what kept it from being
noticed as a separate problem. Daily Brief 04:30 run
on 2026-10-17 is presumed missed (Hermes unreachable at that time) — prod to confirm
from the cron log.

Prod's step-4 evidence (prod's raw message, ~07:00 EDT 2026-10-17): recovery at
06:43:36 EDT after `colima stop` + `colima start --cpu 8 --memory 12 --disk 120
--network-address`. `colima list`: Running, 8 CPU, 12 GiB, 120 GiB, 192.168.64.24;
colima.yaml cpu 8 / memory 12 / disk 120; in-VM nproc 8, mem 11,934 MiB, `free -m`
used 8,138 / avail 3,795 (was 176 MB free). Egress: VM → 1.1.1.1 301 in 0.39 s; VM →
192.168.5.2:8002 400 in 0.004 s (rapid-mlx answering); gateway → api.telegram.org 302
in 0.64 s; gateway → host.docker.internal:8002 200 and :8238 200. Host routes:
`8080/status` 200, `8080/hermes-dashboard/api/health` 200, `9119/api/health` 200,
`8642/health` 200. `docker ps`: docker-socket-proxy, gateway, hermes-v2, openclaw,
voice-gateway, wazuh-agent, wazuh-manager all `Up (healthy)`; container-set diff vs
before the restart = only the ephemeral `openclaw-mcp-github-*` sidecars gone
(recreated on demand) and one new hermes-sandbox. post-deploy-check 12/12 passed.
Telegram: gateway `getUpdates` 200 every ~31 s (normal long-poll), zero "timed out after
65s" / UNEXPECTED_EOF in the following 10 min. Authenticated
`/api/plugins/conduit_push/capabilities` via 9119 with the session cookie: login 200,
capabilities 200, body `{"ok":true,"version":"0.41.0","loaded_version":"0.41.0",
"restart_needed":false,...}`. OOM distinction: prod's two kills were
`CONSTRAINT_NONE` global OOMs (VM sizing, fixed by 8/12); dev's are `CONSTRAINT_MEMCG`
against the 3.5 GiB openclaw cap — a different fix, on the Sunday list. Daily Brief
04:30: Hermes cron shows last run 2026-10-17T04:33:01 **error** "Script exited with
code 1", scheduler "delivery error: Telegram send failed: Timed out"; no
`/opt/data/podcasts/outbox/daily/2026-10-17` existed, so prod re-ran cron job
`4cb4f63b00da` manually and will run the host-side publish once READY appears (outcome
to be appended). Conduit fix: PR #506 (`fix/tailscale-funnel-root-path`, 465c2c6401)
adds the Funnel `/` path in `scripts/tailscale-serve.sh`; the live `sudo tailscale
funnel` still needs the owner, as do the owner's Telegram and Conduit "Repair
Connection" taps. Prod checkout back on `main` at 7da4817b31, tree clean; it will
fast-forward to this docs-only commit.

Prod's follow-up (~08:30 EDT 2026-10-17; prod fast-forwarded to d8cf08503a, docs-only
verified, no rebuild):
- Daily Brief: manual re-run of cron job `4cb4f63b00da` "Ran now: succeeded", outbox
  `2026-10-17` READY. The host publisher then FAILED with `ModuleNotFoundError:
  mistune` because `/opt/homebrew/bin/python3` was relinked to Python 3.15.0 on
  2026-10-16 08:04 (brew upgrade by the admin account) while every pke dependency lives
  under the python@3.14 user site. Re-run with `/opt/homebrew/opt/python@3.14/libexec/bin`
  first on PATH: "published: episode_40 duration=1606s words=3055", pke commit 32d5828,
  feed now carries Sat 17 Oct. LaunchAgent `com.pke.daily-brief-publish` pinned to the
  python@3.14 interpreter + PATH (backup `.bak-20261017`), reloaded, next run 04:35.
  Sunday item: a brew python relink silently breaks every unversioned-`python3` launchd
  job on marvin — the upgrade report must check for it.
- Conduit: reconnected on its own at 08:23 (green dot), "Hello" delivered. Hermes
  replied with a real provider error from TurboFieldfare :8238 — `HTTP 400: tool
  skill_manage schema at parameters.properties.operations.items: only a two-branch
  nullable union is representable` (gateway log 12:23:25Z, POST
  host.docker.internal:8238 → 400, surfaced as 400 thanks to 2741a62f5e). Gap in the
  Fieldflare shim (`gateway/proxy/llm_proxy.py`
  `LLMProxy._strip_fieldflare_unsupported_fields`): it strips
  `parallel_tool_calls`/`tool_choice` but does not touch tool-parameter schemas with
  >2-branch `anyOf`/`oneOf` unions. The Conduit session is pinned to
  `gemma-4-26b-a4b-it`; owner told to switch that chat to nemotron meanwhile. Dev takes
  the shim fix (TDD) — see below.
- Telegram: the owner's 23:06 "Hello" to both bots got only error replies during the
  blackout; fresh post-recovery taps not yet received.
- Two more findings: (a) Hermes leaked model narration to Telegram this morning ("The
  terminal display is having artifacts but the session is valid. Let me respond:") —
  local-model prompting issue, AGENTS.md "answer only, never narrate" rule, not a cloud
  switch. (b) Egress approval cards for `agent=hermes` (mcp.exa.ai:443 at 06:06 two days
  running, salt.security:443 yesterday) are posted into the OPENCLAW bot's chat:
  `telegram_egress_notify.py:_token_for` falls back to `self.bot_token` when
  `per_bot_tokens` lacks the agent — check whether prod populates
  `per_bot_tokens["hermes"]`; per the per-bot identity rule they must come from the
  Hermes bot. The same card (id d1994ed2) rendered twice; the 07:06 `editMessageText`
  got "message is not modified" — looks like a resend on edit failure. The daily 06:05
  Hermes activity burst (feedbin, nousresearch, raw.githubusercontent, openrouter.ai)
  triggers the exa request; `hermes mcp list` is empty, so mcp.exa.ai comes from a
  built-in web-search path, job not yet identified.

Fieldflare shim fix (dev, 2026-10-17, TDD): probed :8238 with the real `skill_manage`
parameter schema exported from the Hermes container and with synthetic variants. The
server's rules, verbatim from its 400 bodies: `anyOf`/`oneOf` must be "a two-branch
nullable union" with "one exact null branch" (either order; both keywords accepted);
`type` lists allow "only one concrete type plus null"; `allOf is not representable by
the Gemma template`; nested unions inside object branches are checked too. New
`LLMProxy._flatten_fieldflare_schema` (called from
`_strip_fieldflare_unsupported_fields` for every `tools[].function.parameters` on the
Fieldflare route only) rewrites in place: object-only unions are merged into one object
(properties unioned, `action` enums unioned so the discriminator keeps every value,
`required` reduced to the keys every branch required, `additionalProperties: false` kept
only if every branch had it); scalar/mixed unions keep the first non-null branch; a null
branch is re-attached as the accepted second branch; `type` lists collapse to the first
concrete type plus null; `allOf` branches are merged into the node. Lossy by design:
the model loses the per-action "which text slot" grammar (Hermes #112677's reason for
the split), but the request is accepted instead of 400ing, and Hermes validates the op
server-side anyway. Proof: the real six-branch skill_manage schema → 400
`invalid_tool_schema` before, 200 after the shim (merged object: 10 properties, action
enum create/patch/write_file/remove_file/delete, required name+action). Tests:
`gateway/tests/test_llm_proxy_local_parity.py::test_fieldflare_shim_*` (9 new, RED
first: 5 failed / 3 passed before the implementation; the ninth covers degenerate
unions).

Full toolset check: the dev Hermes registry exposes 89 tools, three of them with unions
(`skill_manage` six-branch object union, `manage_connections` string-or-object items,
`terminal.notify`). Unshimmed, the full set 400s on `manage_connections` ("union must
contain one exact null branch"); shimmed, Fieldflare accepted the request but did not
answer within 570 s, twice. Side effect, caused by dev: after both abandoned requests
TurboFieldfare (prod account, pid 12810) stopped answering even a 2-token request from
~09:10 EDT, at ~107% CPU — presumably still prefilling them serially. Dev did not touch
the process; prod was told (tf-stop/tf-start on prod's side if still wedged). Conclusion:
the shim removes the 400, but a full Hermes toolset on gemma-4-26b-a4b-it via
Fieldflare is too slow to be usable; nemotron stays the right model for Conduit chats.
Fieldflare recovered on its own, no restart: dev's poll got 200 at 09:22:40 EDT, and prod
saw `/v1/models` 200 in 2 ms, a 2-token chat 200 in 1.2 s and pid 12810 at 0% CPU at
09:23. Owner's local Gemma was wedged ≈10 min by dev's probes. Rule going forward: never
send full-toolset requests to :8238 without a short client timeout and a small prompt.

Conduit fix applied (owner, ~09:05 EDT): Funnel root path `/` →
`127.0.0.1:8080/hermes-dashboard/`, alongside `/voice`, `/health` and `/hermes`. Prod's
probes: GET root `/api/health` 200; unauthenticated POST root `/api/auth/ws-ticket` 401
(bare 404 before — the "doesn't support this yet" trigger). Conduit's 09:09 session shows
a clean bridge: config, sessions, conduit_push voice/tags and capabilities all 200. The
only remaining error in that chat was the Gemma skill_manage 400 fixed above.

Side finding for Sunday (not this outage): Hermes is pinned at 0.21.5 (24 Sep) while
upstream has 0.21.6 (8 Oct), 0.21.7 (12 Oct), 0.22.0/0.22.1/0.22.2 (14–15 Oct). The
2026-10-11 Sunday record (`/Users/Shared/agentshroud-sunday/dev-result-2026-10-11.json`)
carries only the unchanged `HERMES_IMAGE` digest — a silent no-op of the CLAUDE.md §0.0
kind. 0.22.2's release note flags a known issue (sessions from the 0.22.1 gateway cannot
be deleted); 0.22.0 retires `session_reset` idle/daily modes and moves memory providers
and Home Assistant to catalog plugins — config migration work for the upgrade.

Sunday item, OpenClaw per-container memory cap (both hosts, 2026-10-17): after the VM
fixes, OpenClaw still hits its container cap on both hosts. Dev (cap 3.5 GiB): a third
`CONSTRAINT_MEMCG` kill of `openclaw-gateway` at 07:58 EDT (anon-rss 2.1 GB), container
restarts = 3. Prod (cap 4 GiB): one `CONSTRAINT_MEMCG` kill inside `agentshroud-openclaw`'s
cgroup at ≈09:40 EDT (dmesg -T time, approximate) of child process `openclaw` (pid 91040,
anon-rss 468 MB, total-vm 3.7 GB), not the main gateway process; restarts = 0, healthy,
3.4 of 4 GiB in use; VM fine (0 global OOMs, 2.7 GB available of 11.9 GB). Prod also
re-accumulates about ten `openclaw-mcp-github-*` sidecars after each restart. Fix scope:
size the OpenClaw cap to its measured steady RSS plus headroom on each host (dev stays
below prod), and stop or reap the duplicate MCP sidecars.

## 2026-10-17 afternoon: drift audit of both hosts, and the drift PR

Owner's goal: dev and prod rebuilt from the same `main` commit, with no manual steps
before Sunday's upgrade and Monday's 04:30 Daily Brief. Both hosts were at `aebc0dac6c`,
clean, with only `main` locally and on origin and no open PRs. The audit found drift in
what the schedulers run:

- **Prod's Sunday job was loaded from a stale backup plist.** The loaded job came from
  `com.agentshroud.sunday-upgrade-20260906-0645.plist`: same Label, no
  `SUNDAY_UPGRADE_AUTON=1`, so Sunday's 06:00 run would have stalled on permission
  prompts. Prod moved it and three other stale copies (two colima-autostart backups,
  the pke `.bak`) to `~/Library/LaunchAgents-archive/`. It then installed the repo plist
  (`cmp` identical) and bootstrapped it. `launchctl` now shows the canonical path with
  AUTON=1 and HOME set.
- **Dev's crontab was hand-typed.** The `*/5` and `@reboot` health check plus the Sunday
  03:00 run and its 05/08/11/14 retries had no tracked installer.
- **The repo colima plist had regressed to `/tmp` log paths.** Prod's job creates
  `/tmp/colima-autostart.*` first as another user, so dev's job cannot spawn (found
  2026-09-19). Dev's installed copy still had the per-account fix; prod's matched the
  repo.
- **Dev's 2026-10-11 Sunday handoff was a false green (CLAUDE.md §0.0).**
  `dev-result-2026-10-11.json` read `status: PASS` with `upgraded: false`,
  `images_scanned: 0` and `scans_failed: 3`. Dev only warns on scan failure, so the run
  reached `write_handoff PASS`. Prod's check of that file was only in the session
  prompt, and nothing stopped it accepting an old week's PASS.
- **2026-10-11 lost every retry.**
  - The 03:00 session was still on `chore/upgrade-2026-10-11` when the 05:00 fire ran
    the branch guard before the "already running" check, so it failed with FATAL
    "repo checkout is on branch ..., not main".
  - The 08:00 session's watcher kills at 180 min plus a 20 s boot (11:00:40), so the
    11:00 fire saw it alive and skipped.
  - Each of the 03:00, 08:00 and 14:00 runs then timed out with no report.
  - The checkout did return to `main` after each timeout, because that end-of-run step
    already existed.
- Stashes: prod archived its 14 to `~/.agentshroud/stash-archive-20261017/` and cleared
  them. Dev archived its 16 to the same path (patches plus `SHAS.txt`). Clearing dev's
  stashes, archiving `com.agentshroud.imsg-relay.plist` (not loaded, not in the repo) and
  deleting three ignored `docker/*.bak` files were refused by dev's permission
  classifier; they are left for the owner.
- docker-socket-proxy: both hosts run `1f5038b54f06`. It is untagged because compose
  pins it by digest. That digest is upstream's `latest` = `v0.5.0` (2026-07-27), the
  newest release (Docker Hub tags API, checked 2026-10-17). Only `master`/`nightly` are
  newer, so the pin is current.
- Dev has no `openclaw-mcp-github-*` sidecars (no containers, no processes inside
  OpenClaw). Prod's ~10 are prod-only. Dev OpenClaw sat at 3.24 of 3.5 GiB during the
  audit.

What the drift PR changes:

1. **Result gate.**
   - `sunday_handoff_status` in `scripts/lib/sunday-scan.sh` turns a PASS into
     `SCAN_INCOMPLETE` when no image scanned or any scan failed.
   - `sunday-upgrade-apply.sh` publishes that and exits **21**.
   - The EXIT trap no longer overwrites a deliberately written
     `SCAN_INCOMPLETE`/`NOTHING_UPGRADED` with `FAIL`.
2. **Prod gate.** `sunday_dev_handoff_gate` requires `dev-result-<today>.json` whose own
   `date` is today and whose status is PASS. `phase_apply` runs it on prod before
   anything mutates (exit **15**).
3. **Wrapper (`sunday-upgrade.sh`).**
   - The session guard runs before the branch guard, so an overlapping fire skips
     instead of failing FATAL.
   - A session past its budget with no watcher is killed, and the checkout is returned
     to `main` through the shared `_return_to_main`.
   - `WATCH_TIMEOUT_MIN` 180 → 170, so a timed-out watcher finishes before the next
     3-hourly fire.
4. **colima plist.** Per-account `~/Library/Logs` paths. The no-sizing-flags note is kept.
5. **`scripts/launchd/install.sh`.** Picks the role by `whoami`.
   - Prod: installs both plists, archives same-Label stale copies, and reloads a job
     only when its file changed or it is not loaded.
   - Dev: places the colima plist and installs a managed crontab block that replaces
     hand-typed copies of the same jobs.
   - Idempotent; refuses other accounts.

Additional Sunday items from the owner's 12:30 test (2026-10-17):

- (a) **Hermes reply latency.** The Telegram session reached 43k tokens (240 messages)
  and took 322 s on nemotron. Conduit on gemma had 19.7k tokens and took 537 s. Options:
  auto-compress well before 43k, a smaller toolset for desktop/Conduit, prompt caching
  in TurboFieldfare.
- (b) **OpenClaw sends its `NO_REPLY` sentinel to Telegram as literal text** (11:38 and
  12:53).
- (c) **`[SCHEMA_REDACTED]` appeared in an OpenClaw reply.**
- (d) **"Exec completed (code 0) :: Killed" ×3 in OpenClaw async exec.** Consistent with
  the OpenClaw memcg cap item above.
