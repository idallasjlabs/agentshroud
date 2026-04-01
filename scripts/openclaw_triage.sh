#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="${1:-/tmp/openclaw_triage_$(date +%Y%m%d_%H%M%S)}"
mkdir -p "$OUT_DIR"

BOT_CONTAINER="${BOT_CONTAINER:-agentshroud-bot}"
GW_CONTAINER="${GW_CONTAINER:-agentshroud-gateway}"

log() {
  printf '\n[%s] %s\n' "$(date '+%F %T')" "$*"
}

save_cmd() {
  local name="$1"
  shift
  {
    echo "# COMMAND: $*"
    echo
    "$@"
  } >"$OUT_DIR/$name.txt" 2>&1 || true
}

save_shell() {
  local name="$1"
  local cmd="$2"
  {
    echo "# COMMAND: $cmd"
    echo
    /bin/sh -lc "$cmd"
  } >"$OUT_DIR/$name.txt" 2>&1 || true
}

log "Collecting Docker/container status"
save_cmd docker_ps docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
save_cmd docker_ps_a docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'

log "Checking OpenClaw version"
save_cmd bot_openclaw_version docker exec "$BOT_CONTAINER" openclaw --version
save_shell host_openclaw_version 'command -v openclaw >/dev/null 2>&1 && openclaw --version || echo "openclaw not installed on host"'

log "Checking pairing / trusted device state"
save_cmd bot_pairing_list docker exec "$BOT_CONTAINER" openclaw pairing list
save_cmd bot_pairing_list_telegram docker exec "$BOT_CONTAINER" openclaw pairing list telegram

log "Collecting recent bot/gateway logs"
save_cmd bot_logs_7d docker logs --since 168h "$BOT_CONTAINER"
save_cmd gateway_logs_7d docker logs --since 168h "$GW_CONTAINER"

log "Searching logs for suspicious auth / pairing / websocket activity"
save_shell suspicious_bot_log_hits "grep -Ein 'pair|trusted|approve|auth|token|websocket|ws|localhost|127\\.0\\.0\\.1|failed|rate limit|device' \"$OUT_DIR/bot_logs_7d.txt\" || true"
save_shell suspicious_gateway_log_hits "grep -Ein 'pair|trusted|approve|auth|token|websocket|ws|localhost|127\\.0\\.0\\.1|failed|rate limit|device' \"$OUT_DIR/gateway_logs_7d.txt\" || true"

log "Looking for OpenClaw local log files"
save_shell tmp_openclaw_listing "ls -lah /tmp/openclaw 2>/dev/null || true"
save_shell tmp_openclaw_grep "grep -RInE 'pair|trusted|approve|auth|token|websocket|ws|localhost|127\\.0\\.0\\.1|failed' /tmp/openclaw 2>/dev/null || true"

log "Capturing container environment hints (redacted grep only)"
save_shell bot_env_hints "docker exec \"$BOT_CONTAINER\" /bin/sh -lc 'env | grep -E \"OPENCLAW|GATEWAY|BIND|PORT\"' || true"
save_shell gateway_env_hints "docker exec \"$GW_CONTAINER\" /bin/sh -lc 'env | grep -E \"OPENCLAW|GATEWAY|BIND|PORT\"' || true"

log "Summary"
{
  echo "Triage output: $OUT_DIR"
  echo
  echo "Review these first:"
  echo "  - bot_openclaw_version.txt"
  echo "  - bot_pairing_list.txt"
  echo "  - suspicious_bot_log_hits.txt"
  echo "  - suspicious_gateway_log_hits.txt"
  echo
  echo "Red flags:"
  echo "  - OpenClaw version older than 2026.2.25"
  echo "  - Unknown paired/trusted devices"
  echo "  - Many localhost/127.0.0.1 auth failures"
  echo "  - Unexpected pairing approvals"
  echo "  - Unexplained successful auth after repeated failures"
} >"$OUT_DIR/README.txt"

log "Done. Results saved to: $OUT_DIR"
