#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/smoke.d/test-sunday-upgrade-scan.sh — Smoke test for the Sunday
# upgrade scan gate (scripts/lib/sunday-scan.sh, sourced by
# scripts/sunday-upgrade-apply.sh's phase_scan).
#
# Regression coverage for the phantom-tag false-pass bug: docker/versions.env
# is bumped (session judgement) before the corresponding image is rebuilt, so
# the scan phase — which runs BEFORE apply/build — used to look for a tag
# that didn't exist yet, skip every image, and still print "scan: PASS" with
# 0 CRITICAL. That's a fake green, not a real CVE baseline.
#
# Strategy: same as test-container-runtime.sh — source the lib in a subshell
# with a fake PATH containing stub docker/trivy/nix executables, so the gate
# can be exercised end-to-end without a real Docker daemon or scanner, and
# without the top-level script's own PATH-hardening shadowing the doubles.
#
# Tests:
#   T1. Pinned tag not built yet, older tag present -> falls back to the
#       older tag, actually scans it, reports a real PASS (not a skip).
#   T2. Trivy missing but `nix` present -> auto-provisions via
#       `nix shell nixpkgs#trivy` and completes a real scan.
#   T3. Trivy missing, no `nix` on PATH, --max-critical set -> dies (existing
#       no-security-theater gate still enforced).
#   T4. Trivy missing, no `nix` on PATH, --max-critical unset -> warns and
#       marks the scan as skipped/absent, never PASS.
#   T5. No image at all for any target (fresh env) -> skipped, never a fake
#       PASS, and --max-critical still gates it.
#   T6. A partial `--phase scan` run must NOT publish a PASS dev->prod handoff
#       (it proves nothing about apply/verify/soak), and must not clobber an
#       existing one.
#
# NOT covered here, deliberately: the positive case (a full `--phase all` run
# DOES publish a PASS handoff). sunday-upgrade-apply.sh hardens its own PATH to
# /opt/homebrew/bin ahead of everything (line 59, on purpose — a launchd PATH
# without Homebrew broke the 2026-09-06 run), so real docker/compose shadow any
# test double, and a genuine --phase all needs a live stack plus a 120s soak.
# That path is covered by the weekly run itself, not by this smoke test.
#
# Run: bash scripts/smoke.d/test-sunday-upgrade-scan.sh
# Exit 0 = pass. Exit 1 = fail.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"
LIB="${REPO}/scripts/lib/sunday-scan.sh"
BASH_BIN="$(command -v bash)"

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

# Args: <bindir> <script-name> <script-body>
write_fake() {
    local bindir="$1" name="$2" body="$3"
    mkdir -p "$bindir"
    printf '#!/usr/bin/env bash\n%s\n' "$body" > "$bindir/$name"
    chmod +x "$bindir/$name"
}

TMPROOT="$(mktemp -d)"
trap 'rm -rf "$TMPROOT"' EXIT

# Run sunday_run_scan_gate in isolation with a controlled PATH: the fake
# bindir goes first (so it shadows any real docker/trivy/nix), followed by
# bare /usr/bin:/bin for coreutils (grep/head/wc/...) the lib needs — neither
# ships trivy or nix, so this can't accidentally leak a real scanner in.
# Args: <bindir> <scan-json-out> <max-critical> <image>...
run_gate() {
    local bindir="$1" scan_json="$2" max_critical="$3"; shift 3
    env -i PATH="$bindir:/usr/bin:/bin" HOME="$HOME" "$BASH_BIN" -c \
        ". '$LIB'; sunday_run_scan_gate '$scan_json' '$max_critical' \"\$@\"" \
        _ "$@"
}

# ── T1: phantom pinned tag falls back to the currently-present tag ─────────
BIN1="$TMPROOT/t1/bin"
# shellcheck disable=SC2016  # single-quoted stub body: $1/$3/$4 expand inside the fake, not here
write_fake "$BIN1" docker '
case "$1" in
  image)
    # Only the OLD tag (1.6.0) exists locally; the pinned 9.9.9 tag does not.
    case "$3" in *:1.6.0) exit 0 ;; *) exit 1 ;; esac ;;
  images)
    repo="${4:-}"
    printf "%s:1.6.0\n" "$repo" ;;
  *) exit 0 ;;
esac
'
# shellcheck disable=SC2016
write_fake "$BIN1" trivy '
case "$1" in
  --version) echo "Version: 0.0.0-fake" ;;
  image) echo "{\"Results\":[{\"Vulnerabilities\":[{\"Severity\":\"HIGH\"}]}]}" ;;
