#!/bin/sh
# security-scheduler.sh — Background scheduling loop (no cron, no root)
# Runs security scans at scheduled UTC times.

set -e

LOG_DIR="/var/log/security"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SCAN_SCRIPT="${SCRIPT_DIR}/security-scan.sh"
REPORT_SCRIPT="${SCRIPT_DIR}/security-report.sh"
FALCO_ALERT_DIR="${FALCO_ALERT_DIR:-/var/log/falco}"
GATEWAY_URL="${GATEWAY_URL:-http://localhost:8080}"

mkdir -p "$LOG_DIR"

log() {
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [scheduler] $*" >> "$LOG_DIR/scheduler.log"
}

# Track what we've run today to avoid duplicate runs
LAST_TRIVY_DATE=""
LAST_CLAMAV_DATE=""
LAST_OSCAP_DATE=""
LAST_REPORT_DATE=""
LAST_FALCO_CHECK=0

log "Security scheduler started"

while true; do
    CURRENT_HOUR=$(date -u +%H)
    CURRENT_DATE=$(date -u +%Y-%m-%d)
    NOW=$(date +%s)

    # Trivy scan at 3 AM UTC
    if [ "$CURRENT_HOUR" = "03" ] && [ "$LAST_TRIVY_DATE" != "$CURRENT_DATE" ]; then
        log "Running scheduled Trivy scan"
        "$SCAN_SCRIPT" --trivy 2>&1 >> "$LOG_DIR/scheduler.log" || log "Trivy scan failed"
        LAST_TRIVY_DATE="$CURRENT_DATE"
    fi

    # ClamAV scan at 4 AM UTC
    if [ "$CURRENT_HOUR" = "04" ] && [ "$LAST_CLAMAV_DATE" != "$CURRENT_DATE" ]; then
        log "Running scheduled ClamAV scan"
        "$SCAN_SCRIPT" --clamav 2>&1 >> "$LOG_DIR/scheduler.log" || log "ClamAV scan failed"
        LAST_CLAMAV_DATE="$CURRENT_DATE"
    fi

    # OpenSCAP scan at 5 AM UTC
    if [ "$CURRENT_HOUR" = "05" ] && [ "$LAST_OSCAP_DATE" != "$CURRENT_DATE" ]; then
        log "Running scheduled OpenSCAP scan"
        "$SCAN_SCRIPT" --oscap 2>&1 >> "$LOG_DIR/scheduler.log" || log "OpenSCAP scan failed"
        LAST_OSCAP_DATE="$CURRENT_DATE"
    fi

    # Health report at 12 PM UTC (6 AM CST)
    if [ "$CURRENT_HOUR" = "12" ] && [ "$LAST_REPORT_DATE" != "$CURRENT_DATE" ]; then
        log "Generating daily health report"
        "$REPORT_SCRIPT" 2>&1 >> "$LOG_DIR/scheduler.log" || log "Report generation failed"
        LAST_REPORT_DATE="$CURRENT_DATE"
    fi

    # Falco alert check every 5 minutes
    ELAPSED=$((NOW - LAST_FALCO_CHECK))
    if [ "$ELAPSED" -ge 300 ]; then
        if [ -d "$FALCO_ALERT_DIR" ]; then
            # Check for new CRITICAL/HIGH alerts
            CRITICAL_ALERTS=$(find "$FALCO_ALERT_DIR" -name "*.json" -newer "$LOG_DIR/.falco_last_check" 2>/dev/null | head -5)
            if [ -n "$CRITICAL_ALERTS" ]; then
                for alert_file in $CRITICAL_ALERTS; do
                    # Look for Emergency/Alert/Critical/Error priority
                    if grep -q '"priority":\s*"\(Emergency\|Alert\|Critical\|Error\)"' "$alert_file" 2>/dev/null; then
                        log "Falco critical alert found in $alert_file"
                        curl -sf -X POST "$GATEWAY_URL/api/alerts" \
                            -H "Content-Type: application/json" \
                            -d "{\"type\":\"security_alert\",\"severity\":\"CRITICAL\",\"tool\":\"falco\",\"message\":\"New Falco alert detected\"}" \
                            2>/dev/null || true
                    fi
                done
            fi
            touch "$LOG_DIR/.falco_last_check"
        fi
        LAST_FALCO_CHECK=$NOW
    fi

    # Sleep 60 seconds between checks
    sleep 60
done
