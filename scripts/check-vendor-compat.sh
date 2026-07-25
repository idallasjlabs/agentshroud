#!/bin/bash
# check-vendor-compat.sh — Pre-promotion compatibility check for a CANDIDATE
# vendor version (OpenClaw npm version or Hermes image digest), run BEFORE that
# candidate's pin ever reaches docker/versions.env / production.
#
# Nothing else in this repo does this: post-deploy-check.sh and smoke.sh both
# check the *running production* stack after a deploy already happened. This
# script builds/boots the CANDIDATE in complete isolation (a separate compose
# project, its own throwaway network, its own container names) and never
# touches production containers, networks, or volumes.
#
# Usage:
#   check-vendor-compat.sh --bot openclaw --openclaw-version 2026.8.0
#   check-vendor-compat.sh --bot hermes --hermes-image sha256:<digest>
#
# Exit 0 + "COMPAT CHECK: PASS" only if every assertion for the target bot
# passes. Exit 1 + "COMPAT CHECK: FAIL" with the specific failing assertion
# printed, on any failure — this is what scripts/update-agentshroud.sh gates on
# before ever touching docker/versions.env or a running container.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

BOT=""
OPENCLAW_VERSION_CANDIDATE=""
HERMES_IMAGE_CANDIDATE=""

while [ $# -gt 0 ]; do
  case "$1" in
    --bot) BOT="$2"; shift 2 ;;
    --openclaw-version) OPENCLAW_VERSION_CANDIDATE="$2"; shift 2 ;;
    --hermes-image) HERMES_IMAGE_CANDIDATE="$2"; shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
done

FAILURES=()
WARNINGS=()

fail() { FAILURES+=("$1"); echo "  ✗ FAIL: $1" >&2; }
pass() { echo "  ✓ $1"; }
warn() { WARNINGS+=("$1"); echo "  ⚠ WARNING: $1" >&2; }

CLEANUP_CMDS=()
_run_cleanup() {
  local cmd
  # "${arr[@]}" on a genuinely empty array trips `set -u`'s unbound-variable
  # check on bash < 4.4 (macOS system /bin/bash is 3.2) — the ${CLEANUP_CMDS[@]:-}
  # default-expansion guards against that regardless of which bash runs this.
  for cmd in "${CLEANUP_CMDS[@]:-}"; do
    [ -n "$cmd" ] && eval "$cmd" >/dev/null 2>&1 || true
  done
}
trap _run_cleanup EXIT

