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
    # SUNDAY_SCAN_RETRY_SLEEP passes through (default empty -> the lib's own
    # 60s-real-world default) so T7/T8 can override it to 0; env -i otherwise
    # wipes it like everything else, which is the correct isolation for every
    # other test here.
    env -i PATH="$bindir:/usr/bin:/bin" HOME="$HOME" \
        SUNDAY_SCAN_RETRY_SLEEP="${SUNDAY_SCAN_RETRY_SLEEP:-}" \
        "$BASH_BIN" -c \
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

# ── T7: transient trivy failure (DB download hiccup) retries and recovers ──
# 2026-10-04 and 2026-10-11 both saw a real scan get 0/3 images scanned, 3
# failed, from a transient vulnerability-DB-download network blip, with no
# retry -- the handoff then published a stale 0-scanned snapshot for the rest
# of the day. This proves the retry loop added to fix that actually retries
# and actually recovers, not just that the counter file mechanics work.
BIN7="$TMPROOT/t7/bin"
# shellcheck disable=SC2016
write_fake "$BIN7" docker '
case "$1" in
  image) case "$3" in *:1.6.0) exit 0 ;; *) exit 1 ;; esac ;;
  images) repo="${4:-}"; printf "%s:1.6.0\n" "$repo" ;;
  *) exit 0 ;;
esac
'
COUNTER7="$TMPROOT/t7/attempts"
echo 0 > "$COUNTER7"
# shellcheck disable=SC2016
write_fake "$BIN7" trivy '
case "$1" in
  --version) echo "Version: 0.0.0-fake" ;;
  image)
    n="$(cat "'"$COUNTER7"'")"
    n=$((n + 1))
    echo "$n" > "'"$COUNTER7"'"
    if [ "$n" -lt 3 ]; then
      echo "FATAL DB error: context deadline exceeded while downloading vulnerability DB" >&2
      exit 1
    fi
    echo "{\"Results\":[{\"Vulnerabilities\":[{\"Severity\":\"HIGH\"}]}]}"
    ;;
esac
'
JSON7="$TMPROOT/t7/scan.json"
OUT7="$TMPROOT/t7/stdout.log"; ERR7="$TMPROOT/t7/stderr.log"
set +e
SUNDAY_SCAN_RETRY_SLEEP=0 run_gate "$BIN7" "$JSON7" "" "agentshroud-gateway:9.9.9" >"$OUT7" 2>"$ERR7"; rc7=$?
set -e
check "T7: retries a transient trivy failure instead of giving up on attempt 1" \
    "$([ "$(cat "$COUNTER7")" -eq 3 ] && echo true || echo false)" \
    "attempts=$(cat "$COUNTER7") stderr=$(cat "$ERR7")"
check "T7: recovers to a real PASS (not a failed scan) once trivy succeeds" \
    "$([ "$rc7" -eq 0 ] && grep -q 'scan: PASS' "$OUT7" && grep -q '"scanned": 1' "$JSON7" && grep -q '"failed": 0' "$JSON7" && echo true || echo false)" \
    "rc=$rc7 json=$(cat "$JSON7" 2>/dev/null) stdout=$(cat "$OUT7")"

# ── T8: trivy fails all 3 attempts -> honest failure, not a false pass ─────
BIN8="$TMPROOT/t8/bin"
# shellcheck disable=SC2016
write_fake "$BIN8" docker '
case "$1" in
  image) case "$3" in *:1.6.0) exit 0 ;; *) exit 1 ;; esac ;;
  images) repo="${4:-}"; printf "%s:1.6.0\n" "$repo" ;;
  *) exit 0 ;;
esac
'
COUNTER8="$TMPROOT/t8/attempts"
echo 0 > "$COUNTER8"
# shellcheck disable=SC2016
write_fake "$BIN8" trivy '
case "$1" in
  --version) echo "Version: 0.0.0-fake" ;;
  image)
    n="$(cat "'"$COUNTER8"'")"
    n=$((n + 1))
    echo "$n" > "'"$COUNTER8"'"
    echo "FATAL DB error: context deadline exceeded while downloading vulnerability DB" >&2
    exit 1
    ;;
