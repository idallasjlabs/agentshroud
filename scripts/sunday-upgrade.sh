#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# sunday-upgrade.sh — Weekly (Sunday) upgrade of AgentShroud agents/components.
#
# Owner directive 2026-08-30: keep all agents/components/utilities on the
# latest release, prod and dev, and resolve reported security issues.
#
# What this does (in order, fail-loud):
#   1. Tag a rollback anchor (pre-deploy-<UTC>) on main HEAD and push it.
#   2. Vendor bot upgrades: scripts/update-agentshroud.sh --bot both
#      --openclaw-latest --hermes-latest — this already carries the
#      check-vendor-compat.sh pre-gate, full volume/versions.env backup,
#      post-deploy-check.sh live gate, and automatic rollback.
#   3. Rebuild the gateway image (pulls latest apt debs on the digest-pinned
#      base) and redeploy via compose — ONLY with --with-gateway, since a
#      gateway redeploy briefly interrupts every proxied agent.
#   4. Fresh trivy rescan of the RUNNING images + summary to Telegram via
#      the gateway's own report endpoint.
#
# What this deliberately does NOT do:
#   - Edit Dockerfile tool-version ARGs (cosign/falcoctl/docker CLI/etc.) —
#     those are code changes that go through a reviewed PR, not cron.
#   - Touch the dev account's stack — dev runs its own copy of this.
#
# Usage: scripts/sunday-upgrade.sh [--with-gateway] [--dry-run]

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

WITH_GATEWAY=false
DRY_RUN=false
for arg in "$@"; do
  case "$arg" in
    --with-gateway) WITH_GATEWAY=true ;;
    --dry-run) DRY_RUN=true ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

log() { echo "[sunday-upgrade] $(date '+%H:%M:%S') $*"; }
run() {
  if $DRY_RUN; then log "DRY-RUN: $*"; else log "+ $*"; "$@"; fi
}

log "Starting weekly upgrade (with_gateway=$WITH_GATEWAY dry_run=$DRY_RUN)"

# ── 1. Rollback anchor ───────────────────────────────────────────────────────
ANCHOR="pre-deploy-$(date -u '+%Y%m%dT%H%M%SZ')"
if git -C "$REPO_DIR" diff --quiet HEAD -- ':!graphify-out' 2>/dev/null; then
  run git tag "$ANCHOR" main
  run git push -q origin "$ANCHOR"
  log "Rollback anchor: $ANCHOR"
else
  log "WARN: working tree has non-graphify changes — tagging main HEAD anyway"
  run git tag "$ANCHOR" main
  run git push -q origin "$ANCHOR"
fi

# ── 2. Vendor bot upgrades (gated + auto-rollback inside the script) ─────────
if $DRY_RUN; then
  log "DRY-RUN: scripts/update-agentshroud.sh --bot both --openclaw-latest --hermes-latest"
else
  if ! bash scripts/update-agentshroud.sh --bot both --openclaw-latest --hermes-latest; then
    log "ERROR: bot upgrade failed (its own rollback has run) — aborting before gateway"
    exit 1
  fi
fi

# ── 3. Gateway rebuild/redeploy (opt-in) ─────────────────────────────────────
if $WITH_GATEWAY; then
  # Plain docker build (never docker-compose build: compose's image: field
  # ignores -p project isolation — see project_vendor_update_decoupling memory).
  run docker build -t agentshroud-gateway:latest -f gateway/Dockerfile .
  run docker compose -f docker/docker-compose.yml up -d gateway
  if ! $DRY_RUN; then
    bash scripts/post-deploy-check.sh || {
      log "ERROR: gateway post-deploy check failed — investigate (anchor: $ANCHOR)"
      exit 1
    }
  fi
else
  log "Gateway rebuild skipped (pass --with-gateway to include)"
fi

# ── 4. Fresh rescan of the running images + Telegram summary ─────────────────
if ! $DRY_RUN; then
  log "Triggering fresh CVE report (scans running images as of PR for SCRUM-174)"
  docker exec agentshroud-gateway curl -sf -X POST http://127.0.0.1:8080/soc/v1/cve-report \
    -o /dev/null || log "WARN: cve-report trigger failed — run POST /soc/v1/cve-report manually"
fi

log "Weekly upgrade complete."
