#!/usr/bin/env bash
# tests/startup_smoke/test_bot_boot_static.sh
#
# Static (no Docker required) assertions on the key assembly files.
# Each assertion catches a specific bug from the 2026-04-10 session.
# Runs in seconds; safe for all CI runners.
#
# Assertions:
#   S1. start-agentshroud.sh uses --stack-size=65536 (ARM64 V8 stack fix)
#   S2. apply-patches.js sets channels.telegram.apiRoot (photo download fix)
#   S3. apply-patches.js validates xoxb-/xapp- prefixes (Slack crash-loop fix)
#   S4. apply-patches.js primary file is the one COPY'd by Dockerfile
#   S5. docker-compose.yml does NOT bind to 0.0.0.0 on sensitive ports
#   S6. setup-secrets.sh routes display output to /dev/tty (garbled secret fix)
#   S8. no raw ssh/ping/*.ts.net/agentshroud-bot@ in baked bot config (2026-07-17 fix)
#   S9. init-openclaw-config.sh seeds ssh-exec rules into the live AGENTS.md (2026-07-29 fix)
#   S10. start-agentshroud.sh force-reconciles security-critical LIVE cron jobs
#        against known-dangerous patterns, independent of the file-level reseed
#        (2026-08-03 fix — file-level fixes never reached OpenClaw's already-
#        existing sqlite-backed live job)
#   S11. init-openclaw-config.sh seeds jira_dev_ticket.py into the live
#        workspace (2026-08-05 — Jira-ticket-per-dev-batch capability parity)
#   S12. init-config.sh (Hermes) seeds jira_dev_ticket.py into the live
#        workspace (2026-08-05 — same capability, Hermes side)
#
# Run: bash tests/startup_smoke/test_bot_boot_static.sh
# Exit 0 = pass. Exit 1 = fail.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"

pass=0
fail=0

check() {
    local name="$1" condition="$2" detail="${3:-}"
    if [[ "$condition" == "true" ]]; then
        echo "  PASS: $name"
        (( pass++ )) || true
    else
        echo "  FAIL: $name${detail:+ ($detail)}"
        (( fail++ )) || true
    fi
}

echo ""
echo "=== test_bot_boot_static.sh ==="
echo ""

# S1: --stack-size=65536 is in the openclaw launch command
start_sh="$REPO/docker/scripts/start-agentshroud.sh"
check "S1: start-agentshroud.sh: --stack-size=65536 present" \
    "$(grep -q -- '--stack-size=65536' "$start_sh" && echo true || echo false)" \
    "ARM64 V8 stack overflow fix missing"

# S2: apply-patches.js sets channels.telegram.apiRoot
apply_js="$REPO/docker/config/openclaw/apply-patches.js"
check "S2: apply-patches.js: channels.telegram.apiRoot assignment present" \
    "$(grep -q 'channels\.telegram\.apiRoot' "$apply_js" && echo true || echo false)" \
    "Telegram photo download via proxy requires apiRoot to be set"

# S3: apply-patches.js validates xoxb-/xapp- prefix before activating Slack
check "S3: apply-patches.js: Slack token format validation (startsWith) present" \
    "$(grep -q "startsWith('xoxb-')" "$apply_js" && grep -q "startsWith('xapp-')" "$apply_js" && echo true || echo false)" \
    "Missing token format guard — empty/invalid tokens cause invalid_auth crash loop"

# S4: The Dockerfile COPYs from docker/config/openclaw/, not docker/bots/openclaw/config/
dockerfile="$REPO/docker/bots/openclaw/Dockerfile"
if [[ ! -f "$dockerfile" ]]; then
    dockerfile="$REPO/docker/Dockerfile.openclaw"
fi
if [[ -f "$dockerfile" ]]; then
    # Should COPY from docker/config/openclaw/ (the primary file)
    check "S4: Dockerfile does not COPY from stale docker/bots/openclaw/config/ path" \
        "$(grep -v '^#' "$dockerfile" | grep -q 'COPY.*docker/config/openclaw' && echo true || echo false)" \
        "Dockerfile should COPY from docker/config/openclaw/"