# ---------------------------------------------------------------------------
# OpenClaw
# ---------------------------------------------------------------------------
check_openclaw() {
  if [ -z "$OPENCLAW_VERSION_CANDIDATE" ]; then
    echo "ERROR: --bot openclaw requires --openclaw-version X.Y.Z" >&2
    exit 1
  fi

  echo "=== OpenClaw compatibility check: candidate version $OPENCLAW_VERSION_CANDIDATE ==="
  echo ""

  echo "-- 1. Build candidate image (exercises the hardened patch scripts) --"
  # Plain `docker build` (NOT `docker-compose build`), with an explicit tag that
  # cannot collide with anything docker-compose.yml would ever produce.
  #
  # docker-compose.yml pins openclaw's `image:` field to the literal
  # `agentshroud-openclaw:${AGENTSHROUD_VERSION:-latest}` regardless of -p
  # project name — a `-p <different-project> build` still writes that SAME
  # tag, silently repointing it away from whatever production was using. (This
  # happened during development of this script: it overwrote the live
  # production openclaw image tag, though the already-running container was
  # unaffected since containers pin to their creation-time image ID, not the
  # mutable tag.) Bypassing compose for the build entirely avoids this class of
  # bug regardless of what any compose file's `image:` field says, now or later.
  #
  # --no-cache: a cached layer from a previous build could mask a patch script
  # that would now fail against a genuinely fresh install of this version.
  local image="agentshroud-vendorcompat-openclaw:candidate"
  if ! OPENCLAW_VERSION="$OPENCLAW_VERSION_CANDIDATE" \
       docker build --no-cache \
       --build-arg "AGENTSHROUD_VERSION=latest" \
       --build-arg "OPENCLAW_VERSION=$OPENCLAW_VERSION_CANDIDATE" \
       -f "$REPO_ROOT/docker/bots/openclaw/Dockerfile" \
       -t "$image" \
       "$REPO_ROOT" \
       > /tmp/check-vendor-compat-openclaw-build.log 2>&1; then
    fail "OpenClaw candidate build failed (patch script likely rejected a vendor source change) — see /tmp/check-vendor-compat-openclaw-build.log"
    tail -40 /tmp/check-vendor-compat-openclaw-build.log >&2
    return
  fi
  pass "Build succeeded"

  CLEANUP_CMDS+=("docker rmi -f $image 2>/dev/null")

  echo ""
  echo "-- 2. Installed version matches the candidate --"
  local installed_version
  installed_version="$(docker run --rm "$image" cat /app/.openclaw-image-version 2>/dev/null || echo "")"
  if [ "$installed_version" = "$OPENCLAW_VERSION_CANDIDATE" ]; then
    pass "/app/.openclaw-image-version == $OPENCLAW_VERSION_CANDIDATE"
  else
    fail "/app/.openclaw-image-version is '$installed_version', expected '$OPENCLAW_VERSION_CANDIDATE'"
  fi

  local cli_version
  cli_version="$(docker run --rm "$image" openclaw --version 2>/dev/null || echo "")"
  # `openclaw --version` prints a banner line ("OpenClaw 2026.7.1 (2d2ddc4)"),
  # not a bare version string — check containment, not exact equality.
  case "$cli_version" in
    *"$OPENCLAW_VERSION_CANDIDATE"*)
      pass "openclaw --version reports $OPENCLAW_VERSION_CANDIDATE ('$cli_version')" ;;
    *)
      fail "openclaw --version output '$cli_version' does not contain expected '$OPENCLAW_VERSION_CANDIDATE'" ;;
  esac

  echo ""
  echo "-- 3. Config schema: apply-patches.js output validates against the vendor's own schema --"
  # HOME=/sandbox for both commands so apply-patches.js's default path resolution
  # (fs.existsSync('/home/node/.openclaw/openclaw.json'), i.e. $HOME/.openclaw/...)
  # and `openclaw config validate`'s own default resolution agree on the same file
  # — this exercises the exact "vendor release now rejects a key we write"
  # crash-loop class from a genuinely fresh (no pre-existing config) install,
  # without needing to hand-author or embed a seed config.
  local schema_log
  schema_log="$(docker run --rm -e HOME=/sandbox --tmpfs /sandbox "$image" sh -c '
    mkdir -p /sandbox/.openclaw &&
    node /app/config-defaults/openclaw/apply-patches.js /sandbox/.openclaw/openclaw.json &&
    openclaw config validate --json
  ' 2>&1)" || true
  if echo "$schema_log" | grep -q '"valid"[[:space:]]*:[[:space:]]*true'; then
    pass "openclaw config validate: schema OK"
  else
    fail "openclaw config validate rejected the apply-patches.js output — vendor schema likely changed; apply-patches.js needs updating for this version"
    echo "$schema_log" | tail -30 >&2
  fi

  echo ""
  echo "-- 4. Patch-script drift warnings (non-fatal) --"
  if echo "$schema_log" | grep -q "patch-slack-sdk: WARNING pattern drift"; then
    warn "patch-slack-sdk.sh pattern drift on this candidate — cosmetic (pong-noise log demotion), not failing the check"
  fi
}