esac
'
JSON8="$TMPROOT/t8/scan.json"
OUT8="$TMPROOT/t8/stdout.log"; ERR8="$TMPROOT/t8/stderr.log"
set +e
SUNDAY_SCAN_RETRY_SLEEP=0 run_gate "$BIN8" "$JSON8" "0" "agentshroud-gateway:9.9.9" >"$OUT8" 2>"$ERR8"; rc8=$?
set -e
check "T8: gives up after exactly 3 attempts, does not retry forever" \
    "$([ "$(cat "$COUNTER8")" -eq 3 ] && echo true || echo false)" \
    "attempts=$(cat "$COUNTER8")"
check "T8: persistent failure + gated -> hard failure, never a false pass" \
    "$([ "$rc8" -eq 20 ] && grep -q '"failed": 1' "$JSON8" && ! grep -q 'scan: PASS' "$OUT8" && echo true || echo false)" \
    "rc=$rc8 json=$(cat "$JSON8" 2>/dev/null) stdout=$(cat "$OUT8")"

# ── T9: a run that scanned nothing must not publish PASS (§0.0) ─────────────
# The exact 2026-10-11 dev handoff: status PASS, upgraded:false,
# images_scanned:0, scans_failed:3. Dev only WARNS on scan failure, so the run
# reached `write_handoff PASS` and prod read a green it had no basis for.
# shellcheck disable=SC2016  # expands in the child shell, by design
handoff_status() {
    env -i PATH="/usr/bin:/bin" "$BASH_BIN" -c \
        '. "$1"; shift; sunday_handoff_status "$@"' _ "$LIB" "$@"
}
check "T9: 2026-10-11 shape (0 scanned, 3 failed) is not PASS" \
    "$([ "$(handoff_status PASS 0 3)" = "SCAN_INCOMPLETE" ] && echo true || echo false)" \
    "got=$(handoff_status PASS 0 3)"
check "T9: some images scanned but one failed is not PASS" \
    "$([ "$(handoff_status PASS 2 1)" = "SCAN_INCOMPLETE" ] && echo true || echo false)" \
    "got=$(handoff_status PASS 2 1)"
check "T9: no scan artefact at all (null counts) is not PASS" \
    "$([ "$(handoff_status PASS null null)" = "SCAN_INCOMPLETE" ] && echo true || echo false)" \
    "got=$(handoff_status PASS null null)"
check "T9: a real scan (3 scanned, 0 failed) stays PASS" \
    "$([ "$(handoff_status PASS 3 0)" = "PASS" ] && echo true || echo false)" \
    "got=$(handoff_status PASS 3 0)"
check "T9: a non-PASS status passes through unchanged" \
    "$([ "$(handoff_status FAIL 0 3)" = "FAIL" ] && echo true || echo false)" \
    "got=$(handoff_status FAIL 0 3)"

# ── T10: prod accepts only TODAY's dev handoff, and only a PASS ─────────────
# A dev-result file from an earlier Sunday (dev-result-2026-10-11.json sat in
# the shared dir with status PASS) must never satisfy a later prod run.
# shellcheck disable=SC2016  # expands in the child shell, by design
dev_gate() {
    env -i PATH="/usr/bin:/bin" "$BASH_BIN" -c \
        '. "$1"; shift; sunday_dev_handoff_gate "$@"' _ "$LIB" "$@"
}
H10="$TMPROOT/t10"; mkdir -p "$H10"
T10_TODAY="2026-10-18"
printf '{\n  "date": "2026-10-11",\n  "status": "PASS"\n}\n' > "$H10/dev-result-2026-10-11.json"
set +e
dev_gate "$H10" "$T10_TODAY" >/dev/null 2>&1; rc10a=$?
set -e
check "T10: only last week's PASS present -> prod is blocked" \
    "$([ "$rc10a" -ne 0 ] && echo true || echo false)" "rc=$rc10a"

printf '{\n  "date": "2026-10-11",\n  "status": "PASS"\n}\n' > "$H10/dev-result-${T10_TODAY}.json"
set +e
dev_gate "$H10" "$T10_TODAY" >/dev/null 2>&1; rc10b=$?
set -e
check "T10: today's filename but a stale date inside -> prod is blocked" \
    "$([ "$rc10b" -ne 0 ] && echo true || echo false)" "rc=$rc10b"

for st in FAIL NOTHING_UPGRADED SCAN_INCOMPLETE; do
    printf '{\n  "date": "%s",\n  "status": "%s"\n}\n' "$T10_TODAY" "$st" > "$H10/dev-result-${T10_TODAY}.json"
    set +e
    dev_gate "$H10" "$T10_TODAY" >/dev/null 2>&1; rc10c=$?
    set -e
    check "T10: today's handoff with status ${st} -> prod is blocked" \
        "$([ "$rc10c" -ne 0 ] && echo true || echo false)" "rc=$rc10c"
