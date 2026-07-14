# shellcheck shell=bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/lib/container-runtime.sh — Container-runtime detection shim.
#
# SCRUM-92: multi-platform container support. This is a *sourced* library, not an
# executable. It resolves which container engine + compose form is available on the
# host and exports the result via the `COMPOSE=` convention already used by
# scripts/asb (COMPOSE holds the base command that later gets `-f`/`-p` args appended).
#
# Detection contract (deterministic, first match wins):
#   1. If AGENTSHROUD_COMPOSE is set in the environment, honor it verbatim
#      (escape hatch for exotic hosts / CI — never overridden).
#   2. Else if `docker-compose` (standalone v1/v2 binary) is on PATH → "docker-compose".
#      This is the WORKING path on the deploy hosts (marvin, trillian, rpi) and MUST
#      stay first among auto-detected options so production behavior is unchanged.
#   3. Else if `docker` is on PATH AND `docker compose` (plugin) works → "docker compose".
#   4. Else if `podman-compose` is on PATH → "podman-compose".
#   5. Else if `podman` is on PATH AND `podman compose` works → "podman compose".
#   6. Else → return non-zero and print a clear remediation message.
#
# Public API:
#   detect_container_runtime            → echoes the resolved compose command, exit 0
#                                          on success; exit 1 (message on stderr) if
#                                          no runtime is found.
#   container_runtime_engine <compose>  → echoes the underlying engine ("docker" or
#                                          "podman") for a resolved compose command.
#
# Testability: all detection uses `command -v` and a probe function that can be
# overridden by exporting CR_PROBE_CMD (used by the bash subprocess test to inject a
# fake docker/podman on PATH without invoking a real daemon). No global side effects
# are produced by sourcing this file — callers explicitly invoke the functions.
#
# Usage (in a script):
#   . "$(dirname "$0")/lib/container-runtime.sh"
#   COMPOSE="$(detect_container_runtime)" || exit 1
#   $COMPOSE -f docker/docker-compose.yml -p agentshroud up -d

# Probe whether `<engine> compose` (the plugin subcommand form) is functional.
# Overridable for tests via CR_PROBE_CMD: when set, it is eval'd with the engine name
# as $1 and its exit status is used verbatim (so tests never touch a real daemon).
# Returns 0 if the plugin subcommand is usable, non-zero otherwise.
_cr_plugin_works() {
    local engine="$1"
    if [ -n "${CR_PROBE_CMD:-}" ]; then
        # shellcheck disable=SC2086
        CR_PROBE_ENGINE="$engine" eval "$CR_PROBE_CMD"
        return $?
    fi
    # `<engine> compose version` is cheap and does not require a running daemon for
    # plugin presence detection (it reports the plugin version, not daemon state).
    "$engine" compose version >/dev/null 2>&1
}

# detect_container_runtime — resolve the compose command for this host.
# Echoes the command string on stdout; returns 0 on success, 1 if nothing found.
detect_container_runtime() {
    # 1. Explicit override — highest priority, never second-guessed.
    if [ -n "${AGENTSHROUD_COMPOSE:-}" ]; then
        printf '%s\n' "$AGENTSHROUD_COMPOSE"
        return 0
    fi

    # 2. Standalone docker-compose binary — the working deploy-host path.
    if command -v docker-compose >/dev/null 2>&1; then
        printf '%s\n' "docker-compose"
        return 0
    fi

    # 3. docker CLI + compose plugin.
    if command -v docker >/dev/null 2>&1 && _cr_plugin_works docker; then
        printf '%s\n' "docker compose"
        return 0
    fi

    # 4. Standalone podman-compose binary.
    if command -v podman-compose >/dev/null 2>&1; then
        printf '%s\n' "podman-compose"
        return 0
    fi

    # 5. podman CLI + compose plugin.
    if command -v podman >/dev/null 2>&1 && _cr_plugin_works podman; then
        printf '%s\n' "podman compose"
        return 0
    fi

    # 6. Nothing usable.
    echo "ERROR: no container runtime found. Install one of:" >&2
    echo "  - docker-compose (standalone) + Docker Desktop or Colima" >&2
    echo "  - docker + the compose plugin" >&2
    echo "  - podman-compose, or podman + the compose plugin" >&2
    echo "  Or set AGENTSHROUD_COMPOSE to an explicit compose command." >&2
    return 1
}

# container_runtime_engine — echo the underlying engine name for a compose command.
# Input: the compose command string (e.g. "docker compose", "podman-compose").
# Output: "docker" or "podman" (defaults to "docker" when ambiguous).
container_runtime_engine() {
    local compose="$1"
    case "$compose" in
        podman*) printf '%s\n' "podman" ;;
        *)       printf '%s\n' "docker" ;;
    esac
}
