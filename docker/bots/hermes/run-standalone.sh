#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# docker/bots/hermes/run-standalone.sh — Launch Hermes via `docker run`, not compose.
#
# 2026-07-18: a restart storm (735+ restarts, silent SIGTERM 3-14s into the
# Telegram connect handshake) was confirmed reproducible ONLY when Hermes is
# started by `docker-compose ... up -d` — five isolated `docker run` tests with
# an otherwise byte-identical image, token, volume, network, and resource limits
# stayed stable every time (see project memory
# project_hermes_do_request_ptb226_fix.md). Root cause inside compose's own
# container lifecycle was never pinned down; this script sidesteps it entirely
# by launching Hermes the way that has proven stable, while gateway/openclaw/
# voice-gateway keep deploying through docker/docker-compose.yml as before.
#
# This mirrors the hermes: service block in docker/docker-compose.yml field for
# field. If that block changes, update this script in the same commit.
#
# Usage: docker/bots/hermes/run-standalone.sh {up|down|status|logs}
#
# Env (all optional — asb sets these when it calls this script):
#   AGENTSHROUD_PROJECT       compose project name (default: agentshroud)
#   AGENTSHROUD_VERSION       image tag (default: latest)
#   AGENTSHROUD_SECRETS_DIR   dir of <secret_name>.txt files (default:
#                             $HOME/.agentshroud/.asb-secrets if present,
#                             else docker/secrets/ under the repo)

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"

PROJECT="${AGENTSHROUD_PROJECT:-agentshroud}"
VERSION="${AGENTSHROUD_VERSION:-latest}"

# AGENTSHROUD_ENV — auto-detected from the invoking macOS account, since dev
# and prod containers were otherwise indistinguishable from the inside (same
# AGENTSHROUD_BOT_ID, same container name). Found 2026-08-24: dev's
# init-config.sh unconditionally re-seeds the same 9 cron jobs prod runs, on
# the same schedule — every rebuild silently re-enabled a full duplicate
# schedule hitting the same shared local model backends. agentshroud-bot's
# own checkout runs this same script under its own account; prod runs under
# ijefferson.admin. Override with AGENTSHROUD_ENV=dev|prod if this host/
# account naming convention ever changes.
if [ -z "${AGENTSHROUD_ENV:-}" ]; then
  case "$(whoami 2>/dev/null)" in
    agentshroud-bot) AGENTSHROUD_ENV="dev" ;;
    *) AGENTSHROUD_ENV="prod" ;;
  esac
fi
IMAGE="agentshroud/hermes:${VERSION}"

CONTAINER="agentshroud-hermes-v2"
NETWORK="${PROJECT}_agentshroud-isolated"
GATEWAY_DATA_VOL="${PROJECT}_gateway-data"
SECURITY_REPORTS_VOL="${PROJECT}_security-reports"
HERMES_CONFIG_VOL="hermes-config"

if [ -n "${AGENTSHROUD_SECRETS_DIR:-}" ]; then
  SECRETS_DIR="$AGENTSHROUD_SECRETS_DIR"
elif [ -d "$HOME/.agentshroud/.asb-secrets" ]; then
  SECRETS_DIR="$HOME/.agentshroud/.asb-secrets"
else
  SECRETS_DIR="$REPO_DIR/docker/secrets"
fi
FALLBACK_SECRETS_DIR="$REPO_DIR/docker/secrets"

# Same secret keys as docker/docker-compose.yml's `hermes: secrets:` list.
# Compose bind-mounts each at /run/secrets/<key> regardless of source filename;
# replicate that exactly with -v.
HERMES_SECRET_KEYS=(
  hermes_telegram_bot_token
  slack_bot_token_hermes
  slack_app_token_hermes
  brave_api_key
  anthropic_oauth_token
  openai_api_key
  hermes_api_key
  github_pat
  hermes_healthchecks_url
  gateway_password
  feedbin_email
  feedbin_password
  podcastindex_api_key
  podcastindex_api_secret
)

