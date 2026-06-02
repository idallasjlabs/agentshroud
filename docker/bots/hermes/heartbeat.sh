#!/command/with-contenv sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud Hermes Healthchecks.io dead-man's-switch heartbeat.
# Runs as s6 longrun service (root) inside the Hermes container.
# Pings HERMES_HEALTHCHECKS_URL every 60s when both internal health gates pass:
#   1. Dashboard port 9119 (HERMES_DASHBOARD=1 service)
#   2. API server port 8642 /health endpoint
#
# If HERMES_HEALTHCHECKS_URL is absent, logs once per hour and noop.
# Heartbeat flows through HTTP_PROXY=gateway:8181 (inherited from compose env).

set -eu

_TICK=60
_URL="${HERMES_HEALTHCHECKS_URL:-}"
_LOG_SUPPRESS_INTERVAL=3600
_last_disabled_log=0

_log() { echo "[heartbeat] $*"; }

_log "Heartbeat started (interval=${_TICK}s)"

while true; do
    if [ -z "${_URL}" ]; then
        now="$(date +%s)"
        since=$(( now - _last_disabled_log ))
        if [ "${since}" -ge "${_LOG_SUPPRESS_INTERVAL}" ]; then
            _log "disabled: HERMES_HEALTHCHECKS_URL not set"
            _last_disabled_log="${now}"
        fi
        sleep "${_TICK}"
        continue
    fi

    dashboard_ok=0
    api_ok=0

    curl -fsS --max-time 5 -o /dev/null http://127.0.0.1:9119/ 2>/dev/null && dashboard_ok=1 || true
    curl -fsS --max-time 5 -o /dev/null http://127.0.0.1:8642/health 2>/dev/null && api_ok=1 || true

    if [ "${dashboard_ok}" -eq 1 ] && [ "${api_ok}" -eq 1 ]; then
        curl -fsS --max-time 10 "${_URL}" -o /dev/null 2>/dev/null \
            && _log "Pinged Healthchecks.io OK" \
            || _log "WARN: Healthchecks.io ping failed (will retry in ${_TICK}s)"
    else
        _log "Health gates not ready (dashboard=${dashboard_ok} api=${api_ok}) — skipping ping"
    fi

    sleep "${_TICK}"
done
