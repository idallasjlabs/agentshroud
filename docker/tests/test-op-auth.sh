#!/bin/bash
# TDD tests for op-auth-common.sh
# Run: bash docker/tests/test-op-auth.sh

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OP_AUTH_COMMON="$SCRIPT_DIR/../scripts/op-auth-common.sh"

PASS=0
FAIL=0

pass() { echo "  PASS: $1"; PASS=$((PASS + 1)); }
fail() { echo "  FAIL: $1"; echo "    $2"; FAIL=$((FAIL + 1)); }

# Temp workspace
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

MOCK_BIN="$TMPDIR/bin"
MOCK_SECRETS="$TMPDIR/secrets"
MOCK_HOME="$TMPDIR/home"
mkdir -p "$MOCK_BIN" "$MOCK_SECRETS" "$MOCK_HOME/.config"

# Write valid Docker secrets
echo "bot@example.com" > "$MOCK_SECRETS/1password_bot_email"
echo "masterpass"      > "$MOCK_SECRETS/1password_bot_master_password"
echo "SK-XXX-YYY"     > "$MOCK_SECRETS/1password_bot_secret_key"

# Expand paths now so heredocs can embed literal values
REAL_PATH="$MOCK_BIN:$PATH"
REAL_SECRETS="$MOCK_SECRETS"
REAL_HOME="$MOCK_HOME"
REAL_COMMON="$OP_AUTH_COMMON"

# Write the shared mock op binary; behavior is selected by MOCK_OP_MODE env var
cat > "$MOCK_BIN/op" << 'MOCKSCRIPT'
#!/bin/bash
mode="${MOCK_OP_MODE:-account-add-success}"
case "$mode" in
    vault-valid)
        # vault list succeeds (existing session valid)
        if [[ "$*" == *"vault list"* ]]; then exit 0; fi
        exit 1
        ;;
    account-add-success)
        # vault list fails (no valid session); account add --raw prints token
        if [[ "$*" == *"vault list"* ]];                          then exit 1; fi
        if [[ "$*" == *"account add"* ]] && [[ "$*" == *"--raw"* ]]; then
            echo "newsession123"
            exit 0
        fi
        exit 1
        ;;
    signin-fallback)
        # account add fails; signin --raw succeeds
        if [[ "$*" == *"vault list"* ]];                          then exit 1; fi
        if [[ "$*" == *"account add"* ]];                         then exit 1; fi
        if [[ "$*" == *"signin"* ]] && [[ "$*" == *"--raw"* ]];  then
            echo "fallbacksession456"
            exit 0
        fi
        exit 1
        ;;
    all-fail)
        exit 1
        ;;
esac
MOCKSCRIPT
chmod +x "$MOCK_BIN/op"

# ---------------------------------------------------------------------------
# Test 1: Reuse existing valid session — op vault list succeeds
# ---------------------------------------------------------------------------
echo "Test 1: Reuse existing valid session"
result=$(bash --norc << TEST1
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    export MOCK_OP_MODE="vault-valid"
    export OP_SESSION_my="existingsession789"
    source "$REAL_COMMON"
    op_authenticate && echo "SESSION=\$OP_SESSION"
TEST1
)

if echo "$result" | grep -q "SESSION=existingsession789"; then
    pass "Reuses existing valid OP_SESSION_my without re-auth"
else
    fail "Reuses existing valid OP_SESSION_my" "output: $result"
fi

# ---------------------------------------------------------------------------
# Test 2: No existing session → op account add --raw succeeds
# ---------------------------------------------------------------------------
echo "Test 2: No session -> account add fallback"
result=$(bash --norc << TEST2
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    export MOCK_OP_MODE="account-add-success"
    unset OP_SESSION_my 2>/dev/null || true
    source "$REAL_COMMON"
    op_authenticate && echo "SESSION=\$OP_SESSION"
TEST2
)

if echo "$result" | grep -q "SESSION=newsession123"; then
    pass "op account add --raw used when no session exists"
else
    fail "op account add --raw fallback" "output: $result"
fi

# ---------------------------------------------------------------------------
# Test 3: Account already added → op signin --raw succeeds
# ---------------------------------------------------------------------------
echo "Test 3: Account add fails -> op signin fallback"
result=$(bash --norc << TEST3
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    export MOCK_OP_MODE="signin-fallback"
    unset OP_SESSION_my 2>/dev/null || true
    source "$REAL_COMMON"
    op_authenticate && echo "SESSION=\$OP_SESSION"
TEST3
)

if echo "$result" | grep -q "SESSION=fallbacksession456"; then
    pass "op signin --raw fallback succeeds when account add fails"