_secret_mount_args() {
  local key path
  for key in "${HERMES_SECRET_KEYS[@]}"; do
    path="$SECRETS_DIR/${key}.txt"
    if [ ! -f "$path" ] || [ ! -s "$path" ]; then
      path="$FALLBACK_SECRETS_DIR/${key}.txt"
    fi
    if [ -f "$path" ]; then
      printf -- '-v\n%s:/run/secrets/%s:ro\n' "$path" "$key"
    else
      echo "  [hermes-standalone] WARN: no secret file found for '${key}' (checked $SECRETS_DIR and $FALLBACK_SECRETS_DIR) — skipping mount" >&2
    fi
  done
}

_wait_for_gateway_healthy() {
  local timeout="${1:-180}" waited=0 status
  # Resolve by compose labels, not a hardcoded name: host-specific overrides
  # (e.g. docker-compose.agentshroud-bot.marvin.yml) set a custom
  # container_name (e.g. agentshroud-marvin-gateway), but docker-compose
  # always tags containers with these labels regardless of that override, so
  # this works for any host without needing to know its override's naming.
  local gateway_container
  gateway_container="$(docker ps -a \
    --filter "label=com.docker.compose.project=${PROJECT}" \
    --filter "label=com.docker.compose.service=gateway" \
    --format '{{.Names}}' | head -1)"
  if [ -z "$gateway_container" ]; then
    gateway_container="agentshroud-gateway"  # fallback: default (non-overridden) name
  fi
  echo "  [hermes-standalone] waiting for ${gateway_container} to be healthy (timeout ${timeout}s)..."
  while [ "$waited" -lt "$timeout" ]; do
    status="$(docker inspect --format '{{.State.Health.Status}}' "$gateway_container" 2>/dev/null || echo "missing")"
    if [ "$status" = "healthy" ]; then
      echo "  [hermes-standalone] ${gateway_container} is healthy."
      return 0
    fi
    sleep 2
    waited=$((waited + 2))
  done
  echo "  [hermes-standalone] ERROR: ${gateway_container} did not become healthy within ${timeout}s (last status: ${status})" >&2
  return 1
}

