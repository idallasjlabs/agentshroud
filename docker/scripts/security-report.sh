#!/bin/sh
# security-report.sh — Generate and send daily health report
# Collects results from all security tools, generates report, sends via gateway.

set -e

LOG_DIR="/var/log/security"
GATEWAY_URL="${GATEWAY_URL:-http://localhost:8080}"
PYTHON="${PYTHON_BIN:-python3}"
TIMESTAMP=$(date -u +%Y%m%d-%H%M%S)

mkdir -p "$LOG_DIR/reports"

log() {
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [report] $*"
}

log "Generating daily health report..."

# Use Python health_report module to generate the report
REPORT=$($PYTHON -c "
import sys, json
sys.path.insert(0, '/app')

from gateway.security import health_report, trivy_report, clamav_scanner, falco_monitor, wazuh_client
from pathlib import Path

summaries = {}

# Trivy — latest report
trivy_dir = Path('$LOG_DIR/trivy')
if trivy_dir.exists():
    reports = sorted(trivy_dir.glob('trivy-*.json'), reverse=True)
    if reports:
        try:
            import json as _json
            raw = _json.loads(reports[0].read_text())
            parsed = trivy_report.parse_trivy_output(raw)
            summaries['trivy'] = trivy_report.generate_summary(parsed)
        except Exception as e:
            summaries['trivy'] = {'tool': 'trivy', 'status': 'error', 'error': str(e), 'findings': 0, 'critical': 0, 'high': 0}

# ClamAV — latest log
clamav_dir = Path('$LOG_DIR/clamav')
if clamav_dir.exists():
    logs = sorted(clamav_dir.glob('clamscan-*.log'), reverse=True)
    if logs:
        try:
            output = logs[0].read_text()
            parsed = clamav_scanner.parse_clamscan_output(output)
            summaries['clamav'] = clamav_scanner.generate_summary(parsed)
        except Exception as e:
            summaries['clamav'] = {'tool': 'clamav', 'status': 'error', 'error': str(e), 'findings': 0, 'critical': 0, 'high': 0}

# Falco
try:
    alerts = falco_monitor.read_alerts()
    summaries['falco'] = falco_monitor.generate_summary(alerts)
except Exception as e:
    summaries['falco'] = {'tool': 'falco', 'status': 'error', 'error': str(e), 'findings': 0, 'critical': 0, 'high': 0}

# Wazuh
try:
    alerts = wazuh_client.read_alerts()
    summaries['wazuh'] = wazuh_client.generate_summary(alerts)
except Exception as e:
    summaries['wazuh'] = {'tool': 'wazuh', 'status': 'error', 'error': str(e), 'findings': 0, 'critical': 0, 'high': 0}

# Gateway proxy metrics placeholder
summaries['gateway'] = {
    'tool': 'gateway', 'status': 'clean', 'findings': 0,
    'critical': 0, 'high': 0, 'medium': 0, 'low': 0,
}

report = health_report.generate_report(summaries)
formatted = health_report.format_report(report)

# Save report
Path('$LOG_DIR/reports/report-$TIMESTAMP.json').write_text(json.dumps(report, indent=2))
Path('$LOG_DIR/reports/report-$TIMESTAMP.txt').write_text(formatted)

print(formatted)
" 2>&1) || {
    log "ERROR: Failed to generate report"
    REPORT="⚠️ Security report generation failed. Check logs."
}

log "Report generated, sending via gateway..."

# Send report via gateway messaging
curl -sf -X POST "$GATEWAY_URL/api/alerts" \
    -H "Content-Type: application/json" \
    -d "$(printf '{"type":"health_report","severity":"INFO","tool":"health_report","message":"%s"}' "$(echo "$REPORT" | sed 's/"/\\"/g' | tr '\n' ' ')")" \
    2>/dev/null || log "WARNING: Failed to send report via gateway"

log "Daily health report complete"