else
    echo "  SKIP: S4 — Dockerfile not found at expected paths"
fi

# S5: docker-compose.yml does not expose gateway on 0.0.0.0
compose="$REPO/docker/docker-compose.yml"
check "S5: docker-compose.yml: no 0.0.0.0 binding on port 8080" \
    "$(! grep -qE '"0\.0\.0\.0:8080|^[[:space:]]*- 0\.0\.0\.0:8080' "$compose" && echo true || echo false)" \
    "Gateway must only bind to 127.0.0.1:8080, not 0.0.0.0"

# S6: setup-secrets.sh routes display output to /dev/tty in read_secret_masked
secrets_sh="$REPO/docker/setup-secrets.sh"
check "S6: setup-secrets.sh: read_secret_masked routes display to /dev/tty" \
    "$(grep -q '> /dev/tty' "$secrets_sh" && echo true || echo false)" \
    "Display output on stdout corrupts captured secret value (garbled token bug)"

# S7: apply-patches.js removes stale channels.slack block when tokens are absent
# Prevents invalid_auth crash loop when config volume has Slack block from a previous run.
check "S7: apply-patches.js: stale channels.slack block removed when no tokens" \
    "$(grep -q 'delete config.channels.slack' "$apply_js" && echo true || echo false)" \
    "Stale Slack block not removed — causes invalid_auth crash loop on restart"

# S8: no baked bot config (cron prompts, workspace docs) tells the model to use
# raw ssh/ping/Tailscale hostnames to reach lab hosts. Bots run in a sandboxed
# container with NO LAN route and NO Tailscale daemon — the ONLY way to reach a
# lab host is docker/scripts/agentshroud-ssh-exec.sh -> gateway /ssh/exec. Each
# prior fix (PRs #313/#314/#315) patched only the specific file it touched and
# left sibling copies (docker/bots/openclaw/config/cron/jobs.json) or untouched
# docs (workspace/SOUL.md) still instructing raw ssh — this is the repo-wide
# guard so that class of regression can't recur silently again.
# Three precise, non-overlapping signals (no exclusion filter — a prior version
# tried excluding by surrounding phrase and accidentally whitelisted the actual
# bug text, which happened to share innocuous wording with the fix's warning
# copy). Each signal below has no legitimate occurrence in bot-facing content:
#   (a) `ssh <host>` as a command (ssh immediately followed by the hostname —
#       matches command-style instructions like `ssh marvin asb build`, but not
#       prose like "SSH to marvin" or "SSH access to lab hosts")
#   (b) `agentshroud-bot@` — a raw ssh user@host construction; the wrapper never
#       needs to spell out the user, so this never appears legitimately
#   (c) a REAL Tailscale FQDN (`tail<hex>.ts.net`) — distinct from the generic
#       `*.ts.net` wildcard used in warning text ("NEVER use ... *.ts.net")
#
# One precise, literal exception (added 2026-08-05, NOT a surrounding-phrase
# filter like the one that caused the original regression): the i-sec-defense
# and i-sec-offense skills document `agentshroud-bot <agentshroud-bot@agentshroud.ai>`
# as the git commit-author identity to use — a fixed literal string, not a raw
# ssh user@host construction, and not derived from any surrounding wording that
# could coincidentally match real dangerous text.
s8_hit=""
for dir in "$REPO/docker/config/openclaw" "$REPO/docker/bots/openclaw/config" "$REPO/docker/config/hermes" "$REPO/docker/bots/hermes/config" "$REPO/docker/bots/openclaw/workspace/collaborator-workspace"; do
    [[ -d "$dir" ]] || continue
    match="$(grep -rnE '\bssh (marvin|raspberrypi|trillian|pi)\b|agentshroud-bot@|\btail[0-9a-f]+\.ts\.net\b' "$dir" 2>/dev/null | grep -v 'agentshroud-bot@agentshroud\.ai' || true)"
    if [[ -n "$match" ]]; then
        s8_hit="${s8_hit}${match}"$'\n'
    fi
