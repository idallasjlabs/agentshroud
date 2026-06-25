#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/smoke.d/test-skills-sync.sh — Smoke test: skills manifest sync is idempotent.
#
# Tests:
#   T1. sync-llm-settings.sh exits 0 when source exists and has content
#   T2. validate-skills-manifest.sh exits 0 after a successful sync
#   T3. Idempotency: second sync run produces no additional file changes
#   T4. sync-llm-settings.sh exits 1 when source directory is missing
#   T5. sync-llm-settings.sh exits 1 when source directory is empty
#   T6. validate-skills-manifest.sh exits 1 after tampering with a deployed file
#
# Uses a temp directory as source and destination — does NOT require ~/.llm_settings
# to exist (safe for CI runners without a real ~/.llm_settings).
#
# Run: bash scripts/smoke.d/test-skills-sync.sh
# Exit 0 = pass. Exit 1 = fail.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"

SYNC_SCRIPT="${REPO}/scripts/sync-llm-settings.sh"
VALIDATE_SCRIPT="${REPO}/scripts/validate-skills-manifest.sh"

pass=0
fail=0

check() {
    local name="$1" condition="$2" detail="${3:-}"
    if [[ "$condition" == "true" ]]; then
        echo "  PASS: $name"
        (( pass++ )) || true
    else
        echo "  FAIL: $name${detail:+ — $detail}"
        (( fail++ )) || true
    fi
}

# ── Build a minimal fake ~/.llm_settings in a temp dir ───────────────────────
TMPROOT="$(mktemp -d)"
trap 'rm -rf "$TMPROOT"' EXIT

FAKE_SOURCE="${TMPROOT}/llm_settings"
mkdir -p "${FAKE_SOURCE}/skills/graphify"
mkdir -p "${FAKE_SOURCE}/mcp"
mkdir -p "${FAKE_SOURCE}/agents"

printf '# Graphify Skill\nConverts codebases to knowledge graphs.\n' \
    > "${FAKE_SOURCE}/skills/graphify/SKILL.md"
printf '{"servers":{}}\n' > "${FAKE_SOURCE}/mcp/servers.json"
printf '# Hermes Soul\nYou are Hermes.\n' > "${FAKE_SOURCE}/agents/hermes-soul.md"

# Override destinations to write into TMPROOT, not the real repo
FAKE_OPENCLAW="${TMPROOT}/openclaw"
FAKE_HERMES="${TMPROOT}/hermes"
mkdir -p "$FAKE_OPENCLAW" "$FAKE_HERMES"

# We need sync-llm-settings.sh to use our fake source AND fake destinations.
# We do this by setting SOURCE via --source and overriding DESTINATIONS by
# temporarily patching via a wrapper that calls the script with modified env.
#
# The script computes REPO from its own location (SCRIPT_DIR/../), so destinations
# will be under the real repo's docker/config/. For smoke tests we use a thin
# wrapper that sources a patched version pointing at our tmp dirs.

_run_sync() {
    local src="$1" oc="$2" hm="$3" extra_args="${4:-}"
    # Inline wrapper: run sync in a subshell with DESTINATIONS overridden
    (
        # shellcheck disable=SC1090
        DESTINATIONS=("$oc" "$hm")
        export DESTINATIONS
        bash "$SYNC_SCRIPT" --source "$src" $extra_args
    )
}

# Actually, sync-llm-settings.sh hardcodes DESTINATIONS from REPO. We need to
# verify sync + validate with the real script logic, so we test with real
# source=FAKE_SOURCE and the real script destinations. We redirect to a patched
# copy for smoke purposes.

# Create a patched copy of the sync script pointing at our temp destinations
PATCHED_SYNC="${TMPROOT}/sync-patched.sh"
sed \
    -e "s|REPO/docker/config/openclaw|FAKE_OPENCLAW_PLACEHOLDER|g" \
    -e "s|REPO/docker/config/hermes|FAKE_HERMES_PLACEHOLDER|g" \
    "$SYNC_SCRIPT" > "$PATCHED_SYNC"

# Replace placeholders with actual temp paths (using python3 for safe substitution)
python3 - "$PATCHED_SYNC" "$FAKE_OPENCLAW" "$FAKE_HERMES" <<'PYEOF'
import sys
with open(sys.argv[1]) as f:
    content = f.read()
