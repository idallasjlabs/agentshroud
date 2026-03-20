#!/bin/bash
# AgentShroud gateway container startup script.
# Launches in-process security daemons (clamd, fluent-bit) then execs uvicorn.
# Both daemons are non-fatal — gateway starts even if they fail.
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
set -uo pipefail

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

exec uvicorn gateway.ingest_api.main:app --host 0.0.0.0 --port 8080
