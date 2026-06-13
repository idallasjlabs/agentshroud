#!/usr/bin/env bash
# Smoke test: Hermes Competitive Intelligence Email cron — HTML email assertions.
# Verifies that the cron prompt in jobs.yaml and init-config.sh both include
# the --html flag and --body argument required to deliver HTML email.
# Without --html, the gateway defaults to text/plain and delivers raw markdown.
# Run as part of scripts/smoke.sh.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
fail=0

check() {
    local label="$1" file="$2" pattern="$3"
    if /usr/bin/grep -q "$pattern" "$REPO/$file" 2>/dev/null; then
        echo "  OK : $label"
    else
        echo "  FAIL: $label — pattern '$pattern' not found in $file" >&2
        fail=1
    fi
}

echo ""
echo "── Hermes cron HTML email assertions ──────────────────"

check "jobs.yaml: competitive email message includes --html flag" \
    "docker/config/hermes/cron/jobs.yaml" "\-\-html"

check "jobs.yaml: competitive email message uses --body-file (argv-safe large HTML)" \
    "docker/config/hermes/cron/jobs.yaml" "\-\-body-file /tmp/competitive-email.html"

check "jobs.yaml: competitive email message mentions inline CSS" \
    "docker/config/hermes/cron/jobs.yaml" "inline CSS\|inline styles"

check "init-config.sh: competitive email cron create includes --html" \
    "docker/bots/hermes/init-config.sh" "\-\-html"

check "init-config.sh: competitive email cron create uses --body-file" \
    "docker/bots/hermes/init-config.sh" "\-\-body-file /tmp/competitive-email.html"

check "email_helper.sh: supports --body-file option" \
    "docker/bots/hermes/email_helper.sh" "\-\-body-file"

# Stamp-file gating was removed (PR #148): it caused cron job triplication on
# every version bump. Seeding is now idempotent via delete-then-create.
check "init-config.sh: idempotent _seed_cron helper present (stampless re-seed)" \
    "docker/bots/hermes/init-config.sh" "_seed_cron"

if /usr/bin/grep -q "hermes-cron-seeded" "$REPO/docker/bots/hermes/init-config.sh" 2>/dev/null; then
    echo "  FAIL: stamp-file gating reintroduced — causes cron job triplication (PR #148)" >&2
    fail=1
else
    echo "  OK : no stamp-file gating (idempotent seeding only)"
fi

echo ""
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
