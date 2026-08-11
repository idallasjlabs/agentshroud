#!/usr/bin/env bash
# tests/startup_smoke/test_setup_secrets.sh
#
# Static assertions on docker/setup-secrets.sh.
# Validates the secrets management script has all required safety features
# without actually invoking any credential backends.
#
# Assertions:
#   SS1.  detect_backend function exists
#   SS2.  read_secret_masked sends display to /dev/tty
#   SS3.  store_secret uses chmod 600 for files
#   SS4.  get_secret cascades all 4 tiers
#   SS5.  generate_gateway_password uses CSPRNG
#   SS6.  normalize_secret extracts last non-empty line
#   SS7.  cmd_extract sets chmod 600
#   SS8.  AGENTSHROUD_SECRET_BACKEND override wired
#   SS9.  secret_matches_bot_filter handles "all"
#   SS10. keychain_store uses dedicated agentshroud.keychain
#   SS11. homedir backend sets chmod 700 on directory
#   SS12. ensure_keychain uses CSPRNG for keychain password
#
# Run: bash tests/startup_smoke/test_setup_secrets.sh
# Exit 0 = pass. Exit 1 = fail.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"

pass=0
fail=0

check() {
    local name="$1" condition="$2" detail="${3:-}"
    if [[ "$condition" == "true" ]]; then
        echo "  PASS: $name"
        ((pass++)) || true
    else
        echo "  FAIL: $name${detail:+ — $detail}"
        ((fail++)) || true
    fi
}

# grep wrapper that returns "true"/"false" string (never exits non-zero)
has() {
    if grep -q "$@" 2>/dev/null; then echo "true"; else echo "false"; fi
}

# grep a section: extract N lines after a pattern then search within
has_in_section() {
    local file="$1" start="$2" lines="$3" pattern="$4"
    if grep -A"$lines" "$start" "$file" 2>/dev/null | grep -q "$pattern" 2>/dev/null; then
        echo "true"
    else
        echo "false"
    fi
}

SRC="$REPO/docker/setup-secrets.sh"

# Bail if file doesn't exist
if [[ ! -f "$SRC" ]]; then
    echo "FAIL: docker/setup-secrets.sh not found"
    exit 1
fi

# SS1: detect_backend function exists
check "SS1: detect_backend function defined" \
    "$(has '^detect_backend()' "$SRC")"

# SS2: read_secret_masked routes display to /dev/tty
check "SS2: read_secret_masked sends prompt to /dev/tty" \
    "$(has_in_section "$SRC" '^read_secret_masked()' 20 '/dev/tty')"

# SS3: store_secret sets chmod 600 on written files
check "SS3: store_secret uses chmod 600 for file-backed secrets" \
    "$(has_in_section "$SRC" '^store_secret()' 25 'chmod 600')"

# SS4a-d: get_secret cascades through all 4 tiers
check "SS4a: get_secret Tier 1 — macOS Keychain" \
    "$(has_in_section "$SRC" '^get_secret()' 40 'keychain_get')"

check "SS4b: get_secret Tier 2 — Linux secret-tool" \
    "$(has_in_section "$SRC" '^get_secret()' 40 'secret-tool lookup')"

check "SS4c: get_secret Tier 3 — 1Password" \
    "$(has_in_section "$SRC" '^get_secret()' 40 'op_get')"

check "SS4d: get_secret Tier 4 — file fallback" \
    "$(has_in_section "$SRC" '^get_secret()' 50 '\.txt')"

# SS5: generate_gateway_password uses Python secrets module (CSPRNG)
check "SS5: generate_gateway_password uses secrets.token_hex (CSPRNG)" \
    "$(has_in_section "$SRC" '^generate_gateway_password()' 3 'secrets.token_hex')"

# SS6: normalize_secret extracts last non-empty line
check "SS6: normalize_secret uses awk to extract last non-empty line" \
    "$(has_in_section "$SRC" '^normalize_secret()' 3 'awk')"

# SS7: cmd_extract sets chmod 600 on extracted secret files
check "SS7: cmd_extract sets chmod 600 on output files" \
    "$(has_in_section "$SRC" '^cmd_extract()' 50 'chmod 600')"

# SS8: AGENTSHROUD_SECRET_BACKEND env var override is respected
check "SS8: AGENTSHROUD_SECRET_BACKEND env override wired" \
    "$(has 'AGENTSHROUD_SECRET_BACKEND' "$SRC")"

# SS9: secret_matches_bot_filter handles "all" filter
check "SS9: secret_matches_bot_filter accepts 'all' filter" \
    "$(has_in_section "$SRC" '^secret_matches_bot_filter()' 5 'all')"

# SS10: keychain_store uses agentshroud.keychain
check "SS10: keychain_store uses dedicated agentshroud.keychain" \
    "$(has 'agentshroud.keychain' "$SRC")"

# SS11: homedir backend enforces chmod 700 on directory
check "SS11: store_secret homedir sets chmod 700 on secrets directory" \
    "$(has_in_section "$SRC" '^store_secret()' 20 'chmod 700')"

# SS12: ensure_keychain generates random password with CSPRNG
check "SS12: ensure_keychain uses secrets.token_hex for keychain password" \
    "$(has_in_section "$SRC" '^ensure_keychain()' 15 'secrets.token_hex')"

echo ""
echo "${pass} assertions: ${pass} passed, ${fail} failed"
echo ""

if [[ "$fail" -gt 0 ]]; then
    echo "  SUITE FAIL: test_setup_secrets.sh"
    exit 1
else
    echo "  SUITE PASS: test_setup_secrets.sh"
    exit 0
fi
