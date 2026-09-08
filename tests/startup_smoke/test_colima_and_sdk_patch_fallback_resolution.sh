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

check "container names are env-overridable and default to the real marvin names" \
    "docker/scripts/colima-health-check.sh" \
    'GATEWAY_CONTAINER="\$\{AGENTSHROUD_GATEWAY_CONTAINER:-agentshroud-marvin-gateway\}"'

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
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
