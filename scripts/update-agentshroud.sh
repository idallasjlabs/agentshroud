#!/bin/bash
# update-agentshroud.sh — Update OpenClaw and/or Hermes to a new vendor version.
#
# Usage:
#   update-agentshroud.sh --bot openclaw --openclaw-version 2026.8.0
#   update-agentshroud.sh --bot openclaw --openclaw-latest
#   update-agentshroud.sh --bot hermes --hermes-image sha256:<digest>
#   update-agentshroud.sh --bot hermes --hermes-latest
#   update-agentshroud.sh --bot both --openclaw-latest --hermes-latest
#
# Flow: resolve the candidate version -> scripts/check-vendor-compat.sh gates it
# BEFORE anything live is touched -> backup all volumes + docker/versions.env ->
# bump the one relevant line in docker/versions.env -> rebuild + restart ->
# scripts/post-deploy-check.sh as the live gate -> automatic rollback (restores
# docker/versions.env and all volumes) on any live-gate failure.
#
# This never prints "Update Complete" unless the live gate actually passed —
# a failed compatibility check or a failed live gate always exits non-zero with
# the specific reason, and production is left exactly as it was before this run.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VERSIONS_ENV="$REPO_ROOT/docker/versions.env"
BACKUP_DIR="$REPO_ROOT/backup-update-$(date +%Y%m%d-%H%M%S)"

# Compose project name must match scripts/asb's convention (SCRUM-92), not
# Docker Compose's directory-derived default.
if [ "$USER" = "agentshroud-bot" ]; then
  PROJECT="agentshroud-bot"
else
  PROJECT="agentshroud"
fi
# NOTE: `docker compose` (the space-separated plugin form) is broken on this
# host's toolchain (~/.docker/cli-plugins/docker-compose points to a deleted
# Docker.app) — always use the standalone hyphenated `docker-compose` binary.
COMPOSE="docker-compose -f $REPO_ROOT/docker/docker-compose.yml -p $PROJECT"

BOT=""
OPENCLAW_VERSION_TARGET=""
HERMES_IMAGE_TARGET=""
WANT_OPENCLAW=0
WANT_HERMES=0

while [ $# -gt 0 ]; do
  case "$1" in
    --bot) BOT="$2"; shift 2 ;;
    --openclaw-version) OPENCLAW_VERSION_TARGET="$2"; shift 2 ;;
    --openclaw-latest) OPENCLAW_VERSION_TARGET="__LATEST__"; shift ;;
    --hermes-image) HERMES_IMAGE_TARGET="$2"; shift 2 ;;
    --hermes-latest) HERMES_IMAGE_TARGET="__LATEST__"; shift ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
done

case "$BOT" in
  openclaw) WANT_OPENCLAW=1 ;;
  hermes) WANT_HERMES=1 ;;
  both) WANT_OPENCLAW=1; WANT_HERMES=1 ;;
  "")
    echo "Usage: update-agentshroud.sh --bot openclaw|hermes|both \\" >&2
    echo "         [--openclaw-version X.Y.Z | --openclaw-latest] \\" >&2
    echo "         [--hermes-image sha256:<digest> | --hermes-latest]" >&2
    exit 1
    ;;
  *) echo "Unknown --bot: $BOT (expected 'openclaw', 'hermes', or 'both')" >&2; exit 1 ;;
esac

if [ "$WANT_OPENCLAW" -eq 1 ] && [ -z "$OPENCLAW_VERSION_TARGET" ]; then
  echo "ERROR: --bot openclaw|both requires --openclaw-version X.Y.Z or --openclaw-latest" >&2
  exit 1
fi
if [ "$WANT_HERMES" -eq 1 ] && [ -z "$HERMES_IMAGE_TARGET" ]; then
  echo "ERROR: --bot hermes|both requires --hermes-image sha256:<digest> or --hermes-latest" >&2
  exit 1
fi

echo "=== AgentShroud Vendor Update ==="
echo "Repository: $REPO_ROOT"
echo "Compose project: $PROJECT"
echo

# ── Resolve candidates ───────────────────────────────────────────────────────
if [ "$OPENCLAW_VERSION_TARGET" = "__LATEST__" ]; then
  echo "Resolving latest openclaw version from npm..."
  OPENCLAW_VERSION_TARGET="$(npm view openclaw version)"
  echo "  -> $OPENCLAW_VERSION_TARGET"
  echo
fi

if [ "$HERMES_IMAGE_TARGET" = "__LATEST__" ]; then
  echo "Resolving latest nousresearch/hermes-agent digest..."
  docker pull nousresearch/hermes-agent:latest > /dev/null
  HERMES_IMAGE_TARGET="$(docker inspect --format='{{index .RepoDigests 0}}' nousresearch/hermes-agent:latest)"
  echo "  -> $HERMES_IMAGE_TARGET"
  echo
fi

# ── Pre-promotion compatibility gate — BEFORE anything live is touched ──────
if [ "$WANT_OPENCLAW" -eq 1 ]; then
  echo "=== Compatibility check: OpenClaw $OPENCLAW_VERSION_TARGET ==="
  if ! "$SCRIPT_DIR/check-vendor-compat.sh" --bot openclaw --openclaw-version "$OPENCLAW_VERSION_TARGET"; then
    echo
    echo "ERROR: OpenClaw $OPENCLAW_VERSION_TARGET failed the compatibility check (see above)." >&2
    echo "Nothing was touched — production and docker/versions.env are unchanged." >&2
    exit 1
  fi
  echo
fi