done
check "S8: no raw ssh/ping/Tailscale-hostname instructions in baked bot config" \
    "$([[ -z "$s8_hit" ]] && echo true || echo false)" \
    "Found: ${s8_hit}"

# S9: init-openclaw-config.sh seeds explicit ssh-exec-only rules into the LIVE
# workspace AGENTS.md (vendor-scaffolded, distinct from docker/config/openclaw/AGENTS.md).
# AGENTS.md is the one file the project has confirmed local models (Qwen3, qwen2.5-coder,
# deepseek-r1) reliably obey for tool-use rules — workspace/SOUL.md's own "SSH Access"
# section is not reliably read once OpenClaw fails over to a local model, which let a
# freshly-scaffolded (or pre-2026-07-29) AGENTS.md try raw ssh/ping against lab hosts
# with zero guidance, even though S8 above was clean (the raw-ssh text was never baked
# in — the SSH-exec instruction was just entirely absent). This is a positive-presence
# check (S8 is negative-only) so a future edit that quietly drops the injection passes
# S8 but fails here.
init_sh="$REPO/docker/scripts/init-openclaw-config.sh"
check "S9: init-openclaw-config.sh: seeds agentshroud-ssh-exec.sh rules into live AGENTS.md" \
    "$(grep -q 'AGENTS_FILE' "$init_sh" && grep -q 'agentshroud-ssh-exec.sh' "$init_sh" && echo true || echo false)" \
    "Live workspace AGENTS.md never gets SSH-exec-only rules injected — local-model failover can silently regress raw-ssh lab-host access"

# S10: start-agentshroud.sh force-reconciles security-critical LIVE cron jobs.
# init-openclaw-config.sh's cron reseed (S8's subject) is a whole-file checksum
# gate against docker/config/openclaw/cron/jobs.json — it only ever touches the
# file on disk. OpenClaw's actual live cron store is sqlite-backed and, once a
# job with a given ID exists, is deliberately left alone by that reseed logic
# (to preserve real `openclaw cron edit` customizations). Confirmed 2026-08-03:
# this let the "AgentShroud Daily Check-in" job's LIVE payload keep raw
# `ssh ... host.docker.internal` / `raspberrypi.tail240ea8.ts.net` content for
# months, invisible to every prior file-level fix (S8 was clean the whole
# time — the bug was never in the file). This is a positive-presence check
# (S8 is negative-only over the seed file) so a future edit that removes the
# live-job reconciliation call passes S8 but fails here.
start_sh="$REPO/docker/scripts/start-agentshroud.sh"
check "S10: start-agentshroud.sh: force-reconciles security-critical live cron jobs from seed" \
    "$(grep -q '_reconcile_security_critical_cron' "$start_sh" \
        && grep -q '_SECURITY_CRITICAL_CRON_JOB_IDS' "$start_sh" \
        && grep -q 'openclaw cron edit' "$start_sh" \
        && echo true || echo false)" \
    "Live cron jobs are never force-corrected against known-dangerous raw-ssh/Tailscale-hostname patterns — a file-level fix can leave an already-existing live job broken indefinitely"

# S11: init-openclaw-config.sh seeds jira_dev_ticket.py (generalized Jira
# create/comment/transition helper) into the live workspace so the i-odev
# orchestration skill can create/update a real SCRUM ticket per dev batch.
# Positive-presence check — a future edit that drops the seed passes S8-style
# negative checks but would silently leave OpenClaw without the file at all.
check "S11: init-openclaw-config.sh: seeds jira_dev_ticket.py into live workspace" \
    "$(grep -q 'jira_dev_ticket.py' "$init_sh" && echo true || echo false)" \
    "Live workspace never gets jira_dev_ticket.py seeded — i-odev cannot create/update SCRUM tickets"