done

printf '{\n  "date": "%s",\n  "status": "PASS"\n}\n' "$T10_TODAY" > "$H10/dev-result-${T10_TODAY}.json"
set +e
dev_gate "$H10" "$T10_TODAY" >/dev/null 2>&1; rc10d=$?
set -e
check "T10: today's PASS handoff -> prod may proceed" \
    "$([ "$rc10d" -eq 0 ] && echo true || echo false)" "rc=$rc10d"

# ── T11: the apply script actually calls both gates ─────────────────────────
# T9/T10 prove the functions; these prove the wiring. A positive --phase all
# run needs a live stack and a soak (see the header), so the call sites are
# checked statically: the status gate must sit before the final PASS write,
# the dev gate inside phase_apply before the clean-build gate (pre-mutation),
# and the EXIT trap must not overwrite a deliberate status with FAIL.
main_tail="$(sed -n '/^_prune_build_cache$/,$p' "$APPLY_SH")"
check "T11: main derives the handoff status from the scan before writing PASS" \
    "$(printf '%s\n' "$main_tail" | grep -n 'sunday_handoff_status\|^write_handoff PASS' | head -1 | grep -q sunday_handoff_status && echo true || echo false)"
apply_body="$(awk '/^phase_apply\(\) \{/,/Clean-build gate/' "$APPLY_SH")"
check "T11: phase_apply runs sunday_dev_handoff_gate before any build" \
    "$(printf '%s\n' "$apply_body" | grep -q 'sunday_dev_handoff_gate' && echo true || echo false)"
check "T11: EXIT trap leaves a deliberately written handoff alone" \
    "$(grep -E "^trap '.*HANDOFF_WRITTEN.*write_handoff FAIL" "$APPLY_SH" >/dev/null && echo true || echo false)"

# ── T12: wall-clock cutoff (owner directive 2026-10-18: usable by 08:00) ────
# SUNDAY_NOW="<epoch> <HH> <MM> <SS>" pins the clock. 1000000 at 03:00:00 local
# means the 07:20 deadline is 4h20m later.
# shellcheck disable=SC2016  # expands in the child shell, by design
deadline() {
    env -i PATH="/usr/bin:/bin" SUNDAY_NOW="$1" "$BASH_BIN" -c \
        '. "$1"; shift; sunday_deadline_epoch "$@"' _ "$LIB" "$2" 2>/dev/null
}
check "T12: 03:00 launch, 07:20 deadline -> armed 4h20m out" \
    "$([ "$(deadline '1000000 03 00 00' 07:20)" = "$((1000000 + 4*3600 + 20*60))" ] && echo true || echo false)" \
    "got=$(deadline '1000000 03 00 00' 07:20)"
check "T12: leading zeros parse as decimal (08/09 are not octal)" \
    "$([ "$(deadline '1000000 03 08 09' 07:20)" = "$((1000000 + 4*3600 + 12*60 - 9))" ] && echo true || echo false)" \
    "got=$(deadline '1000000 03 08 09' 07:20)"
check "T12: launch after the deadline (an 11:00 retry) -> not armed" \
    "$([ -z "$(deadline '1000000 11 00 00' 07:20)" ] && echo true || echo false)"
check "T12: 'off' disables the cutoff" \
    "$([ -z "$(deadline '1000000 03 00 00' off)" ] && echo true || echo false)"
check "T12: malformed deadline -> not armed (never a cutoff at a guessed time)" \
    "$([ -z "$(deadline '1000000 03 00 00' 7h20)" ] && [ -z "$(deadline '1000000 03 00 00' 25:00)" ] && echo true || echo false)"

