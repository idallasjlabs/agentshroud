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

# Asserts the invocation, not the VM shape: the flags moved into the shared
# $_COLIMA_VM_FLAGS on 2026-09-22 so a resize cannot land on one recovery path
# and miss the other. The memory value itself is covered by the
# "one source of truth" section below — duplicating it here is what let #463
# change one copy and leave the other at 12GB.
check "starts the VM when colima status reports it stopped" \
    "docker/scripts/colima-health-check.sh" \
    'timeout 300 colima start \$_COLIMA_VM_FLAGS'

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

# A FRESH bare remote per scenario. Reusing one across calls looks harmless but
# is not: each call re-inits brepo, so the second scenario pushes an unrelated
# history at a `main` the first one already created. Git rejects that as a
# non-fast-forward, and under `set -e` the failed push killed the whole suite
# mid-run — 49 checks reported OK, 0 FAIL, exit 1, and every section after this
# point silently never ran. Same truncation class as the earlier `set -e` bug
# two sections up, which is why the push is also guarded here.
_mk() {  # $1 = dirty|clean
    rm -rf "$TMPROOT/brepo" "$BREM"
    git init -q --bare "$BREM" 2>/dev/null
    git init -q -b main "$TMPROOT/brepo" 2>/dev/null
    ( cd "$TMPROOT/brepo"
      git config user.email t@t; git config user.name t
      git remote add origin "$BREM"
      echo base > f.txt; git add -A; git commit -qm base
      git push -q -u origin main 2>/dev/null || true
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
echo "── socket-forward repair: bounded stop THEN start, not one restart ──"

# The repair failed on its own first live outage (2026-09-21). It used a single
# `timeout 420 colima restart`; the restart blew that budget, the timeout killed
# it mid-flight leaving the VM stopped, and the run logged "colima restart
# failed" and gave up. What actually recovered the host was step 1a's
# stopped-VM path on the NEXT cron invocation — the repair only worked by
# accident, through a different branch, a tick later.
#
# Split into bounded stop + bounded start so that recovery is deliberate: a
# wedged stop can no longer starve the start, and the start runs even when the
# stop fails, because that is the half that restores service.

# Comments must be stripped first: the block below DOCUMENTS the old
# `timeout 420 colima restart` while explaining why it was replaced, and a
# naive grep matches that prose and reports a regression that isn't there
# (it did, on first run — the same comment-vs-code trap this suite already
# guards against in the llm_settings installer checks).
HC_CODE="$TMPROOT/hc.code.sh"
/usr/bin/sed -e 's/[[:space:]]*#.*$//' -e '/^[[:space:]]*$/d' \
    "$REPO/docker/scripts/colima-health-check.sh" > "$HC_CODE"

if /usr/bin/grep -qE 'timeout [0-9]+ colima restart' "$HC_CODE"; then
    echo "  FAIL: still a single 'colima restart' — a slow stop starves the start" >&2
    fail=1
else
    echo "  OK : no single-command restart remains"
fi

check "stop is bounded separately" \
    "docker/scripts/colima-health-check.sh" \
    "timeout 300 colima stop"

check "start runs even when the stop fails" \
    "docker/scripts/colima-health-check.sh" \
    "continuing to start anyway"

# 300 + 420 must stay under the 900s stale-lock threshold, or a repair can be
# declared stale and re-entered by the next tick — two colima starts racing.
python3 - "$HC_CODE" "$REPO/docker/scripts/colima-health-check.sh" <<'PY'
import re, sys
t = open(sys.argv[1]).read()          # comment-stripped code only
full = open(sys.argv[2]).read()
m = re.search(r'timeout (\d+) colima stop', t)
stop = int(m.group(1))
# The REPAIR's start is the first one AFTER the stop — not step 1a's earlier
# stopped-VM start, which a plain search matches instead (it did, reporting
# 300+300 rather than the real 300+420).
m2 = re.search(r'timeout (\d+) colima start', t[m.end():])
start = int(m2.group(1))
stale = int(re.search(r'LOCK_AGE" -gt (\d+)', full).group(1))
if stop + start < stale:
    print(f"  OK : repair budget {stop}+{start}={stop+start}s stays under the {stale}s stale-lock threshold")
else:
    print(f"  FAIL: {stop}+{start}={stop+start}s >= {stale}s stale lock — concurrent repairs possible", file=sys.stderr)
    sys.exit(1)
PY
[ "$?" -eq 0 ] || fail=1

RS="$TMPROOT/restart"; mkdir -p "$RS/bin" "$RS/home/Library/Logs"
cat > "$RS/bin/colima" <<'STUB'
#!/bin/bash
case "$1" in
  status) exit 0 ;;
  stop)   echo stop >> "$STUB_DIR/calls"; exit ${STOP_RC:-0} ;;
  start)  echo start >> "$STUB_DIR/calls"; [ "${START_RC:-0}" = "0" ] && echo up > "$STUB_DIR/sock"; exit ${START_RC:-0} ;;
  ssh)    exit 0 ;;
