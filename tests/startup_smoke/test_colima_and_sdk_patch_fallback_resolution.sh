#!/usr/bin/env bash
# Smoke test: three related fixes found live on 2026-09-07 during a Colima
# VM rebuild (agentshroud-bot/marvin dev environment).
#
# 1. colima-health-check.sh's Colima-VM-internet check used to be
#    "informational only" with a comment claiming a route auto-heal "requires
#    colima ssh as admin user; not available in cron context" — false: colima
#    ssh uses key-based auth and sudo is passwordless for this user, so a
#    missing default route (observed repeatedly, including on a freshly
#    recreated VM) IS fixable from cron. It also checked hardcoded container
#    names (agentshroud-openclaw / agentshroud-gateway) that don't exist on
#    this host (the real names are agentshroud-marvin-openclaw /
#    agentshroud-marvin-gateway) — the same class of bug already fixed once
#    for daily_cve_report.py in commit 154262fc6.
# 2. & 3. patch-telegram-sdk.sh / patch-anthropic-sdk.sh resolved the SDK
#    path via `npm root -g`, which reports the CONFIGURED prefix regardless
#    of whether anything was actually installed there. When OpenClaw's npm
#    reseed step fails (e.g. a transient 502 from registry.npmjs.org) and it
#    falls back to the image-bundled install, the real files live under a
#    different root entirely — `npm root -g` silently pointed at a
#    nonexistent path, so the "SDK not found — egress would bypass the
#    gateway" check fired as a false positive every time, and (per the
#    caller's `|| echo "... failed (non-fatal)"`) never actually blocked
#    startup either way. Fixed to resolve via the real running `openclaw`
#    binary (command -v, respecting PATH) instead.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
fail=0

echo ""
echo "── colima-health-check.sh: route auto-heal + correct container names ──"

check() {
    local label="$1" file="$2" pattern="$3"
    if /usr/bin/grep -qE "$pattern" "$REPO/$file" 2>/dev/null; then
        echo "  OK : $label"
    else
        echo "  FAIL: $label — pattern not found in $file" >&2
        fail=1
    fi
}

check "no longer treats a missing route as unfixable-in-cron" \
    "docker/scripts/colima-health-check.sh" \
    "sudo ip route add default"

check "container names are env-overridable and default to the real dev names" \
    "docker/scripts/colima-health-check.sh" \
    'GATEWAY_CONTAINER="\$\{AGENTSHROUD_GATEWAY_CONTAINER:-agentshroud-dev-gateway\}"'

check "does not still claim the old false premise" \
    "docker/scripts/colima-health-check.sh" \
    "AUTO-HEAL: no default route on Colima VM"

echo ""
echo "── patch-telegram-sdk.sh / patch-anthropic-sdk.sh: fallback-safe SDK path resolution ──"

for f in patch-telegram-sdk.sh patch-anthropic-sdk.sh; do
    check "$f resolves via the real running openclaw binary, not npm root -g alone" \
        "docker/scripts/$f" \
        'OPENCLAW_ROOT="\$\(dirname "\$\(dirname "\$\(readlink -f "\$OPENCLAW_BIN"\)"\)"\)"'
    check "$f skips the write when nothing changed (avoids EROFS on an already-patched read-only file)" \
        "docker/scripts/$f" \
        "no changes needed"
done

# Dynamic check: build a fake "npm seed failed, using bundled fallback"
# layout and confirm the resolution logic (extracted verbatim from the
# fixed script) finds the fallback copy instead of silently reporting
# not-found.
echo ""
echo "── dynamic: fallback path resolution against a fake bundled install ──"

TMPROOT="$(mktemp -d)"
trap 'rm -rf "$TMPROOT"' EXIT

# Simulate the real layout: bundled install at .../lib/node_modules/openclaw,
# with /usr/local/bin/openclaw as a symlink into it (as confirmed live via
# `readlink -f /usr/local/bin/openclaw` on the actual container).
mkdir -p "$TMPROOT/usr/local/lib/node_modules/openclaw/node_modules/grammy/out/core"
echo 'FAKE_SDK_CONTENTS' > "$TMPROOT/usr/local/lib/node_modules/openclaw/node_modules/grammy/out/core/client.js"
mkdir -p "$TMPROOT/usr/local/bin"
ln -s "../lib/node_modules/openclaw/openclaw.mjs" "$TMPROOT/usr/local/bin/openclaw"
touch "$TMPROOT/usr/local/lib/node_modules/openclaw/openclaw.mjs"
chmod +x "$TMPROOT/usr/local/lib/node_modules/openclaw/openclaw.mjs" "$TMPROOT/usr/local/bin/openclaw"

