#!/bin/sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# security-scan.sh — Unified scan dispatcher
# Usage: security-scan.sh [--trivy] [--clamav] [--oscap] [--all]

set -e

LOG_DIR="/var/log/security"
GATEWAY_URL="${GATEWAY_URL:-http://localhost:8080}"
TIMESTAMP=$(date -u +%Y%m%d-%H%M%S)
WORKSPACE="${AGENTSHROUD_WORKSPACE:-/app}"

mkdir -p "$LOG_DIR/trivy" "$LOG_DIR/clamav" "$LOG_DIR/openscap" "$LOG_DIR/sbom"

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

    # Use pre-seeded DB baked into the image at /var/lib/trivy (set at build time).
    # Fall back to /var/log/security/.trivy-cache if the image cache is missing.
    # On VPN, ghcr.io is blocked — always prefer --skip-db-update with the baked cache.
    TRIVY_CACHE="${TRIVY_CACHE_DIR:-/var/lib/trivy}"
    if [ ! -d "$TRIVY_CACHE/db" ]; then
        TRIVY_CACHE="/var/log/security/.trivy-cache"
        mkdir -p "$TRIVY_CACHE"
        log "WARNING: /var/lib/trivy/db missing — using fallback cache at $TRIVY_CACHE"
    fi

    # Try with pre-seeded cache first (no network needed), then fall back to live download.
    if ! trivy fs --format json --severity CRITICAL,HIGH,MEDIUM,LOW --no-progress \
        --ignore-unfixed \
        --skip-db-update \
        --cache-dir "$TRIVY_CACHE" \
        / \
        > "$LOG_DIR/trivy/trivy-$TIMESTAMP.json" 2>"$LOG_DIR/trivy/trivy-$TIMESTAMP.err"; then
        log "WARNING: Trivy with cached DB failed, attempting live DB download"
        trivy fs --format json --severity CRITICAL,HIGH,MEDIUM,LOW --no-progress \
            --ignore-unfixed \
            --cache-dir "$TRIVY_CACHE" \
            / \
            > "$LOG_DIR/trivy/trivy-$TIMESTAMP.json" 2>"$LOG_DIR/trivy/trivy-$TIMESTAMP.err" || true
    fi

    # If both attempts left an empty file, write a valid error JSON so scorer doesn't fail
    if [ ! -s "$LOG_DIR/trivy/trivy-$TIMESTAMP.json" ]; then
        log "ERROR: Trivy produced no output — writing error report"
        python3 -c "
import json, datetime
print(json.dumps({
    'SchemaVersion': 2, 'Results': [],
    'error': 'scan failed — rebuild image off-VPN to refresh DB',
    'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
}))
" > "$LOG_DIR/trivy/trivy-$TIMESTAMP.json" 2>/dev/null || true
    fi

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

    # Update DB first (non-fatal — run in background so we don't block the scan)
    freshclam --no-warnings --log="$LOG_DIR/clamav/freshclam-$TIMESTAMP.log" \
        2>/dev/null || log "WARNING: freshclam update failed"

    CLAMAV_RAW="$LOG_DIR/clamav/clamscan-$TIMESTAMP.log"
    SCAN_EXIT=0

    # Prefer clamdscan (delegates to running clamd daemon — much lighter than in-process clamscan).
    # Fallback to clamscan with strict size limits if clamd socket is unavailable.
    if command -v clamdscan >/dev/null 2>&1 && \
       ([ -S /run/clamav/clamd.ctl ] || [ -S /var/run/clamav/clamd.ctl ]); then
        log "Using clamdscan (clamd socket found)"
        clamdscan --no-summary --multiscan \
            --max-filesize=50M --max-scansize=200M \
            "$WORKSPACE" > "$CLAMAV_RAW" 2>&1 || SCAN_EXIT=$?
    elif command -v clamscan >/dev/null 2>&1; then
        log "Using clamscan (clamd socket not found)"
        clamscan -r --no-summary \
            --max-filesize=50M --max-scansize=200M \
            --exclude-dir=/proc --exclude-dir=/sys --exclude-dir=/dev \
            "$WORKSPACE" > "$CLAMAV_RAW" 2>&1 || SCAN_EXIT=$?
    else
        log "ERROR: neither clamdscan nor clamscan found"
        python3 -c "
import json
print(json.dumps({'tool':'clamav','status':'error','error':'clamav not installed',
    'files_scanned':0,'infected':0,'findings':[],'scan_target':'$WORKSPACE'}))
" > "$LOG_DIR/clamav/clamav-$TIMESTAMP.json" 2>/dev/null || true
        return 1
    fi

    # Exit code 1 from clamscan/clamdscan means "infected files found" — not a failure
    if [ "$SCAN_EXIT" -gt 1 ]; then
        log "WARNING: ClamAV scanner exited with code $SCAN_EXIT — writing error report"
        python3 -c "
import json
print(json.dumps({'tool':'clamav','status':'error','error':'scanner exit code $SCAN_EXIT',
    'files_scanned':0,'infected':0,'findings':[],'scan_target':'$WORKSPACE'}))
" > "$LOG_DIR/clamav/clamav-$TIMESTAMP.json" 2>/dev/null || true
        return 0
    fi

    INFECTED=$(grep -c "FOUND$" "$CLAMAV_RAW" 2>/dev/null || echo "0")
    SCANNED=$(grep -c ": OK$" "$CLAMAV_RAW" 2>/dev/null || echo "0")
    log "ClamAV: $INFECTED infected, $SCANNED clean files"

    # Write JSON summary that scanner_integration.py can read
    python3 -c "
