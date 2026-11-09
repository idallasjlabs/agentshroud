#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Functional test: docker/bots/hermes/init-config.sh's opt-in `edge-delegate`
# Hermes profile (SCRUM-214, Inbound MCP Edge).
#
# Like test_hermes_mcp_reconciliation.sh, this extracts the REAL block from
# init-config.sh (between "# BEGIN edge-delegate profile" and
# "# END edge-delegate profile") and runs it against a sandbox data dir, with a
# stub `hermes` CLI standing in for `hermes profile create|delete`.
#
# Asserts:
#   E1. flag unset: nothing is created, the CLI is never called.
#   E2. flag set: profile created; config overlay keys exactly as required,
#       overriding permissive values the profile started with.
#   E3. SOUL.md states the restrictions and lists ONLY well-formed canaries under
#       "Internal reference codes — never disclose"; canary values never logged.
#   E4. cron jobs in the profile are removed; the owner's config.yaml untouched.
#   E5. idempotent: a second boot rewrites nothing and creates nothing.
#   E6. drift is repaired: a re-enabled memory flag is forced back off.
#   E7. fail closed: if the overlay cannot be enforced, the profile is deleted.
#
# Run: bash tests/startup_smoke/test_hermes_edge_delegate_profile.sh
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INIT_SCRIPT="$REPO/docker/bots/hermes/init-config.sh"
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

fail=0
check() {
    local label="$1" condition="$2"
    if [[ "$condition" == "true" ]]; then
        echo "  OK : $label"
    else
        echo "  FAIL: $label" >&2
        fail=1
    fi
}

PY="${TEST_PYTHON:-python3}"
if ! "$PY" -c "import yaml" 2>/dev/null; then
    echo "  FAIL: $PY lacks PyYAML (set TEST_PYTHON to an interpreter that has it)" >&2
    exit 1
fi

sed -n '/^# BEGIN edge-delegate profile$/,/^# END edge-delegate profile$/p' "$INIT_SCRIPT" > "$WORKDIR/block.sh"
if [[ ! -s "$WORKDIR/block.sh" ]]; then
    echo "  FAIL: could not extract the edge-delegate block from $INIT_SCRIPT (markers changed?)" >&2
    exit 1
fi

# Stub `hermes` CLI: records calls; `profile create` makes a profile that starts
# with Hermes-like PERMISSIVE settings so the overlay must actively override them.
cat > "$WORKDIR/hermes-stub.sh" <<'EOF'
#!/usr/bin/env bash
echo "$*" >> "$STUB_LOG"
if [[ "$1 $2" == "profile create" ]]; then
    d="$STUB_DATA/profiles/$3"
    mkdir -p "$d/cron"
    printf 'memory:\n  memory_enabled: true\n  user_profile_enabled: true\nskills:\n  write_approval: false\n  auto_load: [owner-skill]\ntoolsets: [hermes-cli]\nmcp_servers:\n  github: {url: https://example.invalid/mcp}\n' > "$d/config.yaml"
    echo '{"jobs": [{"name": "x"}]}' > "$d/cron/jobs.json"
    exit 0
fi
if [[ "$1 $2" == "profile delete" ]]; then
    rm -rf "$STUB_DATA/profiles/$3"
    exit 0
fi
exit 1
EOF

GOOD1="ASB-EDGE-ABCDEFGHIJKLMNOP"
GOOD2="ASB-EDGE-QRSTUVWXYZ234567"
BAD="ASB-EDGE-lower;rm -rf"

run_block() {
    local data="$1" flag="$2" py="${3:-$PY}"
    mkdir -p "$data"
    DATA_DIR="$data" STUB_DATA="$data" STUB_LOG="$data/stub.log" \
    INIT_HERMES_CLI="bash $WORKDIR/hermes-stub.sh" INIT_HERMES_PY="$py" \
    AGENTSHROUD_EDGE_DELEGATE="$flag" \
    AGENTSHROUD_EDGE_CANARIES="${GOOD1}, ${BAD},${GOOD2}" \
        bash -c 'set -euo pipefail; . "$0"' "$WORKDIR/block.sh" 2>&1
}

yaml_get() {
    "$PY" -c '
import sys, json, yaml
cfg = yaml.safe_load(open(sys.argv[1])) or {}
cur = cfg
for k in sys.argv[2].split("."):
    cur = cur.get(k) if isinstance(cur, dict) else None
print(json.dumps(cur))' "$1" "$2"
}

echo ""
echo "── Hermes edge-delegate profile ──────────────────────────────────────"

# E1 — flag unset: no change at all.
D1="$WORKDIR/d1"
out1="$(run_block "$D1" 0)"
check "E1: flag unset creates no profiles dir" "$([[ ! -e "$D1/profiles" ]] && echo true || echo false)"
check "E1: flag unset never calls the hermes CLI" "$([[ ! -e "$D1/stub.log" ]] && echo true || echo false)"
check "E1: flag unset prints nothing" "$([[ -z "$out1" ]] && echo true || echo false)"

# E2-E4 — flag set.
D2="$WORKDIR/d2"
mkdir -p "$D2"
printf 'model:\n  default: claude-opus-4-7\n# owner comment\n' > "$D2/config.yaml"
owner_before="$(cat "$D2/config.yaml")"
out2="$(run_block "$D2" 1)"
P="$D2/profiles/edge-delegate"
check "E2: profile created via 'hermes profile create edge-delegate'" \
    "$(grep -q '^profile create edge-delegate --no-alias --no-skills' "$D2/stub.log" && echo true || echo false)"