# .npm-global exists on PATH first but is EMPTY (the failed-seed scenario) —
# command -v must fall through to /usr/local/bin, exactly as it does in the
# real container's PATH (.npm-global/bin:...:/usr/local/bin:...).
mkdir -p "$TMPROOT/npm-global/bin"

RESOLVED="$(
    PATH="$TMPROOT/npm-global/bin:$TMPROOT/usr/local/bin:/bin:/usr/bin" sh -c '
        OPENCLAW_BIN="$(command -v openclaw)" || exit 1
        OPENCLAW_ROOT="$(dirname "$(dirname "$(readlink -f "$OPENCLAW_BIN")")")"
        echo "$OPENCLAW_ROOT/openclaw/node_modules/grammy/out/core/client.js"
    '
)"

# Canonicalize both sides — on macOS /var is itself a symlink to
# /private/var, so readlink -f inside the resolution logic returns a fully
# canonicalized path that a plain $TMPROOT comparison wouldn't match. This
# is a macOS test-host artifact only; irrelevant on the real Linux container.
EXPECTED="$(readlink -f "$TMPROOT/usr/local/lib/node_modules/openclaw/node_modules/grammy/out/core/client.js")"
if [ "$RESOLVED" = "$EXPECTED" ] && [ -f "$RESOLVED" ]; then
    echo "  OK : fallback resolution finds the bundled SDK ($RESOLVED)"
else
    echo "  FAIL: expected '$EXPECTED', got '$RESOLVED'" >&2
    fail=1
fi

echo ""
echo "── colima-health-check.sh: step 2 + step 3 false-failure fixes (2026-09-19) ──"

# Both found by running the script live on 2026-09-19. Each reported a
# failure on every 5-min run while the thing it checked was actually fine —
# inflating the daily Telegram summary and masking real failures.

check "step 2 probes \$GATEWAY_CONTAINER, not a container name that does not exist here" \
    "docker/scripts/colima-health-check.sh" \
    'docker exec "\$GATEWAY_CONTAINER" curl'

if /usr/bin/grep -q "docker exec agentshroud-gateway" "$REPO/docker/scripts/colima-health-check.sh"; then
    echo "  FAIL: a literal 'agentshroud-gateway' docker exec survived" >&2
    fail=1
else
    echo "  OK : no literal 'agentshroud-gateway' docker exec remains"
fi

# iptables needs root in the VM; without sudo it errors and the count reads 0.
IPT_NOSUDO=$(/usr/bin/grep -c 'colima ssh -- sh -c "iptables -L DOCKER-USER' \
    "$REPO/docker/scripts/colima-health-check.sh" || true)
IPT_SUDO=$(/usr/bin/grep -c 'colima ssh -- sudo sh -c "iptables -L DOCKER-USER' \
    "$REPO/docker/scripts/colima-health-check.sh" || true)
if [ "$IPT_NOSUDO" -eq 0 ] && [ "$IPT_SUDO" -eq 2 ]; then
    echo "  OK : both DOCKER-USER rule counts run under sudo ($IPT_SUDO/2)"
else
    echo "  FAIL: expected 2 sudo'd and 0 unsudo'd iptables counts, got $IPT_SUDO sudo'd / $IPT_NOSUDO unsudo'd" >&2
    fail=1
fi

echo ""
echo "── colima-health-check.sh: auto-starts a stopped Colima VM ──"

# Added 2026-09-19. The VM was found down ~20 min on the agentshroud-bot dev
# host while this check logged CRITICAL every 5 min and healed nothing.
# ~/Library/LaunchAgents/com.agentshroud.colima-autostart.plist was supposed
# to cover boot, but a RunAtLoad LaunchAgent only bootstraps into the Aqua
# domain at GUI login and this account never gets one (console belongs to
# ijefferson.admin; all dev work arrives over SSH, `launchctl managername`
# reports "Background"). Its hardcoded /tmp/colima-autostart.{log,err} are
# also created first by admin's identically-named agent as
# ijefferson.admin:wheel 0644, so launchd cannot spawn this account's copy
# even from a GUI session. Cron is the only path that actually runs here.