# S12: init-config.sh (Hermes) seeds jira_dev_ticket.py into the live
# workspace — same capability, Hermes side, so the two bots never drift.
hermes_init_sh="$REPO/docker/bots/hermes/init-config.sh"
check "S12: init-config.sh (Hermes): seeds jira_dev_ticket.py into live workspace" \
    "$(grep -q 'jira_dev_ticket.py' "$hermes_init_sh" && echo true || echo false)" \
    "Live workspace never gets jira_dev_ticket.py seeded — i-hdev cannot create/update SCRUM tickets"

# S13: start.sh (Hermes) expected-secrets banner accepts an env var in place
# of a mounted file. run-standalone.sh passes feedbin_email/feedbin_password
# as FEEDBIN_EMAIL/FEEDBIN_PASSWORD (its _feedbin_env_args), so before
# 2026-10-16 every prod boot flagged both as "missing" forever. Behavioral:
# extract the real loop from start.sh and run it with no /run/secrets files,
# the two feedbin env vars set, and nothing else — feedbin_* must NOT be
# reported missing, and a genuinely absent key still must be.
hermes_start_sh="$REPO/docker/bots/hermes/start.sh"
_s13_start="$(grep -n '^_hermes_missing_secrets=""$' "$hermes_start_sh" | head -1 | cut -d: -f1)"
_s13_end="$(tail -n "+${_s13_start:-1}" "$hermes_start_sh" | grep -n '^done$' | head -1 | cut -d: -f1)"
_s13_loop="$(sed -n "${_s13_start},$(( _s13_start + _s13_end - 1 ))p" "$hermes_start_sh")"
_s13_missing="$(
    _HERMES_EXPECTED_SECRETS="brave_api_key feedbin_email feedbin_password"  # pragma: allowlist secret -- names, not values
    FEEDBIN_EMAIL="user@example.invalid" FEEDBIN_PASSWORD="x"  # pragma: allowlist secret -- test fixture
    export FEEDBIN_EMAIL FEEDBIN_PASSWORD
    eval "$_s13_loop" 2>/dev/null
    printf '%s' "$_hermes_missing_secrets"
)"
check "S13: start.sh (Hermes): env-provided feedbin secrets are not reported missing" \
    "$([[ -n "$_s13_loop" && "$_s13_missing" == "brave_api_key" ]] && echo true || echo false)" \
    "expected missing list 'brave_api_key', got '${_s13_missing}'"

# S14: run-standalone.sh (Hermes) resolves the image tag from
# docker/versions.env when AGENTSHROUD_VERSION is unset, instead of "latest"
# (no such image exists; 2026-10-16 prod: container removed, replacement
# failed to start, ~5 min outage). Behavioral: run the real fallback block
# extracted from the script with the variable unset.
hermes_run_sh="$REPO/docker/bots/hermes/run-standalone.sh"
_s14_block="$(sed -n '/^# BEGIN version fallback$/,/^# END version fallback$/p' "$hermes_run_sh")"
_s14_expected="$(sed -n 's/^AGENTSHROUD_VERSION=//p' "$REPO/docker/versions.env" | head -1)"
_s14_got="$(
    unset AGENTSHROUD_VERSION
    REPO_DIR="$REPO"
    eval "$_s14_block"
    printf '%s' "$VERSION"
)"
check "S14: run-standalone.sh (Hermes): image tag falls back to docker/versions.env, not 'latest'" \
    "$([[ -n "$_s14_block" && -n "$_s14_expected" && "$_s14_got" == "$_s14_expected" ]] && echo true || echo false)" \
    "expected '${_s14_expected}', got '${_s14_got}'"

