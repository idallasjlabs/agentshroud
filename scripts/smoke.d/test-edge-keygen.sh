#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/smoke.d/test-edge-keygen.sh — Smoke test for the Inbound MCP Edge
# secret helpers in docker/setup-secrets.sh (SCRUM-215): `edge-init`
# generation, the single-line "b64:" storage encoding, and extract's
# decode-and-validate step.
#
# Strategy: source setup-secrets.sh (its dispatch is guarded) inside a
# subshell, point SECRETS_DIR / SECRETS_HOME_DIR at a throwaway temp dir and
# replace get_secret/ensure_keychain with temp-dir-backed doubles, so nothing
# touches the real Keychain, secret-tool, 1Password or docker/secrets/.
#
# Tests:
#   T1. edge-init (file backend) generates both secrets, mode 600.
#   T2. edge_signing_key is an EC P-256 PKCS#8 PEM; edge_gateway_token is
#       64 base64 chars (48 random bytes).
#   T3. edge-init prints neither value (nor any PEM armour).
#   T4. edge-init is idempotent: a second run changes nothing.
#   T5. homedir backend stores ONE "b64:" line and reads it back verified.
#   T6. extract decodes a "b64:" value back to the byte-identical PEM.
#   T7. extract refuses an invalid stored key and leaves the file unchanged.
#   T8. a raw (unprefixed) PEM in the backend is accepted as-is.
#
# Run: bash scripts/smoke.d/test-edge-keygen.sh
# Exit 0 = pass. Exit 1 = fail.

# Snippets are single-quoted on purpose and eval'd inside the sourced subshell,
# where the overridden variables and doubled functions are used.
# shellcheck disable=SC2016,SC2034,SC2329
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"
SETUP="${REPO}/docker/setup-secrets.sh"

pass=0
fail=0

check() {
    local name="$1" condition="$2" detail="${3:-}"
    if [[ "$condition" == "true" ]]; then
        echo "  PASS  ${name}"
        pass=$((pass + 1))
    else
        echo "  FAIL  ${name}  ${detail}"
        fail=$((fail + 1))
    fi
}

_mode() {
    stat -f '%Lp' "$1" 2>/dev/null || stat -c '%a' "$1"
}

TMPROOT="$(mktemp -d)"
trap 'rm -rf "$TMPROOT"' EXIT

# Run a snippet with setup-secrets.sh sourced against temp-dir doubles.
# Args: <backend> <snippet>
run_sourced() {
    local backend="$1" snippet="$2"
    (
        # shellcheck disable=SC1090
        . "$SETUP"
        SECRETS_DIR="$TMPROOT/secrets"
        SECRETS_HOME_DIR="$TMPROOT/home-secrets"
        BACKEND="$backend"
        STORE="$TMPROOT/store"
        mkdir -p "$STORE"
        ensure_keychain() { :; }
        keychain_get() { :; }
        # Double for the backend cascade: one file per secret in $STORE, plus
        # the homedir backend's own directory when that backend is selected.
        get_secret() {
            if [[ -s "$STORE/$1" ]]; then cat "$STORE/$1"; return; fi
            if [[ "$BACKEND" == "homedir" && -s "$SECRETS_HOME_DIR/$1.txt" ]]; then
                cat "$SECRETS_HOME_DIR/$1.txt"
            fi
        }
        eval "$snippet"
    )
}

# ── T1-T3: generation ─────────────────────────────────────────────────────────
OUT1="$(run_sourced prompt 'cmd_edge_init' 2>&1)"
KEY="$TMPROOT/secrets/edge_signing_key.txt"
TOK="$TMPROOT/secrets/edge_gateway_token.txt"
check "T1: edge_signing_key generated" "$([[ -s "$KEY" ]] && echo true || echo false)" "$OUT1"
check "T1: edge_gateway_token generated" "$([[ -s "$TOK" ]] && echo true || echo false)" "$OUT1"
check "T1: edge_signing_key mode 600" "$([[ "$(_mode "$KEY")" == "600" ]] && echo true || echo false)" "$(_mode "$KEY")"
check "T1: edge_gateway_token mode 600" "$([[ "$(_mode "$TOK")" == "600" ]] && echo true || echo false)" "$(_mode "$TOK")"

curve="$(openssl pkey -in "$KEY" -pubout 2>/dev/null | openssl pkey -pubin -noout -text 2>/dev/null | grep -Eo 'P-256|prime256v1' | head -1 || true)"
check "T2: key is EC P-256" "$([[ -n "$curve" ]] && echo true || echo false)" "curve='${curve}'"
check "T2: key is unencrypted PKCS#8" \
    "$(head -1 "$KEY" | grep -qx -- '-----BEGIN PRIVATE'' KEY-----' && echo true || echo false)"