esac
exit 0
STUB
cat > "$RS/bin/docker" <<'STUB'
#!/bin/bash
[ "$1" = "info" ] && { [ -f "$STUB_DIR/sock" ] && exit 0 || exit 1; }
exit 1
STUB
printf '#!/bin/bash\necho agentshroud-bot\n' > "$RS/bin/whoami"
chmod +x "$RS/bin"/*
/usr/bin/sed -e "s|^export PATH=.*|export PATH=\"$RS/bin:/opt/homebrew/bin:/usr/bin:/bin\"|" \
    -e "s|^STATE_FILE=.*|STATE_FILE=\"$RS/state.json\"|" \
    -e "s|^LOCK_DIR=.*|LOCK_DIR=\"$RS/lock\"|" \
    "$REPO/docker/scripts/colima-health-check.sh" > "$RS/hc.sh"

_bounce() { rm -rf "$RS/sock" "$RS/calls" "$RS/state.json" "$RS/lock" \
                   "$RS/home/Library/Logs/agentshroud-health.log"
            env HOME="$RS/home" STUB_DIR="$RS" STOP_RC="$1" START_RC="$2" \
                bash "$RS/hc.sh" >/dev/null 2>&1 || true; }

# The regression that matters: a FAILED stop must not prevent the start.
_bounce 1 0
if /usr/bin/grep -q start "$RS/calls" 2>/dev/null \
   && /usr/bin/grep -q "socket forward restored" \
        "$RS/home/Library/Logs/agentshroud-health.log" 2>/dev/null; then
    echo "  OK : a failed stop still starts the VM and recovers"
else
    echo "  FAIL: a failed stop prevented the start — the original defect" >&2
    fail=1
fi

_bounce 0 0
if [ "$(tr '\n' ' ' < "$RS/calls" 2>/dev/null)" = "stop start " ]; then
    echo "  OK : normal path is stop then start, in order"
else
    echo "  FAIL: unexpected call order: $(tr '\n' ' ' < "$RS/calls" 2>/dev/null)" >&2
    fail=1
fi

echo ""
echo "── colima VM flags: one source of truth, both recovery paths agree ──"

# #463 reduced the VM memory ceiling 12 -> 10GB but changed only ONE of the two
# `colima start` invocations: the stopped-VM path got 10, the socket-forward
# repair kept 12. The resulting VM's memory ceiling depended on which failure
# fired, while the commit message said the ceiling had been reduced. The miss
# was structural, not careless — 1a-bis had been added days earlier in #461, so
# a second copy of the literal existed by the time #463 was written.

HCF="$TMPROOT/hc.flags.sh"
/usr/bin/sed -e 's/[[:space:]]*#.*$//' -e '/^[[:space:]]*$/d' \
    "$REPO/docker/scripts/colima-health-check.sh" > "$HCF"

if /usr/bin/grep -qE 'colima start .*--memory [0-9]+' "$HCF"; then
    echo "  FAIL: a literal --memory survives on a colima start line — it will drift again" >&2
    /usr/bin/grep -nE 'colima start .*--memory [0-9]+' "$HCF" | sed 's/^/        /' >&2
    fail=1
else
    echo "  OK : no literal --memory on any colima start line"
fi

# Anchor on `timeout N colima start` — the actual invocation form. A bare
# 'colima start' also matches the AUTO-HEAL log strings that mention it by
# name ("colima start failed or exceeded the 300s timeout"), which counted 5
# paths where there are 2 (it did, on first run).
STARTS=$(/usr/bin/grep -cE 'timeout [0-9]+ colima start ' "$HCF")
SHARED=$(/usr/bin/grep -cE 'timeout [0-9]+ colima start \$_COLIMA_VM_FLAGS' "$HCF")
if [ "$STARTS" -ge 2 ] && [ "$STARTS" -eq "$SHARED" ]; then
    echo "  OK : all $STARTS colima start paths use the shared flag set"
else
    echo "  FAIL: $SHARED of $STARTS colima start paths use the shared flags" >&2
    fail=1
fi

check "memory is overridable per host without editing the script" \
    "docker/scripts/colima-health-check.sh" \
    "AGENTSHROUD_COLIMA_MEMORY_GB"

# Prove the flags actually expand to one consistent value, rather than just
# looking consistent in source.
EXPANDED=$(/usr/bin/sed -n 's/^_COLIMA_MEMORY_GB=.*:-\([0-9]*\)}"/\1/p' "$HCF")
if [ -n "$EXPANDED" ]; then
    echo "  OK : both paths resolve to a single --memory ${EXPANDED}GB default"
else
    echo "  FAIL: could not resolve the shared memory default" >&2
    fail=1
fi


echo ""
echo "── sunday-upgrade-apply.sh: build routed inside the VM (SUNDAY_BUILD_VIA_VM) ──"

# Context: on 2026-09-23 the image store had grown to 186GiB, every image
# operation triggered a full content-store walk, and clients timed out — which
# had been misread for days as "the docker.sock forward dies under build load".
# A build that had already reached "naming to ... done" was then killed by its
# own SSH channel dropping ("exit status 255") and reported as a build failure.
# SUNDAY_BUILD_VIA_VM=1 builds inside the VM, DETACHED, polling for an exit-code
# sentinel, so neither the host socket nor the SSH channel is in the path.
#
# These checks EXECUTE the real function against stubbed commands rather than
# grepping for it — a grep here would happily match the paragraph above instead
# of the code, which has already produced two false-passing checks in this suite.
APPLY="$REPO/scripts/sunday-upgrade-apply.sh"

_render_build() {
    # $1 = value of SUNDAY_BUILD_VIA_VM. Returns every command that would run.
    # The stubs append to a capture file rather than echoing: the real launch
    # call is redirected to /dev/null, so anything written to stdout by a stub
    # is invisible to this test and every assertion below would pass vacuously.
    local cap; cap="$(mktemp)"
    /usr/bin/env bash -c '
        eval "$(/usr/bin/sed -n "/^_build_one_service()/,/^}/p" "$1")"
        CAP="$3"
        log() { :; }
        docker-compose() { echo "HOSTCALL: docker-compose $*" >> "$CAP"; }
        colima() { echo "VMCALL: colima $*" >> "$CAP"; return 0; }
        sed() { cat; }
        COMPOSE_CMD="docker-compose -f a.yml -p proj --profile full"
        REPO="/repo"
        SUNDAY_BUILD_VIA_VM="$2"
        SUNDAY_BUILD_VM_TIMEOUT=2
        SUNDAY_BUILD_VM_POLL=1
        _build_one_service gateway
    ' _ "$APPLY" "$1" "$cap" >/dev/null 2>&1 || true
    cat "$cap"; rm -f "$cap"
}

HOST_RENDER="$(_render_build 0)"
VM_RENDER="$(_render_build 1)"

# The remote program is base64'd so no quoting survives the ssh hop; decode it
# and assert on what the VM would actually execute.
VM_B64="$(printf '%s\n' "$VM_RENDER" | /usr/bin/sed -n 's/.*echo \([A-Za-z0-9+/=]\{40,\}\) | base64 -d.*/\1/p' | head -1)"
VM_SCRIPT="$(printf '%s' "$VM_B64" | /usr/bin/base64 -d 2>/dev/null || true)"