else
    fail "op signin --raw fallback" "output: $result"
fi

# ---------------------------------------------------------------------------
# Test 4: All auth methods fail → op_authenticate returns non-zero
# ---------------------------------------------------------------------------
echo "Test 4: All auth fails -> non-zero exit"
exit_code=0
bash --norc << TEST4 2>/dev/null || exit_code=$?
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    export MOCK_OP_MODE="all-fail"
    unset OP_SESSION_my 2>/dev/null || true
    source "$REAL_COMMON"
    op_authenticate
TEST4

if [ "$exit_code" -ne 0 ]; then
    pass "All auth methods fail returns non-zero exit code"
else
    fail "All auth methods fail returns non-zero" "expected non-zero, got 0"
fi

# ---------------------------------------------------------------------------
# Test 5: Sensitive vars (password, secret_key) are cleared after auth
# ---------------------------------------------------------------------------
echo "Test 5: Sensitive vars cleared after auth"
result=$(bash --norc << TEST5
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    export MOCK_OP_MODE="account-add-success"
    unset OP_SESSION_my 2>/dev/null || true
    source "$REAL_COMMON"
    op_authenticate 2>/dev/null
    # If password or secret_key are still exported, env will show them
    env | grep -E '^(password|secret_key)=' || echo 'CLEARED'
TEST5
)

if echo "$result" | grep -q "CLEARED"; then
    pass "password and secret_key vars cleared after op_authenticate"
else
    fail "Sensitive vars cleared" "env leak: $result"
fi

# ===========================================================================
# Tests 6-9: setup-secrets.sh get_secret() cascade (Keychain → op → file)
# These tests stub both `security` and `op` as PATH shims so they work on
# Linux CI (no real Keychain). The stubs write/read from a temp directory.
# ===========================================================================

SETUP_SECRETS="$(dirname "$SCRIPT_DIR")/setup-secrets.sh"

# Shared stub environment for cascade tests
MOCK_KC_DIR="$TMPDIR/keychain"
mkdir -p "$MOCK_KC_DIR"

# security stub: reads/writes files named <service>__<account> in MOCK_KC_DIR
cat > "$MOCK_BIN/security" << 'SECSTUB'
#!/bin/bash
kc_dir="${MOCK_KC_DIR:-/tmp/mock_kc}"
mkdir -p "$kc_dir"
case "$1" in
    create-keychain|set-keychain-settings|unlock-keychain|list-keychains) exit 0 ;;
    add-generic-password)
        # parse: -s service -a account -w value
        svc="" acc="" val=""
        while [[ $# -gt 0 ]]; do
            case "$1" in -s) svc="$2"; shift 2 ;; -a) acc="$2"; shift 2 ;; -w) val="$2"; shift 2 ;; *) shift ;; esac
        done
        printf '%s' "$val" > "$kc_dir/${svc}__${acc}"
        exit 0 ;;
    find-generic-password)
        svc="" acc=""
        while [[ $# -gt 0 ]]; do
            case "$1" in -s) svc="$2"; shift 2 ;; -a) acc="$2"; shift 2 ;; *) shift ;; esac
        done
        f="$kc_dir/${svc}__${acc}"
        [[ -f "$f" ]] && cat "$f" && exit 0
        exit 44 ;;  # 44 = item not found
    *) exit 0 ;;
esac
SECSTUB
chmod +x "$MOCK_BIN/security"

# ---------------------------------------------------------------------------
# Test 6: Keychain hit wins — op is NOT called when Keychain has the value
# ---------------------------------------------------------------------------
echo "Test 6: Keychain hit — op not called"
# Pre-populate Keychain stub with a value
mkdir -p "$MOCK_KC_DIR"
printf 'keychain_value_42' > "$MOCK_KC_DIR/agentshroud__my_secret"

# op stub that fails hard if called (proves Keychain won before op)
cat > "$MOCK_BIN/op" << 'OPSTUB6'
#!/bin/bash
if [[ "$*" == *"account list"* ]]; then exit 0; fi
echo "OP_WAS_CALLED" >&2
exit 1
OPSTUB6
chmod +x "$MOCK_BIN/op"

result=$(bash --norc << TEST6
    export PATH="$MOCK_BIN:$PATH"
    export AGENTSHROUD_SECRET_BACKEND=keychain
    export MOCK_KC_DIR="$MOCK_KC_DIR"
    export HOME="$REAL_HOME"
    source "$SETUP_SECRETS"
    get_secret my_secret
TEST6
)