import json, sys
infected = int('$INFECTED')
scanned  = int('$SCANNED')
findings = []
try:
    for line in open('$CLAMAV_RAW'):
        line = line.strip()
        if line.endswith('FOUND'):
            parts = line.rsplit(':', 1)
            findings.append({'path': parts[0].strip(), 'virus': parts[1].replace('FOUND','').strip() if len(parts)>1 else 'unknown'})
except Exception as e:
    pass
result = {
    'tool': 'clamav',
    'status': 'completed',
    'timestamp': '$TIMESTAMP',
    'files_scanned': scanned,
    'infected': infected,
    'findings': findings,
    'scan_target': '$WORKSPACE',
}
print(json.dumps(result, indent=2))
" > "$LOG_DIR/clamav/clamav-$TIMESTAMP.json" 2>/dev/null || log "WARNING: ClamAV JSON summary failed"

    if [ "$INFECTED" -gt 0 ] 2>/dev/null; then
        alert_if_critical "clamav" "Scheduled scan: $INFECTED infected files found"
    fi
}

run_sbom() {
    log "Starting SBOM generation..."
    if ! command -v syft >/dev/null 2>&1; then
        log "ERROR: syft not found — skipping SBOM"
        return 1
    fi

    syft / --exclude ./proc --exclude ./sys --exclude ./dev --exclude ./run/secrets \
        -o spdx-json \
        > "$LOG_DIR/sbom/sbom-$TIMESTAMP.json" 2>"$LOG_DIR/sbom/sbom-$TIMESTAMP.err" || true

    PACKAGES=$(python3 -c "
import json
try:
    d = json.load(open('$LOG_DIR/sbom/sbom-$TIMESTAMP.json'))
    packages = d.get('packages', [])
    print(len(packages))
except: print(0)
" 2>/dev/null || echo "0")

    log "SBOM: $PACKAGES packages catalogued"
}

run_oscap() {
    log "Starting OpenSCAP scan..."
    if ! command -v oscap >/dev/null 2>&1; then
        log "ERROR: oscap not found"
        return 1
    fi

    SCAP_CONTENT="/usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml"
    TAILORING_FILE="/usr/share/xml/scap/ssg/content/agentshroud-tailoring.xml"
    if [ ! -f "$SCAP_CONTENT" ]; then
        log "ERROR: SCAP content not found"
        return 1
    fi

    # Build oscap command — use tailoring file if present to deselect
    # rules inapplicable to containerized environments (PAM, systemd, cron, etc.)
    if [ -f "$TAILORING_FILE" ]; then
        oscap xccdf eval \
            --profile xccdf_org.ssgproject.content_profile_standard \
            --tailoring-file "$TAILORING_FILE" \
            --results "$LOG_DIR/openscap/openscap-$TIMESTAMP.xml" \
            --report "$LOG_DIR/openscap/openscap-$TIMESTAMP.html" \
            "$SCAP_CONTENT" 2>"$LOG_DIR/openscap/openscap-$TIMESTAMP.err" || true
    else
        oscap xccdf eval \
            --profile xccdf_org.ssgproject.content_profile_standard \
            --results "$LOG_DIR/openscap/openscap-$TIMESTAMP.xml" \
            --report "$LOG_DIR/openscap/openscap-$TIMESTAMP.html" \
            "$SCAP_CONTENT" 2>"$LOG_DIR/openscap/openscap-$TIMESTAMP.err" || true
    fi

    # Parse XML results to JSON summary for scanner_integration.py
    python3 -c "
import xml.etree.ElementTree as ET, json, sys
try:
    tree = ET.parse('$LOG_DIR/openscap/openscap-$TIMESTAMP.xml')
    root = tree.getroot()
    ns = {'x': 'http://checklists.nist.gov/xccdf/1.2'}
    results = root.findall('.//x:rule-result', ns)
    pass_count = sum(1 for r in results if r.findtext('x:result', namespaces=ns) == 'pass')
    fail_count = sum(1 for r in results if r.findtext('x:result', namespaces=ns) == 'fail')
    result = {
        'tool': 'openscap',
        'status': 'completed',
        'timestamp': '$TIMESTAMP',
        'pass_count': pass_count,
        'fail_count': fail_count,
        'critical': 0,
        'high': fail_count,
        'profile': 'standard',
    }
    print(json.dumps(result, indent=2))
except Exception as e:
    print(json.dumps({'tool': 'openscap', 'status': 'error', 'error': str(e), 'pass_count': 0, 'fail_count': 0}))
" > "$LOG_DIR/openscap/openscap-$TIMESTAMP.json" 2>/dev/null || log "WARNING: OpenSCAP JSON summary failed"

    log "OpenSCAP scan complete"
}

# Parse arguments
RUN_TRIVY=0
RUN_CLAMAV=0
RUN_OSCAP=0
RUN_SBOM=0

if [ $# -eq 0 ]; then
    echo "Usage: $0 [--trivy] [--clamav] [--oscap] [--sbom] [--all]"
    exit 1
fi

for arg in "$@"; do
    case "$arg" in
        --trivy)  RUN_TRIVY=1 ;;
        --clamav) RUN_CLAMAV=1 ;;
        --oscap)  RUN_OSCAP=1 ;;
        --sbom)   RUN_SBOM=1 ;;
        --all)    RUN_TRIVY=1; RUN_CLAMAV=1; RUN_OSCAP=1; RUN_SBOM=1 ;;
        *) echo "Unknown option: $arg"; exit 1 ;;
    esac
done

[ "$RUN_TRIVY" -eq 1 ]  && run_trivy
[ "$RUN_CLAMAV" -eq 1 ] && run_clamav
[ "$RUN_OSCAP" -eq 1 ]  && run_oscap
[ "$RUN_SBOM" -eq 1 ]   && run_sbom

log "Scan dispatch complete"