# 1. Default (unset/0) must be byte-identical to the pre-change host build, so
#    enabling the flag is the only behaviour change this introduces.
if [[ "$HOST_RENDER" == "HOSTCALL: docker-compose -f a.yml -p proj --profile full build --pull gateway" ]]; then
    echo "  OK : default path is the unchanged host build (no colima in the path)"
else
    echo "  FAIL: default host build render changed: $HOST_RENDER" >&2
    fail=1
fi

DEFAULT_OFF="$(/usr/bin/env bash -c '
    eval "$(/usr/bin/sed -n "/^_build_one_service()/,/^}/p" "$1")"
    log() { :; }
    docker-compose() { echo "HOSTCALL"; }
    colima() { echo "VMCALL"; return 0; }
    COMPOSE_CMD="docker-compose"
    REPO="/repo"
    SUNDAY_BUILD_VIA_VM="${SUNDAY_BUILD_VIA_VM:-0}"
    _build_one_service gateway
' _ "$APPLY" 2>/dev/null || true)"
if [[ "$DEFAULT_OFF" == "HOSTCALL" ]]; then
    echo "  OK : opt-in — with the variable unset the host path still runs"
else
    echo "  FAIL: unset SUNDAY_BUILD_VIA_VM did not take the host path: $DEFAULT_OFF" >&2
    fail=1
fi

# 2. With the flag on, the build must go through colima ssh and NOT the host.
if [[ "$VM_RENDER" == *"VMCALL: colima ssh"* && "$VM_RENDER" != *HOSTCALL* ]]; then
    echo "  OK : SUNDAY_BUILD_VIA_VM=1 builds via colima ssh, never the host socket"
else
    echo "  FAIL: flag did not route the build into the VM: $VM_RENDER" >&2
    fail=1
fi

# 3. The remote program must decode — if it does not, every check below is
#    vacuously true, which is exactly the silent-pass class this file exists for.
if [[ -n "$VM_SCRIPT" ]]; then
    echo "  OK : the remote program is recoverable from the launch command"
else
    echo "  FAIL: could not decode the base64 remote program from the VM render" >&2
    fail=1
fi

# 4. The VM has only the compose *plugin*; a literal 'docker-compose' inside the
#    VM is command-not-found. Assert the translation actually happened.
if [[ "$VM_SCRIPT" == *"docker compose "* && "$VM_SCRIPT" != *"docker-compose"* ]]; then
    echo "  OK : COMPOSE_CMD translated to the plugin form the VM actually has"
else
    echo "  FAIL: remote program did not translate docker-compose -> docker compose" >&2
    fail=1
fi

# 5. Regression: the first in-VM build attempt emitted "OPENCLAW_VERSION is not
#    set, defaulting to a blank string" and would have built unpinned images —
#    the VM shell inherits nothing from the caller.
if [[ "$VM_SCRIPT" == *"versions.env"* ]]; then
    echo "  OK : re-sources docker/versions.env in the VM (no blank version pins)"
else
    echo "  FAIL: remote program does not source versions.env — would build unpinned" >&2
    fail=1
fi

# 6. Service name and --pull must survive the trip.
if [[ "$VM_SCRIPT" == *"build --pull gateway"* ]]; then
    echo "  OK : service name and --pull are preserved through the VM hop"
else
    echo "  FAIL: remote program lost '--pull' or the service name" >&2
    fail=1
fi

# 7. The build must run from the repo path, or compose resolves no files.
if [[ "$VM_SCRIPT" == *"cd '/repo'"* ]]; then
    echo "  OK : in-VM build runs from \$REPO"
else
    echo "  FAIL: remote program does not cd to \$REPO" >&2
    fail=1
fi

# 8. Detachment is the whole point: the build must outlive its SSH channel, and
#    must record its exit status somewhere the host can read back.
if [[ "$VM_RENDER" == *"nohup "* && "$VM_RENDER" == *"&"* ]]; then
    echo "  OK : the in-VM build is launched detached (nohup, backgrounded)"
else
    echo "  FAIL: in-VM build is not detached — an SSH drop would kill it again" >&2
    fail=1
fi
if [[ "$VM_SCRIPT" == *'echo $? >'* ]]; then
    echo "  OK : the build writes an exit-code sentinel for the host to poll"
else
    echo "  FAIL: no exit-code sentinel — success and failure would be indistinguishable" >&2
    fail=1
fi