# S15: asb's _preserve_nonempty_secrets carries non-empty values from the
# previous ephemeral secrets dir into the new one wherever the new copy is
# missing or empty, and never overwrites a non-empty new value. Behavioral:
# run the real function extracted from scripts/asb against two temp dirs.
asb_sh="$REPO/scripts/asb"
_s15_block="$(sed -n '/^# BEGIN preserve-nonempty-secrets$/,/^# END preserve-nonempty-secrets$/p' "$asb_sh")"
_s15_prev="$(mktemp -d)"; _s15_new="$(mktemp -d)"
printf 'old-url' > "$_s15_prev/hermes_healthchecks_url.txt"   # new copy is 0 bytes -> must be restored
printf 'old-key' > "$_s15_prev/podcastindex_api_key.txt"      # new copy is missing  -> must be restored
printf 'old-pat' > "$_s15_prev/github_pat.txt"                # new copy non-empty   -> must be kept
: > "$_s15_new/hermes_healthchecks_url.txt"
printf 'new-pat' > "$_s15_new/github_pat.txt"
_s15_got="$(
    eval "$_s15_block"
    _preserve_nonempty_secrets "$_s15_prev" "$_s15_new" >/dev/null
    printf '%s|%s|%s' "$(cat "$_s15_new/hermes_healthchecks_url.txt")" \
        "$(cat "$_s15_new/podcastindex_api_key.txt" 2>/dev/null)" "$(cat "$_s15_new/github_pat.txt")"
)"
check "S15: asb _preserve_nonempty_secrets restores empty/missing values, keeps new non-empty ones" \
    "$([[ -n "$_s15_block" && "$_s15_got" == "old-url|old-key|new-pat" ]] && echo true || echo false)" \
    "expected 'old-url|old-key|new-pat', got '${_s15_got}'"
rm -rf "$_s15_prev" "$_s15_new"

# S16: asb rebuild / clean-rebuild pass the profile flag to `compose build`.
# Without `--profile voice`, compose builds only un-profiled services, so
# `asb rebuild full` left voice-gateway on its old image (prod, 2026-10-16).
_s16_count="$(grep -c '^\s*\$COMPOSE \$_PROFILE_FLAG build --no-cache$' "$asb_sh" || true)"
_s16_bare="$(grep -c '^\s*\$COMPOSE build --no-cache$' "$asb_sh" || true)"
check "S16: asb rebuild/clean-rebuild build with \$_PROFILE_FLAG (voice-gateway included)" \
    "$([[ "$_s16_count" -ge 2 && "$_s16_bare" -le 1 ]] && echo true || echo false)" \
    "profiled build calls=${_s16_count} (need >=2), bare build calls=${_s16_bare} (only the plain 'build' command may be bare)"

# S17: run-standalone.sh (Hermes) resource caps: prod keeps 3g/1.5, dev gets
# 2g/1.0, explicit AGENTSHROUD_HERMES_MEMORY/CPUS override both. Behavioral:
# run the real block extracted from the script. Also confirms `docker run`
# consumes the variables rather than literals.
_s17_block="$(sed -n '/^# BEGIN hermes resource caps$/,/^# END hermes resource caps$/p' "$hermes_run_sh")"
_s17_prod="$(AGENTSHROUD_ENV=prod bash -c "$_s17_block"$'\n''printf "%s/%s" "$HERMES_MEMORY" "$HERMES_CPUS"')"
_s17_dev="$(AGENTSHROUD_ENV=dev bash -c "$_s17_block"$'\n''printf "%s/%s" "$HERMES_MEMORY" "$HERMES_CPUS"')"
_s17_ovr="$(AGENTSHROUD_ENV=dev AGENTSHROUD_HERMES_MEMORY=1500m AGENTSHROUD_HERMES_CPUS=0.75 bash -c "$_s17_block"$'\n''printf "%s/%s" "$HERMES_MEMORY" "$HERMES_CPUS"')"
_s17_uses_vars="$(grep -c -- '--memory "${HERMES_MEMORY}"' "$hermes_run_sh" || true)"
check "S17: run-standalone.sh (Hermes): caps prod 3g/1.5, dev 2g/1.0, env override honoured" \
    "$([[ -n "$_s17_block" && "$_s17_prod" == "3g/1.5" && "$_s17_dev" == "2g/1.0" && "$_s17_ovr" == "1500m/0.75" && "$_s17_uses_vars" -ge 1 ]] && echo true || echo false)" \
    "prod='${_s17_prod}' dev='${_s17_dev}' override='${_s17_ovr}' docker-run-uses-var=${_s17_uses_vars}"