esac
'
JSON1="$TMPROOT/t1/scan.json"
OUT1="$TMPROOT/t1/stdout.log"; ERR1="$TMPROOT/t1/stderr.log"
set +e
run_gate "$BIN1" "$JSON1" "" "agentshroud-gateway:9.9.9" >"$OUT1" 2>"$ERR1"; rc1=$?
set -e
check "T1: falls back to currently-deployed tag instead of skipping" \
    "$([ "$rc1" -eq 0 ] && grep -q '"agentshroud-gateway:1.6.0"' "$JSON1" && ! grep -q '"scanner": "absent"' "$JSON1" && echo true || echo false)" \
    "rc=$rc1 json=$(cat "$JSON1" 2>/dev/null)"
check "T1: scan.json is valid JSON (regression: log() lines used to leak into it)" \
    "$(python3 -c "import json,sys; json.load(open('$JSON1'))" 2>/dev/null && echo true || echo false)" \
    "json=$(cat "$JSON1" 2>/dev/null)"
check "T1: reports a real PASS, not a phantom skip-all" \
    "$(grep -q 'scan: PASS' "$OUT1" && ! grep -q 'no image existed locally for any scan target' "$OUT1" && echo true || echo false)" \
    "stdout=$(cat "$OUT1")"

# ── T2: trivy missing, nix present -> auto-provision and real scan ─────────
BIN2="$TMPROOT/t2/bin"
# shellcheck disable=SC2016
write_fake "$BIN2" docker '
case "$1" in
  image) case "$3" in *:1.6.0) exit 0 ;; *) exit 1 ;; esac ;;
  images) repo="${4:-}"; printf "%s:1.6.0\n" "$repo" ;;
  *) exit 0 ;;
esac
'
# shellcheck disable=SC2016
write_fake "$BIN2" nix '
# nix shell nixpkgs#trivy --command trivy [args...]
shift 4   # shell nixpkgs#trivy --command trivy
exec "'"$BIN2"'/real-trivy" "$@"
'
# shellcheck disable=SC2016
write_fake "$BIN2" real-trivy '
case "$1" in
  --version) echo "Version: 0.0.0-fake" ;;
  image) echo "{\"Results\":[{\"Vulnerabilities\":[]}]}" ;;
esac
'
JSON2="$TMPROOT/t2/scan.json"
OUT2="$TMPROOT/t2/stdout.log"; ERR2="$TMPROOT/t2/stderr.log"
set +e
run_gate "$BIN2" "$JSON2" "" "agentshroud-gateway:9.9.9" >"$OUT2" 2>"$ERR2"; rc2=$?
set -e
check "T2: auto-provisions trivy via nix and completes a real scan" \
    "$([ "$rc2" -eq 0 ] && grep -q "provisioning via 'nix shell nixpkgs#trivy'" "$ERR2" && grep -q 'scan: PASS' "$OUT2" && echo true || echo false)" \
    "rc=$rc2 stderr=$(cat "$ERR2") stdout=$(cat "$OUT2")"
check "T2: scan.json is valid JSON" \
    "$(python3 -c "import json,sys; json.load(open('$JSON2'))" 2>/dev/null && echo true || echo false)" \
    "json=$(cat "$JSON2" 2>/dev/null)"

# ── T3: trivy missing, no nix, --max-critical set -> dies (no fake pass) ───
BIN3="$TMPROOT/t3/bin"; mkdir -p "$BIN3"
JSON3="$TMPROOT/t3/scan.json"
OUT3="$TMPROOT/t3/stdout.log"; ERR3="$TMPROOT/t3/stderr.log"
set +e
run_gate "$BIN3" "$JSON3" "0" "agentshroud-gateway:9.9.9" >"$OUT3" 2>"$ERR3"; rc3=$?
set -e
check "T3: no scanner + gated -> hard failure, not a pass" \
    "$([ "$rc3" -eq 20 ] && echo true || echo false)" \
    "rc=$rc3 stderr=$(cat "$ERR3")"

# ── T4: trivy missing, no nix, ungated -> warns + marks absent, never PASS ─
BIN4="$TMPROOT/t4/bin"; mkdir -p "$BIN4"
JSON4="$TMPROOT/t4/scan.json"
OUT4="$TMPROOT/t4/stdout.log"; ERR4="$TMPROOT/t4/stderr.log"
set +e
run_gate "$BIN4" "$JSON4" "" "agentshroud-gateway:9.9.9" >"$OUT4" 2>"$ERR4"; rc4=$?
set -e
check "T4: no scanner + ungated -> honest skip, never a fake PASS" \
    "$([ "$rc4" -eq 0 ] && grep -q '"scanner": "absent"' "$JSON4" && ! grep -q 'scan: PASS' "$OUT4" && echo true || echo false)" \
    "rc=$rc4 json=$(cat "$JSON4" 2>/dev/null) stdout=$(cat "$OUT4")"

# ── T5: scanner present but no image anywhere -> honest skip, gate enforced ─
BIN5="$TMPROOT/t5/bin"
# shellcheck disable=SC2016
write_fake "$BIN5" docker '
case "$1" in
  image) exit 1 ;;
  images) exit 0 ;;   # no output at all: nothing to fall back to
  *) exit 0 ;;