if echo "$result" | grep -q "keychain_value_42" && ! echo "$result" | grep -q "OP_WAS_CALLED"; then
    pass "Keychain hit returns value and does not call op"
else
    fail "Keychain hit wins over op" "output: $result"
fi

# ---------------------------------------------------------------------------
# Test 7: Keychain miss → 1Password fallback returns value
# ---------------------------------------------------------------------------
echo "Test 7: Keychain miss → op fallback"
# Remove the Keychain entry so it misses
rm -f "$MOCK_KC_DIR/agentshroud__missing_secret"

# op stub that returns a value for "missing_secret"
cat > "$MOCK_BIN/op" << 'OPSTUB7'
#!/bin/bash
if [[ "$*" == *"account list"* ]]; then echo "my.1password.com"; exit 0; fi
if [[ "$*" == *"item get"* ]]; then
    if [[ "$*" == *"missing_secret"* ]]; then echo "op_fallback_value"; exit 0; fi
fi
exit 1
OPSTUB7
chmod +x "$MOCK_BIN/op"

result=$(bash --norc << TEST7
    export PATH="$MOCK_BIN:$PATH"
    export AGENTSHROUD_SECRET_BACKEND=keychain
    export MOCK_KC_DIR="$MOCK_KC_DIR"
    export HOME="$REAL_HOME"
    source "$SETUP_SECRETS"
    get_secret missing_secret
TEST7
)

if echo "$result" | grep -q "op_fallback_value"; then
    pass "Keychain miss falls back to 1Password and returns value"
else
    fail "Keychain miss → op fallback" "output: $result"
fi

# ---------------------------------------------------------------------------
# Test 8: Both Keychain and op miss → file fallback returns value
# ---------------------------------------------------------------------------
echo "Test 8: Keychain + op miss → file fallback"
rm -f "$MOCK_KC_DIR/agentshroud__file_secret"
mkdir -p "$REAL_HOME/.agentshroud/secrets"
printf 'file_value_99' > "$REAL_HOME/.agentshroud/secrets/file_secret.txt"

cat > "$MOCK_BIN/op" << 'OPSTUB8'
#!/bin/bash
if [[ "$*" == *"account list"* ]]; then exit 1; fi  # op not signed in
exit 1
OPSTUB8
chmod +x "$MOCK_BIN/op"

result=$(bash --norc << TEST8
    export PATH="$MOCK_BIN:$PATH"
    export AGENTSHROUD_SECRET_BACKEND=homedir
    export MOCK_KC_DIR="$MOCK_KC_DIR"
    export HOME="$REAL_HOME"
    source "$SETUP_SECRETS"
    get_secret file_secret
TEST8
)

if echo "$result" | grep -q "file_value_99"; then
    pass "Keychain + op miss falls through to homedir file"
else
    fail "File fallback tier" "output: $result"
fi

# ---------------------------------------------------------------------------
# Test 9: migrate cmd populates Keychain from op for each SECRET_DEFS entry
# ---------------------------------------------------------------------------
echo "Test 9: migrate populates Keychain from op"
rm -rf "$MOCK_KC_DIR"
mkdir -p "$MOCK_KC_DIR"

# op stub that returns a predictable value per secret name
cat > "$MOCK_BIN/op" << 'OPSTUB9'
#!/bin/bash
if [[ "$*" == *"account list"* ]]; then echo "my.1password.com"; exit 0; fi
if [[ "$*" == *"item get"* ]]; then
    # Extract the field name from the last --fields argument
    field=""
    while [[ $# -gt 0 ]]; do
        if [[ "$1" == "--fields" ]]; then field="$2"; fi
        shift
    done
    [[ -n "$field" ]] && echo "migrated_${field}" && exit 0
fi
exit 1
OPSTUB9
chmod +x "$MOCK_BIN/op"

bash --norc << TEST9 2>/dev/null
    export PATH="$MOCK_BIN:$PATH"
    export AGENTSHROUD_SECRET_BACKEND=keychain
    export MOCK_KC_DIR="$MOCK_KC_DIR"
    export HOME="$REAL_HOME"
    source "$SETUP_SECRETS"
    cmd_migrate
TEST9

# Verify that gateway_password was written to the Keychain stub
if [[ -f "$MOCK_KC_DIR/agentshroud__gateway_password" ]]; then
    val=$(cat "$MOCK_KC_DIR/agentshroud__gateway_password")
    if [[ "$val" == migrated_* ]]; then
        pass "migrate wrote gateway_password to Keychain"
    else
        fail "migrate gateway_password value" "got: $val"
    fi
else
    fail "migrate did not write gateway_password to Keychain" "file not found"
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