# S18: `asb rebuild` exits with post-deploy-check's failure code (it used to
# `|| true` and report success on DEPLOY FAILED, 2026-10-17). Behavioral: run
# the real block against a stub check that fails with rc=3. `asb up` keeps
# `|| true` -- sunday-upgrade-apply.sh reads `asb up hermes`'s rc itself.
_s18_block="$(sed -n '/^    _pdc_rc=0$/,/^    fi$/p' "$asb_sh")"
_s18_tmp="$(mktemp -d)"; mkdir -p "$_s18_tmp/scripts"
printf '#!/bin/bash\nexit 3\n' > "$_s18_tmp/scripts/post-deploy-check.sh"
_s18_rc=0; REPO_DIR="$_s18_tmp" bash -c "$_s18_block" >/dev/null 2>&1 || _s18_rc=$?
printf '#!/bin/bash\nexit 0\n' > "$_s18_tmp/scripts/post-deploy-check.sh"
_s18_ok_rc=0; REPO_DIR="$_s18_tmp" bash -c "$_s18_block" >/dev/null 2>&1 || _s18_ok_rc=$?
rm -rf "$_s18_tmp"
_s18_true="$(grep -c 'post-deploy-check.sh" || true' "$asb_sh" || true)"
check "S18: asb rebuild propagates a failed post-deploy-check; asb up unchanged" \
    "$([[ -n "$_s18_block" && "$_s18_rc" -eq 3 && "$_s18_ok_rc" -eq 0 && "$_s18_true" -eq 1 ]] && echo true || echo false)" \
    "fail-rc=${_s18_rc} (want 3) ok-rc=${_s18_ok_rc} (want 0) '|| true' calls left=${_s18_true} (want 1: up)"

# S19: post-deploy-check waits 600s for the bot by default (cold starts took
# 5 min dev / 7 min prod on 2026-10-17/18; 300s failed both healthy deploys).
_s19_wait="$(unset AGENTSHROUD_POST_DEPLOY_BOT_WAIT; bash -c "$(grep '^BOT_WAIT_SECS=' "$REPO/scripts/post-deploy-check.sh")"$'\n''echo "$BOT_WAIT_SECS"')"
check "S19: post-deploy-check default bot wait is 600s" \
    "$([[ "$_s19_wait" == "600" ]] && echo true || echo false)" "BOT_WAIT_SECS='${_s19_wait}'"

# S20: clamd runs under a restart loop in both containers (a memcg OOM kill
# left the gateway without clamd, 2026-10-18), and nothing probes the
# /var/run/clamav socket path that clamd.conf never uses.
_s20_sup=0
for _f in "$REPO/docker/scripts/gateway-start.sh" "$REPO/docker/scripts/start-agentshroud.sh"; do
    grep -q 'clamd --config-file=/etc/clamav/clamd.conf --foreground' "$_f" && grep -q 'while :; do' "$_f" && _s20_sup=$((_s20_sup + 1))
done
_s20_bad="$( { grep -rln 'run/clamav/clamd.ctl' "$REPO/gateway" "$REPO/docker/scripts" --include='*.py' --include='*.sh' 2>/dev/null || true; } | { grep -v '/tests/' || true; } | wc -l | tr -d ' ')"
check "S20: clamd supervised in gateway + bot; no /var/run/clamav socket probes" \
    "$([[ "$_s20_sup" -eq 2 && "$_s20_bad" -eq 0 ]] && echo true || echo false)" \
    "supervised=${_s20_sup}/2 files-probing-wrong-path=${_s20_bad}"

# ── Summary ────────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "${total} assertions: ${pass} passed, ${fail} failed"
echo ""

[[ "$fail" -eq 0 ]]
