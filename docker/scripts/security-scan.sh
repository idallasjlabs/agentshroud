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
WORKSPACE="${AGENTSHROUD_WORKSPACE:-/home/node}"

mkdir -p "$LOG_DIR"/{trivy,clamav,openscap,sbom}

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

    CLAMAV_RAW="$LOG_DIR/clamav/clamscan-$TIMESTAMP.log"
    clamscan -r --no-summary "$WORKSPACE" > "$CLAMAV_RAW" 2>&1 || true

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

    syft "$WORKSPACE" -o spdx-json \
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
    if [ ! -f "$SCAP_CONTENT" ]; then
        log "ERROR: SCAP content not found"
        return 1
    fi

    oscap xccdf eval \
        --profile xccdf_org.ssgproject.content_profile_standard \
        --results "$LOG_DIR/openscap/openscap-$TIMESTAMP.xml" \
        --report "$LOG_DIR/openscap/openscap-$TIMESTAMP.html" \
        "$SCAP_CONTENT" 2>"$LOG_DIR/openscap/openscap-$TIMESTAMP.err" || true

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
