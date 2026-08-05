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

# ── Summary ────────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "${total} assertions: ${pass} passed, ${fail} failed"
echo ""

[[ "$fail" -eq 0 ]]
