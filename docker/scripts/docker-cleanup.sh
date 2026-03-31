#!/usr/bin/env bash
# docker-cleanup.sh — Docker / BuildKit recovery commands for AgentShroud on Marvin
#
# Use this script when builds fail with "no space" errors or Docker is in a bad state.
# For routine clean rebuilds, use: ./scripts/asb clean-rebuild
#
# Account labels on each command:
#   [both]    — run from ijefferson.admin OR agentshroud-bot; affects the shared daemon
#   [admin]   — run from ijefferson.admin only (prod account)
#   [bot]     — run from agentshroud-bot only (dev account)
#
# Both accounts share the same Colima VM and Docker daemon. Actions that restart the
# daemon or prune from inside the VM affect both accounts simultaneously.

set -euo pipefail

SCRIPT_NAME="$(basename "$0")"

usage() {
  cat >&2 <<EOF
Usage: $SCRIPT_NAME <command>

Commands:
  diagnose    Show disk usage + BuildKit cache size (safe, read-only)
  buildkit    Prune BuildKit cache — fixes phantom "no space" build errors
  safe-prune  Remove stopped containers + dangling images (preserves volumes)
  restart     Restart Docker daemon inside Colima VM
  nuclear     Full system prune inside VM + daemon restart (DESTRUCTIVE)

Run from the repo root. All commands work from either account unless noted.
EOF
  exit 1
}

# ──────────────────────────────────────────────────────────────────────────────
cmd_diagnose() {
  echo "=== Docker data partition (Colima VM) ==="
  echo "[both] colima ssh -- df -h /var/lib/docker"
  colima ssh -- df -h /var/lib/docker
  echo ""

  echo "=== Docker disk usage summary (host view) ==="
  echo "[both] docker system df"
  docker system df
  echo ""

  echo "=== BuildKit cache size ==="
  echo "[both] docker buildx du"
  # docker buildx du may fail on older Docker versions; don't abort on error
  docker buildx du 2>/dev/null || echo "(docker buildx du not available on this Docker version)"
  echo ""

  echo "=== Container health ==="
  echo "[both] docker ps --format ..."
  docker ps --format 'table {{.Names}}\t{{.Status}}'
}

# ──────────────────────────────────────────────────────────────────────────────
cmd_buildkit() {
  cat <<'EOF'
=== Prune BuildKit cache ===
[both] Affects the shared Docker daemon — both prod and dev accounts.

This fixes the phantom "no space" error caused by stale BuildKit overlay snapshots
left behind by previously failed builds. docker compose uses BuildKit (not the
legacy builder), so docker builder prune does NOT help — use docker buildx prune.

EOF
  docker buildx prune -a -f
  echo "BuildKit cache pruned. Retry: ./scripts/asb clean-rebuild"
}

# ──────────────────────────────────────────────────────────────────────────────
cmd_safe_prune() {
  cat <<'EOF'
=== Safe prune: stopped containers + dangling images ===
[both] Affects the shared Docker daemon. Named volumes are NOT removed.

EOF
  docker system prune -f
  docker image prune -f
  echo ""
  echo "Safe prune complete. Named volumes preserved."
  echo "For BuildKit cache, run: $SCRIPT_NAME buildkit"
}

# ──────────────────────────────────────────────────────────────────────────────
cmd_restart() {
  cat <<'EOF'
=== Restart Docker daemon inside Colima VM ===
[both] Affects both prod and dev accounts simultaneously.
       Coordinate with the other account before running if prod is serving traffic.

Restarting the daemon clears stale overlay references that survive docker buildx prune.
Running containers will be stopped and must be restarted with: ./scripts/asb up

EOF
  read -r -p "This will stop all running containers. Continue? [y/N] " confirm
  [[ "$confirm" =~ ^[Yy]$ ]] || { echo "Aborted."; exit 0; }
  colima ssh -- sudo systemctl restart docker
  echo ""
  echo "Docker daemon restarted. Restart containers with: ./scripts/asb up"
}

# ──────────────────────────────────────────────────────────────────────────────
cmd_nuclear() {
  cat <<'EOF'
=== Nuclear: full system prune inside VM + daemon restart ===
[both] Affects both prod and dev accounts simultaneously. DESTRUCTIVE.
       Removes ALL stopped containers, ALL unused images, and ALL build cache.
       Named volumes (workspace, config, SSH keys) are NOT removed.

Use only when all other options have failed.

EOF
  read -r -p "This is DESTRUCTIVE and affects both accounts. Continue? [y/N] " confirm
  [[ "$confirm" =~ ^[Yy]$ ]] || { echo "Aborted."; exit 0; }

  echo "Pruning from inside VM (avoids host-side hang)..."
  colima ssh -- docker system prune -a -f
  echo ""

  echo "Pruning BuildKit cache..."
  docker buildx prune -a -f
  echo ""

  echo "Restarting Docker daemon..."
  colima ssh -- sudo systemctl restart docker
  echo ""

  echo "Nuclear complete. Restart containers with: ./scripts/asb up"
  echo "If disk was full, verify: colima ssh -- df -h /var/lib/docker"
}

# ──────────────────────────────────────────────────────────────────────────────
case "${1:-}" in
  diagnose)   cmd_diagnose ;;
  buildkit)   cmd_buildkit ;;
  safe-prune) cmd_safe_prune ;;
  restart)    cmd_restart ;;
  nuclear)    cmd_nuclear ;;
  *)          usage ;;
esac