content = content.replace(
    '"${REPO}/docker/config/openclaw"',
    '"' + sys.argv[2] + '"'
).replace(
    '"${REPO}/docker/config/hermes"',
    '"' + sys.argv[3] + '"'
)
with open(sys.argv[1], 'w') as f:
    f.write(content)
PYEOF
chmod +x "$PATCHED_SYNC"

# Patched validate script pointing at temp destinations
PATCHED_VALIDATE="${TMPROOT}/validate-patched.sh"
python3 - "$VALIDATE_SCRIPT" "$PATCHED_VALIDATE" "$FAKE_OPENCLAW" "$FAKE_HERMES" <<'PYEOF'
import sys
with open(sys.argv[1]) as f:
    content = f.read()
content = content.replace(
    '"${REPO}/docker/config/openclaw"',
    '"' + sys.argv[3] + '"'
).replace(
    '"${REPO}/docker/config/hermes"',
    '"' + sys.argv[4] + '"'
)
with open(sys.argv[2], 'w') as f:
    f.write(content)
PYEOF
chmod +x "$PATCHED_VALIDATE"

echo ""
echo "=== test-skills-sync.sh ==="
echo ""

# T1: Sync succeeds with valid source
sync_exit=0
bash "$PATCHED_SYNC" --source "$FAKE_SOURCE" > /dev/null 2>&1 || sync_exit=$?
check "T1: sync exits 0 with valid source" "$([ $sync_exit -eq 0 ] && echo true || echo false)" \
    "exit code: $sync_exit"

# T2: validate exits 0 after sync
validate_exit=0
bash "$PATCHED_VALIDATE" --source "$FAKE_SOURCE" > /dev/null 2>&1 || validate_exit=$?
check "T2: validate exits 0 after sync" "$([ $validate_exit -eq 0 ] && echo true || echo false)" \
    "exit code: $validate_exit"

# T3: Idempotency — second sync changes no content files (manifest.json always refreshed)
# Capture content hash of all non-manifest files before second sync
_content_hash_before="$(find "$FAKE_OPENCLAW" "$FAKE_HERMES" \
    -type f \! -name "manifest.json" \
    -exec shasum -a 256 {} + 2>/dev/null | sort | shasum -a 256 | awk '{print $1}')"

bash "$PATCHED_SYNC" --source "$FAKE_SOURCE" > /dev/null 2>&1

_content_hash_after="$(find "$FAKE_OPENCLAW" "$FAKE_HERMES" \
    -type f \! -name "manifest.json" \
    -exec shasum -a 256 {} + 2>/dev/null | sort | shasum -a 256 | awk '{print $1}')"

check "T3: idempotency — second sync does not change content files" \
    "$([ "$_content_hash_before" = "$_content_hash_after" ] && echo true || echo false)" \
    "hashes differ — files were rewritten unnecessarily"

# T4: Sync exits 1 on missing source
missing_source_exit=0
bash "$PATCHED_SYNC" --source "${TMPROOT}/does_not_exist" > /dev/null 2>&1 || missing_source_exit=$?
check "T4: sync exits 1 on missing source" "$([ $missing_source_exit -eq 1 ] && echo true || echo false)" \
    "expected 1, got $missing_source_exit"

# T5: Sync exits 1 on empty source
EMPTY_SOURCE="${TMPROOT}/empty_source"
mkdir -p "$EMPTY_SOURCE"
empty_exit=0
bash "$PATCHED_SYNC" --source "$EMPTY_SOURCE" > /dev/null 2>&1 || empty_exit=$?
check "T5: sync exits 1 on empty source" "$([ $empty_exit -eq 1 ] && echo true || echo false)" \
    "expected 1, got $empty_exit"

# T6: Validate exits 1 after tampering
printf 'TAMPERED\n' >> "${FAKE_OPENCLAW}/skills/graphify/SKILL.md"
tamper_exit=0
bash "$PATCHED_VALIDATE" --source "$FAKE_SOURCE" > /dev/null 2>&1 || tamper_exit=$?
check "T6: validate exits 1 after tamper" "$([ $tamper_exit -eq 1 ] && echo true || echo false)" \
    "expected 1, got $tamper_exit"

# ── Summary ──────────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "  Tests: ${total}  Passed: ${pass}  Failed: ${fail}"
echo ""
[[ "$fail" -eq 0 ]]