check "starts the VM when colima status reports it stopped" \
    "docker/scripts/colima-health-check.sh" \
    "timeout 300 colima start --cpu 8 --memory 12 --disk 120 --network-address"

check "gates the start on the dev account (never boots a VM on production)" \
    "docker/scripts/colima-health-check.sh" \
    '\[ "\$\(whoami\)" = "agentshroud-bot" \] && ! colima status'

check "re-resolves DOCKER_HOST after start (socket does not exist while down)" \
    "docker/scripts/colima-health-check.sh" \
    "resolve_docker_host"

# Dynamic check: drive the real script against stubbed colima/docker/whoami
# so the branch is exercised, not just grepped. Isolated HOME/state/lock so
# it cannot touch the live VM, the real health log, or the cron state file.
echo ""
echo "── dynamic: auto-start branch against a stubbed Colima ──"

CT="$TMPROOT/colima"
mkdir -p "$CT/bin" "$CT/home/Library/Logs"

cat > "$CT/bin/colima" <<'STUB'
#!/bin/bash
case "$1" in
  status) [ -f "$STUB_DIR/started" ] && exit 0 || exit 1 ;;
  start)  touch "$STUB_DIR/started"; exit ${STUB_START_RC:-0} ;;
  ssh)    exit 0 ;;