tok_len="$(tr -d '\n' < "$TOK" | wc -c | tr -d ' ')"
check "T2: token is 64 base64 chars" \
    "$([[ "$tok_len" == "64" ]] && tr -d '\n' < "$TOK" | grep -Eqx '[A-Za-z0-9+/=]{64}' && echo true || echo false)" "len=${tok_len}"

tok_val="$(tr -d '\n' < "$TOK")"
key_body="$(sed -n 2p "$KEY")"
leaked=false
[[ "$OUT1" == *"$tok_val"* || "$OUT1" == *"$key_body"* || "$OUT1" == *"PRIVATE KEY"* ]] && leaked=true
check "T3: no secret value in edge-init output" "$([[ "$leaked" == false ]] && echo true || echo false)"

# ── T4: idempotent ────────────────────────────────────────────────────────────
key_sum="$(openssl dgst -sha256 < "$KEY")"; tok_sum="$(openssl dgst -sha256 < "$TOK")"
OUT4="$(run_sourced prompt 'cmd_edge_init' 2>&1)"
check "T4: second edge-init reports existing" \
    "$([[ "$(grep -c '\[exists\]' <<< "$OUT4")" == "2" ]] && echo true || echo false)" "$OUT4"
check "T4: files unchanged" \
    "$([[ "$key_sum" == "$(openssl dgst -sha256 < "$KEY")" && "$tok_sum" == "$(openssl dgst -sha256 < "$TOK")" ]] && echo true || echo false)"

# ── T5: homedir backend stores a single verified b64 line ─────────────────────
OUT5="$(run_sourced homedir 'edge_store_from_file edge_signing_key "$SECRETS_DIR/edge_signing_key.txt"' 2>&1)"
stored="$TMPROOT/home-secrets/edge_signing_key.txt"
check "T5: stored and verified" "$(grep -q 'read back and verified' <<< "$OUT5" && echo true || echo false)" "$OUT5"
check "T5: stored value is one b64: line" \
    "$([[ "$(wc -l < "$stored" | tr -d ' ')" == "0" && "$(head -c 4 "$stored")" == "b64:" ]] && echo true || echo false)"
check "T5: homedir file mode 600" "$([[ "$(_mode "$stored")" == "600" ]] && echo true || echo false)" "$(_mode "$stored")"

# ── T6: extract decodes back to the identical PEM ─────────────────────────────
cp "$stored" "$TMPROOT/store/edge_signing_key"
mkdir -p "$TMPROOT/extract"
run_sourced prompt 'SECRETS_DIR="$TMPROOT/extract"; extract_edge_secrets' >/dev/null 2>&1
check "T6: extracted key is byte-identical (modulo trailing newline)" \
    "$([[ "$(cat "$TMPROOT/extract/edge_signing_key.txt")" == "$(cat "$KEY")" ]] && echo true || echo false)"
check "T6: extracted key mode 600" \
    "$([[ "$(_mode "$TMPROOT/extract/edge_signing_key.txt")" == "600" ]] && echo true || echo false)"

# ── T7: invalid stored key is refused, existing file untouched ────────────────
printf 'b64:%s' "$(printf 'not a key' | openssl base64 -A)" > "$TMPROOT/store/edge_signing_key"
before="$(openssl dgst -sha256 < "$TMPROOT/extract/edge_signing_key.txt")"
OUT7="$(run_sourced prompt 'SECRETS_DIR="$TMPROOT/extract"; extract_edge_secrets' 2>&1)"
check "T7: invalid key reported" "$(grep -q '\[invalid\] edge_signing_key' <<< "$OUT7" && echo true || echo false)" "$OUT7"
check "T7: previous key file unchanged" \
    "$([[ "$before" == "$(openssl dgst -sha256 < "$TMPROOT/extract/edge_signing_key.txt")" ]] && echo true || echo false)"

# ── T8: raw PEM accepted ──────────────────────────────────────────────────────
cp "$KEY" "$TMPROOT/store/edge_signing_key"
rm -f "$TMPROOT/extract/edge_signing_key.txt"
run_sourced prompt 'SECRETS_DIR="$TMPROOT/extract"; extract_edge_secrets' >/dev/null 2>&1
check "T8: raw PEM extracted intact" \
    "$([[ "$(cat "$TMPROOT/extract/edge_signing_key.txt" 2>/dev/null)" == "$(cat "$KEY")" ]] && echo true || echo false)"

echo ""
echo "  Tests: $((pass + fail))  Passed: ${pass}  Failed: ${fail}"
[[ "$fail" -eq 0 ]]