# ── T13: restore ladder — check, then start the default stack, then roll back ─
# The hooks are the lib's seams: each stub records its call and passes or fails
# on the Nth check, so every rung is exercised without a live stack.
H13="$TMPROOT/t13"; mkdir -p "$H13"
# shellcheck disable=SC2016  # expands in the child shell, by design
restore() {
    # $1 = which check attempt first passes (0 = never), $2 = rollback script path
    : > "$H13/calls"
    env -i PATH="/usr/bin:/bin" PASS_ON="$1" CALLS="$H13/calls" "$BASH_BIN" -c '
        . "$1"
        n=0
        sunday_stack_check()    { n=$((n + 1)); echo check >> "$CALLS"; [ "$PASS_ON" -ne 0 ] && [ "$n" -ge "$PASS_ON" ]; }
        sunday_stack_start()    { echo start >> "$CALLS"; }
        sunday_stack_rollback() { echo "rollback $1" >> "$CALLS"; }
        sunday_restore_stack "$2"' _ "$LIB" "$2"
}
RB13="$H13/rollback.sh"; printf '#!/bin/sh\n' > "$RB13"
set +e
out13a="$(restore 1 "$RB13" 2>/dev/null)"; rc13a=$?
check "T13: healthy stack -> STACK_OK, nothing restarted or rolled back" \
    "$([ "$rc13a" -eq 0 ] && [ "$out13a" = STACK_OK ] && [ "$(tr '\n' ' ' < "$H13/calls")" = "check " ] && echo true || echo false)" \
    "rc=$rc13a out=$out13a calls=$(tr '\n' ' ' < "$H13/calls")"
out13b="$(restore 2 "$RB13" 2>/dev/null)"; rc13b=$?
check "T13: down stack fixed by starting it -> STACK_RESTARTED, no rollback" \
    "$([ "$rc13b" -eq 0 ] && [ "$out13b" = STACK_RESTARTED ] && [ "$(tr '\n' ' ' < "$H13/calls")" = "check start check " ] && echo true || echo false)" \
    "rc=$rc13b out=$out13b calls=$(tr '\n' ' ' < "$H13/calls")"
out13c="$(restore 3 "$RB13" 2>/dev/null)"; rc13c=$?
check "T13: start does not fix it -> rolls back to the anchor -> STACK_ROLLED_BACK" \
    "$([ "$rc13c" -eq 0 ] && [ "$out13c" = STACK_ROLLED_BACK ] && grep -qx "rollback $RB13" "$H13/calls" && echo true || echo false)" \
    "rc=$rc13c out=$out13c calls=$(tr '\n' ' ' < "$H13/calls")"
out13d="$(restore 0 "$RB13" 2>/dev/null)"; rc13d=$?
check "T13: nothing works -> STACK_DEGRADED and a non-zero exit" \
    "$([ "$rc13d" -ne 0 ] && [ "$out13d" = STACK_DEGRADED ] && echo true || echo false)" \
    "rc=$rc13d out=$out13d"
out13e="$(restore 0 "$H13/missing.sh" 2>/dev/null)"; rc13e=$?
check "T13: no rollback anchor -> STACK_DEGRADED without calling a rollback" \
    "$([ "$rc13e" -ne 0 ] && [ "$out13e" = STACK_DEGRADED ] && ! grep -q rollback "$H13/calls" && echo true || echo false)" \
    "rc=$rc13e out=$out13e calls=$(tr '\n' ' ' < "$H13/calls")"
set -e

# ── T13b: a still-running apply is stopped before the restore touches the stack
L13="$TMPROOT/t13b/apply-running.lock.d"; mkdir -p "$L13"
sleep 300 & SLEEPER=$!
echo "$SLEEPER" > "$L13/pid"
env -i PATH="/usr/bin:/bin" SUNDAY_STOP_WAIT=5 "$BASH_BIN" -c '. "$1"; sunday_stop_apply "$2"' _ "$LIB" "$L13" 2>/dev/null
sleep 1
check "T13b: live apply pid in the lock is stopped" \
    "$(kill -0 "$SLEEPER" 2>/dev/null && echo false || echo true)"
kill "$SLEEPER" 2>/dev/null || true
echo 999999 > "$L13/pid"
set +e
env -i PATH="/usr/bin:/bin" "$BASH_BIN" -c '. "$1"; sunday_stop_apply "$2"' _ "$LIB" "$L13" >/dev/null 2>&1; rc13b=$?
set -e
check "T13b: stale lock (dead pid) -> no-op, exit 0" "$([ "$rc13b" -eq 0 ] && echo true || echo false)"

# ── T14: the wrapper and the deploy check are wired to the above ────────────
WRAP_SH="$REPO/scripts/sunday-upgrade.sh"
PDC_SH="$REPO/scripts/post-deploy-check.sh"
check "T14: wrapper sources the Sunday lib" \
    "$(grep -qE '^\. "\$REPO/scripts/lib/sunday-scan.sh"' "$WRAP_SH" && echo true || echo false)"
