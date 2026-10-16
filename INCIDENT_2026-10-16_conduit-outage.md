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
- Dev VM resized 8 CPU / 10 GiB → **4 CPU / 8 GiB** (persisted; verified `nproc`=4,
  `free`=7.9 GiB). Prod VM target **6 CPU / 10 GiB** (prod applies it at its restart).
- `3955d3b267` — dev container caps under that VM: gateway 3g/1.0, openclaw 2560m/1.5,
  voice-gateway 2560m/1.5, wazuh-manager 768m/0.5, Hermes 2g/1.0 (run-standalone.sh now
  sets caps by environment; prod keeps 4g/1.0, 4g/2.0, 4g/2.0, 1g/1.0, 3g/1.5). Prod's
  compose caps left unchanged pending `docker stats` at steady state.

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
