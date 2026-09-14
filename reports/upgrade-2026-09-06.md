# AgentShroud Sunday Upgrade — 2026-09-06 (dev-only, read-only inventory → scoped fixes)

## Summary line

**PARTIAL (2 components BLOCKED, 1 attempted fix reverted)**

Scope actually executed (per explicit user direction this run, not the full
7-phase autonomous procedure): read-only inventory + security scan, then a
targeted "fix all flagged issues and upgrade what's safe" pass against the
**dev** stack only. Prod was never touched (this session runs on the
`agentshroud-bot` dev account, not `ijefferson.admin`/prod — see below).
No git push, no Jira ticket, no cross-account handoff file — none of those
were corroborated by anything in this repo's own docs, so none were
fabricated; see "Not done" at the bottom. One follow-up fix attempt (voice
gateway CVE remediation via a Debian base-image rebase) was tried, measured
with Trivy, found to make things worse, and reverted — see §5 item 1.

## 0. Pre-existing session context worth recording

- Before any of this work, the session flagged and got explicit user
  confirmation on: (a) this is the `agentshroud-bot` dev account on
  `marvin.local`, not the `ijefferson.admin` prod account the generic
  mission prompt assumed; (b) this is an interactive session, not a
  headless cron run; (c) none of the Jira/cross-account-handoff machinery
  described in the generic prompt is documented anywhere in this repo's
  own `CLAUDE.md`/scripts.