esac
'
# shellcheck disable=SC2016
write_fake "$BIN5" trivy 'case "$1" in --version) echo ok ;; esac'
JSON5="$TMPROOT/t5/scan.json"
OUT5="$TMPROOT/t5/stdout.log"; ERR5="$TMPROOT/t5/stderr.log"
set +e
run_gate "$BIN5" "$JSON5" "0" "agentshroud-gateway:9.9.9" >"$OUT5" 2>"$ERR5"; rc5=$?
set -e
check "T5: nothing to scan anywhere + gated -> hard failure, not a phantom pass" \
    "$([ "$rc5" -eq 20 ] && echo true || echo false)" \
    "rc=$rc5 stderr=$(cat "$ERR5")"

# ── T6/T7: dev->prod handoff must reflect what actually ran ──────────────────
# These exercise the REAL sunday-upgrade-apply.sh end to end (not just the
# lib), because the bug was in its phase dispatch: `write_handoff PASS` ran
# unconditionally after whatever subset of phases `--phase` selected, so
# `--phase scan` published a gate asserting apply+verify+soak had passed.
# SUNDAY_HANDOFF_DIR keeps that write inside a tmpdir instead of the real
# /Users/Shared gate that prod reads.
APPLY_SH="${REPO}/scripts/sunday-upgrade-apply.sh"

# Build a self-contained fake repo so the script's REPO/BASH_SOURCE resolution,
# versions.env sourcing, and lib sourcing all work without touching the real tree.
make_fake_repo() {
    local root="$1"
    mkdir -p "$root/scripts/lib" "$root/docker"
    cp "$APPLY_SH" "$root/scripts/sunday-upgrade-apply.sh"
    cp "$REPO/scripts/lib/container-runtime.sh" "$root/scripts/lib/"
    cp "$REPO/scripts/lib/sunday-scan.sh"       "$root/scripts/lib/"
    printf 'AGENTSHROUD_VERSION=9.9.9\nOPENCLAW_VERSION=9.9.9\n' > "$root/docker/versions.env"
    : > "$root/docker/docker-compose.yml"
}

# Fake toolchain: compose resolution + scan targets, no real daemon involved.
make_apply_bin() {
    local bindir="$1"
    # shellcheck disable=SC2016
    write_fake "$bindir" docker '
case "$1" in
  image) case "$3" in *:1.6.0) exit 0 ;; *) exit 1 ;; esac ;;
  images) repo="${4:-}"; printf "%s:1.6.0\n" "$repo" ;;
  inspect) exit 1 ;;
  info) exit 0 ;;
  *) exit 0 ;;
esac
'
    # shellcheck disable=SC2016
    write_fake "$bindir" docker-compose '
for a in "$@"; do
  case "$a" in
    -q) exit 0 ;;
    --services) printf "gateway\nhermes\n"; exit 0 ;;
  esac
done
exit 0
'
    # shellcheck disable=SC2016
    write_fake "$bindir" trivy '
case "$1" in
  --version) echo "Version: 0.0.0-fake" ;;
  image) echo "{\"Results\":[{\"Vulnerabilities\":[]}]}" ;;
esac
'
}

# Args: <case-root> <phase> [pre-existing handoff content]
run_apply() {
    local root="$1" phase="$2"
    local bindir="$root/bin" handoff="$root/handoff"
    mkdir -p "$handoff"
    env -i PATH="$bindir:/usr/bin:/bin" HOME="$HOME" USER="${USER:-tester}" \
        SUNDAY_HANDOFF_DIR="$handoff" \
        SUNDAY_CONTAINERS="gateway" \
        SUNDAY_SCAN_IMAGES="agentshroud-gateway:9.9.9" \
        "$BASH_BIN" "$root/scripts/sunday-upgrade-apply.sh" --env dev --phase "$phase"
}

# T6: partial run must not publish PASS, and must leave an existing file alone.
R6="$TMPROOT/t6"; make_fake_repo "$R6"; make_apply_bin "$R6/bin"
mkdir -p "$R6/handoff"
TODAY="$(date +%F)"
printf '{"status":"SENTINEL"}\n' > "$R6/handoff/dev-result-${TODAY}.json"
set +e
run_apply "$R6" scan >"$R6/stdout.log" 2>"$R6/stderr.log"; rc6=$?
set -e
check "T6: --phase scan does not publish a PASS handoff, nor clobber an existing one" \
    "$([ "$rc6" -eq 0 ] && grep -q 'SENTINEL' "$R6/handoff/dev-result-${TODAY}.json" && echo true || echo false)" \
    "rc=$rc6 handoff=$(cat "$R6/handoff/dev-result-${TODAY}.json" 2>/dev/null) stdout=$(tail -5 "$R6/stdout.log" 2>/dev/null)"

# ── Summary ──────────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "  Tests: ${total}  Passed: ${pass}  Failed: ${fail}"
echo ""
[[ "$fail" -eq 0 ]]
