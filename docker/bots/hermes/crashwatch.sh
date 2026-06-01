#!/command/with-contenv sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud Hermes crash-rate alerting daemon.
# Runs as s6 longrun service (root) inside the Hermes container.
# Reads /opt/data/.start-history (populated by start.sh on every boot) and alerts
# via Telegram when ≥3 restarts occur within the last 3600 seconds.
# Alert cooldown: 1h to prevent notification storms.
#
# State file: /opt/data/.crashwatch-state.json
#   { "last_alert_epoch": <int> }

set -eu

_HISTORY_FILE="/opt/data/.start-history"
_STATE_FILE="/opt/data/.crashwatch-state.json"
_GATEWAY_TELEGRAM_BASE="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}/telegram-api"
_OWNER_CHAT_ID="8096968754"
_ALERT_COOLDOWN=3600      # 1h between alerts
_STORM_THRESHOLD=3        # restarts in the window
_STORM_WINDOW=3600        # 1h rolling window
_TICK=60                  # poll interval

_log() { echo "[crashwatch] $*"; }

_read_last_alert_epoch() {
    if [ -f "${_STATE_FILE}" ]; then
        _epoch="$(jq -r '.last_alert_epoch // 0' "${_STATE_FILE}" 2>/dev/null || echo 0)"
        echo "${_epoch}"
    else
        echo 0
    fi
}

_write_last_alert_epoch() {
    local epoch="$1"
    printf '{"last_alert_epoch":%s}\n' "${epoch}" > "${_STATE_FILE}.tmp" \
        && mv "${_STATE_FILE}.tmp" "${_STATE_FILE}" 2>/dev/null || true
}

_count_recent_restarts() {
    local window_start
    window_start=$(( $(date +%s) - _STORM_WINDOW ))
    if [ ! -f "${_HISTORY_FILE}" ]; then
        echo 0
        return
    fi
    count=0
    while IFS= read -r ts; do
        [ "${ts:-0}" -gt "${window_start}" ] 2>/dev/null && count=$(( count + 1 )) || true
    done < "${_HISTORY_FILE}"
    echo "${count}"
}

_telegram_alert() {
    local text="$1"
    local token="${TELEGRAM_BOT_TOKEN:-}"
    [ -z "$token" ] && return 0
    curl -sf --max-time 10 -X POST \
        "${_GATEWAY_TELEGRAM_BASE}/bot${token}/sendMessage" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -d "{\"chat_id\":\"${_OWNER_CHAT_ID}\",\"text\":\"${text}\"}" \
        >/dev/null 2>&1 || true
}

_log "Crashwatch started (threshold=${_STORM_THRESHOLD} restarts / ${_STORM_WINDOW}s, cooldown=${_ALERT_COOLDOWN}s)"

while true; do
    now="$(date +%s)"
    recent="$(_count_recent_restarts)"
    last_alert="$(_read_last_alert_epoch)"

    if [ "${recent}" -ge "${_STORM_THRESHOLD}" ]; then
        since_last=$(( now - last_alert ))
        if [ "${since_last}" -ge "${_ALERT_COOLDOWN}" ]; then
            latest_iso="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u)"
            msg="🚨 Hermes crash storm: ${recent} restarts in last ${_STORM_WINDOW}s (latest: ${latest_iso})"
            _log "ALERT: ${msg}"
            _telegram_alert "${msg}" && _write_last_alert_epoch "${now}" || true
        else
            _log "Storm detected (${recent} restarts) — alert suppressed (cooldown ${since_last}/${_ALERT_COOLDOWN}s)"
        fi
    fi

    sleep "${_TICK}"
done