check "T14: wrapper arms the wall-clock deadline" \
    "$(grep -q 'sunday_deadline_epoch "\${SUNDAY_UPGRADE_DEADLINE:-07:20}"' "$WRAP_SH" && echo true || echo false)"
wait_loop="$(awk '/^while tmux has-session/,/^done$/' "$WRAP_SH")"
check "T14: the wait loop kills the session at the deadline" \
    "$(printf '%s\n' "$wait_loop" | grep -q 'DEADLINE_EPOCH' && printf '%s\n' "$wait_loop" | grep -q 'CUT_OFF=1' && echo true || echo false)"
wrap_tail="$(sed -n '/^done$/,$p' "$WRAP_SH")"
check "T14: restore runs after the session ends and before the report is staged" \
    "$(printf '%s\n' "$wrap_tail" | grep -n 'sunday_restore_stack\|docker cp "\$STAGED"' | head -1 | grep -q sunday_restore_stack && echo true || echo false)"
check "T14: post-deploy-check has a --functional mode" \
    "$(grep -q -- '--functional' "$PDC_SH" && echo true || echo false)"

# ── T15: direct Telegram notice — reaches the owner when Hermes cannot ──────
# The post seam is stubbed: it records its argv and stdin and answers with a
# canned Bot API response, so no request leaves the machine.
H15="$TMPROOT/t15"; mkdir -p "$H15"
printf 'tok-123:SECRET\n' > "$H15/token"
# shellcheck disable=SC2016  # expands in the child shell, by design
notify() {
    # $1 = canned response, $2 = token file
    : > "$H15/argv"; : > "$H15/stdin"
    env -i PATH="/usr/bin:/bin" RESP="$1" H="$H15" "$BASH_BIN" -c '
        . "$1"
        sunday_telegram_post() { printf "%s\n" "$@" > "$H/argv"; cat > "$H/stdin"; printf "%s" "$RESP"; }
        sunday_notify_direct "$2" 42 "hello owner"' _ "$LIB" "$2"
}
set +e
out15a="$(notify '{"ok":true,"result":{"message_id":7}}' "$H15/token" 2>/dev/null)"; rc15a=$?
check "T15: Bot API accepts the message -> NOTIFY_SENT" \
    "$([ "$rc15a" -eq 0 ] && [ "$out15a" = NOTIFY_SENT ] && echo true || echo false)" "rc=$rc15a out=$out15a"
check "T15: token goes over stdin, never argv (ps shows every user's argv)" \
    "$(! grep -q SECRET "$H15/argv" && grep -q 'bottok-123:SECRET/sendMessage' "$H15/stdin" && grep -qx 'hello owner' "$H15/argv" && echo true || echo false)"
check "T15: the real post reads its URL from stdin (curl -K -)" \
    "$(awk '/^sunday_telegram_post\(\) \{/,/^\}/' "$LIB" | grep -q 'curl .*-K -' && echo true || echo false)"
out15b="$(notify '{"ok":false,"error_code":401}' "$H15/token" 2>/dev/null)"; rc15b=$?
check "T15: Bot API rejects it -> NOTIFY_FAILED, non-zero (a failed send is not a sent one)" \
    "$([ "$rc15b" -ne 0 ] && [ "$out15b" = NOTIFY_FAILED ] && echo true || echo false)" "rc=$rc15b out=$out15b"
out15c="$(notify '' "$H15/token" 2>/dev/null)"; rc15c=$?
check "T15: no response (network down) -> NOTIFY_FAILED" \
    "$([ "$rc15c" -ne 0 ] && [ "$out15c" = NOTIFY_FAILED ] && echo true || echo false)" "rc=$rc15c out=$out15c"
out15d="$(notify '{"ok":true,"result":{"message_id":7}}' "$H15/missing" 2>/dev/null)"; rc15d=$?
check "T15: missing token file -> NOTIFY_NO_TOKEN without calling the API" \
    "$([ "$rc15d" -ne 0 ] && [ "$out15d" = NOTIFY_NO_TOKEN ] && [ ! -s "$H15/stdin" ] && echo true || echo false)" "rc=$rc15d out=$out15d"
set -e

# shellcheck disable=SC2016  # expands in the child shell, by design
summary() {
    env -i PATH="/usr/bin:/bin" "$BASH_BIN" -c '. "$1"; shift; sunday_run_summary "$@"' _ "$LIB" "$@" 2>/dev/null
}
s15="$(summary 7 STACK_DEGRADED 0 1)"
check "T15: summary names the outcome, the stack state, the cutoff and a missing Hermes report" \
    "$(printf '%s' "$s15" | grep -q 'DEGRADED' && printf '%s' "$s15" | grep -q 'STACK_DEGRADED' \
        && printf '%s' "$s15" | grep -q 'cut off' && printf '%s' "$s15" | grep -qi 'not staged' && echo true || echo false)" "got=$s15"