# 9. Behavioural: a dropped SSH mid-poll must cost one tick, not the build.
#    The stub fails the first sentinel read outright, then reports success.
DROP_RC=$(/usr/bin/env bash -c '
    eval "$(/usr/bin/sed -n "/^_build_one_service()/,/^}/p" "$1")"
    log() { :; }
    CNT=$(mktemp); echo 0 > "$CNT"
    sed() { cat; }
    colima() {
        case "$*" in
            *"base64 -d"*) return 0 ;;
            *cat*) n=$(cat "$CNT"); n=$((n+1)); echo "$n" > "$CNT"
                   if [ "$n" -le 2 ]; then return 255; fi   # two dropped channels
                   echo 0 ;;
            *) return 0 ;;
        esac
    }
    COMPOSE_CMD="docker-compose"
    REPO="/repo"
    SUNDAY_BUILD_VIA_VM=1
    SUNDAY_BUILD_VM_TIMEOUT=10
    SUNDAY_BUILD_VM_POLL=1
    _build_one_service gateway >/dev/null 2>&1
    echo "rc=$?"
' _ "$APPLY" 2>/dev/null || true)
if [[ "$DROP_RC" == "rc=0" ]]; then
    echo "  OK : two dropped SSH channels mid-build cost a poll tick, not the build"
else
    echo "  FAIL: a dropped SSH during polling still fails the build ($DROP_RC)" >&2
    fail=1
fi

# 10. A build that never finishes must fail loudly rather than be read as success
#     — the exact no-op-reads-as-PASS class CLAUDE.md 0.0 was written for.
TIMEOUT_RC=$(/usr/bin/env bash -c '
    eval "$(/usr/bin/sed -n "/^_build_one_service()/,/^}/p" "$1")"
    log() { :; }
    sed() { cat; }
    colima() { case "$*" in *cat*) return 0 ;; *) return 0 ;; esac; }   # sentinel never appears
    COMPOSE_CMD="docker-compose"
    REPO="/repo"
    SUNDAY_BUILD_VIA_VM=1
    SUNDAY_BUILD_VM_TIMEOUT=2
    SUNDAY_BUILD_VM_POLL=1
    _build_one_service gateway >/dev/null 2>&1
    echo "rc=$?"
' _ "$APPLY" 2>/dev/null || true)
if [[ "$TIMEOUT_RC" != "rc=0" ]]; then
    echo "  OK : a build that never reports an exit code fails, never passes silently"
else
    echo "  FAIL: a never-finishing in-VM build reported success" >&2
    fail=1
fi

# 11. The call site must actually use the helper — the helper existing while the
#     call site still ran $COMPOSE_CMD directly would be a silent no-op.
if /usr/bin/grep -qE '^[[:space:]]*if ! _build_one_service "\$svc"; then' "$APPLY"; then
    echo "  OK : the build call site invokes the helper, not \$COMPOSE_CMD directly"
else
    echo "  FAIL: build call site still bypasses _build_one_service" >&2
    fail=1
fi

echo ""
echo "── upgrade-in-progress guard: health check must not bounce a live build ──"

# On 2026-09-23 the health check bounced Colima ~30 times in one day. A heavy
# build stops the daemon answering the host socket, which IS this script's
# trigger to restart the VM — so the repair kept destroying the very builds the
# upgrade job existed to run (10:20 EDT: in-flight build killed, /tmp wiped,
# exit-code sentinel lost). The guard defers the bounce while a build is alive.
#
# It MUST fail safe: a crashed upgrade cannot be allowed to suppress repair
# forever. These checks execute the real helper against a real lock file.
HCF_GUARD="$REPO/docker/scripts/colima-health-check.sh"
APPLY_GUARD="$REPO/scripts/sunday-upgrade-apply.sh"

_guard_says() {
    # $1 = lock file path, $2 = max age override. Prints DEFER or BOUNCE.
    /usr/bin/env bash -c '
        eval "$(/usr/bin/sed -n "/^_UPGRADE_LOCK=/,/^}/p" "$1")"
        _UPGRADE_LOCK="$2"
        _UPGRADE_LOCK_MAX_AGE="$3"
        if _upgrade_in_progress; then echo DEFER; else echo BOUNCE; fi
    ' _ "$HCF_GUARD" "$1" "$2" 2>/dev/null || echo BOUNCE
}

_GLOCK="$(mktemp)"; rm -f "$_GLOCK"

# 1. No lock at all — ordinary operation, repair must proceed.
if [ "$(_guard_says "$_GLOCK" 300)" = "BOUNCE" ]; then
    echo "  OK : with no upgrade running the socket repair still bounces normally"
else
    echo "  FAIL: guard deferred the repair with no lock present" >&2
    fail=1
fi

# 2. Live PID, fresh heartbeat — this is the case that was destroying builds.
printf '%s\n' "$$" > "$_GLOCK"
if [ "$(_guard_says "$_GLOCK" 300)" = "DEFER" ]; then
    echo "  OK : a live, freshly-stamped upgrade defers the VM bounce"
else
    echo "  FAIL: guard would still bounce Colima during a live build" >&2
    fail=1
fi

# 3. FAIL SAFE — dead PID must not suppress repair.
printf '%s\n' "999999" > "$_GLOCK"
if [ "$(_guard_says "$_GLOCK" 300)" = "BOUNCE" ]; then
    echo "  OK : a dead upgrade PID does not suppress repair (fails safe)"
else
    echo "  FAIL: a stale PID would block socket repair indefinitely" >&2
    fail=1
fi

# 4. FAIL SAFE — a live but hung process that stopped heartbeating must lapse.
printf '%s\n' "$$" > "$_GLOCK"
sleep 1
if [ "$(_guard_says "$_GLOCK" 0)" = "BOUNCE" ]; then
    echo "  OK : a stopped heartbeat lapses the guard even with the PID alive"
else
    echo "  FAIL: a hung upgrade would suppress repair forever" >&2
    fail=1
fi

# 5. Garbage in the lock must not be read as a live upgrade.
printf '%s\n' "not-a-pid" > "$_GLOCK"
if [ "$(_guard_says "$_GLOCK" 300)" = "BOUNCE" ]; then
    echo "  OK : an unparseable lock does not suppress repair"