- `reports/upgrade-run-2026-09-06.log` (2.2MB raw ANSI terminal capture) is
  a live recording of *this* interactive session (verified: it contains
  this session's own text near-verbatim), not a separate prior automated
  run. Not touched.
- Two pre-existing untracked dirs (`docs/dev-notes/cron-backup-2026083*`)
  and one pre-existing modified file (`.claude/settings.json`) were present
  at session start, unrelated to this work, and left untouched per the
  ground rules.

## 1. Environment mapping

Dev vs. prod is keyed off `$USER` running `scripts/asb`, not a branch or
compose profile:

| | dev (`agentshroud-bot`) | prod (any other `$USER`, e.g. `ijefferson.admin`) |
|---|---|---|
| Compose project | `agentshroud-bot` | `agentshroud` |
| Compose files | `docker/docker-compose.yml` + `docker/docker-compose.agentshroud-bot.<host>.yml` | `docker/docker-compose.yml` only |
| `AGENTSHROUD_INSTANCE_LABEL` | `dev-<host>` | `prod` (default, `docker/docker-compose.yml:158,430`) |
| Ports | gateway 9080, bot 18790 | gateway 8080, bot 18789 |
| Colima VM | separate, per-account | separate, per-account |

Both accounts share the physical host (`marvin.local`) but run isolated
Colima VMs — this session structurally cannot start/stop/exec into the prod
VM, confirming the account-mismatch flag raised at the start of the session.

Root-level `docker-compose.secure.yml` ("Proxy Mode") and
`docker-compose.sidecar.yml` ("Sidecar Mode") are **not** part of the live
dev/prod stack — `scripts/asb` never references them. They're a documented,
undeployed standalone reference setup (`CLAUDE.md:333,336`,
`docs/setup/setup-guide.md`) for third parties self-hosting AgentShroud, with
no CI job (`scripts/verify-proxy.sh` isn't called from `.github/workflows/`).

## 2. Upgrade table

| Component | Env | Before | After | Status | Notes |
|---|---|---|---|---|---|
| OpenClaw (`OPENCLAW_VERSION`) | dev | 2026.7.1-2 | 2026.7.1-2 | **BLOCKED** | Candidate 2026.9.2 fails `scripts/check-vendor-compat.sh` — vendor config schema now rejects our `apply-patches.js` output (`Unrecognized key: "memorySearch"`, `"ownerDisplay"`, `"maxConcurrentRuns"`). Needs `docker/scripts/apply-patches.js` updated for the new schema before this can move — a code change, not a version bump. |
| OpenClaw base image (`node:22-bookworm-slim`) | dev | digest `6c74791e…` | digest `83f487e0…` | **UPGRADED** | OS-layer security patch only, no functional change. Rebuilt + verified (see §4). |
| Hermes (`HERMES_IMAGE`) | dev | v0.20.1 (digest `68e15ae2…`) | v0.20.1 (unchanged) | **BLOCKED** | Latest (`nousresearch/hermes-agent:latest`, digest `7ce7d2ab…`, ≈v0.21.0 "Pantheon") fails `check-vendor-compat.sh`: our `patch_telegram_send_base_url.py` can't find its anchor — upstream refactored `_send_telegram`'s signature. Separately, v0.20.6→v0.21.0 also introduce agent browser control, a `hermes peer` bot-to-bot channel, and 6 new model providers — new egress/consent surfaces that would need gateway policy review even once the patch is fixed. Per the "do not modify security policy to force an upgrade" rule, left BLOCKED either way. |
| `tecnativa/docker-socket-proxy` | dev | digest `1f5038b5…` | unchanged | ALREADY CURRENT | Pulled `:latest`, digest matches current pin exactly. |
| `wazuh/wazuh-agent` (secure/sidecar templates only) | n/a (undeployed) | `:latest` (floating) | `4.14.7` (pinned) | **UPGRADED** | Not part of live stack; fixed as a config-correctness issue, not a live rollout. |
| `openclaw:latest` (secure/sidecar templates) | n/a (undeployed) | floating | `${OPENCLAW_VERSION:-2026.7.1-2}` | **UPGRADED** | Now tracks the same pin as the live stack instead of floating. |
| browser-extension npm deps | repo-wide | no lockfile tracked | `package-lock.json` committed, 269 packages | **FIXED** | Root cause: `.gitignore` regression (see §3), not a missing lockfile per se. |
| gateway (Python) | dev | 1.6.0 | 1.6.0 | ALREADY CURRENT | This is AgentShroud's own codebase — "upgrading" it means normal development, not a vendor pin bump. Not in scope for this pass. |
| Submodule `lvgl_kawaii_face` | dev | `ef9b47c6` (v1.0.0-4-g…) | unchanged | ALREADY CURRENT | Not checked against upstream this pass (out of scope — firmware, not part of dev/prod stack). |
| Colima / Docker CLI / Compose plugin | host | 0.10.3 / 29.8.0 / v5.5.1 | unchanged | SKIPPED | Host tooling ownership isn't documented as this job's responsibility anywhere in the repo. |
| voice_gateway base image (`python:3.12-slim`, trixie) | dev | digest `c3d81d25…` | digest `c3d81d25…` (unchanged) | **ATTEMPTED, REVERTED** | Tried `python:3.12-slim-bookworm@sha256:782412e8…` to reduce the 235 unfixed HIGH/CRITICAL findings below. Measured with Trivy: bookworm scored *worse* (262 HIGH/CRITICAL, 11 CRITICAL, 3 `end_of_life`). Reverted to trixie; rebuilt, restarted, verified healthy (0 restarts, clean logs, `/health` OK). Net change: none to the pin, comment-only explaining why not to retry blind. See §5 item 1. |

## 3. Security findings

| ID / area | Severity | Component | Before | After | Status |
|---|---|---|---|---|---|
| `.gitignore` lockfile regression | — | repo-wide (npm audit coverage) | `package-lock.json`/`yarn.lock` silently re-ignored since commit `ac7acc6081` (2026-03-22), undoing the deliberate `!package-lock.json` carve-out from `ae25622630` (2026-03-07) | Regression reverted; `browser-extension/package-lock.json` now committed | **FIXED** |
| `npm audit` (browser-extension) | — | browser-extension | blocked (`ENOLOCK`) | 0 vulnerabilities (269 packages audited) | **FIXED** |
| Floating `:latest` tags | — | `docker-compose.secure.yml`/`sidecar.yml` (openclaw, wazuh-agent) | 2 floating tags | 0 — both pinned | **FIXED** |
| `pip-audit` (gateway, chatbot) | — | gateway, chatbot | — | 0 vulns (unchanged from recon pass) | ACCEPTED — clean |
| `pip-audit` (voice_gateway) | — | voice_gateway | tool-error (Python 3.14 resolver can't solve `kokoro>=0.9.2`) | — | **ACCEPTED-with-reason**: pip-audit isn't this repo's canonical Python vuln-scan tool (`scripts/security-scan.sh` documents Trivy + Semgrep, not pip-audit); ran the canonical Trivy image scan instead (next row) rather than fix an ad-hoc tool invocation outside the sanctioned toolchain. |
| Trivy image scan — `agentshroud-bot-voice-gateway:latest` (trixie, current) | 7 CRITICAL, 228 HIGH | voice_gateway (Debian 13/trixie base) | 235 findings, **0 with a FixedVersion available** | unchanged (bookworm rebase attempted, measured worse, reverted — see below) | **OPEN, ACCEPTED-with-reason: no fix released yet.** Debian trixie's security team has not backported patches for the affected packages (status breakdown: 156 `fix_deferred`, 78 `affected`, 1 `will_not_fix`). Bulk of volume is `ffmpeg`/`libav*` (17 CVEs × 9 packages ≈ 153) pulled in by `faster-whisper` for ASR — **this is genuinely reachable**, not a false positive: `faster-whisper` feeds ffmpeg/libav on audio input, so a crafted audio file is a plausible attack surface, not just theoretical. CRITICAL list: `CVE-2026-58016` (glib), `CVE-2026-34873`/`CVE-2026-34875` (mbedtls — client impersonation / RCE), `CVE-2026-6653` (libxml2 DoS), `CVE-2026-13221`/`CVE-2026-42496`/`CVE-2026-8376` (perl-base). One `will_not_fix`: `CVE-2026-36849` (libtiff6 DoS). **See manual follow-up below — this needs a real decision, not a rubber stamp.** |
| Trivy image scan — `agentshroud-bot-voice-gateway:latest` (bookworm, attempted) | 11 CRITICAL, 251 HIGH | voice_gateway (Debian 12/bookworm base) | 262 findings, **worse than trixie** | reverted, not deployed | Attempted fix for the row above; made it worse (262 vs 235, 11 vs 7 CRITICAL) and introduced 3 `end_of_life` `libmbedcrypto7` CVEs (`CVE-2025-47917`, `CVE-2025-48965`, `CVE-2025-52496` — bookworm's mbedtls is past upstream support, unfixable on this Debian release ever). Reverted same session; not running anywhere. |
| Trivy image scan — gateway | 0 HIGH/CRITICAL | gateway | clean (recon pass) | unchanged | ACCEPTED — clean |
| `gh` Dependabot alerts | — | idallasjlabs/agentshroud | 0 open (recon pass) | not re-checked this pass (no code dependency changes made to gateway) | ACCEPTED — clean as of recon |
| OpenClaw compat gate | — | openclaw | — | FAIL (schema drift) | See upgrade table — BLOCKED, not a vulnerability finding but a real gate failure |
| Hermes compat gate | — | hermes | — | FAIL (patch anchor drift) | See upgrade table — BLOCKED |

## 4. Verification evidence

**Build (openclaw, new base digest only):**
```
Successfully built cecdda9d303a
Successfully tagged agentshroud-openclaw:1.6.0
```

**Live stack after rebuild+restart** (`docker-compose ... ps`):
```
agentshroud-docker-socket-proxy   Up 11 hours
agentshroud-marvin-gateway        agentshroud-gateway:1.6.0    Up (healthy)
agentshroud-marvin-openclaw       agentshroud-openclaw:1.6.0   Up (healthy)
agentshroud-voice-gateway         agentshroud-bot-voice-gateway Up 11h (healthy)
```
Restart counts: `agentshroud-marvin-openclaw`=0, `agentshroud-marvin-gateway`=0
(no restart loop). `docker logs --since 5m` for openclaw: no `error|panic|fatal|traceback`.

**`scripts/post-deploy-check.sh`** (project's own live gate):
```
PASS: Gateway /status 200 within 60s
PASS: Bot container started successfully within 300s
PASS: Bot logs: no RangeError (V8 stack overflow)
PASS: Bot logs: no 'invalid_auth' (Slack token guard working)
PASS: Bot logs: no 'Failed to start CLI'
PASS: Hermes dashboard :9119 returns 200 within 60s
PASS: Hermes API :8642 reachable
PASS: Hermes logs: no crash on startup
PASS: No 'Pool overlaps' error in Docker network state
Results: 9 checks, 9 passed, 0 failed
```

**`scripts/smoke.sh`** (static suite): `Suites: 10  Passed: 10  Failed: 0`
(live boot suite `test_bot_boot_live.sh` skipped — requires `SMOKE_LIVE=1`,
not exercised since the rest already validated the live stack directly).

**`npm audit` (browser-extension):** `found 0 vulnerabilities`

**Not run this pass:** `pytest gateway/tests/` (`make test`) — attempted, but
`.venv` (repo-committed, Python 3.9.6) can't even collect the test suite:
`gateway/pyproject.toml` requires `>=3.10`, and `gateway/ingest_api/routes/
approval.py` uses `str | None` union syntax that fails to parse on 3.9. This
is a **pre-existing environment defect, unrelated to anything changed in
this run** (no gateway Python files were touched) — `.venv` itself is stale/
wrong for this host. Flagged as a manual follow-up below rather than
"fixed" by provisioning a new venv, which would be scope creep beyond the
fixes requested.

**Not run this pass:** live hermes-sandbox-through-docker-socket-proxy spawn
test — no such test script exists in the repo (`scripts/smoke.sh` and
`post-deploy-check.sh` are the only existing live gates, and both already
confirm Hermes API/dashboard reachability + no crash). Per the "use existing
scripts, don't invent new attack traffic/tests" ground rule, didn't
improvise one.

**Not run this pass:** an explicit "policy still blocks a disallowed
request" e2e probe — no existing script in this repo performs that check
against the live gateway; `post-deploy-check.sh`'s `/status` check is the
only live-gateway assertion that exists. Flagged rather than improvised.

## 5. Breaking changes / manual follow-ups (human review needed)

1. **HIGH PRIORITY — voice_gateway CVE exposure is real, not theoretical,
   and the obvious fix doesn't work. Tried and reverted this run.**
   `faster-whisper` (ASR) feeds attacker-influenceable audio into
   `ffmpeg`/`libav*`, which carry unfixed HIGH/CRITICAL CVEs on Debian
   trixie. The initially-proposed fix — rebase
   `voice_gateway/Dockerfile` from `python:3.12-slim` (trixie) to
   `python:3.12-slim-bookworm`, on the assumption that bookworm's active
   security-backport track record would help — was **attempted and made
   things worse**: rebuilt, re-scanned with Trivy, and got 262 HIGH/CRITICAL
   (11 CRITICAL) vs. trixie's 235 (7 CRITICAL), including 3
   `libmbedcrypto7` CVEs marked `end_of_life` — bookworm's bundled mbedtls
   version is past upstream support entirely, so those specific CVEs will
   *never* be fixed on this Debian release, whereas trixie's equivalent
   findings are `affected`/`fix_deferred` (still eligible for a future
   patch). **Reverted** to the original trixie digest; rebuilt, restarted,
   and verified dev voice-gateway is healthy again (0 restarts, clean logs,
   `/health` returns `{"status":"ok"}`). The Dockerfile now carries a
   comment recording this so it isn't retried blind.
   **Still open — needs a different approach**, e.g.: a static/portable
   ffmpeg build from a trusted upstream (BtbN builds, or building from
   source with the patches Debian is deferring), Debian `testing`/`sid`
   (newer ffmpeg major, different risk profile, needs its own CVE check),
   or reassessing whether `faster-whisper`'s ffmpeg dependency can be
   narrowed/sandboxed further so the unpatched CVEs matter less even
   without a fix. None of these attempted this run — each needs its own
   research and test pass, not a second blind guess.
2. **OpenClaw `apply-patches.js` needs a schema update** before 2026.9.2 (or
   any version introducing the `memorySearch`/`ownerDisplay`/
   `maxConcurrentRuns` keys) can be adopted. Candidate versions between
   2026.7.1-2 and 2026.9.2 were not individually bisected — worth checking
   whether an intermediate version passes compat before assuming *all* of
   them fail.
3. **Hermes `patch_telegram_send_base_url.py` needs its anchor updated**
   for upstream's refactored `_send_telegram`. Separately, v0.20.6+ adds
   browser control + a bot-to-bot `hermes peer` channel + 6 new model
   providers — **before re-attempting this upgrade, the gateway's egress/
   consent policy needs explicit review for those new surfaces**; don't
   just fix the patch script and re-run `--hermes-latest` without that
   review.
4. **`.venv` is stale** (Python 3.9.6, repo requires ≥3.10) and cannot
   collect `gateway/tests/`. `pytest`/coverage gates could not be validated
   this pass as a result. This blocks CI-equivalent local verification
   entirely, independent of any upgrade — worth fixing on its own.
5. A `docker-compose up -d openclaw` warning surfaced: volume
   `openclaw-runtime` was created under compose project `agentshroud-dev`,
   not `agentshroud-bot` (the name `scripts/asb` actually uses per
   `SCRUM-92`). Compose tolerated the mismatch and proceeded, but this
   suggests a stale/renamed project convention somewhere in this volume's
   history — worth a quick audit, not urgent.
6. Cross-account Jira tracking, the `dev-result-*.json` handoff file, and
   git push/PR were all part of the *generic* mission template pasted at
   the start of this session but are **not corroborated anywhere in this
   repo's `CLAUDE.md` or scripts** — none were fabricated or attempted.
   If a real recurring Sunday job is wanted, that machinery needs to be
   actually built (or pointed at what already exists) before a future run
   assumes it's live.
7. The generic mission template also assumed LibreChat/MongoDB/Meilisearch/
   searxng — none of that exists in this repo. Worth correcting the
   template itself so a future automated run doesn't waste time hunting for
   services that were never here.

## 6. Rollback instructions

**voice_gateway (already rolled back this session, no action needed):** the
bookworm rebase was reverted and dev is already back on the original trixie
digest, rebuilt, restarted, and verified healthy. Nothing further to do here.
For reference, the fast-path used: `docker tag 3249347810a0
agentshroud-bot-voice-gateway:latest` (original pre-experiment image, kept
around as a dangling image) followed by `docker-compose ... up -d --no-build
voice-gateway` — faster than a full rebuild since the Dockerfile now matches
the original bit-for-bit apart from the explanatory comment.

**OpenClaw base-image bump (the only live-stack change still in effect):**
```bash
cd ~/Development/agentshroud
git revert 5a228f978   # or: git checkout 154262fc6 -- docker/bots/openclaw/Dockerfile
export USER=agentshroud-bot
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.agentshroud-bot.marvin.yml -p agentshroud-bot build openclaw
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.agentshroud-bot.marvin.yml -p agentshroud-bot up -d openclaw
bash scripts/post-deploy-check.sh
```
Pre-change image is preserved (dangling, not pruned): `docker tag
8883f43636c5 agentshroud-openclaw:1.6.0` restores it directly without a
rebuild if needed. **Do not run `docker image prune` before this window
closes** — the dangling pre-change image is the fast-path rollback.

**Config-only fixes** (`.gitignore`, secure/sidecar compose pins,
`browser-extension/package-lock.json`): no live service depends on these;
`git revert <commit>` on the branch is sufficient, no rebuild needed.

**Nothing was applied to prod** — no prod rollback is needed.

## 7. Time spent

Approximately 100 minutes of active work total (recon fork + initial fix
pass + the voice_gateway CVE remediation attempt/revert), across two user
turns. The original 90-minute budget referenced by the generic mission
template isn't strictly binding here since this was a user-directed scoped
task, not the full autonomous procedure, but is noted as exceeded for
honesty.

## 8. Branch / commits

Branch: `chore/upgrade-2026-09-06` (not pushed, not merged, per ground
rules — no instruction in this repo says the Sunday job should push).

```
2945aabf7 docs(voice-gateway): record failed bookworm rebase attempt, keep trixie base
f96783c3b docs(reports): Sunday upgrade report 2026-09-06 (dev-only scoped run)
5a228f978 fix(openclaw): refresh node:22-bookworm-slim base image digest
053a09243 fix(docker): pin floating :latest tags in secure/sidecar compose templates
5f3a39086 fix(deps): restore lockfile tracking, commit browser-extension lockfile
```