s15b="$(summary 0 STACK_OK 1 0)"
check "T15: a completed run reads as complete, with no cutoff or missing-report line" \
    "$(printf '%s' "$s15b" | grep -q 'complete' && ! printf '%s' "$s15b" | grep -q 'cut off' \
        && ! printf '%s' "$s15b" | grep -qi 'not staged' && echo true || echo false)" "got=$s15b"
s15c="$(summary 3 '' 0 0)"
check "T15: a preflight failure still says what failed (exit 3: git fetch)" \
    "$(printf '%s' "$s15c" | grep -q 'exit 3' && printf '%s' "$s15c" | grep -q 'fetch' && echo true || echo false)" "got=$s15c"

check "T15: wrapper sends the notice from an EXIT trap (covers preflight exits too)" \
    "$(grep -qE '^trap _notify_on_exit EXIT' "$WRAP_SH" && echo true || echo false)"

# ── T16: container names come from the running stack, not prod's literals ───
# Dev's containers are agentshroud-dev-*, so prod's hardcoded names meant dev
# never staged its report for Hermes, its rollback skipped Hermes, and P5
# never ran. A fake docker answers the role-label query and the plain listing.
B16="$TMPROOT/t16/bin"
write_fake "$B16" docker '#!/bin/sh
case "$*" in
  *com.agentshroud.role=hermes*) printf "%s" "$LABELLED" ;;
  ps*) printf "%s" "$NAMES" ;;
esac'
# shellcheck disable=SC2016  # expands in the child shell, by design
hermes_name() {
    env -i PATH="$B16:/usr/bin:/bin" LABELLED="$1" NAMES="$2" "$BASH_BIN" -c \
        '. "$1"; sunday_hermes_container' _ "$LIB" 2>/dev/null
}
check "T16: Hermes found by its com.agentshroud.role label" \
    "$([ "$(hermes_name $'agentshroud-dev-hermes-v2\n' '')" = agentshroud-dev-hermes-v2 ] && echo true || echo false)"
check "T16: unlabelled Hermes found by name, dev or prod" \
    "$([ "$(hermes_name '' $'agentshroud-dev-gateway\nagentshroud-dev-hermes-v2\n')" = agentshroud-dev-hermes-v2 ] \
        && [ "$(hermes_name '' $'agentshroud-hermes-v2\n')" = agentshroud-hermes-v2 ] && echo true || echo false)"
check "T16: no Hermes running -> empty, so the wrapper reports it not staged" \
    "$([ -z "$(hermes_name '' $'agentshroud-dev-gateway\n')" ] && echo true || echo false)"
check "T16: wrapper resolves Hermes at staging time, no hardcoded name" \
    "$(! grep -q '^HERMES_CONTAINER="agentshroud-hermes-v2"' "$WRAP_SH" && grep -q 'HERMES_CONTAINER="$(sunday_hermes_container)"' "$WRAP_SH" && echo true || echo false)"
check "T16: rollback script restores the Hermes snapshot under this host's name" \
    "$(! grep -q 'agentshroud-rollback/agentshroud-hermes-v2' "$APPLY_SH" && grep -q 'agentshroud-rollback/${HERMES_C}' "$APPLY_SH" && echo true || echo false)"
check "T16: P5 finds the gateway by compose service label, not prod's name" \
    "$(! grep -q "grep -q '^agentshroud-gateway\$'" "$PDC_SH" && awk '/── P5/,/── P6|── F|Summary/' "$PDC_SH" | grep -q 'com.docker.compose.service=gateway' && echo true || echo false)"
check "T15: the two 'nothing to do' skips do not send a notice" \
    "$(grep -A2 'already running — skipping' "$WRAP_SH" | grep -q 'NOTIFY_ON_EXIT=0' \
        && grep -A2 'run already completed today' "$WRAP_SH" | grep -q 'NOTIFY_ON_EXIT=0' && echo true || echo false)"

# ── Summary ──────────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "  Tests: ${total}  Passed: ${pass}  Failed: ${fail}"
echo ""
[[ "$fail" -eq 0 ]]
