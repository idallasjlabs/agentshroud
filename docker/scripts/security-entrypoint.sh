#!/bin/sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# security-entrypoint.sh — Runs on container boot
# Updates virus DBs, runs initial scans, alerts on critical findings.
# Designed for non-root execution.

set -e

LOG_DIR="/var/log/security"
GATEWAY_URL="${GATEWAY_URL:-http://localhost:8080}"
TIMESTAMP=$(date -u +%Y%m%d-%H%M%S)

mkdir -p "$LOG_DIR"/{trivy,clamav,oscap}

log() {
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG_DIR/entrypoint-$TIMESTAMP.log"
}

alert_critical() {
    local tool="$1" message="$2"
    log "CRITICAL ALERT from $tool: $message"
    curl -sf -X POST "$GATEWAY_URL/api/alerts" \
        -H "Content-Type: application/json" \
        -d "{\"type\":\"security_alert\",\"severity\":\"CRITICAL\",\"tool\":\"$tool\",\"message\":\"$message\"}" \
        2>/dev/null || log "Failed to send alert to gateway"
}

# --- ClamAV DB Update ---
log "Updating ClamAV virus database..."
if command -v freshclam >/dev/null 2>&1; then
    freshclam --no-warnings 2>&1 | tee -a "$LOG_DIR/clamav/freshclam-$TIMESTAMP.log" || \
        log "WARNING: freshclam update failed (may need network)"
    log "ClamAV DB update complete"
else
    log "WARNING: freshclam not found, skipping DB update"
fi

# --- Initial Trivy Scan ---
log "Running initial Trivy filesystem scan..."
if command -v trivy >/dev/null 2>&1; then
    trivy fs --format json --severity CRITICAL,HIGH,MEDIUM,LOW --no-progress / \
        > "$LOG_DIR/trivy/trivy-$TIMESTAMP.json" 2>"$LOG_DIR/trivy/trivy-$TIMESTAMP.err" || true

    TRIVY_CRITICAL=$(cat "$LOG_DIR/trivy/trivy-$TIMESTAMP.json" | \
        python3 -c "import sys,json; d=json.load(sys.stdin); print(sum(1 for r in d.get('Results',[]) for v in r.get('Vulnerabilities',[]) if v.get('Severity')=='CRITICAL'))" 2>/dev/null || echo "0")

    log "Trivy scan complete: $TRIVY_CRITICAL critical vulnerabilities"
    if [ "$TRIVY_CRITICAL" -gt 0 ] 2>/dev/null; then
        alert_critical "trivy" "Initial scan found $TRIVY_CRITICAL CRITICAL vulnerabilities"
    fi
else
    log "WARNING: trivy not found, skipping scan"
fi

# --- Initial ClamAV Scan ---
log "Running initial ClamAV scan on workspace..."
if command -v clamscan >/dev/null 2>&1; then
    WORKSPACE="${AGENTSHROUD_WORKSPACE:-/home/node}"
    clamscan -r --no-summary "$WORKSPACE" \
        > "$LOG_DIR/clamav/clamscan-$TIMESTAMP.log" 2>&1 || true

    INFECTED=$(grep -c "FOUND$" "$LOG_DIR/clamav/clamscan-$TIMESTAMP.log" 2>/dev/null || echo "0")
    log "ClamAV scan complete: $INFECTED infected files"
    if [ "$INFECTED" -gt 0 ] 2>/dev/null; then
        alert_critical "clamav" "Initial scan found $INFECTED infected files"
    fi
else
    log "WARNING: clamscan not found, skipping scan"
fi

# --- Initial OpenSCAP Check ---
log "Running initial OpenSCAP compliance check..."
if command -v oscap >/dev/null 2>&1; then
    SCAP_CONTENT="/usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml"
    if [ -f "$SCAP_CONTENT" ]; then
        oscap xccdf eval \
            --profile xccdf_org.ssgproject.content_profile_standard \
            --results "$LOG_DIR/oscap/oscap-$TIMESTAMP.xml" \
            --report "$LOG_DIR/oscap/oscap-$TIMESTAMP.html" \
            "$SCAP_CONTENT" 2>"$LOG_DIR/oscap/oscap-$TIMESTAMP.err" || true
        log "OpenSCAP compliance check complete"
    else
        log "WARNING: SCAP content not found at $SCAP_CONTENT"
    fi
else
    log "WARNING: oscap not found, skipping compliance check"
fi

log "Security entrypoint complete"
