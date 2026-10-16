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
