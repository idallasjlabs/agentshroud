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
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
