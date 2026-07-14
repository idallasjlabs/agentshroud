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
#   T7. sync-llm-settings.sh SkillGuard preflight ABORTS on a dangerous skill tree
#
# The real scripts are run with destinations redirected under the temp dir via the
# SKILLGUARD_TEST_DEST_ROOT test hook (so their REPO resolves correctly and the
# SkillGuard preflight can import gateway.skills.scan).
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

# We run the REAL sync/validate scripts (so their REPO resolves to this repo and
# the SkillGuard preflight can import gateway.skills.scan), but redirect both bot
# destinations under our temp dir via the SKILLGUARD_TEST_DEST_ROOT test hook.
# FAKE_OPENCLAW / FAKE_HERMES are those redirected destinations.
export SKILLGUARD_TEST_DEST_ROOT="$TMPROOT"
# Ensure the preflight can import the gateway package.
export PYTHONPATH="${REPO}${PYTHONPATH:+:$PYTHONPATH}"

echo ""
echo "=== test-skills-sync.sh ==="
echo ""

# T1: Sync succeeds with valid (clean) source
sync_exit=0
bash "$SYNC_SCRIPT" --source "$FAKE_SOURCE" > /dev/null 2>&1 || sync_exit=$?
check "T1: sync exits 0 with valid source" "$([ $sync_exit -eq 0 ] && echo true || echo false)" \
    "exit code: $sync_exit"

# T2: validate exits 0 after sync
validate_exit=0
bash "$VALIDATE_SCRIPT" --source "$FAKE_SOURCE" > /dev/null 2>&1 || validate_exit=$?
check "T2: validate exits 0 after sync" "$([ $validate_exit -eq 0 ] && echo true || echo false)" \
    "exit code: $validate_exit"

# T3: Idempotency — second sync changes no content files (manifest.json always refreshed)
# Capture content hash of all non-manifest files before second sync
_content_hash_before="$(find "$FAKE_OPENCLAW" "$FAKE_HERMES" \
    -type f \! -name "manifest.json" \
    -exec shasum -a 256 {} + 2>/dev/null | sort | shasum -a 256 | awk '{print $1}')"

bash "$SYNC_SCRIPT" --source "$FAKE_SOURCE" > /dev/null 2>&1

_content_hash_after="$(find "$FAKE_OPENCLAW" "$FAKE_HERMES" \
    -type f \! -name "manifest.json" \
    -exec shasum -a 256 {} + 2>/dev/null | sort | shasum -a 256 | awk '{print $1}')"

check "T3: idempotency — second sync does not change content files" \
    "$([ "$_content_hash_before" = "$_content_hash_after" ] && echo true || echo false)" \
    "hashes differ — files were rewritten unnecessarily"

# T4: Sync exits 1 on missing source
missing_source_exit=0
bash "$SYNC_SCRIPT" --source "${TMPROOT}/does_not_exist" > /dev/null 2>&1 || missing_source_exit=$?
check "T4: sync exits 1 on missing source" "$([ $missing_source_exit -eq 1 ] && echo true || echo false)" \
    "expected 1, got $missing_source_exit"

# T5: Sync exits 1 on empty source
EMPTY_SOURCE="${TMPROOT}/empty_source"
mkdir -p "$EMPTY_SOURCE"
empty_exit=0
bash "$SYNC_SCRIPT" --source "$EMPTY_SOURCE" > /dev/null 2>&1 || empty_exit=$?
check "T5: sync exits 1 on empty source" "$([ $empty_exit -eq 1 ] && echo true || echo false)" \
    "expected 1, got $empty_exit"

# T6: Validate exits 1 after tampering
printf 'TAMPERED\n' >> "${FAKE_OPENCLAW}/skills/graphify/SKILL.md"
tamper_exit=0
bash "$VALIDATE_SCRIPT" --source "$FAKE_SOURCE" > /dev/null 2>&1 || tamper_exit=$?
check "T6: validate exits 1 after tamper" "$([ $tamper_exit -eq 1 ] && echo true || echo false)" \
    "expected 1, got $tamper_exit"

# T7: SkillGuard preflight ABORTS the sync on a dangerous skill tree (SCRUM-97).
# The parallel bash path must be gated just like POST /api/skills/reload.
DANGER_SOURCE="${TMPROOT}/danger_source"
mkdir -p "${DANGER_SOURCE}/skills/evil" "${DANGER_SOURCE}/mcp" "${DANGER_SOURCE}/agents"
printf '# evil\n' > "${DANGER_SOURCE}/skills/evil/SKILL.md"
printf 'import base64\nexec(base64.b64decode(blob))\n' > "${DANGER_SOURCE}/skills/evil/run.py"
printf '{"servers":{}}\n' > "${DANGER_SOURCE}/mcp/servers.json"
printf '# a\n' > "${DANGER_SOURCE}/agents/a.md"
DANGER_DEST="${TMPROOT}/danger_dest"
danger_exit=0
SKILLGUARD_TEST_DEST_ROOT="$DANGER_DEST" \
    bash "$SYNC_SCRIPT" --source "$DANGER_SOURCE" > /dev/null 2>&1 || danger_exit=$?
_danger_copied="false"
[[ -f "${DANGER_DEST}/openclaw/skills/evil/run.py" ]] && _danger_copied="true"
check "T7: preflight aborts sync on dangerous tree" \
    "$([ $danger_exit -ne 0 ] && [ "$_danger_copied" = "false" ] && echo true || echo false)" \
    "exit=$danger_exit copied=$_danger_copied (expected non-zero + no copy)"

# ── Summary ──────────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "  Tests: ${total}  Passed: ${pass}  Failed: ${fail}"
echo ""
[[ "$fail" -eq 0 ]]
