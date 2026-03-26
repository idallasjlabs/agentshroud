#!/bin/bash
# AgentShroud gateway container startup script.
# Launches in-process security daemons (clamd, fluent-bit) then execs uvicorn.
# Both daemons are non-fatal — gateway starts even if they fail.
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
set -uo pipefail

# Seed Trivy vulnerability DB from image-baked cache to writable security-reports volume.
# The image may have the DB pre-seeded at /var/lib/trivy (build-time download).
# The writable volume is at /var/log/security/.trivy-cache; copy DB there on first run.
_TRIVY_WRITABLE_CACHE="${TRIVY_CACHE_DIR:-/var/log/security/.trivy-cache}"
if [ ! -d "$_TRIVY_WRITABLE_CACHE/db" ] && [ -d "/var/lib/trivy/db" ]; then
    mkdir -p "$_TRIVY_WRITABLE_CACHE"
    cp -r /var/lib/trivy/db "$_TRIVY_WRITABLE_CACHE/" 2>/dev/null && \
        echo "[gateway-start] Trivy DB seeded from image cache to $_TRIVY_WRITABLE_CACHE" || \
        echo "[gateway-start] WARNING: failed to copy Trivy DB to writable cache"
fi

# Update ClamAV virus DB before starting daemon (clamd won't start without it).
# Use explicit log path so freshclam writes to writable tmpfs (read-only rootfs safe).
if command -v freshclam >/dev/null 2>&1; then
    freshclam --no-warnings --log=/tmp/freshclam-start.log 2>/tmp/freshclam-start.log || echo "[gateway-start] freshclam update failed (non-fatal)"
    echo "[gateway-start] freshclam DB update complete"
fi

# Start ClamAV daemon (non-fatal); wait up to 10s for socket so health checks pass
if command -v clamd >/dev/null 2>&1; then
    clamd --config-file=/etc/clamav/clamd.conf 2>/tmp/clamd-start.log &
    echo "[gateway-start] clamd launched (pid=$!)"
    for _i in $(seq 1 10); do [ -S /tmp/clamd.ctl ] && break; sleep 1; done
    [ -S /tmp/clamd.ctl ] && echo "[gateway-start] clamd socket ready" || echo "[gateway-start] clamd socket not yet ready (still initialising)"
fi

# Start Fluent Bit log collector (non-fatal); write pidfile for health check.
# fluent-bit deb installs to /opt/fluent-bit/bin/fluent-bit which is not on PATH.
_FB_BIN=$(command -v fluent-bit 2>/dev/null || command -v td-agent-bit 2>/dev/null || echo /opt/fluent-bit/bin/fluent-bit)
if [ -x "$_FB_BIN" ]; then
    "$_FB_BIN" -c /etc/fluent-bit/fluent-bit.conf 2>/tmp/fluent-bit-start.log &
    echo $! > /tmp/fluent-bit.pid
    echo "[gateway-start] fluent-bit launched via $_FB_BIN (pid=$(cat /tmp/fluent-bit.pid))"
fi

# Start Wazuh agent (non-fatal) — FIM on /app/gateway + Falco alert ingestion
# Runs as agentshroud (non-root); /var/ossec owned by agentshroud at build time.
if [ -x /var/ossec/bin/wazuh-agentd ]; then
    # Ensure runtime dirs exist on tmpfs (created fresh each container start)
    mkdir -p /var/ossec/var/run /var/ossec/queue/sockets /var/ossec/tmp 2>/dev/null || true
    /var/ossec/bin/wazuh-agentd 2>/tmp/wazuh-start.log &
    echo "[gateway-start] wazuh-agentd launched (pid=$!)"
fi

# Start Falco runtime monitor (non-fatal) — try modern_ebpf first, fall back to --nodriver
# (Colima/runc environments don't support eBPF; --nodriver uses userspace tracing)
if command -v falco >/dev/null 2>&1; then
    _FALCO_COMMON_OPTS="-o file_output.enabled=true -o file_output.keep_alive=true \
        -o file_output.filename=/var/log/falco/falco_alerts.json \
        -o json_output=true -o json_include_output_property=true"
    falco -o engine.kind=modern_ebpf \
        -o file_output.enabled=true -o file_output.keep_alive=true \
        -o file_output.filename=/var/log/falco/falco_alerts.json \
        -o json_output=true -o json_include_output_property=true \
        2>/tmp/falco-start.log &
    _FALCO_PID=$!
    sleep 3
    if ! kill -0 $_FALCO_PID 2>/dev/null; then
        echo "[gateway-start] falco eBPF not supported, retrying with --nodriver"
        falco --nodriver \
            -o file_output.enabled=true -o file_output.keep_alive=true \
            -o file_output.filename=/var/log/falco/falco_alerts.json \
            -o json_output=true -o json_include_output_property=true \
            2>/tmp/falco-start.log &
        _FALCO_PID=$!
    fi
    echo "[gateway-start] falco launched (pid=$_FALCO_PID)"
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