else
    echo "  FAIL: garbage in the lock file suppressed repair" >&2
    fail=1
fi
rm -f "$_GLOCK"

# 6. The apply script's EXIT trap must actually drop the lock, or every later
#    run would be protected by a lock nobody owns.
_TLOCK="$(mktemp)"
/usr/bin/env bash -c '
    UPGRADE_LOCK="$1"
    eval "$(/usr/bin/grep "^trap " "$2" | head -1)"
    printf "%s\n" "$$" > "$UPGRADE_LOCK"
    exit 0
' _ "$_TLOCK" "$APPLY_GUARD" >/dev/null 2>&1 || true
if [ ! -f "$_TLOCK" ]; then
    echo "  OK : the apply script's EXIT trap removes the lock it took"
else
    echo "  FAIL: the lock outlives the run that took it" >&2
    fail=1
fi
rm -f "$_TLOCK"

# 7. The build poll loop must re-stamp the lock, or a build longer than MAX_AGE
#    would lose its own protection partway through and be bounced.
_HLOCK="$(mktemp)"; rm -f "$_HLOCK"
/usr/bin/env bash -c '
    eval "$(/usr/bin/sed -n "/^_build_one_service()/,/^}/p" "$1")"
    log() { :; }
    sed() { cat; }
    colima() { return 0; }          # sentinel never appears: loop keeps polling
    COMPOSE_CMD="docker-compose"
    REPO="/repo"
    UPGRADE_LOCK="$2"
    SUNDAY_BUILD_VIA_VM=1
    SUNDAY_BUILD_VM_TIMEOUT=2
    SUNDAY_BUILD_VM_POLL=1
    _build_one_service gateway
' _ "$APPLY_GUARD" "$_HLOCK" >/dev/null 2>&1 || true
if [ -f "$_HLOCK" ]; then
    echo "  OK : the build poll loop heartbeats the lock so long builds stay protected"
else
    echo "  FAIL: the lock is never re-stamped — a long build loses its guard" >&2
    fail=1
fi
rm -f "$_HLOCK"

# 8. The guard must actually wrap the bounce. A helper that nothing calls is the
#    same silent no-op class already caught once in this file at the build call
#    site — every check above would pass while the VM still got bounced.
if /usr/bin/grep -qE '^[[:space:]]*if _upgrade_in_progress; then' "$HCF_GUARD"; then
    echo "  OK : the socket-repair block actually consults the guard"
else
    echo "  FAIL: guard helper exists but the bounce does not call it" >&2
    fail=1
fi

echo ""
echo "── docker socket wait: survive a transient forward outage, not a real one ──"

# The host socket is a Lima SSH forward with ControlMaster/ControlPersist and
# NO keepalive (verified 2026-09-23: zero ServerAliveInterval/TCPKeepAlive in
# the generated ssh.config). It dies silently every few minutes; the health
# check repairs it on its 5-minute tick. Failing instantly on that is what made
# this job a coin flip unattended. The wait must NOT turn a real outage into a
# pass — that would be the 0.0 defect class, so it is asserted below.
APPLY_WAIT="$REPO/scripts/sunday-upgrade-apply.sh"

_wait_result() {
    # $1 = number of failed probes before docker comes back (999 = never).
    /usr/bin/env bash -c '
        eval "$(/usr/bin/sed -n "/^_wait_for_docker()/,/^}/p" "$1")"
        log() { echo "LOG: $*"; }
        sleep() { :; }                 # keep the test fast; budget is counted, not slept
        CNT="$(mktemp)"; echo 0 > "$CNT"
        FAILS="$2"
        docker() {
            local n; n=$(cat "$CNT"); n=$((n+1)); echo "$n" > "$CNT"
            [ "$n" -gt "$FAILS" ]      # nonzero (unreachable) until we exceed FAILS
        }
        SUNDAY_DOCKER_WAIT=120
        if _wait_for_docker; then echo "RC=0"; else echo "RC=1"; fi
    ' _ "$APPLY_WAIT" "$1" 2>/dev/null || echo "RC=ERR"
}

# 1. Healthy socket: return immediately, and do not log a wait that never happened.
R_OK="$(_wait_result 0)"
if [ "${R_OK##*$'\n'}" = "RC=0" ] && ! printf '%s' "$R_OK" | /usr/bin/grep -q "waiting for repair"; then
    echo "  OK : a reachable socket returns at once with no spurious wait"
else
    echo "  FAIL: healthy socket did not short-circuit: $(printf '%s' "$R_OK" | tr '\n' ' ')" >&2
    fail=1
fi

# 2. Transient outage that repairs — the case that was killing runs outright.
R_T="$(_wait_result 2)"
if printf '%s' "$R_T" | /usr/bin/grep -q "RC=0" && printf '%s' "$R_T" | /usr/bin/grep -q "recovered after"; then
    echo "  OK : a socket that returns mid-wait is waited out, not failed"
else
    echo "  FAIL: transient outage was not survived: $(printf '%s' "$R_T" | tr '\n' ' ')" >&2
    fail=1
fi

# 3. A REAL outage must still fail. If this ever passes, the gate is decorative.
R_N="$(_wait_result 999)"
if printf '%s' "$R_N" | /usr/bin/grep -q "RC=1"; then
    echo "  OK : a socket that never returns still fails, never passes silently"
else
    echo "  FAIL: a permanently dead socket was reported as success" >&2
    fail=1
fi