if [ "$WANT_HERMES" -eq 1 ]; then
  echo "=== Compatibility check: Hermes $HERMES_IMAGE_TARGET ==="
  if ! "$SCRIPT_DIR/check-vendor-compat.sh" --bot hermes --hermes-image "$HERMES_IMAGE_TARGET"; then
    echo
    echo "ERROR: Hermes $HERMES_IMAGE_TARGET failed the compatibility check (see above)." >&2
    echo "Nothing was touched — production and docker/versions.env are unchanged." >&2
    exit 1
  fi
  echo
fi

echo "All compatibility checks passed. Proceeding with the real update."
echo

# ── Backup — only reached once every requested compat check has passed ─────
echo "1. Backing up current state..."
mkdir -p "$BACKUP_DIR"
cp "$VERSIONS_ENV" "$BACKUP_DIR/versions.env.bak"
echo "  ✓ docker/versions.env snapshotted"

# Volume names are project-prefixed by Docker Compose (no explicit `name:`
# override in docker-compose.yml for these four) — see scripts/restore-backup.sh,
# which this backup set is designed to be restored by on the rollback path below.
# Parallel entries (not an associative array — `declare -A` needs bash 4+, and
# macOS ships bash 3.2 by default; a bare `bash update-agentshroud.sh` there
# would fail immediately on this line otherwise).
VOL_TAR_PAIRS="agentshroud-config:openclaw-config.tar.gz gateway-data:gateway-data.tar.gz agentshroud-workspace:openclaw-workspace.tar.gz agentshroud-ssh:openclaw-ssh.tar.gz"
for pair in $VOL_TAR_PAIRS; do
  vol_key="${pair%%:*}"
  tar_name="${pair##*:}"
  volume_name="${PROJECT}_${vol_key}"
  if docker volume inspect "$volume_name" >/dev/null 2>&1; then
    docker run --rm \
      -v "${volume_name}:/data" \
      -v "${BACKUP_DIR}:/backup" \
      alpine tar czf "/backup/${tar_name}" -C /data .
    echo "  ✓ ${vol_key} -> ${tar_name}"
  else
    echo "  - (skip) ${vol_key}: volume ${volume_name} does not exist yet"
  fi
done
echo "✓ Backup saved to: $BACKUP_DIR"
echo

# ── Rollback helper — invoked only on a live-gate failure below ────────────
_rollback() {
  echo
  echo "=== ROLLING BACK to pre-update state ==="
  cp "$BACKUP_DIR/versions.env.bak" "$VERSIONS_ENV"
  echo "  ✓ Restored docker/versions.env"
  bash "$SCRIPT_DIR/restore-backup.sh" --yes "$BACKUP_DIR"
  echo "=== ROLLBACK COMPLETE ==="
}

# ── Bump the pin — the one deliberate, reviewable line-edit ────────────────
echo "2. Bumping docker/versions.env..."
if [ "$WANT_OPENCLAW" -eq 1 ]; then
  sed -i.bak "s|^OPENCLAW_VERSION=.*|OPENCLAW_VERSION=${OPENCLAW_VERSION_TARGET}|" "$VERSIONS_ENV"
  echo "  ✓ OPENCLAW_VERSION -> $OPENCLAW_VERSION_TARGET"
fi
if [ "$WANT_HERMES" -eq 1 ]; then
  sed -i.bak "s|^HERMES_IMAGE=.*|HERMES_IMAGE=${HERMES_IMAGE_TARGET}|" "$VERSIONS_ENV"
  echo "  ✓ HERMES_IMAGE -> $HERMES_IMAGE_TARGET"
fi
rm -f "${VERSIONS_ENV}.bak"
echo

# ── Rebuild + restart ────────────────────────────────────────────────────────
set -a
# shellcheck source=docker/versions.env
. "$VERSIONS_ENV"
set +a

echo "3. Rebuilding and restarting..."
if [ "$WANT_OPENCLAW" -eq 1 ]; then
  $COMPOSE up -d --build openclaw
  echo "  ✓ openclaw rebuilt and restarted"
fi
if [ "$WANT_HERMES" -eq 1 ]; then
  # Hermes deploys via docker run (run-standalone.sh), not compose — see
  # project_hermes_do_request_ptb226_fix.md for why (compose-specific race).
  bash "$REPO_ROOT/docker/bots/hermes/run-standalone.sh" down 2>/dev/null || true
  AGENTSHROUD_PROJECT="$PROJECT" \
  AGENTSHROUD_VERSION="${AGENTSHROUD_VERSION:-latest}" \
  AGENTSHROUD_SECRETS_DIR="$HOME/.agentshroud/.asb-secrets" \
    bash "$REPO_ROOT/docker/bots/hermes/run-standalone.sh" up
  echo "  ✓ hermes rebuilt and restarted"
fi
echo

# ── Live gate ────────────────────────────────────────────────────────────────
echo "4. Waiting for services to settle (30s)..."
sleep 30
echo

echo "5. Running post-deploy checks..."
if ! bash "$REPO_ROOT/scripts/post-deploy-check.sh"; then
  echo
  echo "ERROR: post-deploy-check.sh failed after the update." >&2
  _rollback
  echo
  echo "=== UPDATE FAILED — rolled back to the pre-update state ===" >&2
  exit 1
fi
echo

echo "=== Update Complete ==="
echo "Backup saved to: $BACKUP_DIR"
echo "Manual rollback if ever needed:"
echo "  cp $BACKUP_DIR/versions.env.bak docker/versions.env"
echo "  bash scripts/restore-backup.sh $BACKUP_DIR"
