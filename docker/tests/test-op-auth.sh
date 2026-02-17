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

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