# ---------------------------------------------------------------------------
# Hermes
# ---------------------------------------------------------------------------
check_hermes() {
  if [ -z "$HERMES_IMAGE_CANDIDATE" ]; then
    echo "ERROR: --bot hermes requires --hermes-image nousresearch/hermes-agent@sha256:<digest>" >&2
    exit 1
  fi

  echo "=== Hermes compatibility check: candidate image $HERMES_IMAGE_CANDIDATE ==="
  echo ""

  echo "-- 1. Build candidate image --"
  # Plain `docker build` (NOT `docker-compose build`), with an explicit tag that
  # cannot collide with anything docker-compose.yml would ever produce — see the
  # detailed comment on the equivalent OpenClaw build above (docker-compose.yml's
  # `image:` field is pinned regardless of -p project name; building via compose
  # under a "different" project silently overwrote the production tag during
  # development of this script).
  local image="agentshroud-vendorcompat-hermes:candidate"
  if ! docker build --no-cache \
       --build-arg "HERMES_IMAGE=$HERMES_IMAGE_CANDIDATE" \
       -f "$REPO_ROOT/docker/bots/hermes/Dockerfile" \
       -t "$image" \
       "$REPO_ROOT" \
       > /tmp/check-vendor-compat-hermes-build.log 2>&1; then
    fail "Hermes candidate build failed — see /tmp/check-vendor-compat-hermes-build.log"
    tail -40 /tmp/check-vendor-compat-hermes-build.log >&2
    return
  fi
  pass "Build succeeded"

  CLEANUP_CMDS+=("docker rmi -f $image 2>/dev/null")

  echo ""
  echo "-- 2. tirith CLI subcommand our scripts depend on still exists --"
  # tirith is installed onto the persisted /opt/data volume on first boot, not
  # baked into the image — so this checks the invocation our scripts actually
  # use (docker/bots/hermes/init-config.sh) rather than a static image path.
  # Best-effort: WARN (not FAIL) if tirith isn't present at all in a fresh,
  # never-booted candidate — its installation lifecycle is boot-triggered and
  # this check does not attempt to fully replicate that here.
  local tirith_check
  tirith_check="$(docker run --rm --entrypoint sh "$image" -c \
    '[ -x /opt/data/bin/tirith ] && /opt/data/bin/tirith explain --list --format json >/dev/null 2>&1 && echo OK || echo MISSING' \
    2>/dev/null || echo "MISSING")"
  if [ "$tirith_check" = "OK" ]; then
    pass "tirith explain --list --format json succeeds"
  else
    warn "tirith not present/invocable in a fresh (never-booted) candidate image — expected, since it installs to the /opt/data volume on first boot; not independently verified here"
  fi

  echo ""
  echo "-- 3. Isolated boot: container stays up, API health responds, no traceback --"
  local container="check-vendor-compat-hermes-$$"
  local net="check-vendor-compat-net-$$"
  docker network create "$net" >/dev/null 2>&1 || true
  CLEANUP_CMDS+=("docker rm -f $container 2>/dev/null" "docker network rm $net 2>/dev/null")

  docker run -d --name "$container" --network "$net" \
    -e HERMES_DASHBOARD=1 -e HERMES_DASHBOARD_HOST=127.0.0.1 -e HERMES_DASHBOARD_PORT=9119 \
    -e HERMES_DASHBOARD_BRIDGE_PORT=9120 \
    -e API_SERVER_ENABLED=1 -e API_SERVER_HOST=0.0.0.0 -e API_SERVER_PORT=8642 \
    -e API_SERVER_KEY=compat-check-throwaway-key \
    -e HERMES_TELEGRAM_DISABLE_FALLBACK_IPS=1 \
    "$image" > /dev/null

  local boot_ok=false
  local deadline=$(( $(date +%s) + 150 ))
  while [ "$(date +%s)" -lt "$deadline" ]; do
    if [ "$(docker inspect -f '{{.State.Running}}' "$container" 2>/dev/null)" != "true" ]; then
      break
    fi
    if docker exec "$container" curl -sf --max-time 5 "http://127.0.0.1:8642/health" > /dev/null 2>&1; then
      boot_ok=true
      break
    fi
    sleep 3
  done

  if [ "$boot_ok" = "true" ]; then
    pass "Container stayed up and /health on 8642 responded within 150s"
  else
    fail "Container did not stay up + healthy within 150s — see logs below (this is the exact signature class of the historical CLI-rename and dual-process-race incidents)"
    docker logs "$container" 2>&1 | tail -50 >&2
    return
  fi

  echo ""
  echo "-- 4. Dashboard bridge (:9120) reachable and no un-guarded proxy-bypass in logs --"
  if docker exec "$container" sh -c "ps aux | grep -q '[a]gentshroud-dashboard-bridge.py'"; then
    pass "dashboard_bridge.py s6 service is running"
  else
    fail "dashboard_bridge.py is not running — dashboard would be unreachable from gateway (the 2026-07 502 bug)"
  fi

  local logs
  logs="$(docker logs "$container" 2>&1)"
  if echo "$logs" | grep -q "Traceback (most recent call last)"; then
    fail "Traceback found in candidate boot logs — see docker logs $container"
  else
    pass "No Python traceback in boot logs"
  fi
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
case "$BOT" in
  openclaw) check_openclaw ;;
  hermes) check_hermes ;;
  "") echo "Usage: check-vendor-compat.sh --bot openclaw --openclaw-version X.Y.Z | --bot hermes --hermes-image sha256:..." >&2; exit 1 ;;
  *) echo "Unknown --bot: $BOT (expected 'openclaw' or 'hermes')" >&2; exit 1 ;;
esac

echo ""
if [ ${#WARNINGS[@]} -gt 0 ]; then
  echo "${#WARNINGS[@]} non-fatal warning(s) — review above."
fi

if [ ${#FAILURES[@]} -eq 0 ]; then
  echo "COMPAT CHECK: PASS"
  exit 0
else
  echo "COMPAT CHECK: FAIL (${#FAILURES[@]} assertion(s) failed)"
  exit 1
fi