# 4. The budget must be finite — an unbounded wait would hang the job forever
#    and is indistinguishable from a hang to anything watching it.
if /usr/bin/grep -qE '^SUNDAY_DOCKER_WAIT="\$\{SUNDAY_DOCKER_WAIT:-[0-9]+\}"' "$APPLY_WAIT"; then
    echo "  OK : the wait is bounded by a finite, overridable budget"
else
    echo "  FAIL: no finite wait budget — the job could hang indefinitely" >&2
    fail=1
fi

# 5/6. Both call sites must actually use it: preflight (before anything runs)
#      and after the build loop (the socket can die while we build in-VM).
if /usr/bin/grep -qE '^[[:space:]]*_wait_for_docker \|\| die 10' "$APPLY_WAIT"; then
    echo "  OK : preflight waits for the socket instead of dying instantly"
else
    echo "  FAIL: preflight still fails immediately on an unreachable socket" >&2
    fail=1
fi
if /usr/bin/grep -qE '_wait_for_docker \|\| \{ err "apply: docker socket did not return after the build"' "$APPLY_WAIT"; then
    echo "  OK : the post-build path re-checks the socket before using it"
else
    echo "  FAIL: nothing re-checks the socket after the in-VM build" >&2
    fail=1
fi

echo ""
echo "── deploy verdicts must follow STATE, not the exit code of the tool ──"

# All four of these are corrections to code shipped earlier the same day, after
# a run that printed "'scripts/asb up hermes' FAILED", "rollback script FAILED"
# and "STACK MAY BE DEGRADED" over a stack that was entirely healthy — three
# false claims from one dead socket. CLAUDE.md 0.0: assert on resulting state.
APPLY_V="$REPO/scripts/sunday-upgrade-apply.sh"

# 1. The wait budget must cover the worst case it exists to survive:
#    300s lock staleness + 300s until the next health-check tick + ~80s bounce.
BUDGET="$(/usr/bin/sed -n 's/^SUNDAY_DOCKER_WAIT="\${SUNDAY_DOCKER_WAIT:-\([0-9]*\)}"/\1/p' "$APPLY_V")"
if [ -n "$BUDGET" ] && [ "$BUDGET" -ge 700 ]; then
    echo "  OK : socket wait budget ${BUDGET}s covers the 680s worst case"
else
    echo "  FAIL: wait budget '${BUDGET}' cannot cover 300+300+80s — a run dies ~2min short" >&2
    fail=1
fi

# 2. Rollback must not call an unreachable daemon a degraded stack.
if /usr/bin/grep -qE 'if ! _wait_for_docker; then' "$APPLY_V" \
   && /usr/bin/grep -q 'rollback NOT attempted, stack state UNKNOWN' "$APPLY_V"; then
    echo "  OK : rollback waits for the daemon and reports UNKNOWN, not damage"
else
    echo "  FAIL: rollback still reports degradation when it merely cannot connect" >&2
    fail=1
fi

# 3. The lock must be released when builds finish, not held to the end of the
#    run — holding it defers the socket repair the very next line waits for.
_REL="$(/usr/bin/awk '/builds complete — released the upgrade lock/{found=1} /_wait_for_docker \|\| \{ err "apply: docker socket did not return/{if(found) print "ORDERED"; exit}' "$APPLY_V")"
if [ "$_REL" = "ORDERED" ]; then
    echo "  OK : the lock is released BEFORE the post-build socket wait"
else
    echo "  FAIL: lock is not released before the post-build wait — self-deadlock" >&2
    fail=1
fi

# 4/5. _container_is_up must judge by state: healthy/none passes, and a
#      container that never runs fails rather than passing on a timeout.
_up_says() {
    /usr/bin/env bash -c '
        eval "$(/usr/bin/sed -n "/^_container_is_up()/,/^}/p" "$1")"
        err() { :; }
        sleep() { :; }
        _ST="$2"; _HL="$3"      # capture: inside docker(), $2/$3 are ITS args
        docker() {
            case "$*" in
                *State.Status*) echo "$_ST" ;;
                *Health*)       echo "$_HL" ;;
            esac
        }
        if _container_is_up c 20; then echo UP; else echo DOWN; fi
    ' _ "$APPLY_V" "$1" "$2" 2>/dev/null || echo DOWN
}
if [ "$(_up_says running healthy)" = "UP" ] && [ "$(_up_says running none)" = "UP" ]; then
    echo "  OK : a running container (healthy, or with no healthcheck) counts as up"
else
    echo "  FAIL: a genuinely running container was not recognised as up" >&2
    fail=1
fi
if [ "$(_up_says absent none)" = "DOWN" ] && [ "$(_up_says running unhealthy)" = "DOWN" ]; then
    echo "  OK : absent and unhealthy containers fail, never pass on timeout"
else
    echo "  FAIL: a container that never came up was reported as up" >&2
    fail=1
fi

# 6. The hermes gate must consult the container, not asb's exit status alone.
if /usr/bin/grep -qE '^[[:space:]]*"\$REPO/scripts/asb" up hermes \|\| asb_rc=\$\?' "$APPLY_V" \
   && /usr/bin/grep -qE '^[[:space:]]*elif ! _container_is_up "\$hermes_c"; then' "$APPLY_V"; then
    echo "  OK : the hermes verdict comes from the container, asb's rc only informs"
else
    echo "  FAIL: hermes is still judged solely by asb's exit code (incl. its prune)" >&2
    fail=1
fi

# 7. A non-zero asb rc with a healthy container must NOT roll back — that is the
#    exact false rollback of 2026-09-23 12:52.
if /usr/bin/grep -q 'treating as deployed. asb'"'"'s status includes its trailing prune' "$APPLY_V"; then
    echo "  OK : a prune-only failure is reported, not escalated to a rollback"
else
    echo "  FAIL: a trailing-prune failure would still trigger a false rollback" >&2
    fail=1
