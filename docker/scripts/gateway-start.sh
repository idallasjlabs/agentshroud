#!/bin/bash
# AgentShroud gateway container startup script.
# Launches in-process security daemons (clamd, fluent-bit) then execs uvicorn.
# Both daemons are non-fatal — gateway starts even if they fail.
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
set -uo pipefail

# Update ClamAV virus DB before starting daemon (clamd won't start without it)
if command -v freshclam >/dev/null 2>&1; then
    freshclam --no-warnings 2>/tmp/freshclam-start.log || echo "[gateway-start] freshclam update failed (non-fatal)"
    echo "[gateway-start] freshclam DB update complete"
fi

# Start ClamAV daemon (non-fatal)
if command -v clamd >/dev/null 2>&1; then
    clamd --config-file=/etc/clamav/clamd.conf 2>/tmp/clamd-start.log &
    echo "[gateway-start] clamd launched (pid=$!)"
fi

# Start Fluent Bit log collector (non-fatal); write pidfile for health check
if command -v fluent-bit >/dev/null 2>&1; then
    fluent-bit -c /etc/fluent-bit/fluent-bit.conf 2>/tmp/fluent-bit-start.log &
    echo $! > /tmp/fluent-bit.pid
    echo "[gateway-start] fluent-bit launched (pid=$(cat /tmp/fluent-bit.pid))"
fi

# Start Wazuh agent (non-fatal) — FIM on /app/gateway + Falco alert ingestion
# Runs as agentshroud (non-root); /var/ossec owned by agentshroud at build time.
if [ -x /var/ossec/bin/wazuh-agentd ]; then
    # Ensure runtime dirs exist on tmpfs (created fresh each container start)
    mkdir -p /var/ossec/var/run /var/ossec/queue/sockets /var/ossec/tmp 2>/dev/null || true
    /var/ossec/bin/wazuh-agentd 2>/tmp/wazuh-start.log &
    echo "[gateway-start] wazuh-agentd launched (pid=$!)"
fi

# Start Falco runtime monitor (non-fatal) — eBPF syscall detection
if command -v falco >/dev/null 2>&1; then
    falco \
        -o engine.kind=modern_ebpf \
        -o file_output.enabled=true \
        -o file_output.keep_alive=true \
        -o file_output.filename=/var/log/falco/falco_alerts.json \
        -o json_output=true \
        -o json_include_output_property=true \
        2>/tmp/falco-start.log &
    echo "[gateway-start] falco launched (pid=$!)"
fi

# Run boot-time security scans (initial scan results for SOC dashboard)
if [ -x /usr/local/bin/security-entrypoint.sh ]; then
    /usr/local/bin/security-entrypoint.sh &
    echo "[gateway-start] security-entrypoint launched (pid=$!)"
fi

# Start daily security scheduler (Trivy/ClamAV/OpenSCAP/SBOM scans)
if [ -x /usr/local/bin/security-scheduler.sh ]; then
    /usr/local/bin/security-scheduler.sh &
    echo "[gateway-start] security-scheduler launched (pid=$!)"
fi

exec uvicorn gateway.ingest_api.main:app --host 0.0.0.0 --port 8080 --no-access-log
