#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
COMPOSE_FILE="${REPO_ROOT}/docker/docker-compose.yml"

usage() {
  cat <<'EOF'
Usage: scripts/switch_model.sh <target>

Targets:
  local       Use local Ollama model (qwen2.5-coder:7b)
  gemini      Use Google Gemini cloud model (gemini-2.5-flash)
  anthropic   Use Anthropic cloud model (claude-opus-4-6)
  openai      Use OpenAI cloud model (gpt-4o-mini)

Examples:
  scripts/switch_model.sh local
  scripts/switch_model.sh gemini
EOF
}

if [[ $# -ne 1 ]]; then
  usage
  exit 2
fi

TARGET="$(echo "$1" | tr '[:upper:]' '[:lower:]')"
MODEL_MODE="local"
LOCAL_REF="ollama/qwen2.5-coder:7b"
CLOUD_REF="anthropic/claude-opus-4-6"
OPENCLAW_MAIN_MODEL=""
LOCAL_MODEL_NAME="qwen2.5-coder:7b"

case "$TARGET" in
  local)
    MODEL_MODE="local"
    LOCAL_REF="ollama/qwen2.5-coder:7b"
    CLOUD_REF="anthropic/claude-opus-4-6"
    OPENCLAW_MAIN_MODEL="ollama/qwen2.5-coder:7b"
    LOCAL_MODEL_NAME="qwen2.5-coder:7b"
    ;;
  gemini)
    MODEL_MODE="cloud"
    CLOUD_REF="google/gemini-2.5-flash"
    OPENCLAW_MAIN_MODEL="google/gemini-2.5-flash"
    ;;
  anthropic)
    MODEL_MODE="cloud"
    CLOUD_REF="anthropic/claude-opus-4-6"
    OPENCLAW_MAIN_MODEL="anthropic/claude-opus-4-6"
    ;;
  openai)
    MODEL_MODE="cloud"
    CLOUD_REF="openai/gpt-4o-mini"
    OPENCLAW_MAIN_MODEL="openai/gpt-4o-mini"
    ;;
  -h|--help|help)
    usage
    exit 0
    ;;
  *)
    echo "Unknown target: $TARGET" >&2
    usage
    exit 2
    ;;
esac

echo "[switch-model] target=${TARGET} mode=${MODEL_MODE} model=${OPENCLAW_MAIN_MODEL}"

cd "${REPO_ROOT}"
AGENTSHROUD_MODEL_MODE="${MODEL_MODE}" \
AGENTSHROUD_LOCAL_MODEL_REF="${LOCAL_REF}" \
AGENTSHROUD_CLOUD_MODEL_REF="${CLOUD_REF}" \
AGENTSHROUD_LOCAL_MODEL="${LOCAL_MODEL_NAME}" \
OPENCLAW_MAIN_MODEL="${OPENCLAW_MAIN_MODEL}" \
OLLAMA_API_KEY="${OLLAMA_API_KEY:-ollama-local}" \
OPENCLAW_GATEWAY_BIND="${OPENCLAW_GATEWAY_BIND:-lan}" \
docker compose -f "${COMPOSE_FILE}" up -d --force-recreate gateway bot

echo "[switch-model] complete"
