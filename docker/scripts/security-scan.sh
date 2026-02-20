#!/bin/sh
# security-scan.sh — Unified scan dispatcher
# Usage: security-scan.sh [--trivy] [--clamav] [--oscap] [--all]

set -e

LOG_DIR="/var/log/security"
GATEWAY_URL="${GATEWAY_URL:-http://localhost:8080}"
TIMESTAMP=$(date -u +%Y%m%d-%H%M%S)
WORKSPACE="${AGENTSHROUD_WORKSPACE:-/home/node}"

mkdir -p "$LOG_DIR"/{trivy,clamav,oscap}

log() {
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [scan] $*"
}

alert_if_critical() {
    local tool="$1" message="$2"
    log "ALERT: $tool — $message"
    curl -sf -X POST "$GATEWAY_URL/api/alerts" \
        -H "Content-Type: application/json" \
        -d "{\"type\":\"security_alert\",\"severity\":\"CRITICAL\",\"tool\":\"$tool\",\"message\":\"$message\",\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}" \
        2>/dev/null || log "Failed to POST alert to gateway"
}

run_trivy() {
    log "Starting Trivy scan..."
    if ! command -v trivy >/dev/null 2>&1; then
        log "ERROR: trivy not found"
        return 1
    fi

    trivy fs --format json --severity CRITICAL,HIGH,MEDIUM,LOW --no-progress / \
        > "$LOG_DIR/trivy/trivy-$TIMESTAMP.json" 2>"$LOG_DIR/trivy/trivy-$TIMESTAMP.err" || true

    CRITICAL=$(python3 -c "
import json, sys
try:
    d = json.load(open('$LOG_DIR/trivy/trivy-$TIMESTAMP.json'))
    print(sum(1 for r in d.get('Results', []) for v in r.get('Vulnerabilities', []) if v.get('Severity') == 'CRITICAL'))
except: print(0)
" 2>/dev/null || echo "0")

    HIGH=$(python3 -c "
import json, sys
try:
    d = json.load(open('$LOG_DIR/trivy/trivy-$TIMESTAMP.json'))
    print(sum(1 for r in d.get('Results', []) for v in r.get('Vulnerabilities', []) if v.get('Severity') == 'HIGH'))
except: print(0)
" 2>/dev/null || echo "0")

    log "Trivy: $CRITICAL critical, $HIGH high"
    if [ "$CRITICAL" -gt 0 ] 2>/dev/null; then
        alert_if_critical "trivy" "Scheduled scan: $CRITICAL CRITICAL, $HIGH HIGH vulnerabilities"
    fi
}

run_clamav() {
    log "Starting ClamAV scan..."
    if ! command -v clamscan >/dev/null 2>&1; then
        log "ERROR: clamscan not found"
        return 1
    fi

    # Update DB first
    freshclam --no-warnings 2>/dev/null || log "WARNING: freshclam update failed"

    clamscan -r --no-summary "$WORKSPACE" \
        > "$LOG_DIR/clamav/clamscan-$TIMESTAMP.log" 2>&1 || true

    INFECTED=$(grep -c "FOUND$" "$LOG_DIR/clamav/clamscan-$TIMESTAMP.log" 2>/dev/null || echo "0")
    log "ClamAV: $INFECTED infected files"
    if [ "$INFECTED" -gt 0 ] 2>/dev/null; then
        alert_if_critical "clamav" "Scheduled scan: $INFECTED infected files found"
    fi
}

run_oscap() {
    log "Starting OpenSCAP scan..."
    if ! command -v oscap >/dev/null 2>&1; then
        log "ERROR: oscap not found"
        return 1
    fi

    SCAP_CONTENT="/usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml"
    if [ ! -f "$SCAP_CONTENT" ]; then
        log "ERROR: SCAP content not found"
        return 1
    fi

    oscap xccdf eval \
        --profile xccdf_org.ssgproject.content_profile_standard \
        --results "$LOG_DIR/oscap/oscap-$TIMESTAMP.xml" \
        --report "$LOG_DIR/oscap/oscap-$TIMESTAMP.html" \
        "$SCAP_CONTENT" 2>"$LOG_DIR/oscap/oscap-$TIMESTAMP.err" || true

    log "OpenSCAP scan complete"
}

# Parse arguments
RUN_TRIVY=0
RUN_CLAMAV=0
RUN_OSCAP=0

if [ $# -eq 0 ]; then
    echo "Usage: $0 [--trivy] [--clamav] [--oscap] [--all]"
    exit 1
fi

for arg in "$@"; do
    case "$arg" in
        --trivy)  RUN_TRIVY=1 ;;
        --clamav) RUN_CLAMAV=1 ;;
        --oscap)  RUN_OSCAP=1 ;;
        --all)    RUN_TRIVY=1; RUN_CLAMAV=1; RUN_OSCAP=1 ;;
        *) echo "Unknown option: $arg"; exit 1 ;;
    esac
done

[ "$RUN_TRIVY" -eq 1 ]  && run_trivy
[ "$RUN_CLAMAV" -eq 1 ] && run_clamav
[ "$RUN_OSCAP" -eq 1 ]  && run_oscap

log "Scan dispatch complete"