fi

# 8. The container name must be derived per-environment, never hardcoded: dev
#    and prod spell it differently and a hardcoded name silently matches neither.
if /usr/bin/grep -qE '^_hermes_container\(\) \{' "$APPLY_V" \
   && ! /usr/bin/grep -qE '_container_is_up "agentshroud(-dev)?-hermes' "$APPLY_V"; then
    echo "  OK : the hermes container name is derived from CONTAINERS per env"
else
    echo "  FAIL: hermes container name is hardcoded and will miss one environment" >&2
    fail=1
fi

echo ""
echo "── build-cache hygiene: bound growth without weakening rollback ──"

# 2026-09-23: the VM docker volume hit 236G/236G, ZERO bytes free. Build cache
# alone regenerated 57GiB in nine hours across five builds. openclaw's build
# died on ENOSPC, the gateway crashed on sqlite "disk I/O error" and never bound
# :8080, and two containers crash-looped. A weekly job that only ever ADDS disk
# cannot run unattended.
APPLY_C="$REPO/scripts/sunday-upgrade-apply.sh"

# 1. The rollback safety net must not be touched. Rollback restores TAGGED
#    images; `docker builder prune` only ever removes cache. If cleanup ever
#    reaches for `image prune`/`image rm`, the anchors are at risk.
if /usr/bin/grep -qE 'docker builder prune -f --max-used-space' "$APPLY_C" \
   && ! /usr/bin/sed -n '/^_prune_build_cache()/,/^}/p' "$APPLY_C" | /usr/bin/grep -qE 'image (prune|rm)|rmi'; then
    echo "  OK : cleanup prunes build cache only — rollback tags are never touched"
else
    echo "  FAIL: cleanup can remove images — the rollback anchors are at risk" >&2
    fail=1
fi

# 2. Bound, don't empty: --max-used-space keeps incremental builds fast.
if /usr/bin/grep -qE '^SUNDAY_BUILD_CACHE_MAX_GB="\$\{SUNDAY_BUILD_CACHE_MAX_GB:-[0-9]+\}"' "$APPLY_C" \
   && ! /usr/bin/sed -n '/^_prune_build_cache()/,/^}/p' "$APPLY_C" | /usr/bin/grep -qE 'builder prune [^|]*-a'; then
    echo "  OK : the cache is bounded to a budget, not emptied every run"
else
    echo "  FAIL: cleanup empties the cache (or has no budget) — cold builds every week" >&2
    fail=1
fi

# 3. Cleanup must never turn a successful upgrade into a failure.
_CLEAN_RC=$(/usr/bin/env bash -c '
    eval "$(/usr/bin/sed -n "/^_prune_build_cache()/,/^}/p" "$1")"
    log() { :; }; warn() { :; }; _mutating() { return 0; }
    _docker_free_gb() { echo 10; }
    timeout() { return 1; }          # prune fails outright
    SUNDAY_BUILD_CACHE_MAX_GB=20
    _prune_build_cache; echo "rc=$?"
' _ "$APPLY_C" 2>/dev/null || echo "rc=ERR")
if [ "$_CLEAN_RC" = "rc=0" ]; then
    echo "  OK : a failed prune is reported but does not fail the run"
else
    echo "  FAIL: a cleanup failure would fail an otherwise successful upgrade ($_CLEAN_RC)" >&2
    fail=1
fi

# 4/5/6. The pre-build space guard: the preflight disk check runs ONCE, but
#        today's exhaustion happened mid-run, between services.
_SPACE() {
    /usr/bin/env bash -c '
        eval "$(/usr/bin/sed -n "/^_ensure_build_space()/,/^}/p" "$1")"
        eval "$(/usr/bin/sed -n "/^_prune_build_cache()/,/^}/p" "$1")"
        log() { :; }; warn() { :; }; err() { :; }; _mutating() { return 0; }
        CNT="$(mktemp)"; echo 0 > "$CNT"
        _FREE_SEQ="$2"
        _docker_free_gb() {
            local n; n=$(cat "$CNT"); n=$((n+1)); echo "$n" > "$CNT"
            local v; v="$(printf "%s" "$_FREE_SEQ" | cut -d, -f"$n")"
            # An exhausted sequence means the test under-specified the calls;
            # emit a sentinel rather than "" so it fails loudly instead of
            # silently taking the unknown-free-space path.
            [ -n "$v" ] || v=SEQ_EXHAUSTED
            printf "%s" "$v"
        }
        timeout() { return 0; }
        SUNDAY_BUILD_CACHE_MAX_GB=20
        SUNDAY_BUILD_MIN_GB=25
        if _ensure_build_space gateway; then echo GO; else echo STOP; fi
    ' _ "$APPLY_C" "$1" 2>/dev/null || echo STOP
}
if [ "$(_SPACE '90,90')" = "GO" ]; then
    echo "  OK : plenty of space proceeds straight to the build"
else
    echo "  FAIL: the guard blocked a build with ample free space" >&2
    fail=1
fi
if [ "$(_SPACE '5,5,80,80')" = "GO" ]; then
    echo "  OK : low space triggers a prune, and the build proceeds once recovered"
else
    echo "  FAIL: space recovered by pruning did not unblock the build" >&2
    fail=1
fi
if [ "$(_SPACE '5,5,6,6')" = "STOP" ]; then
    echo "  OK : space that pruning cannot recover stops the build BEFORE ENOSPC"
else
    echo "  FAIL: a build would start with no disk — the exact 2026-09-23 failure" >&2
    fail=1
fi