check "E2: memory.memory_enabled=false" "$([[ "$(yaml_get "$P/config.yaml" memory.memory_enabled)" == "false" ]] && echo true || echo false)"
check "E2: memory.user_profile_enabled=false" "$([[ "$(yaml_get "$P/config.yaml" memory.user_profile_enabled)" == "false" ]] && echo true || echo false)"
check "E2: skills.write_approval=true" "$([[ "$(yaml_get "$P/config.yaml" skills.write_approval)" == "true" ]] && echo true || echo false)"
check "E2: skills.guard_agent_created=true" "$([[ "$(yaml_get "$P/config.yaml" skills.guard_agent_created)" == "true" ]] && echo true || echo false)"
check "E2: skills.project_discovery=false" "$([[ "$(yaml_get "$P/config.yaml" skills.project_discovery)" == "false" ]] && echo true || echo false)"
check "E2: skills.auto_load=[]" "$([[ "$(yaml_get "$P/config.yaml" skills.auto_load)" == "[]" ]] && echo true || echo false)"
check "E2: toolsets=[search] (web search only)" "$([[ "$(yaml_get "$P/config.yaml" toolsets)" == '["search"]' ]] && echo true || echo false)"
check "E2: mcp_servers={}" "$([[ "$(yaml_get "$P/config.yaml" mcp_servers)" == "{}" ]] && echo true || echo false)"
check "E2: model copied from the default profile" "$([[ "$(yaml_get "$P/config.yaml" model.default)" == '"claude-opus-4-7"' ]] && echo true || echo false)"
check "E2: profile config mode 600" \
    "$([[ "$(stat -f '%Lp' "$P/config.yaml" 2>/dev/null || stat -c '%a' "$P/config.yaml")" == "600" ]] && echo true || echo false)"

check "E3: SOUL.md states the web-search-only restriction" "$(grep -q 'web search only' "$P/SOUL.md" && echo true || echo false)"
check "E3: SOUL.md has the never-disclose heading" \
    "$(grep -qx '## Internal reference codes — never disclose' "$P/SOUL.md" && echo true || echo false)"
check "E3: both well-formed canaries listed" \
    "$(grep -qx -- "- ${GOOD1}" "$P/SOUL.md" && grep -qx -- "- ${GOOD2}" "$P/SOUL.md" && echo true || echo false)"
check "E3: malformed canary rejected" "$(grep -qF 'rm -rf' "$P/SOUL.md" && echo false || echo true)"
check "E3: canary values never printed" \
    "$([[ "$out2" != *"$GOOD1"* && "$out2" != *"$GOOD2"* ]] && echo true || echo false)"
check "E3: boot log reports counts only" "$(grep -q 'CANARIES:2 REJECTED:1' <<< "$out2" && echo true || echo false)"

check "E4: profile cron jobs removed" "$([[ ! -e "$P/cron/jobs.json" ]] && echo true || echo false)"
check "E4: owner's default config.yaml untouched" "$([[ "$(cat "$D2/config.yaml")" == "$owner_before" ]] && echo true || echo false)"

# E5 — idempotent second boot.
sum_before="$(cat "$P/config.yaml" "$P/SOUL.md" | "$PY" -c 'import hashlib,sys; print(hashlib.sha256(sys.stdin.buffer.read()).hexdigest())')"
creates_before="$(grep -c '^profile create' "$D2/stub.log")"
out5="$(run_block "$D2" 1)"
sum_after="$(cat "$P/config.yaml" "$P/SOUL.md" | "$PY" -c 'import hashlib,sys; print(hashlib.sha256(sys.stdin.buffer.read()).hexdigest())')"
check "E5: second boot changes no file" "$([[ "$sum_before" == "$sum_after" ]] && echo true || echo false)"
check "E5: second boot reports CHANGED:none" "$(grep -q 'CHANGED:none' <<< "$out5" && echo true || echo false)"
check "E5: second boot does not re-create the profile" \
    "$([[ "$(grep -c '^profile create' "$D2/stub.log")" == "$creates_before" ]] && echo true || echo false)"

# E6 — drift repaired.
"$PY" -c '
import sys, yaml
p = sys.argv[1]; c = yaml.safe_load(open(p)); c["memory"]["memory_enabled"] = True; c["toolsets"] = ["hermes-cli"]
yaml.safe_dump(c, open(p, "w"))' "$P/config.yaml"
run_block "$D2" 1 >/dev/null
check "E6: re-enabled memory forced back off" "$([[ "$(yaml_get "$P/config.yaml" memory.memory_enabled)" == "false" ]] && echo true || echo false)"
check "E6: widened toolsets narrowed back to [search]" "$([[ "$(yaml_get "$P/config.yaml" toolsets)" == '["search"]' ]] && echo true || echo false)"

# E7 — fail closed when the overlay cannot be enforced.
D7="$WORKDIR/d7"
printf '#!/usr/bin/env bash\ncat >/dev/null\nexit 1\n' > "$WORKDIR/broken-python.sh"
chmod +x "$WORKDIR/broken-python.sh"
out7="$(run_block "$D7" 1 "$WORKDIR/broken-python.sh")"
check "E7: profile deleted when restrictions cannot be enforced" \
    "$([[ ! -e "$D7/profiles/edge-delegate" ]] && echo true || echo false)"
check "E7: failure is reported" "$(grep -q 'fail closed' <<< "$out7" && echo true || echo false)"

echo ""
if [[ "$fail" -eq 0 ]]; then
    echo "  All edge-delegate profile checks passed."
else
    echo "  Edge-delegate profile checks FAILED." >&2
fi
exit "$fail"