esac
exit 0
STUB
cat > "$CT/bin/docker" <<'STUB'
#!/bin/bash
[ "$1" = "info" ] && { [ -f "$STUB_DIR/started" ] && exit 0 || exit 1; }
exit 1
STUB
cat > "$CT/bin/whoami" <<'STUB'
#!/bin/bash
echo "${STUB_USER:-agentshroud-bot}"
STUB
chmod +x "$CT/bin"/*

# Stub PATH first; redirect state/lock away from the live cron paths.
sed -e "s|^export PATH=.*|export PATH=\"$CT/bin:/opt/homebrew/bin:/usr/bin:/bin\"|" \
    -e "s|^STATE_FILE=.*|STATE_FILE=\"$CT/state.json\"|" \
    -e "s|^LOCK_DIR=.*|LOCK_DIR=\"$CT/lock\"|" \
    "$REPO/docker/scripts/colima-health-check.sh" > "$CT/hc.sh"

HC_LOG="$CT/home/Library/Logs/agentshroud-health.log"
hc_run() {  # $1 = STUB_USER (empty for dev account), $2 = start rc
    rm -rf "$CT/started" "$CT/state.json" "$CT/lock" "$HC_LOG"
    env HOME="$CT/home" STUB_DIR="$CT" STUB_USER="$1" STUB_START_RC="$2" \
        bash "$CT/hc.sh" >/dev/null 2>&1 || true
}

hc_run "" 0
if /usr/bin/grep -q "Colima VM started" "$HC_LOG" 2>/dev/null \
   && /usr/bin/grep -q "internet check failed\|iptables" "$HC_LOG" 2>/dev/null; then
    echo "  OK : stopped VM is started, then the run continues to the later checks"
else
    echo "  FAIL: stopped VM was not started, or the run exited instead of continuing" >&2
    fail=1
fi

hc_run "" 1
if /usr/bin/grep -q "colima start failed" "$HC_LOG" 2>/dev/null; then
    echo "  OK : a failed start is reported and the run stops at the Docker check"
else
    echo "  FAIL: a failed colima start was not reported" >&2
    fail=1
fi

hc_run "ijefferson.admin" 0
if /usr/bin/grep -q "CRITICAL" "$HC_LOG" 2>/dev/null \
   && ! /usr/bin/grep -q "Colima VM is stopped" "$HC_LOG" 2>/dev/null; then
    echo "  OK : no start is attempted on the production account"
else
    echo "  FAIL: production account attempted a VM start" >&2
    fail=1
fi

echo ""
echo "── colima-health-check.sh: diagnostic baseline is compared, not swallowed ──"

# Until 2026-09-20 this branch logged ANY number of diagnostic failures as
# "expected", so a new failure was absorbed silently. The documented set
# ("5 expected failures ... DNS resolution ... pass") had also drifted: the
# real figure is 8 and DNS resolution is NOT among the passes — the
# container's embedded resolver cannot reach its upstreams under egress
# enforcement, and does not need to (all egress goes via gateway:8181,
# which resolves for it).

check "compares against a baseline instead of accepting any count" \
    "docker/scripts/colima-health-check.sh" \
    'DIAG_FAILS" -le "\$DIAG_EXPECTED_FAILS'

check "baseline is env-overridable (repo convention)" \
    "docker/scripts/colima-health-check.sh" \
    'DIAG_EXPECTED_FAILS="\$\{AGENTSHROUD_DIAG_EXPECTED_FAILS:-8\}"'

check "exceeding the baseline raises a real failure" \
    "docker/scripts/colima-health-check.sh" \
    'FAILURES\+=\("container net diag: \$DIAG_FAILS failures exceeds'

if /usr/bin/grep -q "The 5 expected failures" "$REPO/docker/scripts/colima-health-check.sh"; then
    echo "  FAIL: stale '5 expected failures' comment still present" >&2
    fail=1
else
    echo "  OK : stale '5 expected failures' comment is gone"
fi

echo ""
echo "── com.agentshroud.colima-autostart.plist: per-account log paths ──"

PLIST="$HOME/Library/LaunchAgents/com.agentshroud.colima-autostart.plist"
if [ ! -f "$PLIST" ]; then
    echo "  SKIP: plist not installed on this host"
elif /usr/bin/grep -q "<string>/tmp/colima-autostart" "$PLIST"; then
    echo "  FAIL: plist still writes to /tmp (collides with the production account's agent)" >&2
    fail=1
elif /usr/bin/plutil -lint "$PLIST" >/dev/null 2>&1; then
    echo "  OK : plist is valid and no longer writes to shared /tmp paths"
else
    echo "  FAIL: plist does not pass plutil -lint" >&2
    fail=1
fi

echo ""
echo "── hook ownership: installers must be additive, never clobber ──"

# .git/hooks/pre-commit is a single file. Four things used to write it
# (.llm_settings/git-hooks/install.sh twice, its `git secrets --install
# --force`, and scripts/pre-commit-hook.sh's documented `cp`), so whichever ran
# last silently won. On 2026-09-20 a bare `git secrets --install` had reduced
# it to a two-line git-secrets call, leaving gitleaks, detect-secrets, ruff,
# black and semgrep running on no commit at all. Owner will keep installing
# llm_settings into this and other repos as it grows; these checks are what
# stop that from costing coverage again.

# Strip comments and blanks first — this file DOCUMENTS the old clobbering
# behaviour at length, and a naive grep matches that prose and reports a
# regression that isn't there (it did, on first run).
INSTALL_CODE="$TMPROOT/install.code.sh"
/usr/bin/sed -e 's/[[:space:]]*#.*$//' -e '/^[[:space:]]*$/d' \
    "$REPO/.llm_settings/git-hooks/install.sh" > "$INSTALL_CODE"

if /usr/bin/grep -qE 'cp .*\$HOOK_SOURCE.* \.git/hooks/pre-commit' "$INSTALL_CODE"; then
    echo "  FAIL: install.sh still copies a hook over .git/hooks/pre-commit" >&2
    fail=1
else
    echo "  OK : install.sh no longer clobbers the hook path"
fi

if /usr/bin/grep -q 'git secrets --install --force' "$INSTALL_CODE"; then
    echo "  FAIL: install.sh still runs 'git secrets --install --force'" >&2
    fail=1
else
    echo "  OK : install.sh no longer force-installs git-secrets over the hook"
fi

check "install.sh hands ownership to pre-commit" \
    ".llm_settings/git-hooks/install.sh" \
    "pre-commit install"

check "install.sh refuses to overwrite an existing config" \
    ".llm_settings/git-hooks/install.sh" \
    "left untouched"

check "scripts/pre-commit-hook.sh warns against being copied into place" \
    "scripts/pre-commit-hook.sh" \
    "DO NOT INSTALL THIS BY COPYING"

if /usr/bin/grep -A2 'gitleaks not found' "$REPO/scripts/pre-commit-hook.sh" \
    | /usr/bin/grep -q 'exit 0'; then
    echo "  FAIL: pre-commit-hook.sh still exits 0 when gitleaks is missing" >&2
    fail=1
else
    echo "  OK : a missing gitleaks fails instead of silently passing"
fi

# Dynamic: prove the installer preserves a config and hook it did not write.
echo ""
echo "── dynamic: installer preserves pre-existing config + hook ──"

HR="$TMPROOT/hookrepo"
mkdir -p "$HR"
(
  cd "$HR" && git init -q 2>/dev/null
  printf 'repos:\n  - repo: local\n    hooks:\n      - id: sentinel-hook\n        name: sentinel\n        entry: true\n        language: system\n' > .pre-commit-config.yaml
  printf '#!/bin/sh\necho custom\n' > .git/hooks/pre-commit
  chmod +x .git/hooks/pre-commit
  shasum .pre-commit-config.yaml | awk '{print $1}' > .sentinel-before
  bash "$REPO/.llm_settings/git-hooks/install.sh" >/dev/null 2>&1 || true
  shasum .pre-commit-config.yaml | awk '{print $1}' > .sentinel-after
)
if [ "$(cat "$HR/.sentinel-before" 2>/dev/null)" = "$(cat "$HR/.sentinel-after" 2>/dev/null)" ] \
   && /usr/bin/grep -q sentinel-hook "$HR/.pre-commit-config.yaml" 2>/dev/null; then
    echo "  OK : pre-existing .pre-commit-config.yaml survives the installer byte-for-byte"
else
    echo "  FAIL: installer modified or replaced a config it did not write" >&2
    fail=1
fi
if ls "$HR"/.git/hooks/pre-commit.pre-llm-settings.* >/dev/null 2>&1; then
    echo "  OK : pre-existing hook was backed up, not discarded"
else
    echo "  FAIL: pre-existing hook was not backed up" >&2
    fail=1
fi

echo ""
echo "── sunday-upgrade.sh: transient fetch failure must not forfeit the week ──"

# 2026-09-20: the 03:02 unattended run died on its FIRST `git fetch origin
# main` and nothing retried it, so no upgrade ran that Sunday at all. The job
# fires once a week (0 3 * * 0), so a single-shot network call means one blip
# costs seven days. Not theoretical on this host: streams from
# files.pythonhosted.org abort at random sizes with TLS "bad decrypt" while a
# 41.9MB file from another host downloads cleanly.

check "git fetch is retried rather than single-shot" \
    "scripts/sunday-upgrade.sh" \
    "_fetch_ok"

check "still FATALs (exit 3) once the retries are exhausted" \
    "scripts/sunday-upgrade.sh" \
    "failed after 5 attempts"

if /usr/bin/grep -qE '^git fetch origin main >/dev/null 2>&1 \|\| \{' \
    "$REPO/scripts/sunday-upgrade.sh"; then
    echo "  FAIL: the old single-shot fetch guard is still present" >&2
    fail=1
else
    echo "  OK : the single-shot fetch guard is gone"
fi

# Dynamic: drive the retry block with a stubbed git, to prove it both recovers
# and still gives up — asserting behaviour, not the presence of text.
RT="$TMPROOT/retry.sh"
/usr/bin/sed -n '/^_fetch_ok=0$/,/^fi$/p' "$REPO/scripts/sunday-upgrade.sh" > "$RT.body"
{
  echo 'sleep() { :; }'
  echo 'git() { [ "$ATTEMPT_N" -ge "${FAIL_UNTIL:-99}" ] && return 0; ATTEMPT_N=$((ATTEMPT_N+1)); return 1; }'
  echo 'ATTEMPT_N=1'
  cat "$RT.body"
  echo 'exit 0'
} > "$RT"

if OUT=$(FAIL_UNTIL=3 bash "$RT" 2>&1) && echo "$OUT" | /usr/bin/grep -q "succeeded on attempt 3"; then
    echo "  OK : recovers when a later attempt succeeds"
else
    echo "  FAIL: did not recover on a later successful attempt" >&2
    fail=1
fi

# Must be inside the `if` condition: this file runs under `set -e`, so a bare
# invocation that exits 3 aborts the whole suite and silently truncates every
# check after it (it did, on first run).
if FAIL_UNTIL=99 bash "$RT" >/dev/null 2>&1; then _rc=0; else _rc=$?; fi
if [ "$_rc" -eq 3 ]; then
    echo "  OK : still exits 3 when every attempt fails"
else
    echo "  FAIL: exhausted retries did not exit 3" >&2
    fail=1
fi

echo ""
echo "── sunday-upgrade.sh: memory precondition ──"

# This box runs two Colima VMs on one machine; a build started into a
# critically-pressured host gets OOM-killed for reasons that appear nowhere in
# the job's log. Exit 5 keeps "deferred" distinct from 3 (fetch) and 4 (wrong
# branch), so a defer is never read as success or failure.
#
# Keyed on macOS's pressure level, NOT free swap. The first version used swap
# headroom and was wrong: on 2026-09-20 this host showed 392MB free swap while
# physical memory was 32% free of 64GB at pressure level 2. macOS grows swap
# under load and never releases it, so free swap sits near zero on a healthy
# host — that threshold would have deferred every run forever.

check "keys on the kernel pressure level, not free swap" \
    "scripts/sunday-upgrade.sh" \
    "kern.memorystatus_vm_pressure_level"

if /usr/bin/grep -q "SUNDAY_UPGRADE_MIN_SWAP_FREE_MB" "$REPO/scripts/sunday-upgrade.sh"; then
    echo "  FAIL: the swap-based threshold is still present" >&2
    fail=1
else
    echo "  OK : the swap-based threshold is gone"
fi

check "defers with a distinct exit code" \
    "scripts/sunday-upgrade.sh" \
    "exit 5"

MG="$TMPROOT/memguard.sh"
/usr/bin/sed -n '/^# ── Memory precondition/,/^fi$/p' \
    "$REPO/scripts/sunday-upgrade.sh" > "$MG.body"
{
  echo '#!/bin/bash'
  echo 'sysctl() { [ "${FAKE_FAIL:-0}" = "1" ] && return 1; echo "${FAKE_LEVEL:-2}"; }'
  cat "$MG.body"
  echo 'exit 0'
} > "$MG"

for lvl in 1 2; do
    if FAKE_LEVEL=$lvl bash "$MG" >/dev/null 2>&1; then
        echo "  OK : proceeds at pressure level $lvl"
    else
        echo "  FAIL: deferred at pressure level $lvl (should proceed)" >&2
        fail=1
    fi
done

if FAKE_LEVEL=4 bash "$MG" >/dev/null 2>&1; then _rc=0; else _rc=$?; fi
if [ "$_rc" -eq 5 ]; then
    echo "  OK : defers (exit 5) at critical pressure"
else
    echo "  FAIL: critical pressure did not defer with exit 5 (got $_rc)" >&2
    fail=1
fi

if FAKE_FAIL=1 bash "$MG" >/dev/null 2>&1; then
    echo "  OK : an unreadable probe skips the check rather than blocking"
else
    echo "  FAIL: a failed probe blocked the run" >&2
    fail=1
fi

echo ""
echo "── sunday-upgrade.sh: 3h ceiling is enforced, and no branch is left behind ──"

# 2026-09-20/21, both found live:
#  * The 180m watchdog logged "leaving the session running" and broke out of
#    the wait loop WITHOUT killing tmux. An 11:00 run was "timed out" at 14:00
#    and kept working until 21:09 — ten hours against a three-hour ceiling.
#  * The sentinel was written unconditionally, so that timed-out run marked the
#    day complete at 14:00 while its report was not written until 19:53, and
#    every remaining retry that day skipped.
#  * The run left the checkout on chore/upgrade-<date>, so the next day's 03:00
#    and 05:00 fires both FATAL'd on the branch guard. The job sabotaged its
#    own next invocation.

check "the watchdog actually kills the session" \
    "scripts/sunday-upgrade.sh" \
    "tmux kill-session -t"

check "a timed-out run is flagged rather than silently completed" \
    "scripts/sunday-upgrade.sh" \
    "TIMED_OUT=1"

check "a timed-out run writes no sentinel and stays retryable" \
    "scripts/sunday-upgrade.sh" \
    "no sentinel written"

if /usr/bin/grep -q "leaving the session running" "$REPO/scripts/sunday-upgrade.sh"; then
    echo "  FAIL: the watchdog still leaves the session running" >&2
    fail=1
else
    echo "  OK : the 'leaving the session running' behaviour is gone"
fi

check "the checkout is returned to main" \
    "scripts/sunday-upgrade.sh" \
    "checkout returned to main"

# Dynamic: drive the branch-return block against real scratch repos.
BR="$TMPROOT/br.body"
/usr/bin/sed -n '/^_final_branch=/,/^fi$/p' "$REPO/scripts/sunday-upgrade.sh" > "$BR"
BREM="$TMPROOT/bremote"; git init -q --bare "$BREM" 2>/dev/null

_mk() {  # $1 = dirty|clean
    rm -rf "$TMPROOT/brepo"; git init -q -b main "$TMPROOT/brepo" 2>/dev/null
    ( cd "$TMPROOT/brepo"
      git config user.email t@t; git config user.name t
      git remote add origin "$BREM"
      echo base > f.txt; git add -A; git commit -qm base; git push -q -u origin main 2>/dev/null
      git checkout -q -b chore/upgrade-test; echo work >> f.txt; git add -A; git commit -qm work
      [ "$1" = "dirty" ] && echo uncommitted >> f.txt
      true )
}

_mk clean
( cd "$TMPROOT/brepo" && source "$BR" ) >/dev/null 2>&1 || true
if [ "$(cd "$TMPROOT/brepo" && git rev-parse --abbrev-ref HEAD)" = "main" ]; then
    echo "  OK : a clean tree is returned to main"
else
    echo "  FAIL: a clean tree was left on the upgrade branch" >&2
    fail=1
fi
if [ "$(cd "$TMPROOT/brepo" && git ls-remote --heads origin chore/upgrade-test | wc -l | tr -d ' ')" = "1" ]; then
    echo "  OK : the branch is pushed before switching, so work is never stranded"
else
    echo "  FAIL: the upgrade branch was not pushed" >&2
    fail=1
fi

_mk dirty
( cd "$TMPROOT/brepo" && source "$BR" ) >/dev/null 2>&1 || true
if [ "$(cd "$TMPROOT/brepo" && git rev-parse --abbrev-ref HEAD)" = "chore/upgrade-test" ]; then
    echo "  OK : a dirty tree is left alone rather than losing uncommitted work"
else
    echo "  FAIL: switched away from a dirty tree" >&2
    fail=1
fi

echo ""
echo "── unattended run must not be able to hang on a permission prompt ──"

# Root cause of ~3 weeks of failed unattended runs, found 2026-09-21.
# --permission-mode acceptEdits auto-accepts EDITS but still prompts for Bash,
# and a prompt in an unattended session hangs forever. The job only appeared to
# work on the dev host because .claude/settings.local.json had accumulated 287
# allow rules (265 Bash) from prompts answered by hand over weeks — and that
# file is gitignored, so a fresh clone has none of them and stalls on the first
# Bash call. Reliability was a function of how many prompts someone had clicked
# on that specific machine, which cannot be shipped to anyone else.

if /usr/bin/grep -q 'permission-mode acceptEdits' "$REPO/scripts/sunday-upgrade.sh"; then
    echo "  FAIL: unattended run still uses acceptEdits (prompts on Bash -> hangs)" >&2
    fail=1
else
    echo "  OK : acceptEdits is no longer used for the unattended run"
fi

check "uses a mode that never prompts" \
    "scripts/sunday-upgrade.sh" \
    "SUNDAY_UPGRADE_PERMISSION_MODE:-dontAsk"

if /usr/bin/grep -qE 'SUNDAY_UPGRADE_PERMISSION_MODE:-bypassPermissions' \
    "$REPO/scripts/sunday-upgrade.sh"; then
    echo "  FAIL: bypassPermissions is the DEFAULT — ships a no-boundary posture" >&2
    fail=1
else
    echo "  OK : bypassPermissions is an opt-in override, not the default"
fi

# The committed allowlist is what makes dontAsk workable on a fresh clone.
python3 - "$REPO/.claude/settings.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1])); p = d.get("permissions", {})
allow, deny = p.get("allow", []), p.get("deny", [])
hooks = sum(len(m["hooks"]) for k in d.get("hooks", {}) for m in d["hooks"][k])
ok = True
if len(allow) < 40:
    print("  FAIL: committed allowlist too small (%d) — a fresh clone will stall" % len(allow)); ok = False
else:
    print("  OK : committed allowlist carries %d rules (no reliance on gitignored local state)" % len(allow))
if not deny:
    print("  FAIL: deny rules missing — secrets would be readable"); ok = False
else:
    print("  OK : %d deny rules preserved" % len(deny))
if hooks < 10:
    print("  FAIL: PreToolUse/PostToolUse hooks were weakened (%d)" % hooks); ok = False
else:
    print("  OK : %d hooks preserved — they refuse with exit 2, returning control" % hooks)
sys.exit(0 if ok else 1)
PY
[ "$?" -eq 0 ] || fail=1

echo ""
echo "── colima-health-check.sh: repairs a dead docker socket forward ──"

# Happened four separate times on 2026-09-21. lima establishes the
# /var/run/docker.sock forward exactly ONCE, at VM start. When the ssh
# connection carrying it drops, lima re-establishes a mux for `colima ssh` but
# never restores the socket forward — so `colima ssh` keeps working and
# `colima status` reports "running" while every docker call fails with
# "Cannot connect" or a bare EOF. Nothing self-heals it. Verified live:
# dockerd active inside the VM, all 7 containers healthy, 5.9GB free, host
# unable to reach either socket path; the hostagent log showed the forward set
# up once at 08:01:59 with no error after — it does not know it lost anything.
# This is a DIFFERENT failure from a stopped VM and needs a restart, not a start.

check "detects VM-running-but-docker-unreachable as its own condition" \
    "docker/scripts/colima-health-check.sh" \
    "socket forward is dead"

check "repairs it by restarting Colima" \
    "docker/scripts/colima-health-check.sh" \
    "colima restart"

HS="$TMPROOT/hcheck"; mkdir -p "$HS/bin" "$HS/home/Library/Logs"
cat > "$HS/bin/colima" <<'STUB'
#!/bin/bash
case "$1" in
  status)  [ "${VM_UP:-1}" = "1" ] && exit 0 || exit 1 ;;
  start)   echo up > "$STUB_DIR/sock"; exit 0 ;;
  restart) [ "${RESTART_OK:-1}" = "1" ] && { echo up > "$STUB_DIR/sock"; exit 0; } || exit 1 ;;
  ssh)     exit 0 ;;
esac
exit 0
STUB
cat > "$HS/bin/docker" <<'STUB'
#!/bin/bash
[ "$1" = "info" ] && { [ -f "$STUB_DIR/sock" ] && exit 0 || exit 1; }
exit 1
STUB
printf '#!/bin/bash\necho "${STUB_USER:-agentshroud-bot}"\n' > "$HS/bin/whoami"
chmod +x "$HS/bin"/*
/usr/bin/sed -e "s|^export PATH=.*|export PATH=\"$HS/bin:/opt/homebrew/bin:/usr/bin:/bin\"|" \
    -e "s|^STATE_FILE=.*|STATE_FILE=\"$HS/state.json\"|" \
    -e "s|^LOCK_DIR=.*|LOCK_DIR=\"$HS/lock\"|" \
    "$REPO/docker/scripts/colima-health-check.sh" > "$HS/hc.sh"

HL="$HS/home/Library/Logs/agentshroud-health.log"
_hc() { rm -rf "$HS/sock" "$HS/state.json" "$HS/lock" "$HL"
        env HOME="$HS/home" STUB_DIR="$HS" VM_UP="$1" RESTART_OK="$2" STUB_USER="$3" \
            bash "$HS/hc.sh" >/dev/null 2>&1 || true; }

_hc 1 1 agentshroud-bot
if /usr/bin/grep -q "socket forward restored" "$HL" 2>/dev/null; then
    echo "  OK : VM up + socket dead is repaired by a restart"
else
    echo "  FAIL: a dead socket forward was not repaired" >&2
    fail=1
fi

_hc 0 1 agentshroud-bot
if /usr/bin/grep -q "Colima VM is stopped" "$HL" 2>/dev/null \
   && ! /usr/bin/grep -q "socket forward is dead" "$HL" 2>/dev/null; then
    echo "  OK : a STOPPED VM still takes the start path, not the restart path"
else
    echo "  FAIL: stopped VM and dead socket forward are being confused" >&2
    fail=1
fi

_hc 1 1 ijefferson.admin
if ! /usr/bin/grep -q "socket forward is dead" "$HL" 2>/dev/null; then
    echo "  OK : no restart is attempted on the production account"
else
    echo "  FAIL: production account attempted a Colima restart" >&2
    fail=1
fi

echo ""
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