cmd_up() {
  if ! docker network inspect "$NETWORK" >/dev/null 2>&1; then
    echo "  [hermes-standalone] ERROR: network '$NETWORK' not found — start gateway via compose first (asb up)" >&2
    exit 1
  fi

  _wait_for_gateway_healthy 180

  docker rm -f "$CONTAINER" >/dev/null 2>&1 || true

  # Portable equivalent of `mapfile -t` — macOS ships bash 3.2 as /bin/bash
  # (mapfile/readarray need bash 4+), and asb invokes this script via a literal
  # `bash run-standalone.sh`, which resolves to /bin/bash regardless of any
  # newer Homebrew bash earlier on PATH (bypasses the #!/usr/bin/env bash
  # shebang lookup this script would otherwise get if run directly).
  SECRET_ARGS=()
  while IFS= read -r _secret_arg_line; do
    SECRET_ARGS+=("$_secret_arg_line")
  done < <(_secret_mount_args)

  echo "  [hermes-standalone] starting ${CONTAINER} from ${IMAGE} on ${NETWORK}..."
  # shellcheck disable=SC2086
  # com.agentshroud.role=hermes: this is a `docker run` container, not
  # compose, so it gets none of compose's automatic com.docker.compose.*
  # labels — tag it explicitly so scripts/post-deploy-check.sh can resolve
  # the real container by label instead of a hardcoded name, the same
  # principle as the compose-label lookup above in _wait_for_gateway_healthy.
  docker run -d \
    --name "$CONTAINER" \
    --hostname "$CONTAINER" \
    --label "com.agentshroud.role=hermes" \
    --restart unless-stopped \
    --network "$NETWORK" \
    -v "${HERMES_CONFIG_VOL}:/opt/data" \
    -v "${GATEWAY_DATA_VOL}:/data/gateway:ro" \
    -v "${SECURITY_REPORTS_VOL}:/data/security-reports:ro" \
    "${SECRET_ARGS[@]}" \
    -e HTTP_PROXY="http://gateway:8181" \
    -e HTTPS_PROXY="http://gateway:8181" \
    -e NO_PROXY="gateway,${CONTAINER},api.telegram.org,127.0.0.1,localhost" \
    -e ANTHROPIC_BASE_URL="http://gateway:8080" \
    -e OLLAMA_BASE_URL="http://gateway:8080/v1" \
    -e AGENTSHROUD_MODEL_MODE="${AGENTSHROUD_MODEL_MODE:-cloud}" \
    -e AGENTSHROUD_LOCAL_MODEL_REF="${AGENTSHROUD_LOCAL_MODEL_REF:-ollama/qwen3:14b}" \
    -e AGENTSHROUD_LOCAL_MODEL="${AGENTSHROUD_LOCAL_MODEL:-qwen3:14b}" \
    -e AGENTSHROUD_CLOUD_MODEL_REF="${AGENTSHROUD_CLOUD_MODEL_REF:-anthropic/claude-opus-4-6}" \
    -e HERMES_MAIN_MODEL="${HERMES_MAIN_MODEL:-}" \
    -e TELEGRAM_ALLOWED_USERS="8096968754" \
    -e TELEGRAM_HOME_CHANNEL="8096968754" \
    -e HERMES_TELEGRAM_DISABLE_FALLBACK_IPS="1" \
    -e HERMES_TELEGRAM_HTTP_CONNECT_TIMEOUT="90" \
    -e HERMES_TELEGRAM_INIT_TIMEOUT="90" \
    -e HERMES_DASHBOARD="1" \
    -e HERMES_DASHBOARD_HOST="127.0.0.1" \
    -e HERMES_DASHBOARD_PORT="9119" \
    -e HERMES_DASHBOARD_BRIDGE_PORT="9120" \
    -e AGENTSHROUD_BOT_ID="hermes" \
    -e AGENTSHROUD_VERSION="${VERSION}" \
    -e AGENTSHROUD_ENV="${AGENTSHROUD_ENV}" \
    -e AGENTSHROUD_PROD_CRON_KEEP="${AGENTSHROUD_PROD_CRON_KEEP:-}" \
    -e TZ="${HERMES_TZ:-America/New_York}" \
    -e SEARXNG_URL="${SEARXNG_URL:-http://searxng-local:8080}" \
    -e API_SERVER_ENABLED="1" \
    -e API_SERVER_HOST="0.0.0.0" \
    -e API_SERVER_PORT="8642" \
    -e DOCKER_HOST="tcp://127.0.0.1:12375" \
    --security-opt "seccomp=${REPO_DIR}/docker/seccomp/agentshroud-seccomp.json" \
    --tmpfs /tmp:size=128m,mode=1777 \
    --memory 3g \
    --cpus 1.5 \
    --pids-limit 512 \
    --health-cmd "curl -fsS http://127.0.0.1:8642/health || exit 1" \
    --health-interval 30s \
    --health-timeout 10s \
    --health-start-period 120s \
    --health-retries 3 \
    "$IMAGE"

  # SearXNG lives in a separate stack (~/Development/local-llms), on the
  # default `bridge` network — not on Hermes's isolated network, so Hermes's
  # web_search tool can't reach it without this. Found 2026-08-24: without
  # this connection, web_search silently falls through to direct
  # DuckDuckGo/Bing calls, which fail outright on this network (no general
  # internet egress by design), and every research-based cron job returned
  # false "nothing new" results for an unknown period. `docker network
  # connect` is idempotent-safe here (harmless no-op) if already connected,
  # or if searxng-local isn't running yet (logged, not fatal — Hermes still
  # starts; reconnect manually or restart Hermes once SearXNG is up).
  if docker network connect agentshroud_agentshroud-isolated searxng-local 2>/dev/null; then
    echo "  [hermes-standalone] connected to searxng-local (web_search backend)"
  else
    echo "  [hermes-standalone] WARN: could not connect to searxng-local (not running, or already connected) — web_search may fall back to broken direct-engine calls"
  fi

  echo "  [hermes-standalone] ${CONTAINER} started."
}

cmd_down() {
  docker rm -f "$CONTAINER" >/dev/null 2>&1 \
    && echo "  [hermes-standalone] ${CONTAINER} removed." \
    || echo "  [hermes-standalone] ${CONTAINER} was not running."
}

cmd_status() {
  docker ps -a --filter "name=^${CONTAINER}\$" \
    --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'
}

cmd_logs() {
  docker logs -f --tail=100 "$CONTAINER"
}

case "${1:-}" in
  up)     cmd_up ;;
  down)   cmd_down ;;
  status) cmd_status ;;
  logs)   cmd_logs ;;
  *)
    echo "Usage: $0 {up|down|status|logs}" >&2
    exit 1
    ;;
esac