# 7. An unknown free-space reading must not block the run (df can fail while the
#    socket is flaky, and refusing to build then would be a self-inflicted outage).
_UNK=$(/usr/bin/env bash -c '
    eval "$(/usr/bin/sed -n "/^_ensure_build_space()/,/^}/p" "$1")"
    log() { :; }; warn() { :; }; err() { :; }
    _docker_free_gb() { echo ""; }
    SUNDAY_BUILD_MIN_GB=25
    if _ensure_build_space gateway; then echo GO; else echo STOP; fi
' _ "$APPLY_C" 2>/dev/null || echo STOP)
if [ "$_UNK" = "GO" ]; then
    echo "  OK : an unreadable free-space figure does not block the build"
else
    echo "  FAIL: unknown free space blocks builds — a flaky df would stop every run" >&2
    fail=1
fi

# 8/9. Both call sites must exist: guard before each build, bound after the run.
if /usr/bin/grep -qE '^[[:space:]]*if ! _ensure_build_space "\$svc"; then' "$APPLY_C"; then
    echo "  OK : every service build is preceded by the space guard"
else
    echo "  FAIL: builds are not guarded — exhaustion mid-run recurs" >&2
    fail=1
fi
if /usr/bin/awk '/^_prune_build_cache$/{found=1} /^write_handoff PASS$/{if(found) print "ORDERED"; exit}' "$APPLY_C" | /usr/bin/grep -q ORDERED; then
    echo "  OK : the cache is bounded before the run reports PASS"
else
    echo "  FAIL: a successful run leaves its cache growth for the next one" >&2
    fail=1
fi

echo ""
echo "── CVE scan gate: a crashed scanner is not a clean image ──"

# Until 2026-09-23 the trivy call ended in `2>/dev/null || true`, so a crashing
# scanner and a vulnerability-free image produced the IDENTICAL observable: an
# empty string, logged as "trivy returned nothing". Three images were reported
# that way while the real error went unread for weeks:
#   unable to initialize a scan service: ... docker error ...; remote error: UNAUTHORIZED
# trivy reaches local images through the docker socket; when that socket is down
# it falls back to a registry that 401s on local-only tags.
SCANLIB="$REPO/scripts/lib/sunday-scan.sh"

# 1. stderr must never be discarded — without it no failure is diagnosable.
if ! /usr/bin/grep -qE 'format json "\$resolved" 2>/dev/null' "$SCANLIB" \
   && /usr/bin/grep -qE 'format json "\$resolved" 2>"\$errf"' "$SCANLIB"; then
    echo "  OK : trivy stderr is captured, not discarded"
else
    echo "  FAIL: trivy stderr is still thrown away — failures stay undiagnosable" >&2
    fail=1
fi

# 2. A non-zero trivy exit must be counted as a FAILURE, not skipped silently.
if /usr/bin/grep -qE 'failed=\$\(\(failed \+ 1\)\)' "$SCANLIB" \
   && /usr/bin/grep -q 'this is NOT a clean result' "$SCANLIB"; then
    echo "  OK : a scanner error is recorded as a failure, not a clean skip"
else
    echo "  FAIL: a crashed scan is still indistinguishable from a clean one" >&2
    fail=1
fi

# 3. The machine-readable artefact must carry the counts, or a downstream reader
#    (report, handoff, prod promotion) cannot tell a partial scan from a full one.
if /usr/bin/grep -qE '"scanned": %s' "$SCANLIB" && /usr/bin/grep -qE '"failed": %s' "$SCANLIB"; then
    echo "  OK : scan.json records how many images scanned and how many errored"
else
    echo "  FAIL: scan.json cannot express a partial scan — a reader must assume it is complete" >&2
    fail=1
fi

# 4. With a CVE gate requested, an errored scan must HARD FAIL. Reporting a pass
#    on findings the scanner never produced is the 0.0 defect verbatim.
if /usr/bin/grep -qE 'die 20 "CVE gate FAILED: \$\{failed\} image scan\(s\) errored' "$SCANLIB"; then
    echo "  OK : --max-critical + a failed scan is a hard failure, never a pass"
else
    echo "  FAIL: a failed scan could still satisfy an explicit CVE gate" >&2
    fail=1
fi

# 5. Without --max-critical it must still say loudly that this is NOT a baseline.
if /usr/bin/grep -q 'this is NOT a complete CVE baseline' "$SCANLIB"; then
    echo "  OK : a partial scan is labelled as not a CVE baseline"
else
    echo "  FAIL: a partial scan can be read as a complete baseline" >&2
    fail=1
fi

# 6. Behavioural: a scanner that errors must NOT be counted as scanned. Runs the
#    real loop body's accounting against a stubbed failing trivy.
_SCAN_ACC=$(/usr/bin/env bash -c '
    # Source FIRST, then override: the library defines these itself, so stubs
    # declared before the source are silently replaced by the real ones.
    . "$1" 2>/dev/null
    log() { :; }; warn() { :; }; err() { :; }; die() { echo "DIE:$1"; exit 0; }
    sunday_resolve_scan_image() { echo "img:$1"; }
    sunday_ensure_trivy() { return 0; }
    TRIVY_CMD=(false)                 # trivy always exits non-zero
    out="$(mktemp)"
    sunday_run_scan_gate "$out" "" a b 2>/dev/null
    python3 -c "import json,sys;d=json.load(open(sys.argv[1]));print(\"scanned=%s failed=%s\"%(d.get(\"scanned\"),d.get(\"failed\")))" "$out"
' _ "$SCANLIB" 2>/dev/null || echo "ERR")
if [ "$_SCAN_ACC" = "scanned=0 failed=2" ]; then
    echo "  OK : two erroring scans count as 0 scanned / 2 failed, not 0/0"
else
    echo "  FAIL: scan accounting does not distinguish error from absence ($_SCAN_ACC)" >&2
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
