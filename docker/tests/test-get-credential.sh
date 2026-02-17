#!/bin/bash
# TDD tests for get-credential.sh env-var fast-path and error handling
# Run: bash docker/tests/test-get-credential.sh

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GET_CRED="$SCRIPT_DIR/../scripts/get-credential.sh"

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
echo "SK-XXX"         > "$MOCK_SECRETS/1password_bot_secret_key"

# Expand paths now so heredocs embed literal values
REAL_PATH="$MOCK_BIN:$PATH"
REAL_SECRETS="$MOCK_SECRETS"
REAL_HOME="$MOCK_HOME"
REAL_GET_CRED="$GET_CRED"

# Sentinel op: exits 99 to prove op is never called in fast-path tests
cat > "$MOCK_BIN/op" << 'MOCK'
#!/bin/bash
echo "SENTINEL: op was called unexpectedly" >&2
exit 99
MOCK
chmod +x "$MOCK_BIN/op"

# ---------------------------------------------------------------------------
# Test 1: GMAIL_APP_PASSWORD env var fast-path — op must NOT be called
# ---------------------------------------------------------------------------
echo "Test 1: GMAIL_APP_PASSWORD env var fast-path"

result=$(bash --norc << TEST1
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    export GMAIL_APP_PASSWORD="testapppass123"
    bash "$REAL_GET_CRED" gmail-app-password
TEST1
)

if [ "$result" = "testapppass123" ]; then
    pass "GMAIL_APP_PASSWORD fast-path returns env var value without calling op"
else
    fail "GMAIL_APP_PASSWORD fast-path" "output: '$result'"
fi

# ---------------------------------------------------------------------------
# Test 2: GMAIL_USERNAME env var fast-path — op must NOT be called
# ---------------------------------------------------------------------------
echo "Test 2: GMAIL_USERNAME env var fast-path"

result=$(bash --norc << TEST2
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    export GMAIL_USERNAME="testuser@gmail.com"
    bash "$REAL_GET_CRED" gmail-username
TEST2
)

if [ "$result" = "testuser@gmail.com" ]; then
    pass "GMAIL_USERNAME fast-path returns env var value without calling op"
else
    fail "GMAIL_USERNAME fast-path" "output: '$result'"
fi

# Replace sentinel with a failing op for auth-dependent tests
cat > "$MOCK_BIN/op" << 'MOCK'
#!/bin/bash
exit 1
MOCK
chmod +x "$MOCK_BIN/op"

# ---------------------------------------------------------------------------
# Test 3: Unknown credential name → non-zero exit
# ---------------------------------------------------------------------------
echo "Test 3: Unknown credential name -> exit non-zero"
exit_code=0
bash --norc << TEST3 2>/dev/null || exit_code=$?
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    unset GMAIL_APP_PASSWORD GMAIL_USERNAME 2>/dev/null || true
    bash "$REAL_GET_CRED" unknown-credential-name
TEST3

if [ "$exit_code" -ne 0 ]; then
    pass "Unknown credential name exits non-zero"
else
    fail "Unknown credential name exits non-zero" "expected non-zero, got $exit_code"
fi

# ---------------------------------------------------------------------------
# Test 4: Auth failure → exit non-zero with stderr message
# ---------------------------------------------------------------------------
echo "Test 4: Auth failure -> exit non-zero"
exit_code=0
bash --norc << TEST4 2>/dev/null || exit_code=$?
    export PATH="$REAL_PATH"
    export OP_SECRETS_DIR="$REAL_SECRETS"
    export HOME="$REAL_HOME"
    unset GMAIL_APP_PASSWORD GMAIL_USERNAME 2>/dev/null || true
    bash "$REAL_GET_CRED" gmail-totp
TEST4

if [ "$exit_code" -ne 0 ]; then
    pass "Auth failure exits non-zero"
else
    fail "Auth failure exits non-zero" "expected non-zero, got $exit_code"
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
