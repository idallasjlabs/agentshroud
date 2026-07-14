#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/smoke.d/test-container-runtime.sh — Smoke test for the container-runtime
# detection shim (SCRUM-92: scripts/lib/container-runtime.sh).
#
# Strategy: build a fake PATH containing stub `docker`/`podman`/`docker-compose`/
# `podman-compose` executables so the detection logic can be exercised WITHOUT a
# real container daemon. Each test runs detect_container_runtime in a subshell with a
# controlled PATH + CR_PROBE_CMD and asserts the resolved compose command.
#
# Tests:
#   T1. AGENTSHROUD_COMPOSE override wins over everything.
#   T2. standalone docker-compose is preferred (deploy-host path) even when docker
#       and podman are also present.
#   T3. docker + compose plugin selected when docker-compose binary is absent.
#   T4. podman-compose selected when only podman tooling is present.
#   T5. podman + compose plugin selected when only podman + plugin present.
#   T6. no runtime → non-zero exit + remediation message on stderr.
#   T7. container_runtime_engine maps compose commands to the right engine.
#
# Run: bash scripts/smoke.d/test-container-runtime.sh
# Exit 0 = pass. Exit 1 = fail.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"
SHIM="${REPO}/scripts/lib/container-runtime.sh"

# Absolute path to bash so subshells launch even when we replace PATH with a
# fake-tools-only directory (env -i wipes PATH; bash itself must still resolve).
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

# Build an isolated bin dir with only the requested fake tools on PATH.
# Args: <bindir> <tool>...
make_fake_bin() {
    local bindir="$1"; shift
    mkdir -p "$bindir"
    local tool
    for tool in "$@"; do
        # The stub just exits 0; detection uses `command -v` for binary presence and
        # CR_PROBE_CMD for plugin presence, so the stub body is never relied upon.
        printf '#!/usr/bin/env bash\nexit 0\n' > "${bindir}/${tool}"
        chmod +x "${bindir}/${tool}"
    done
}

# Run detect_container_runtime with a controlled PATH + probe. Echoes result.
# Args: <bindir> <probe_cmd> [override]
run_detect() {
    local bindir="$1" probe="$2" override="${3:-}"
    env -i PATH="$bindir" HOME="$HOME" \
        AGENTSHROUD_COMPOSE="$override" \
        CR_PROBE_CMD="$probe" \
        "$BASH_BIN" -c ". '$SHIM'; detect_container_runtime" 2>/dev/null || true
}

TMPROOT="$(mktemp -d)"
trap 'rm -rf "$TMPROOT"' EXIT

# ── T1: override wins ─────────────────────────────────────────────────────────
BIN1="$TMPROOT/t1"; make_fake_bin "$BIN1" docker-compose docker podman
OUT1="$(run_detect "$BIN1" 'exit 0' 'podman compose -f custom.yml')"
check "T1: AGENTSHROUD_COMPOSE override wins" \
    "$([ "$OUT1" = "podman compose -f custom.yml" ] && echo true || echo false)" \
    "got: '$OUT1'"

# ── T2: docker-compose preferred (deploy-host path) ───────────────────────────
BIN2="$TMPROOT/t2"; make_fake_bin "$BIN2" docker-compose docker podman
OUT2="$(run_detect "$BIN2" 'exit 0')"
check "T2: standalone docker-compose preferred over docker/podman" \
    "$([ "$OUT2" = "docker-compose" ] && echo true || echo false)" \
    "got: '$OUT2'"

# ── T3: docker + plugin when no docker-compose binary ─────────────────────────
BIN3="$TMPROOT/t3"; make_fake_bin "$BIN3" docker
# Probe reports success only for the docker engine. CR_PROBE_ENGINE is expanded
# later inside the shim's probe, so single quotes here are intentional.
# shellcheck disable=SC2016
OUT3="$(run_detect "$BIN3" '[ "$CR_PROBE_ENGINE" = docker ]')"
check "T3: docker + compose plugin selected" \
    "$([ "$OUT3" = "docker compose" ] && echo true || echo false)" \
    "got: '$OUT3'"

# ── T4: podman-compose when only podman tooling ───────────────────────────────
BIN4="$TMPROOT/t4"; make_fake_bin "$BIN4" podman podman-compose
OUT4="$(run_detect "$BIN4" 'exit 1')"
check "T4: podman-compose selected when only podman present" \
    "$([ "$OUT4" = "podman-compose" ] && echo true || echo false)" \
    "got: '$OUT4'"

# ── T5: podman + plugin when only podman + plugin present ─────────────────────
BIN5="$TMPROOT/t5"; make_fake_bin "$BIN5" podman
# shellcheck disable=SC2016
OUT5="$(run_detect "$BIN5" '[ "$CR_PROBE_ENGINE" = podman ]')"
check "T5: podman + compose plugin selected" \
    "$([ "$OUT5" = "podman compose" ] && echo true || echo false)" \
    "got: '$OUT5'"

# ── T6: nothing found → non-zero + remediation on stderr ──────────────────────
BIN6="$TMPROOT/t6"; make_fake_bin "$BIN6" # empty bin, no tools
detect_exit=0
STDERR6="$(env -i PATH="$BIN6" HOME="$HOME" CR_PROBE_CMD='exit 1' \
    "$BASH_BIN" -c ". '$SHIM'; detect_container_runtime" 2>&1 >/dev/null)" || detect_exit=$?
_has_msg="false"
case "$STDERR6" in *"no container runtime found"*) _has_msg="true" ;; esac
check "T6: no runtime → non-zero exit + remediation message" \
    "$([ "$detect_exit" -ne 0 ] && [ "$_has_msg" = "true" ] && echo true || echo false)" \
    "exit=$detect_exit has_msg=$_has_msg"

# ── T7: engine mapping ────────────────────────────────────────────────────────
ENG_DC="$(bash -c ". '$SHIM'; container_runtime_engine 'docker-compose'")"
ENG_DP="$(bash -c ". '$SHIM'; container_runtime_engine 'docker compose'")"
ENG_PC="$(bash -c ". '$SHIM'; container_runtime_engine 'podman-compose'")"
ENG_PP="$(bash -c ". '$SHIM'; container_runtime_engine 'podman compose'")"
check "T7: container_runtime_engine maps engines correctly" \
    "$([ "$ENG_DC" = docker ] && [ "$ENG_DP" = docker ] && \
        [ "$ENG_PC" = podman ] && [ "$ENG_PP" = podman ] && echo true || echo false)" \
    "dc=$ENG_DC dp=$ENG_DP pc=$ENG_PC pp=$ENG_PP"

# ── Summary ──────────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "  Tests: ${total}  Passed: ${pass}  Failed: ${fail}"
echo ""
[[ "$fail" -eq 0 ]]
